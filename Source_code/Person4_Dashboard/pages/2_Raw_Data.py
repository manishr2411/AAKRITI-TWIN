import streamlit as st

from src.loaders.json_loader import load_latest_snapshot, load_object_data, load_scan_data


st.title("Raw Data")
st.markdown("This page shows the incoming raw JSON data in table form.")

scan_df = load_scan_data()
object_df = load_object_data()
snapshot = load_latest_snapshot()

st.subheader("Scan Data")
st.dataframe(scan_df, use_container_width=True)

st.subheader("Object Data")
st.dataframe(object_df, use_container_width=True)

st.subheader("Latest Snapshot")
st.json(snapshot)