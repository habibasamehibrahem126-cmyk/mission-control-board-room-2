"""Step 2 check: the clean table. They fail until you build the functions."""
import pandas as pd

from src.common import CLEAN_COLUMNS, RAW_API_FILE
from src.data.prepare import build_report, check_columns, clean


def load():
    return pd.read_csv(RAW_API_FILE)


def test_a_missing_column_is_named():
    broken = load().drop(columns=["Orbit"])
    try:
        check_columns(broken)
    except ValueError as error:
        assert "Orbit" in str(error)
    else:
        assert False, "check_columns accepted a file without the Orbit column"


def test_columns_follow_the_contract():
    assert list(clean(load()).columns) == CLEAN_COLUMNS


def test_only_the_landing_pad_may_be_blank():
    table = clean(load())
    assert table.drop(columns=["LandingPad"]).isnull().sum().sum() == 0


def test_label_is_0_or_1_and_follows_the_outcome():
    table = clean(load())
    assert set(table["Class"]) == {0, 1}
    landed = table["Outcome"].str.startswith("True")
    assert (table.loc[landed, "Class"] == 1).all()
    assert (table.loc[~landed, "Class"] == 0).all()


def test_the_raw_data_is_not_changed():
    raw = load()
    before = raw.copy()
    clean(raw)
    assert raw.equals(before)


def test_report_counts_what_was_filled():
    raw = load()
    report = build_report(raw, clean(raw))
    assert report["rows_in"] == len(raw)
    assert report["missing_filled"]["PayloadMass"] == raw["PayloadMass"].isnull().sum()
