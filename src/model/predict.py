"""Model module: answer one prediction (contract C2).   Step 3"""
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
    # TODO: load the saved model with joblib, then use predict_proba on mission_to_row(mission).
    return 0.5  # stand-in: replace it in step 3
