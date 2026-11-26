"""Step 3 check: the model. It uses the made-up sample."""
import joblib
import pandas as pd

from src.common import EXAMPLE_MISSION, FEATURES, MODEL_FILE, SAMPLE_FILE
from src.model.predict import mission_to_row, predict
from src.model.train import build_model, evaluate, main, split

TEST_MODEL = MODEL_FILE.with_name("test_model.joblib")
TEST_METRICS = MODEL_FILE.with_name("test_metrics.json")


def load():
    return pd.read_csv(SAMPLE_FILE, parse_dates=["Date"])


def test_test_set_is_the_most_recent_launches():
    table = load()
    train, test = split(table)
    assert len(train) + len(test) == len(table)
    assert train["Date"].max() <= test["Date"].min()


def test_model_gives_probabilities():
    table = load()
    model = build_model()
    model.fit(table[FEATURES], table["Class"])
    assert model.predict_proba(table[FEATURES]).shape == (len(table), 2)


def test_metrics_follow_the_contract():
    train, test = split(load())
    model = build_model()
    model.fit(train[FEATURES], train["Class"])
    metrics = evaluate(model, train, test)
    for key in ["accuracy", "baseline_accuracy", "confusion_matrix", "n_train", "n_test", "trained_at"]:
        assert key in metrics
    assert 0 <= metrics["accuracy"] <= 1


def test_predict_uses_the_saved_model():
    main(SAMPLE_FILE, TEST_MODEL, TEST_METRICS)
    model = joblib.load(TEST_MODEL)
    expected = model.predict_proba(mission_to_row(EXAMPLE_MISSION))[0][1]
    assert abs(predict(EXAMPLE_MISSION, TEST_MODEL) - expected) < 0.000001
