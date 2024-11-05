import streamlit as st
from layout_settings import setup_layout
from inputs import get_user_inputs
from simulation import run_simulation
from report import generate_report
from home import home_page

def main():
    setup_layout()
    
    # Sidebar logo and navigation
    with st.sidebar:
        # Display the logo
        st.image("path/to/logo.png", use_column_width=True)
        
        st.write("")  # Add a bit of space
        st.write("")  # Add more space if needed
        
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
    
    # Ensure pKa is captured correctly
    pKa, concentration_mg, selected_env = get_user_inputs()

    # Only proceed if pKa has a valid input
    if pKa and concentration_mg and selected_env:
        st.write("### Simulation Results")
        report_data, fig = run_simulation(pKa, concentration_mg, selected_env)
        st.pyplot(fig)
        generate_report(report_data, concentration_mg)

