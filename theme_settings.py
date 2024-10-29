# theme_settings.py

import streamlit as st

def apply_theme():
    # Custom CSS for background and font colors with improved contrast
    st.markdown(
        """
        <style>
        /* Set background color to black */
        .stApp {
            background-color: black;
        }
        /* Set font color to light gray for main text and white for headers */
        .css-1v0mbdj p {
            color: #d3d3d3;  /* Light gray for readability */
        }
        .css-1v0mbdj h1, .css-1v0mbdj h2, .css-1v0mbdj h3 {
            color: white;    /* White for headers */
        }
        /* Customize input field colors for readability */
        .stSlider > div > div > div > div {
            background-color: #5a5a5a !important; /* Darker gray slider bar */
        }
        .css-1aumxhk {
            color: white !important; /* White slider text */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
