from datetime import datetime


def format_timestamp(ts) -> str:
    """
    Convert numeric timestamp into readable text.
    If conversion fails, return original value as string.
    """
    try:
        return datetime.fromtimestamp(float(ts)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(ts)


def is_dataframe_empty(df) -> bool:
    """
    Safe dataframe empty check.
    """
    try:
        return df is None or df.empty
    except Exception:
        return True
    