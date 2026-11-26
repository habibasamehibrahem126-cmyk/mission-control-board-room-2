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
    required_columns = [col for col in CLEAN_COLUMNS if col != "Class"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")


def clean(df):
    """Return the clean table. Do not change the DataFrame that was passed in."""
    table = df.copy()

    if "PayloadMass" in table.columns:
        median_mass = table["PayloadMass"].median()
        table["PayloadMass"] = table["PayloadMass"].fillna(median_mass)

    table["Class"] = table["Outcome"].astype(str).str.startswith("True").astype(int)

    table["Block"] = table["Block"].astype(int)
    for bool_col in ["Reused", "GridFins", "Legs"]:
        table[bool_col] = table[bool_col].astype(bool)

    return table[CLEAN_COLUMNS]


def build_report(raw, table):
    """Return {"rows_in": int, "rows_out": int, "missing_filled": {column: count}, "notes": [str]}."""
    payload_missing = int(raw["PayloadMass"].isnull().sum()) if "PayloadMass" in raw.columns else 0
    return {
        "rows_in": int(len(raw)),
        "rows_out": int(len(table)),
        "missing_filled": {"PayloadMass": payload_missing},
        "notes": [
            f"Filled {payload_missing} missing PayloadMass values.",
            "Left LandingPad blanks intact.",
        ],
    }


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
