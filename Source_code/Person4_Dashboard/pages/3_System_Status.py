import streamlit as st

from src.loaders.json_loader import load_object_data, load_scan_data


st.title("System Status")
st.markdown("This page shows whether the dashboard is receiving valid input data.")

scan_df = load_scan_data()
object_df = load_object_data()

st.subheader("Input Health Check")

col1, col2 = st.columns(2)
col1.metric("Scan Packets Received", len(scan_df))
col2.metric("Object Packets Received", len(object_df))

st.subheader("Scan Data Status")
if scan_df.empty:
    st.error("No scan data available.")
else:
    st.success("Scan data loaded successfully.")
    st.write("Columns found:", list(scan_df.columns))

st.subheader("Object Data Status")
if object_df.empty:
    st.warning("No object data available yet.")
else:
    st.success("Object data loaded successfully.")
    st.write("Columns found:", list(object_df.columns))

st.subheader("Required Field Check")

required_scan_cols = {"scan_id", "timestamp", "angle_deg", "distance_cm"}
required_object_cols = {"timestamp", "label", "confidence", "angle_deg", "distance_cm", "x", "y"}

missing_scan = required_scan_cols - set(scan_df.columns)
missing_object = required_object_cols - set(object_df.columns)

if missing_scan:
    st.error(f"Missing scan fields: {sorted(missing_scan)}")
else:
    st.success("All required scan fields are present.")

if missing_object:
    st.error(f"Missing object fields: {sorted(missing_object)}")
else:
    st.success("All required object fields are present.")