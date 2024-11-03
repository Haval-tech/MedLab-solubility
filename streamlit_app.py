import streamlit as st
from layout_settings import setup_layout
from inputs import get_user_inputs
from simulation import run_simulation
from report import generate_report
from home import home_page  # Import the home page function

def main():
    setup_layout()
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Drug Solubility Simulation"])
    
    if page == "Home":
        home_page()  # Show the home page
    elif page == "Drug Solubility Simulation":
        solubility_simulation_page()  # Show the solubility simulation page

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
