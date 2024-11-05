import streamlit as st
from layout_settings import setup_layout
from inputs import get_user_inputs
from simulation import run_simulation
from report import generate_report
from home import home_page

def main():
    setup_layout()
    
    # Initialize session state for 'page' if it does not exist
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Home'  # Default to Home
    
    # Sidebar logo and navigation
    with st.sidebar:
        st.image("logo.png.webp", use_column_width=True)
        
        st.title("Navigation")
        if st.button('Home'):
            st.session_state.page = 'Home'
        st.write("")  # Add space between buttons
        if st.button('Drug Solubility Simulation'):
            st.session_state.page = 'Drug Solubility Simulation'
    
    # Render the selected page
    if st.session_state.page == 'Home':
        home_page()
    elif st.session_state.page == 'Drug Solubility Simulation':
        solubility_simulation_page()

def solubility_simulation_page():
    st.title("Drug Solubility Simulation Tool")
    st.write("### Input Parameters")
    st.write("This tool simulates drug solubility over time in different gastrointestinal environments.")
    
    pKa, concentration_mg, selected_env = get_user_inputs()

    if pKa and concentration_mg and selected_env:
        st.write("### Simulation Results")
        report_data, fig = run_simulation(pKa, concentration_mg, selected_env)
        st.pyplot(fig)
        generate_report(report_data, concentration_mg)

if __name__ == "__main__":
    main()

import streamlit as st

# Set page config to ensure sidebar is expanded by default
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Custom CSS to hide the sidebar toggle arrow
hide_toggle_css = """
    <style>
    /* Hide the sidebar collapse/expand button */
    .css-1v0mbdj.e1fqkh3o2 { 
        display: none; 
    }
    </style>
"""

# Inject the custom CSS into the app
st.markdown(hide_toggle_css, unsafe_allow_html=True)

# Your main app code here
st.sidebar.title("Navigation")
st.sidebar.button("Home")
st.sidebar.button("Drug Solubility Simulation")
st.title("Drug Solubility Simulation Tool")
# Add the rest of your app layout and functionality here

