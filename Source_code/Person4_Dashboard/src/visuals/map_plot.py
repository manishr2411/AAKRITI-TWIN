import plotly.graph_objects as go
import pandas as pd

from src.config.settings import MAP_TITLE, X_LIMIT, Y_LIMIT


def create_map_figure(scan_df: pd.DataFrame, object_df: pd.DataFrame) -> go.Figure:
    """
    Create a 2D environment map with:
    - scan points from ultrasonic data
    - labeled object points from fused AI output
    """
    fig = go.Figure()

    # 1. Scan points
    if not scan_df.empty and {"x", "y"}.issubset(scan_df.columns):
        fig.add_trace(
            go.Scatter(
                x=scan_df["x"],
                y=scan_df["y"],
                mode="markers+lines",
                name="Scan Points",
                marker=dict(size=8),
                line=dict(width=2),
                text=[
                    f"Angle: {a}°<br>Distance: {d} cm"
                    for a, d in zip(scan_df["angle_deg"], scan_df["distance_cm"])
                ],
                hovertemplate="%{text}<extra></extra>",
            )
        )

    # 2. Detected / fused objects
    if not object_df.empty and {"x", "y", "label"}.issubset(object_df.columns):
        fig.add_trace(
            go.Scatter(
                x=object_df["x"],
                y=object_df["y"],
                mode="markers+text",
                name="Detected Objects",
                marker=dict(size=14, symbol="diamond"),
                text=object_df["label"],
                textposition="top center",
                hovertemplate=(
                    "Label: %{text}<br>"
                    "X: %{x}<br>"
                    "Y: %{y}<extra></extra>"
                ),
            )
        )

    fig.update_layout(
        title=MAP_TITLE,
        xaxis_title="X Position (cm)",
        yaxis_title="Y Position (cm)",
        xaxis=dict(range=list(X_LIMIT), zeroline=True),
        yaxis=dict(range=list(Y_LIMIT), zeroline=True),
        template="plotly_white",
        height=600,
        showlegend=True,
    )

    return fig