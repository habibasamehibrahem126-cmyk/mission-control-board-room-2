"""Step 4 check: the rules in src/api/rules.py."""
from src.api import rules
from src.common import EXAMPLE_MISSION

PRICES = {"reused_price_usd_million": 60, "other_price_usd_million": 160}


def test_a_valid_mission_has_no_errors():
    assert rules.validate(EXAMPLE_MISSION) == {}


def test_each_wrong_value_is_named():
    wrong = [("payload_mass_kg", -1), ("payload_mass_kg", "heavy"), ("orbit", "MOON"),
             ("launch_site", "Cairo"), ("block", 9), ("flights", 0), ("reused", "yes")]
    for field, value in wrong:
        mission = dict(EXAMPLE_MISSION)
        mission[field] = value
        assert field in rules.validate(mission), f"{field} = {value!r} was accepted"


def test_a_missing_field_is_named():
    mission = dict(EXAMPLE_MISSION)
    del mission["orbit"]
    assert "orbit" in rules.validate(mission)


def test_certainty_levels():
    expected = [(0.95, "high"), (0.80, "high"), (0.10, "high"),
                (0.70, "medium"), (0.30, "medium"), (0.50, "low")]
    for probability, level in expected:
        assert rules.certainty(probability) == level, f"probability {probability}"


def test_price_rule():
    assert abs(rules.price(1.0, PRICES) - 60) < 0.01
    assert abs(rules.price(0.0, PRICES) - 160) < 0.01
    assert abs(rules.price(0.87, PRICES) - 73.0) < 0.01
