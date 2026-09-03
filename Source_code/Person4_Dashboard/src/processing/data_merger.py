import pandas as pd


def build_dashboard_snapshot(scan_df: pd.DataFrame, object_df: pd.DataFrame) -> dict:
    """
    Build one combined snapshot dictionary for dashboard use.
    """
    if scan_df is None or scan_df.empty:
        scan_points = []
    else:
        scan_points = scan_df.to_dict(orient="records")

    if object_df is None or object_df.empty:
        objects = []
    else:
        objects = object_df.to_dict(orient="records")

    return {
        "scan_points": scan_points,
        "objects": objects,
    }


def merge_for_display(scan_df: pd.DataFrame, object_df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a simple combined dataframe for debugging / display.
    This does NOT do true sensor fusion.
    It just creates a readable table for the dashboard.
    """
    scan_display = pd.DataFrame()
    object_display = pd.DataFrame()

    if scan_df is not None and not scan_df.empty:
        scan_display = scan_df.copy()
        scan_display["source"] = "scan"

    if object_df is not None and not object_df.empty:
        object_display = object_df.copy()
        object_display["source"] = "object"

    if scan_display.empty and object_display.empty:
        return pd.DataFrame()

    if scan_display.empty:
        return object_display.reset_index(drop=True)

    if object_display.empty:
        return scan_display.reset_index(drop=True)

    return pd.concat([scan_display, object_display], ignore_index=True, sort=False)