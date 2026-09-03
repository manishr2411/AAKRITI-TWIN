from pathlib import Path

# Project root: person4_dashboard/
BASE_DIR = Path(__file__).resolve().parents[2]

# Data files
DATA_DIR = BASE_DIR / "data"
SCAN_FILE = DATA_DIR / "live_scan.json"
OBJECT_FILE = DATA_DIR / "live_objects.json"
SNAPSHOT_FILE = DATA_DIR / "latest_snapshot.json"

# Dashboard settings
APP_TITLE = "AI Environment Digital Twin"
APP_ICON = "🛰️"

# Map settings
MAP_TITLE = "Live 2D Environment Map"
X_LIMIT = (-200, 200)
Y_LIMIT = (0, 200)

# Refresh / display
DEFAULT_REFRESH_SECONDS = 2
MAX_POINTS_TO_SHOW = 500