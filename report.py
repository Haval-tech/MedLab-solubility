import streamlit as st

def generate_report(report_data, concentration_mg):
    """Generate and display the simulation report."""
    st.write("### Report")
    concentration_molar = concentration_mg / 1000
    for env, selected_pH, peak_solubility, time_to_50_peak_solubility in report_data:
        st.write(f"**{env}** (pH {selected_pH:.1f}): Final Solubility = {peak_solubility:.2f}% of concentration ({concentration_molar:.2f} M) at 120 minutes")
        st.write(f"Time to reach 50% of peak solubility: {time_to_50_peak_solubility:.1f} minutes")
