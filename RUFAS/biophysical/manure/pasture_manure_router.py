from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from RUFAS.biophysical.animal.data_types.animal_combination import AnimalCombination
from RUFAS.biophysical.field.field.field import Field
from RUFAS.biophysical.field.manager.field_manager import FieldManager
from RUFAS.data_structures.animal_to_manure_connection import ManureStream
from RUFAS.input_manager import InputManager
from RUFAS.output_manager import OutputManager
from RUFAS.rufas_time import RufasTime

AMMONIUM_FRACTION = 0.75
"""Fraction of TAN applied to soil as NH4+ (vs. NH3) during pasture deposition.

This value is a SurPhos-calibrated parameter, consistent with the
``ammonium_fraction_of_inorganic_nitrogen`` value used in the static
``GrazingSchedule`` inputs.  It is **not** derived from Henderson-Hasselbalch
equilibrium (which gives ~98 % NH4+ at pH 7.5); instead it implicitly accounts
for the portion of TAN lost as NH3 before infiltration into the soil profile.

.. note::
   Year-crossing grazing periods (start_day > end_day, e.g. 300–60) are not
   supported; ``_get_active_period`` assumes start_day ≤ end_day.
"""


@dataclass
class _PasturePeriod:
    """One annual grazing window for a pen."""

    start_day: int  # Julian day (1–365), inclusive
    end_day: int  # Julian day (1–365), inclusive
    pasture_field: str  # metadata key of the target pasture field


@dataclass
class _PenPastureConfig:
    """Aggregated pasture routing configuration for a single pen."""

    pen_id: int
    animal_combination: AnimalCombination
    periods: list[_PasturePeriod]


