import json
from pathlib import Path
from typing import Any

import pandas as pd

from src.config.settings import SCAN_FILE, OBJECT_FILE, SNAPSHOT_FILE


def _safe_read_json(file_path: Path) -> Any:
    """
    Safely read a JSON file and return parsed content.
    Returns [] fallback if file is missing/invalid.
    """
    try:
        if not file_path.exists():
            return []

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        if not content:
            return []

        return json.loads(content)

    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON in file: {file_path}")
        return []
    except Exception as e:
        print(f"[ERROR] Failed to read file {file_path}: {e}")
        return []


def load_scan_data() -> pd.DataFrame:
    """
    Load scan data from sample_scan.json into a DataFrame.
    Expected fields:
    - scan_id
    - timestamp
    - angle_deg
    - distance_cm
    """
    data = _safe_read_json(SCAN_FILE)

    if not isinstance(data, list):
        data = []

    df = pd.DataFrame(data)

    if df.empty:
        return pd.DataFrame(columns=["scan_id", "timestamp", "angle_deg", "distance_cm"])

    return df


def load_object_data() -> pd.DataFrame:
    """
    Load fused object data from sample_objects.json into a DataFrame.
    Expected fields:
    - timestamp
    - label
    - confidence
    - angle_deg
    - distance_cm
    - x
    - y
    """
    data = _safe_read_json(OBJECT_FILE)

    if not isinstance(data, list):
        data = []

    df = pd.DataFrame(data)

    if df.empty:
        return pd.DataFrame(
            columns=["timestamp", "label", "confidence", "angle_deg", "distance_cm", "x", "y"]
        )

    return df


def load_latest_snapshot() -> dict:
    """
    Load latest snapshot JSON.
    Expected structure:
    {
      "scan_points": [...],
      "objects": [...]
    }
    """
    data = _safe_read_json(SNAPSHOT_FILE)

    if not isinstance(data, dict):
        return {"scan_points": [], "objects": []}

    data.setdefault("scan_points", [])
    data.setdefault("objects", [])

    return data