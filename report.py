import streamlit as st

def generate_report(report_data, concentration_mg):
    st.write("### Report")
    concentration_molar = concentration_mg / 1000
    for env, pH_min, pH_max, avg_solubility, time_to_50_solubility in report_data:
        st.write(f"**{env}** (pH {pH_min}-{pH_max}): Final Solubility = {avg_solubility:.2f}% of concentration ({concentration_molar:.2f} M) at 120 minutes")
        st.write(f"Time to reach 50% of final solubility: {time_to_50_solubility:.1f} minutes")
