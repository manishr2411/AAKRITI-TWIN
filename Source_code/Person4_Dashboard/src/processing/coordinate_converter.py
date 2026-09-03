import math

import pandas as pd


def polar_to_cartesian(angle_deg: float, distance_cm: float) -> tuple[float, float]:
    """
    Convert angle (degrees) and distance (cm) into x, y coordinates.

    Assumption:
    - 90 degrees = straight ahead
    - 0 degrees = right side
    - 180 degrees = left side
    """
    angle_rad = math.radians(angle_deg)

    x = distance_cm * math.cos(angle_rad)
    y = distance_cm * math.sin(angle_rad)

    return round(x, 2), round(y, 2)


def convert_scan_to_xy(scan_df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert scan DataFrame with angle_deg and distance_cm into x, y coordinates.
    Returns the same DataFrame with added x and y columns.
    """
    if scan_df.empty:
        result = scan_df.copy()
        result["x"] = []
        result["y"] = []
        return result

    result = scan_df.copy()

    coords = result.apply(
        lambda row: polar_to_cartesian(row["angle_deg"], row["distance_cm"]),
        axis=1
    )

    result["x"] = coords.apply(lambda item: item[0])
    result["y"] = coords.apply(lambda item: item[1])

    return result   