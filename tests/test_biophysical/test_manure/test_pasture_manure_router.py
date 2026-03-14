"""Tests for PastureManureRouter.

All tests bypass __init__ (which reads from InputManager) and instead construct
the router via object.__new__, injecting _configs directly.  This keeps the tests
hermetic and fast.
"""
import pytest

from RUFAS.biophysical.animal.data_types.animal_combination import AnimalCombination
from RUFAS.biophysical.manure.pasture_manure_router import (
    AMMONIUM_FRACTION,
    PastureManureRouter,
    _PasturePeriod,
    _PenPastureConfig,
)
from RUFAS.data_structures.animal_to_manure_connection import ManureStream
from RUFAS.output_manager import OutputManager


# ---------------------------------------------------------------------------
# Test helpers / fixtures
# ---------------------------------------------------------------------------


def _make_stream(
    total_solids: float = 10.0,
    water: float = 80.0,
    ammoniacal_nitrogen: float = 0.35,
    nitrogen: float = 0.50,
    phosphorus: float = 0.065,
) -> ManureStream:
    """Factory for a minimal ManureStream with the fields used by the router."""
    return ManureStream(
        water=water,
        ammoniacal_nitrogen=ammoniacal_nitrogen,
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=0.1,
        ash=0.0,
        degradable_volatile_solids=total_solids * 0.7,
        non_degradable_volatile_solids=total_solids * 0.3,
        bedding_non_degradable_volatile_solids=0.0,
        total_solids=total_solids,
        volume=0.09,
        methane_production_potential=0.17,
        pen_manure_data=None,
    )


class _ApplyCapture:
    """Captures the last call to apply_grazing_manure for inspection."""

    def __init__(self):
        self.calls: list[dict] = []

    def apply_grazing_manure(self, **kwargs):
        self.calls.append(kwargs)


class _MockField:
    """Minimal field-like object with manure_applicator and field_data."""

    def __init__(self, field_size: float = 10.0):
        self.manure_applicator = _ApplyCapture()

        class _FieldData:
            pass

        fd = _FieldData()
        fd.field_size = field_size
        self.field_data = fd


class _MockFieldManager:
    def __init__(self, fields: dict):
        self._fields = fields

    def get_field_by_name(self, name: str):
        return self._fields.get(name)


class _MockTime:
    def __init__(self, julian_day: int):
        self.current_julian_day = julian_day


def _make_router(*configs: _PenPastureConfig) -> PastureManureRouter:
    """Construct a PastureManureRouter without touching InputManager."""
    router = object.__new__(PastureManureRouter)
    router._configs = list(configs)
    router._om = OutputManager()
    return router


def _make_period(start: int, end: int, field: str = "field_3") -> _PasturePeriod:
    return _PasturePeriod(start_day=start, end_day=end, pasture_field=field)


def _make_config(
    pen_id: int = 1,
    combination: AnimalCombination = AnimalCombination.GROWING,
    periods: list[_PasturePeriod] | None = None,
) -> _PenPastureConfig:
    return _PenPastureConfig(
        pen_id=pen_id,
        animal_combination=combination,
        periods=periods or [_make_period(121, 273)],
    )


# ---------------------------------------------------------------------------
# _get_active_period
# ---------------------------------------------------------------------------


class TestGetActivePeriod:
    def test_returns_period_when_day_is_in_range(self):
        period = _make_period(121, 273)
        result = PastureManureRouter._get_active_period([period], 150)
        assert result is period

    def test_returns_period_on_start_day(self):
        period = _make_period(121, 273)
        assert PastureManureRouter._get_active_period([period], 121) is period

    def test_returns_period_on_end_day(self):
        period = _make_period(121, 273)
        assert PastureManureRouter._get_active_period([period], 273) is period

    def test_returns_none_before_start(self):
        period = _make_period(121, 273)
        assert PastureManureRouter._get_active_period([period], 120) is None

    def test_returns_none_after_end(self):
        period = _make_period(121, 273)
        assert PastureManureRouter._get_active_period([period], 274) is None

    def test_returns_none_for_empty_periods(self):
        assert PastureManureRouter._get_active_period([], 150) is None

    def test_returns_first_matching_period(self):
        p1 = _make_period(100, 200, "field_a")
        p2 = _make_period(150, 250, "field_b")
        result = PastureManureRouter._get_active_period([p1, p2], 175)
        assert result is p1


# ---------------------------------------------------------------------------
# has_pasture_config
# ---------------------------------------------------------------------------


class TestHasPastureConfig:
    def test_false_when_no_configs(self):
        router = _make_router()
        assert router.has_pasture_config is False

    def test_true_when_configs_present(self):
        router = _make_router(_make_config())
        assert router.has_pasture_config is True


# ---------------------------------------------------------------------------
# route_pasture_manure – pass-through when outside period
# ---------------------------------------------------------------------------


class TestRouteOutsidePeriod:
    def test_all_streams_passed_through_when_no_config(self):
        router = _make_router()
        streams = {"grow_pen_GROWING_PEN_1": _make_stream()}
        result = router.route_pasture_manure(streams, _MockFieldManager({}), _MockTime(150))
        assert result is streams  # unchanged object returned

    def test_streams_unchanged_when_day_outside_period(self):
        router = _make_router(_make_config(periods=[_make_period(121, 273)]))
        key = "grow_pen_GROWING_PEN_1"
        streams = {key: _make_stream()}
        time = _MockTime(300)  # after Sep 30
        result = router.route_pasture_manure(streams, _MockFieldManager({}), time)
        assert key in result

    def test_unrelated_stream_always_passed_through(self):
        router = _make_router(_make_config())
        key = "early_lac_pen_LAC_COW_PEN_3"
        streams = {key: _make_stream()}
        result = router.route_pasture_manure(streams, _MockFieldManager({}), _MockTime(150))
        assert key in result


