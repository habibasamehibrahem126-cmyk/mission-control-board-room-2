"""API module: the business rules.   Step 4"""
import json

from src.common import LAUNCH_SITES, ORBITS, PRICES_FILE


def validate(mission):
    """Return {field: message} for every field that is missing or wrong. Return {} if all is well.

    payload_mass_kg: a number above 0        orbit: one of ORBITS
    launch_site: one of LAUNCH_SITES         block: a whole number from 1 to 5
    flights: a whole number, 1 or more       reused, grid_fins, legs: True or False
    """
    errors = {}

    mass = mission.get("payload_mass_kg")
    if isinstance(mass, bool) or not isinstance(mass, (int, float)) or mass <= 0:
        errors["payload_mass_kg"] = "must be a number above 0"

    if mission.get("orbit") not in ORBITS:
        errors["orbit"] = "must be one of ORBITS"

    if mission.get("launch_site") not in LAUNCH_SITES:
        errors["launch_site"] = "must be one of LAUNCH_SITES"

    block = mission.get("block")
    if isinstance(block, bool) or not isinstance(block, int) or not 1 <= block <= 5:
        errors["block"] = "must be a whole number from 1 to 5"

    flights = mission.get("flights")
    if isinstance(flights, bool) or not isinstance(flights, int) or flights < 1:
        errors["flights"] = "must be a whole number, 1 or more"

    for field in ("reused", "grid_fins", "legs"):
        if not isinstance(mission.get(field), bool):
            errors[field] = "must be True or False"

    return errors


def certainty(probability):
    """Return "high", "medium" or "low".

    high:   0.80 or more, or 0.20 or less
    medium: 0.65 or more, or 0.35 or less
    low:    everything else
    """
    if probability >= 0.80 or probability <= 0.20:
        return "high"
    if probability >= 0.65 or probability <= 0.35:
        return "medium"
    return "low"


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
    if prices is None:
        return None
    reused_price = prices["reused_price_usd_million"]
    other_price = prices["other_price_usd_million"]
    return probability * reused_price + (1 - probability) * other_price
