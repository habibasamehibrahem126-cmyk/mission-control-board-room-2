"""Step 5 check: /predict and /metrics. The first two pass from the start."""
import json

import pytest

from src.api.app import create_app
from src.common import EXAMPLE_MISSION, MODEL_FILE
from tests.stand_in import stand_in_model

# made-up figures: the real ones stay out of git
PRICES = {"reused_price_usd_million": 60, "other_price_usd_million": 160}
NO_FILE = MODEL_FILE.with_name("there_is_no_such_file")
TEST_PRICES = MODEL_FILE.with_name("test_prices.json")


@pytest.fixture
def client():
    TEST_PRICES.write_text(json.dumps(PRICES))
    return create_app(model_path=stand_in_model(), prices_path=TEST_PRICES, metrics_path=NO_FILE).test_client()


def test_the_dashboard_opens(client):
    assert client.get("/").status_code == 200


def test_options(client):
    assert "orbits" in client.get("/options").get_json()


def test_predict_answers_a_valid_mission(client):
    response = client.post("/predict", json=EXAMPLE_MISSION)
    assert response.status_code == 200, "is POST /predict built?"
    answer = response.get_json()
    for key in ["lands", "probability", "certainty", "price_usd_million"]:
        assert key in answer


def test_predict_names_a_wrong_field(client):
    mission = dict(EXAMPLE_MISSION, payload_mass_kg=-5)
    response = client.post("/predict", json=mission)
    assert response.status_code == 422
    assert "payload_mass_kg" in response.get_json()["fields"]


def test_no_price_file_means_no_price():
    app = create_app(model_path=stand_in_model(), prices_path=NO_FILE, metrics_path=NO_FILE)
    response = app.test_client().post("/predict", json=EXAMPLE_MISSION)
    assert response.status_code == 200
    assert response.get_json()["price_usd_million"] is None
    assert response.get_json()["price_note"]


def test_metrics_without_a_model(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "note" in response.get_json()
