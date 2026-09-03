import pandas as pd


REQUIRED_SCAN_COLUMNS = {"scan_id", "timestamp", "angle_deg", "distance_cm"}
REQUIRED_OBJECT_COLUMNS = {"timestamp", "label", "confidence", "angle_deg", "distance_cm", "x", "y"}


def validate_scan_df(scan_df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Validate scan dataframe structure.
    Returns:
    - is_valid
    - list of error messages
    """
    errors = []

    if scan_df.empty:
        errors.append("Scan dataframe is empty.")
        return False, errors

    missing_cols = REQUIRED_SCAN_COLUMNS - set(scan_df.columns)
    if missing_cols:
        errors.append(f"Missing scan columns: {sorted(missing_cols)}")

    return len(errors) == 0, errors


def validate_object_df(object_df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Validate object dataframe structure.
    Returns:
    - is_valid
    - list of error messages
    """
    errors = []

    if object_df.empty:
        errors.append("Object dataframe is empty.")
        return False, errors

    missing_cols = REQUIRED_OBJECT_COLUMNS - set(object_df.columns)
    if missing_cols:
        errors.append(f"Missing object columns: {sorted(missing_cols)}")

    return len(errors) == 0, errors