"""Model module: train, evaluate and save the model.   Step 3

Run:  python -m src.model.train
If there is no clean table yet, this uses the made-up sample file.
"""
from datetime import datetime, timezone
import json

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.common import CLEAN_FILE, FEATURES, METRICS_FILE, MODEL_FILE, SAMPLE_FILE


def load_table(path=None):
    """Already done: the clean table if it exists, otherwise the made-up sample."""
    if path is None:
        path = CLEAN_FILE if CLEAN_FILE.exists() else SAMPLE_FILE
    print(f"Training data: {path}")
    return pd.read_csv(path, parse_dates=["Date"])


def split(table):
    """Return (train, test). Train on earlier launches, test on the most recent 20 percent."""
    ordered = table.sort_values("Date").reset_index(drop=True)
    split_idx = int(len(ordered) * 0.8)
    train = ordered.iloc[:split_idx].copy()
    test = ordered.iloc[split_idx:].copy()
    return train, test


def build_model():
    """Return an untrained scikit-learn model that accepts the FEATURES columns."""
    categorical_cols = ["Orbit", "LaunchSite"]
    numeric_cols = [col for col in FEATURES if col not in categorical_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", RandomForestClassifier(n_estimators=100, random_state=42)),
        ]
    )


def evaluate(model, train, test):
    """Return the metrics of contract C2:
    {"accuracy", "baseline_accuracy", "confusion_matrix", "n_train", "n_test", "trained_at"}.
    baseline_accuracy = accuracy of always answering the most common Class of the training set.
    The values must be plain Python types so they can be saved as JSON.
    """
    y_test = test["Class"].astype(int)
    preds = model.predict(test[FEATURES])

    most_common_class = int(train["Class"].mode().iloc[0])
    baseline_preds = [most_common_class] * len(test)

    cm = confusion_matrix(y_test, preds, labels=[0, 1]).tolist()

    return {
        "accuracy": float(accuracy_score(y_test, preds)),
        "baseline_accuracy": float(accuracy_score(y_test, baseline_preds)),
        "confusion_matrix": [[int(cell) for cell in row] for row in cm],
        "n_train": int(len(train)),
        "n_test": int(len(test)),
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }


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