# ---------------------------------------------------------------------------
# route_pasture_manure – routing during pasture period
# ---------------------------------------------------------------------------


class TestRouteDuringPeriod:
    def _setup(self, julian_day: int = 150):
        field = _MockField(field_size=10.0)
        fm = _MockFieldManager({"field_3": field})
        router = _make_router(_make_config())
        stream = _make_stream()
        streams = {"grow_pen_GROWING_PEN_1": stream}
        remaining = router.route_pasture_manure(streams, fm, _MockTime(julian_day))
        return remaining, field

    def test_pasture_stream_removed_from_remaining(self):
        remaining, _ = self._setup()
        assert "grow_pen_GROWING_PEN_1" not in remaining

    def test_apply_grazing_manure_called_once(self):
        _, field = self._setup()
        assert len(field.manure_applicator.calls) == 1

    def test_dry_matter_mass_equals_total_solids(self):
        stream = _make_stream(total_solids=12.0)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert field.manure_applicator.calls[0]["dry_matter_mass"] == pytest.approx(12.0)

    def test_phosphorus_mass_equals_stream_phosphorus(self):
        stream = _make_stream(phosphorus=0.065)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert field.manure_applicator.calls[0]["total_phosphorus_mass"] == pytest.approx(0.065)

    def test_ammonium_fraction_is_constant(self):
        stream = _make_stream()
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert field.manure_applicator.calls[0]["ammonium_fraction"] == pytest.approx(AMMONIUM_FRACTION)

    def test_inorganic_nitrogen_fraction_derived_correctly(self):
        stream = _make_stream(total_solids=10.0, ammoniacal_nitrogen=0.5)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        expected = 0.5 / 10.0
        assert field.manure_applicator.calls[0]["inorganic_nitrogen_fraction"] == pytest.approx(expected)

    def test_organic_nitrogen_fraction_derived_correctly(self):
        # total_n=0.8, ammoniacal_n=0.5 → organic_n=0.3, fraction=0.3/10
        stream = _make_stream(total_solids=10.0, ammoniacal_nitrogen=0.5, nitrogen=0.8)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        expected = (0.8 - 0.5) / 10.0
        assert field.manure_applicator.calls[0]["organic_nitrogen_fraction"] == pytest.approx(expected)

    def test_dry_matter_fraction_derived_from_total_solids_and_mass(self):
        # total_solids=10, water=90 → mass=100, dm_fraction=0.1
        stream = _make_stream(total_solids=10.0, water=90.0)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert field.manure_applicator.calls[0]["dry_matter_fraction"] == pytest.approx(10.0 / 100.0)

    def test_field_size_passed_correctly(self):
        stream = _make_stream()
        field = _MockField(field_size=25.0)
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert field.manure_applicator.calls[0]["field_size"] == pytest.approx(25.0)

    def test_other_streams_unaffected(self):
        field = _MockField()
        fm = _MockFieldManager({"field_3": field})
        router = _make_router(_make_config())
        other_key = "calf_pen_CALF_PEN_0"
        streams = {
            "grow_pen_GROWING_PEN_1": _make_stream(),
            other_key: _make_stream(),
        }
        remaining = router.route_pasture_manure(streams, fm, _MockTime(150))
        assert other_key in remaining


# ---------------------------------------------------------------------------
# route_pasture_manure – field not found
# ---------------------------------------------------------------------------


class TestRouteFieldNotFound:
    def test_stream_passed_through_when_field_missing(self):
        router = _make_router(_make_config())
        key = "grow_pen_GROWING_PEN_1"
        streams = {key: _make_stream()}
        # Field manager returns None for any name
        result = router.route_pasture_manure(streams, _MockFieldManager({}), _MockTime(150))
        assert key in result


# ---------------------------------------------------------------------------
# _apply_stream_to_field – edge cases
# ---------------------------------------------------------------------------


class TestApplyStreamToField:
    def test_empty_stream_is_skipped(self):
        stream = _make_stream(total_solids=0.0)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert len(field.manure_applicator.calls) == 0

    def test_dry_matter_fraction_floor_prevents_zero(self):
        # zero water AND zero total_solids edge case: total_solids=1, water=0 → mass=1, dm=1.0
        stream = _make_stream(total_solids=1.0, water=0.0)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        call = field.manure_applicator.calls[0]
        assert call["dry_matter_fraction"] > 0.0

    def test_organic_nitrogen_clamped_to_zero_when_ammoniacal_exceeds_total(self):
        # ammoniacal_nitrogen slightly > nitrogen (floating-point edge)
        stream = _make_stream(total_solids=10.0, ammoniacal_nitrogen=0.5, nitrogen=0.49)
        field = _MockField()
        PastureManureRouter._apply_stream_to_field(stream, field)
        assert field.manure_applicator.calls[0]["organic_nitrogen_fraction"] >= 0.0
