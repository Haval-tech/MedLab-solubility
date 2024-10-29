# solubility_simulation.py

import numpy as np

def calculate_degree_of_ionization(pKa, pH):
    """Calculate the degree of ionization using the Henderson-Hasselbalch equation."""
    ratio = 10 ** (pH - pKa)
    degree_of_ionization = 100 * (ratio / (1 + ratio))
    return degree_of_ionization

def dissolution_profile(pKa, concentration, environment_data):
    """
    Calculate the solubility profile over time for different environments using 
    a first-order dissolution model with environment-specific max solubility limits.
    """
    solubility_profile = {}
    time_steps = np.linspace(0, 120, 120)  # Time in minutes (up to 2 hours)
    
    for env in environment_data:
        pH = env['pH']
        env_name = env['name']
        max_solubility = env['max_solubility']  # pH-specific solubility cap
        
        ionization = calculate_degree_of_ionization(pKa, pH)
        env_solubility = []
        
        for t in time_steps:
            # First-order dissolution model: rate depends on time and ionization degree
            dissolved_amount = min(max_solubility, ionization * (1 - np.exp(-0.05 * t)))
            env_solubility.append(dissolved_amount)
        
        solubility_profile[env_name] = env_solubility

    return time_steps, solubility_profile

def find_optimal_solubility(solubility_profile):
    """Determine which environment has the highest solubility for azithromycin."""
    optimal_env = max(solubility_profile, key=lambda env: max(solubility_profile[env]))
    max_solubility = max(solubility_profile[optimal_env])
    return optimal_env, max_solubility
