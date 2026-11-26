"""Data module: turn the raw file into the clean table (contract C1).   Step 2

Run:  python -m src.data.prepare
"""
import json

import pandas as pd

from src.common import CLEAN_COLUMNS, CLEAN_FILE, QUALITY_FILE, RAW_API_FILE


def load_raw(path=RAW_API_FILE):
    """Already done: read the raw file."""
    return pd.read_csv(path)


def check_columns(df):
    """Raise ValueError, naming the column, if a column the clean table needs is missing."""
    # TODO: which of CLEAN_COLUMNS must already be in the raw file? (Class is not one of them.)
    raise NotImplementedError


def clean(df):
    """Return the clean table. Do not change the DataFrame that was passed in."""
    # TODO 1: work on a copy.
    # TODO 2: find the missing values. Fill the missing PayloadMass. A blank LandingPad stays blank.
    # TODO 3: add Class: 1 if the first stage landed, 0 if not.
    #         Look at df["Outcome"].value_counts() first, and read docs/requirements.md.
    # TODO 4: make Block a whole number and the True/False columns booleans.
    # TODO 5: return exactly the columns in CLEAN_COLUMNS, in that order.
    raise NotImplementedError


def build_report(raw, table):
    """Return {"rows_in": int, "rows_out": int, "missing_filled": {column: count}, "notes": [str]}."""
    # TODO
    raise NotImplementedError


def main(raw_path=RAW_API_FILE, clean_path=CLEAN_FILE, report_path=QUALITY_FILE):
    """Already done: check, clean, then save. Nothing is saved if a step fails."""
    raw = load_raw(raw_path)
    check_columns(raw)
    table = clean(raw)
    report = build_report(raw, table)
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(clean_path, index=False)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Saved {len(table)} rows to {clean_path}")


if __name__ == "__main__":
    main()
