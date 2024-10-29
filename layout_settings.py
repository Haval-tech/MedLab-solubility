# layout_settings.py

import streamlit as st

def apply_layout():
    # Set the sidebar to an expanded view for better user experience
    st.sidebar.markdown("# Options")
    st.set_page_config(layout="wide")
