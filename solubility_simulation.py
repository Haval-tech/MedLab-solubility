# solubility_simulation.py

import numpy as np

def calculate_solubility(pKa, concentration, selected_environments, dissolution_rate):
    time_steps = np.linspace(0, 120, 100)
    solubility_profile = {}
    for env in selected_environments:
        pH = env['pH']
        env_name = env['name']
        # Mock calculation for demonstration
        solubility_profile[env_name] = dissolution_rate * time_steps * (pH / pKa) * concentration
    return time_steps, solubility_profile
