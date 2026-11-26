"""API: the only door to the model.   Steps 5 and 6

Run:  python -m src.api.app      then open http://127.0.0.1:5001

The dashboard is ready (dashboard/index.html). Each panel starts to work as soon as
the endpoint it calls exists. The endpoints are described in docs/api.md.
"""
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

    # TODO (step 5): POST /predict

    # TODO (step 5): GET /metrics

    # TODO (step 6): the endpoints of your dashboard

    return app


if __name__ == "__main__":
    create_app().run(port=API_PORT)
