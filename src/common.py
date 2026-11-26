"""Everything the modules agree on (the contracts). Change this file only if the whole team agrees."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# files
RAW_API_FILE = ROOT / "data" / "raw" / "launches_api.csv"
SAMPLE_FILE = ROOT / "data" / "sample" / "launches_clean_sample.csv"
CLEAN_FILE = ROOT / "data" / "processed" / "launches_clean.csv"
QUALITY_FILE = ROOT / "data" / "processed" / "quality_report.json"
MODEL_FILE = ROOT / "models" / "model.joblib"
METRICS_FILE = ROOT / "models" / "metrics.json"
PRICES_FILE = ROOT / "config" / "prices.local.json"
DASHBOARD_DIR = ROOT / "dashboard"

# ports
API_PORT = 5001

# allowed values (taken from the data)
ORBITS = ["LEO", "VLEO", "ISS", "PO", "SSO", "SO", "MEO", "GTO", "GEO", "HEO", "ES-L1"]
LAUNCH_SITES = ["CCAFS SLC 40", "KSC LC 39A", "VAFB SLC 4E"]

# contract C1: the clean table
FEATURES = ["PayloadMass", "Orbit", "LaunchSite", "Block", "Reused", "Flights", "GridFins", "Legs"]
CLEAN_COLUMNS = ["Class", *FEATURES, "Date", "Outcome", "Serial", "LandingPad", "Longitude", "Latitude"]

# contract C2 and C3: a mission, and the column each field belongs to
MISSION_TO_COLUMN = {
    "payload_mass_kg": "PayloadMass",
    "orbit": "Orbit",
    "launch_site": "LaunchSite",
    "block": "Block",
    "reused": "Reused",
    "flights": "Flights",
    "grid_fins": "GridFins",
    "legs": "Legs",
}

EXAMPLE_MISSION = {
    "payload_mass_kg": 5500,
    "orbit": "GTO",
    "launch_site": "CCAFS SLC 40",
    "block": 5,
    "reused": True,
    "flights": 3,
    "grid_fins": True,
    "legs": True,
}
