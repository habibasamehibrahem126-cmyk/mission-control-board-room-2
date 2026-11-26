"""Already done: a tiny stand-in model, so the API tests do not depend on your model."""
import joblib
import pandas as pd
from sklearn.dummy import DummyClassifier

from src.common import FEATURES, MODEL_FILE, SAMPLE_FILE


def stand_in_model():
    path = MODEL_FILE.with_name("stand_in_model.joblib")
    table = pd.read_csv(SAMPLE_FILE)
    joblib.dump(DummyClassifier(strategy="prior").fit(table[FEATURES], table["Class"]), path)
    return path
