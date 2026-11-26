"""Model module: answer one prediction (contract C2).   Step 3"""
from pathlib import Path

import joblib
import pandas as pd

from src.common import FEATURES, MISSION_TO_COLUMN, MODEL_FILE


def mission_to_row(mission):
    """Already done: turn a mission dict into a one-row table with the model's column names."""
    return pd.DataFrame([{column: mission[field] for field, column in MISSION_TO_COLUMN.items()}])[FEATURES]


def predict(mission, model_path=MODEL_FILE):
    """Return the probability, from 0 to 1, that the first stage lands.

    Raise FileNotFoundError if no model has been trained yet.
    """
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(f"Model file not found: {path}")

    model = joblib.load(path)
    row = mission_to_row(mission)
    probs = model.predict_proba(row)
    return float(probs[0][1])
