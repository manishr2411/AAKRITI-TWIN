import streamlit as st

from src.config.settings import APP_ICON

st.set_page_config(
    page_title="Aakriti Twin",
    page_icon=APP_ICON,
    layout="wide",
)

st.title("Aakriti Twin: AI-Powered Environment Mapping and Digital Twin System")
st.markdown("### Built by Team Neural Circuits")
st.info("Use the pages in the left sidebar to view the live map, raw data, system status, and camera view.")