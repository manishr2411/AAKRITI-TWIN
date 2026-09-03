import streamlit as st

from src.loaders.json_loader import load_object_data, load_scan_data
from src.processing.coordinate_converter import convert_scan_to_xy
from src.visuals.map_plot import create_map_figure

st.title("Live Map")
st.markdown("This page shows the live 2D digital twin of the environment.")

@st.fragment(run_every="1s")
def live_map_fragment():
    scan_df = load_scan_data()
    object_df = load_object_data()
    scan_xy_df = convert_scan_to_xy(scan_df)

    col1, col2 = st.columns(2)
    col1.metric("Scan Points", len(scan_xy_df))
    col2.metric("Detected Objects", len(object_df))

    fig = create_map_figure(scan_xy_df, object_df)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Preview processed scan data"):
        st.dataframe(scan_xy_df, use_container_width=True)

    with st.expander("Preview object data"):
        st.dataframe(object_df, use_container_width=True)

live_map_fragment()