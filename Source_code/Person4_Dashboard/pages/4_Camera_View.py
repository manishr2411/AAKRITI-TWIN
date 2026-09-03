import streamlit as st
from pathlib import Path

st.title("Camera View")
st.markdown("This page shows the latest annotated webcam frame.")

FRAME_PATH = Path("data/latest_frame.jpg")

@st.fragment(run_every="1s")
def camera_fragment():
    if FRAME_PATH.exists():
        st.image(str(FRAME_PATH), caption="Latest YOLO camera frame", use_container_width=True)
    else:
        st.warning("No camera frame available yet.")

camera_fragment()