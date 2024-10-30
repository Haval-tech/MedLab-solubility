# streamlit_app.py

import streamlit as st
import layout_settings
import plot_settings
import solubility_simulation
from theme_settings import apply_theme

# Apply custom theme
apply_theme()

# Sidebar and layout settings
pKa, concentration, dissolution_rate, selected_environments = layout_settings.setup_sidebar()

# Simulation calculations
time_steps, solubility_profile = solubility_simulation.calculate_solubility(pKa, concentration, selected_environments, dissolution_rate)

# Display plot
st.header("Simulated Solubility Profile")
plot_settings.plot_simulated_profile(time_steps, solubility_profile, selected_environments)
