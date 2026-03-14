from __future__ import annotations

from datetime import timedelta

from RUFAS.data_structures.events import GrazingEvent
from RUFAS.rufas_time import RufasTime
from RUFAS.util import Utility


class GrazingSchedule:
    """
    Defines one or more seasonal grazing periods for a pasture field and generates a daily GrazingEvent for each day
    animals are on the pasture.

    Each grazing period spans a continuous range of days (start to end, inclusive). For every calendar day within
    that range, one GrazingEvent is generated, representing the manure deposited on that day by the grazing herd.

    Parameters
    ----------
    name : str
        Unique name for this grazing schedule.
    start_years : list[int]
        Calendar year(s) in which each grazing period begins.
    start_days : list[int]
        Julian day(s) on which each grazing period begins.
    end_years : list[int]
        Calendar year(s) in which each grazing period ends.
    end_days : list[int]
        Julian day(s) on which each grazing period ends (inclusive).
    num_animals_list : list[int]
        Number of animals on the pasture during each period.
    daily_manure_dm_per_animal_list : list[float]
        Daily dry matter manure production per animal (kg DM/animal/day).
    dry_matter_fractions : list[float]
        Dry matter fraction of manure (unitless), in the range (0.0, 1.0].
    phosphorus_fractions_of_dm : list[float]
        Fraction of manure dry matter that is total phosphorus (kg P / kg DM).
    inorganic_nitrogen_fractions : list[float]
        Fraction of manure dry matter that is inorganic nitrogen (kg inorganic N / kg DM).
    ammonium_fractions : list[float]
        Fraction of inorganic nitrogen that is ammonium (unitless).
    organic_nitrogen_fractions : list[float]
        Fraction of manure dry matter that is organic nitrogen (kg organic N / kg DM).

    Notes
    -----
    All list parameters must have the same length, corresponding to the number of grazing periods defined.
    Unlike the pattern-based Schedule subclasses, GrazingSchedule periods are specified explicitly.

    References
    ----------
    James E., Kleinman P., Veith T., Stedman R., Sharpley A. (2007) Phosphorus contributions from
        pastured dairy cattle to streams of the Cannonsville Watershed, New York. Journal of Soil
        and Water Conservation 62:40-47.

    """

    def __init__(
        self,
        name: str,
        start_years: list[int],
        start_days: list[int],
        end_years: list[int],
        end_days: list[int],
        num_animals_list: list[int],
        daily_manure_dm_per_animal_list: list[float],
        dry_matter_fractions: list[float],
        phosphorus_fractions_of_dm: list[float],
        inorganic_nitrogen_fractions: list[float],
        ammonium_fractions: list[float],
        organic_nitrogen_fractions: list[float],
    ):
        self.name = name
        self.start_years = start_years
        self.start_days = Utility.elongate_list(start_days, len(start_years))
        self.end_years = Utility.elongate_list(end_years, len(start_years))
        self.end_days = Utility.elongate_list(end_days, len(start_years))
        self.num_animals_list = Utility.elongate_list(num_animals_list, len(start_years))
        self.daily_manure_dm_per_animal_list = Utility.elongate_list(
            daily_manure_dm_per_animal_list, len(start_years)
        )
        self.dry_matter_fractions = Utility.elongate_list(dry_matter_fractions, len(start_years))
        self.phosphorus_fractions_of_dm = Utility.elongate_list(phosphorus_fractions_of_dm, len(start_years))
        self.inorganic_nitrogen_fractions = Utility.elongate_list(inorganic_nitrogen_fractions, len(start_years))
        self.ammonium_fractions = Utility.elongate_list(ammonium_fractions, len(start_years))
        self.organic_nitrogen_fractions = Utility.elongate_list(organic_nitrogen_fractions, len(start_years))

        self._validate()

    def _validate(self) -> None:
        """
        Validates that all grazing period parameters are consistent and within valid ranges.

        Raises
        ------
        ValueError
            If any list lengths are inconsistent, or if any parameter value is out of range.

        """
        n = len(self.start_years)
        lists_to_check = {
            "start_days": self.start_days,
            "end_years": self.end_years,
            "end_days": self.end_days,
            "num_animals_list": self.num_animals_list,
            "daily_manure_dm_per_animal_list": self.daily_manure_dm_per_animal_list,
            "dry_matter_fractions": self.dry_matter_fractions,
            "phosphorus_fractions_of_dm": self.phosphorus_fractions_of_dm,
            "inorganic_nitrogen_fractions": self.inorganic_nitrogen_fractions,
            "ammonium_fractions": self.ammonium_fractions,
            "organic_nitrogen_fractions": self.organic_nitrogen_fractions,
        }
        for param_name, param_list in lists_to_check.items():
            if len(param_list) != n:
                raise ValueError(
                    f"'{self.name}': '{param_name}' length {len(param_list)} does not match "
                    f"'start_years' length {n}."
                )

        for i in range(n):
            start = RufasTime.convert_year_jday_to_date(self.start_years[i], self.start_days[i])
            end = RufasTime.convert_year_jday_to_date(self.end_years[i], self.end_days[i])
            if end < start:
                raise ValueError(
                    f"'{self.name}': Period {i} end date ({end.date()}) is before start date ({start.date()})."
                )
            if self.num_animals_list[i] < 0:
                raise ValueError(
                    f"'{self.name}': Period {i} num_animals must be non-negative, "
                    f"received {self.num_animals_list[i]}."
                )
            if self.daily_manure_dm_per_animal_list[i] < 0:
                raise ValueError(
                    f"'{self.name}': Period {i} daily_manure_dm_per_animal must be non-negative."
                )
            if not 0.0 < self.dry_matter_fractions[i] <= 1.0:
                raise ValueError(
                    f"'{self.name}': Period {i} dry_matter_fraction must be in (0.0, 1.0], "
                    f"received {self.dry_matter_fractions[i]}."
                )
            for frac_name, frac_val in [
                ("phosphorus_fraction_of_dm", self.phosphorus_fractions_of_dm[i]),
                ("inorganic_nitrogen_fraction", self.inorganic_nitrogen_fractions[i]),
                ("ammonium_fraction", self.ammonium_fractions[i]),
                ("organic_nitrogen_fraction", self.organic_nitrogen_fractions[i]),
            ]:
                if not 0.0 <= frac_val <= 1.0:
                    raise ValueError(
                        f"'{self.name}': Period {i} '{frac_name}' must be in [0.0, 1.0], "
                        f"received {frac_val}."
                    )

    def generate_grazing_events(self) -> list[GrazingEvent]:
        """
        Generates one GrazingEvent for every day in each specified grazing period.

        Returns
        -------
        list[GrazingEvent]
            Daily grazing events across all defined grazing periods, sorted chronologically.

        """
        events: list[GrazingEvent] = []

        for i in range(len(self.start_years)):
            start_dt = RufasTime.convert_year_jday_to_date(self.start_years[i], self.start_days[i])
            end_dt = RufasTime.convert_year_jday_to_date(self.end_years[i], self.end_days[i])

            num_animals = self.num_animals_list[i]
            dm_per_animal = self.daily_manure_dm_per_animal_list[i]
            dm_fraction = self.dry_matter_fractions[i]
            p_fraction = self.phosphorus_fractions_of_dm[i]
            inorganic_n_fraction = self.inorganic_nitrogen_fractions[i]
            ammonium_fraction = self.ammonium_fractions[i]
            organic_n_fraction = self.organic_nitrogen_fractions[i]

            total_dm_mass = num_animals * dm_per_animal
            total_phosphorus_mass = total_dm_mass * p_fraction

            current_dt = start_dt
            while current_dt <= end_dt:
                tt = current_dt.timetuple()
                event = GrazingEvent(
                    year=tt.tm_year,
                    day=tt.tm_yday,
                    dry_matter_mass=total_dm_mass,
                    dry_matter_fraction=dm_fraction,
                    total_phosphorus_mass=total_phosphorus_mass,
                    inorganic_nitrogen_fraction=inorganic_n_fraction,
                    ammonium_fraction=ammonium_fraction,
                    organic_nitrogen_fraction=organic_n_fraction,
                )
                events.append(event)
                current_dt += timedelta(days=1)

        return sorted(events, key=lambda e: (e.year, e.day))
