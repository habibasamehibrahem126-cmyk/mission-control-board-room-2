"""Tests for the Board Room endpoint: GET /summary. They use the made-up sample table."""
from src.api.app import create_app
from src.common import SAMPLE_FILE


def summary():
    response = create_app(clean_path=SAMPLE_FILE).test_client().get("/summary")
    assert response.status_code == 200
    return response.get_json()


def test_totals():
    data = summary()
    assert data["launches"] == 30
    assert 0 <= data["landed"] <= data["launches"]
    assert abs(data["landing_rate"] - data["landed"] / data["launches"]) < 0.01


def test_each_group_adds_up_to_the_total():
    data = summary()
    for group, name in [("by_year", "year"), ("by_site", "site"), ("by_orbit", "orbit")]:
        assert sum(row["launches"] for row in data[group]) == data["launches"], group
        assert sum(row["landed"] for row in data[group]) == data["landed"], group
        assert name in data[group][0]
