# layout_settings.py

import streamlit as st

def setup_sidebar():
    st.sidebar.title("Simulation Controls")
    
    pKa = st.sidebar.slider("pKa", 0.0, 14.0, 8.1)
    concentration = st.sidebar.slider("Concentration (mg)", 100, 1000, 500)
    dissolution_rate = st.sidebar.slider("Dissolution Rate", 0.01, 0.2, 0.1)

    # Environment selection
    selected_environments = []
    if st.sidebar.checkbox("Stomach"):
        selected_environments.append({'name': 'Stomach', 'pH': st.sidebar.slider("Stomach pH", 1.0, 3.0, 2.0)})
    if st.sidebar.checkbox("Duodenum"):
        selected_environments.append({'name': 'Duodenum', 'pH': st.sidebar.slider("Duodenum pH", 3.0, 7.0, 5.0)})
    if st.sidebar.checkbox("Jejunum"):
        selected_environments.append({'name': 'Jejunum', 'pH': st.sidebar.slider("Jejunum pH", 5.5, 7.5, 6.5)})
    if st.sidebar.checkbox("Ileum"):
        selected_environments.append({'name': 'Ileum', 'pH': st.sidebar.slider("Ileum pH", 6.5, 8.0, 7.5)})

    return pKa, concentration, dissolution_rate, selected_environments
