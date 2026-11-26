"""API module: the business rules.   Step 4"""
import json

from src.common import LAUNCH_SITES, ORBITS, PRICES_FILE


def validate(mission):
    """Return {field: message} for every field that is missing or wrong. Return {} if all is well.

    payload_mass_kg: a number above 0        orbit: one of ORBITS
    launch_site: one of LAUNCH_SITES         block: a whole number from 1 to 5
    flights: a whole number, 1 or more       reused, grid_fins, legs: True or False
    """
    # TODO
    raise NotImplementedError


def certainty(probability):
    """Return "high", "medium" or "low".

    high:   0.80 or more, or 0.20 or less
    medium: 0.65 or more, or 0.35 or less
    low:    everything else
    """
    # TODO
    raise NotImplementedError


def load_prices(path=PRICES_FILE):
    """Already done: return the price figures, or None if the file is missing or not filled in."""
    try:
        prices = json.loads(path.read_text(encoding="utf-8"))
        if prices["reused_price_usd_million"] > 0 and prices["other_price_usd_million"] > 0:
            return prices
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None


def price(probability, prices):
    """Return the expected launch price in USD million (see docs/requirements.md, REQ-04)."""
    # TODO
    raise NotImplementedError