class PastureManureRouter:
    """Routes manure from grazing pens directly to a pasture field during configured periods.

    During a pasture period the manure streams produced by a configured pen bypass the manure
    processor chain entirely.  Their nutrients are deposited on the designated pasture field
    through ``ManureApplication.apply_grazing_manure``, which uses the SurPhos grazing manure
    phosphorus partitioning fractions and the cow-pad field-coverage formula.

    Outside pasture periods all streams are returned unchanged so the normal processor chain
    handles them.

    Configuration
    -------------
    Add an optional ``pasture_periods`` list to any pen entry in ``animal.pen_information``::

        {
            "id": 1,
            "animal_combination": "GROWING",
            ...
            "pasture_periods": [
                {"start_day": 121, "end_day": 273, "pasture_field": "field_3"}
            ]
        }

    Periods are **annual** and repeat every simulation year.  ``start_day`` and ``end_day`` are
    Julian days (1–365), inclusive.  ``pasture_field`` must match a field metadata key.

    Notes
    -----
    If the target field cannot be found, a warning is logged and the stream passes through to the
    processor chain unchanged so the simulation continues without data loss.
    """

    def __init__(self) -> None:
        self._configs: list[_PenPastureConfig] = []
        self._om = OutputManager()
        self._parse_configs()

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    @property
    def has_pasture_config(self) -> bool:
        """True when at least one pen has pasture periods configured."""
        return bool(self._configs)

    def route_pasture_manure(
        self,
        manure_streams: dict[str, ManureStream],
        field_manager: FieldManager,
        time: RufasTime,
    ) -> dict[str, ManureStream]:
        """Intercept grazing-pen streams and apply them to the pasture field.

        Parameters
        ----------
        manure_streams : dict[str, ManureStream]
            All manure streams produced by the herd for the current day.
        field_manager : FieldManager
            Used to look up the target pasture field by name.
        time : RufasTime
            Current simulation time.

        Returns
        -------
        dict[str, ManureStream]
            Remaining streams to pass to the manure processor chain.  Streams
            belonging to pens that are currently on pasture are removed.
        """
        if not self._configs:
            return manure_streams

        current_day = time.current_julian_day
        remaining = dict(manure_streams)

        for config in self._configs:
            active_period = self._get_active_period(config.periods, current_day)
            if active_period is None:
                continue

            pen_suffix = f"_{config.animal_combination.name}_PEN_{config.pen_id}"
            pasture_keys = [k for k in remaining if k.endswith(pen_suffix)]
            if not pasture_keys:
                continue

            field = field_manager.get_field_by_name(active_period.pasture_field)
            if field is None:
                self._om.add_warning(
                    "PastureManureRouter: pasture field not found",
                    f"Field '{active_period.pasture_field}' (referenced by pen {config.pen_id}) "
                    f"was not found. Routing through the processor chain instead.",
                    {"class": self.__class__.__name__, "function": "route_pasture_manure"},
                )
                continue

            for key in pasture_keys:
                stream = remaining.pop(key)
                self._apply_stream_to_field(stream, field)

        return remaining

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _parse_configs(self) -> None:
        """Read pasture_periods from the animal pen_information in the InputManager."""
        im = InputManager()
        pen_information: list[dict[str, Any]] | None = im.get_data("animal.pen_information")
        if not pen_information:
            return
        for pen in pen_information:
            raw_periods: list[dict[str, Any]] | None = pen.get("pasture_periods")
            if not raw_periods:
                continue
            pen_id: int = int(pen["id"])
            combination = AnimalCombination(pen["animal_combination"])
            periods = [
                _PasturePeriod(
                    start_day=int(p["start_day"]),
                    end_day=int(p["end_day"]),
                    pasture_field=str(p["pasture_field"]),
                )
                for p in raw_periods
            ]
            self._configs.append(_PenPastureConfig(pen_id, combination, periods))

    @staticmethod
    def _get_active_period(periods: list[_PasturePeriod], current_day: int) -> _PasturePeriod | None:
        """Return the first period whose window contains *current_day*, or None."""
        for period in periods:
            if period.start_day <= current_day <= period.end_day:
                return period
        return None

    @staticmethod
    def _apply_stream_to_field(stream: ManureStream, field: Field) -> None:
        """Deposit one day's manure stream on the pasture field via apply_grazing_manure.

        Parameters
        ----------
        stream : ManureStream
            Daily manure produced by the pen (already includes bedding adjustments
            from the Pen layer).
        field : Field
            The pasture field that will receive the manure.

        Notes
        -----
        Nitrogen fractions are derived from the ManureStream's ``nitrogen`` and
        ``ammoniacal_nitrogen`` attributes (both in kg):

        * **inorganic_nitrogen_fraction** = ammoniacal N / dry matter mass
        * **organic_nitrogen_fraction**   = (total N − ammoniacal N) / dry matter mass
        * **ammonium_fraction**           = ``AMMONIUM_FRACTION`` constant (0.75)

        An empty stream (total_solids ≤ 0) is silently skipped.
        """
        if stream.total_solids <= 0.0:
            return

        dry_matter_mass = stream.total_solids
        wet_mass = stream.mass
        dry_matter_fraction = dry_matter_mass / wet_mass if wet_mass > 0.0 else 0.12

        ammoniacal_nitrogen = stream.ammoniacal_nitrogen
        organic_nitrogen = max(0.0, stream.nitrogen - ammoniacal_nitrogen)

        inorganic_nitrogen_fraction = ammoniacal_nitrogen / dry_matter_mass
        organic_nitrogen_fraction = organic_nitrogen / dry_matter_mass

        field.manure_applicator.apply_grazing_manure(
            dry_matter_mass=dry_matter_mass,
            dry_matter_fraction=max(dry_matter_fraction, 1e-6),
            total_phosphorus_mass=stream.phosphorus,
            inorganic_nitrogen_fraction=inorganic_nitrogen_fraction,
            ammonium_fraction=AMMONIUM_FRACTION,
            organic_nitrogen_fraction=organic_nitrogen_fraction,
            field_size=field.field_data.field_size,
        )
