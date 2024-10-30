# theme_settings.py

import streamlit as st

def apply_theme():
    # Apply custom theme settings or CSS here
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
