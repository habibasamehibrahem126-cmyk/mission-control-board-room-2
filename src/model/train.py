"""Model module: train, evaluate and save the model.   Step 3

Run:  python -m src.model.train
If there is no clean table yet, this uses the made-up sample file.
"""
import json

import joblib
import pandas as pd

from src.common import CLEAN_FILE, FEATURES, METRICS_FILE, MODEL_FILE, SAMPLE_FILE


def load_table(path=None):
    """Already done: the clean table if it exists, otherwise the made-up sample."""
    if path is None:
        path = CLEAN_FILE if CLEAN_FILE.exists() else SAMPLE_FILE
    print(f"Training data: {path}")
    return pd.read_csv(path, parse_dates=["Date"])


def split(table):
    """Return (train, test). Train on earlier launches, test on the most recent 20 percent."""
    # TODO: sort by Date, then cut.
    raise NotImplementedError


def build_model():
    """Return an untrained scikit-learn model that accepts the FEATURES columns."""
    # TODO: Orbit and LaunchSite are text, so encode them (OneHotEncoder inside a Pipeline).
    #       Use a fixed random_state so the same data always gives the same model.
    raise NotImplementedError


def evaluate(model, train, test):
    """Return the metrics of contract C2:
    {"accuracy", "baseline_accuracy", "confusion_matrix", "n_train", "n_test", "trained_at"}.
    baseline_accuracy = accuracy of always answering the most common Class of the training set.
    The values must be plain Python types so they can be saved as JSON.
    """
    # TODO
    raise NotImplementedError


def main(table_path=None, model_path=MODEL_FILE, metrics_path=METRICS_FILE):
    """Already done: split, train, evaluate, save."""
    table = load_table(table_path)
    train, test = split(table)
    model = build_model()
    model.fit(train[FEATURES], train["Class"])
    metrics = evaluate(model, train, test)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
