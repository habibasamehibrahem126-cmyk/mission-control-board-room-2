"""API: the only door to the model.   Steps 5 and 6

Run:  python -m src.api.app      then open http://127.0.0.1:5001

The dashboard is ready (dashboard/index.html). Each panel starts to work as soon as
the endpoint it calls exists. The endpoints are described in docs/api.md.
"""
import json

from flask import Flask, jsonify, request, send_from_directory

from src.api import rules
from src.api.data_access import load_launches
from src.common import (API_PORT, CLEAN_FILE, DASHBOARD_DIR, EXAMPLE_MISSION, LAUNCH_SITES,
                        METRICS_FILE, MODEL_FILE, ORBITS, PRICES_FILE)
from src.model import predict as model


def create_app(model_path=MODEL_FILE, prices_path=PRICES_FILE, metrics_path=METRICS_FILE,
               clean_path=CLEAN_FILE):
    app = Flask(__name__)

    @app.get("/")
    def dashboard():
        return send_from_directory(DASHBOARD_DIR, "index.html")

    # Already done: use it as your example.
    @app.get("/options")
    def options():
        return jsonify(orbits=ORBITS, launch_sites=LAUNCH_SITES)

    @app.post("/predict")
    def predict_endpoint():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify(error="Invalid JSON body"), 400

        errors = rules.validate(data)
        if errors:
            return jsonify(errors=errors), 400

        try:
            prob = model.predict(data, model_path=model_path)
        except FileNotFoundError as exc:
            return jsonify(error=str(exc)), 500

        prices = rules.load_prices(prices_path)
        return jsonify(
            probability=prob,
            certainty=rules.certainty(prob),
            expected_price_usd_million=rules.price(prob, prices),
        )

    @app.get("/metrics")
    def metrics():
        try:
            content = json.loads(metrics_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return jsonify(error="Metrics not found"), 404
        return jsonify(content)

    @app.get("/summary")
    def summary():
        records = load_launches(clean_path)
        return jsonify(records)

    return app


if __name__ == "__main__":
    create_app().run(port=API_PORT)
