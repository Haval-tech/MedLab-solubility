# theme_settings.py

import streamlit as st

def apply_theme():
    # Custom CSS for background and font color
    st.markdown(
        """
        <style>
        /* Set background color to black */
        .stApp {
            background-color: black;
        }
        /* Set font color to white */
        .css-1v0mbdj p, .css-1v0mbdj h1, .css-1v0mbdj h2, .css-1v0mbdj h3 {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
