import pytest

from RUFAS.data_structures.events import GrazingEvent
from RUFAS.biophysical.field.manager.grazing_schedule import GrazingSchedule


def _make_schedule(**kwargs) -> GrazingSchedule:
    """Helper to create a single-period GrazingSchedule with sensible defaults."""
    defaults = dict(
        name="test_schedule",
        start_years=[2019],
        start_days=[121],
        end_years=[2019],
        end_days=[123],
        num_animals_list=[50],
        daily_manure_dm_per_animal_list=[3.5],
        dry_matter_fractions=[0.12],
        phosphorus_fractions_of_dm=[0.0065],
        inorganic_nitrogen_fractions=[0.035],
        ammonium_fractions=[0.75],
        organic_nitrogen_fractions=[0.025],
    )
    defaults.update(kwargs)
    return GrazingSchedule(**defaults)


class TestGrazingScheduleGeneration:
    def test_generates_one_event_per_day(self):
        schedule = _make_schedule(start_days=[121], end_days=[123])
        events = schedule.generate_grazing_events()
        assert len(events) == 3  # days 121, 122, 123

    def test_event_day_values_are_correct(self):
        schedule = _make_schedule(start_days=[121], end_days=[123])
        events = schedule.generate_grazing_events()
        assert [e.day for e in events] == [121, 122, 123]

    def test_single_day_period(self):
        schedule = _make_schedule(start_days=[200], end_days=[200])
        events = schedule.generate_grazing_events()
        assert len(events) == 1
        assert events[0].day == 200

    def test_dry_matter_mass_is_num_animals_times_dm_per_animal(self):
        schedule = _make_schedule(num_animals_list=[100], daily_manure_dm_per_animal_list=[4.0])
        events = schedule.generate_grazing_events()
        for event in events:
            assert event.dry_matter_mass == pytest.approx(400.0)

    def test_phosphorus_mass_is_dm_times_p_fraction(self):
        schedule = _make_schedule(
            num_animals_list=[50],
            daily_manure_dm_per_animal_list=[3.5],
            phosphorus_fractions_of_dm=[0.0065],
        )
        events = schedule.generate_grazing_events()
        expected_p = 50 * 3.5 * 0.0065
        for event in events:
            assert event.total_phosphorus_mass == pytest.approx(expected_p)

    def test_events_are_grazing_event_instances(self):
        schedule = _make_schedule()
        events = schedule.generate_grazing_events()
        for event in events:
            assert isinstance(event, GrazingEvent)

    def test_events_sorted_chronologically(self):
        schedule = GrazingSchedule(
            name="multi_period",
            start_years=[2020, 2019],
            start_days=[121, 121],
            end_years=[2020, 2019],
            end_days=[121, 121],
            num_animals_list=[50, 50],
            daily_manure_dm_per_animal_list=[3.5, 3.5],
            dry_matter_fractions=[0.12, 0.12],
            phosphorus_fractions_of_dm=[0.0065, 0.0065],
            inorganic_nitrogen_fractions=[0.035, 0.035],
            ammonium_fractions=[0.75, 0.75],
            organic_nitrogen_fractions=[0.025, 0.025],
        )
        events = schedule.generate_grazing_events()
        years = [e.year for e in events]
        assert years == sorted(years)

    def test_empty_period_list_returns_no_events(self):
        schedule = GrazingSchedule(
            name="empty",
            start_years=[],
            start_days=[],
            end_years=[],
            end_days=[],
            num_animals_list=[],
            daily_manure_dm_per_animal_list=[],
            dry_matter_fractions=[],
            phosphorus_fractions_of_dm=[],
            inorganic_nitrogen_fractions=[],
            ammonium_fractions=[],
            organic_nitrogen_fractions=[],
        )
        events = schedule.generate_grazing_events()
        assert events == []

    def test_nutrient_fractions_stored_on_events(self):
        schedule = _make_schedule(
            inorganic_nitrogen_fractions=[0.035],
            ammonium_fractions=[0.75],
            organic_nitrogen_fractions=[0.025],
            dry_matter_fractions=[0.12],
        )
        events = schedule.generate_grazing_events()
        ev = events[0]
        assert ev.inorganic_nitrogen_fraction == pytest.approx(0.035)
        assert ev.ammonium_fraction == pytest.approx(0.75)
        assert ev.organic_nitrogen_fraction == pytest.approx(0.025)
        assert ev.dry_matter_fraction == pytest.approx(0.12)


class TestGrazingScheduleValidation:
    def test_end_before_start_raises(self):
        with pytest.raises(ValueError, match="end date.*before start date"):
            _make_schedule(start_days=[200], end_days=[199])

    def test_negative_num_animals_raises(self):
        with pytest.raises(ValueError, match="num_animals must be non-negative"):
            _make_schedule(num_animals_list=[-1])

    def test_zero_dry_matter_fraction_raises(self):
        with pytest.raises(ValueError, match="dry_matter_fraction must be in"):
            _make_schedule(dry_matter_fractions=[0.0])

    def test_phosphorus_fraction_above_1_raises(self):
        with pytest.raises(ValueError, match="phosphorus_fraction_of_dm.*must be in"):
            _make_schedule(phosphorus_fractions_of_dm=[1.1])

    def test_ammonium_fraction_above_1_raises(self):
        with pytest.raises(ValueError, match="ammonium_fraction.*must be in"):
            _make_schedule(ammonium_fractions=[1.5])
