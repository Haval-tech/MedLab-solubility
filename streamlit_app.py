import streamlit as st
from layout_settings import setup_layout
from inputs import get_user_inputs
from simulation import run_simulation
from report import generate_report

def main():
    setup_layout()
    st.title("Drug Solubility Simulation Tool")
    st.write("### Input Parameters")
    st.write("This tool simulates drug solubility over time in different gastrointestinal environments.")
    
    pKa, concentration_mg, selected_env = get_user_inputs()

    if pKa and concentration_mg and selected_env:
        st.write("### Simulation Results")
        report_data, fig = run_simulation(pKa, concentration_mg, selected_env)
        st.pyplot(fig)  # Display the plot
        generate_report(report_data, concentration_mg)

if __name__ == "__main__":
    main()
