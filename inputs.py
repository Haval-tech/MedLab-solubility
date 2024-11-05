import streamlit as st

def get_user_inputs():
    """Collect user inputs for the simulation."""
    pKa = st.number_input("Enter the pKa of the drug:", min_value=0.0, max_value=14.0, step=0.1)
    concentration_mg = st.number_input("Enter drug concentration (mg):", min_value=0.0, step=0.1)
    
    environments = {
        "Stomach": (1, 3),
        "Duodenum": (5, 6),
        "Jejunum": (6, 7),
        "Ileum": (7, 8)
    }

    st.write("### Select the Environment(s) and Adjust pH (if necessary)")
    selected_env = {}
    
    for env, (pH_min, pH_max) in environments.items():
        if st.checkbox(env):
            default_pH = (pH_min + pH_max) / 2  # Default pH is the middle of the range
            selected_pH = st.slider(
                f"Adjust pH for {env} (Range: {float(pH_min)}-{float(pH_max)})", 
                min_value=float(pH_min), 
                max_value=float(pH_max), 
                value=float(default_pH), 
                step=0.1
            )
            selected_env[env] = selected_pH

    return pKa, concentration_mg, selected_env
