"""Already done: read the launch table for the dashboard endpoints."""
import pandas as pd

from src.common import CLEAN_FILE, SAMPLE_FILE


def load_launches(path=CLEAN_FILE):
    """The clean table, or the made-up sample if you have not built it yet."""
    if not path.exists():
        path = SAMPLE_FILE
    return pd.read_csv(path)
