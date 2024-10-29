import numpy as np
import matplotlib.pyplot as plt

def calculate_degree_of_ionization(pKa, pH):
    """Calculate the degree of ionization using the Henderson-Hasselbalch equation."""
    ratio = 10 ** (pH - pKa)
    degree_of_ionization = 100 * (ratio / (1 + ratio))
    return degree_of_ionization

def dissolution_profile(pKa, concentration, environment_data, dissolution_rate):
    """
    Calculate the solubility profile over time for different environments.
    environment_data: dict with 'name', 'pH', and 'dissolution_rate_constant' for each environment.
    """
    solubility_profile = {}
    time_steps = np.linspace(0, 120, 120)  # Time in minutes (up to 2 hours)
    
    for env in environment_data:
        pH = env['pH']
        env_name = env['name']
        ionization = calculate_degree_of_ionization(pKa, pH)
        env_solubility = []

        # Simulate dissolution over time
        for t in time_steps:
            dissolved_amount = dissolution_rate * ionization * t
            if dissolved_amount >= concentration:
                env_solubility.append(concentration)  # Saturation reached
            else:
                env_solubility.append(dissolved_amount)
        
        solubility_profile[env_name] = env_solubility

    return time_steps, solubility_profile

def find_optimal_solubility(solubility_profile):
    """Determine which environment has the highest solubility for azithromycin."""
    optimal_env = max(solubility_profile, key=lambda env: max(solubility_profile[env]))
    max_solubility = max(solubility_profile[optimal_env])
    return optimal_env, max_solubility

# Example setup
pKa = 8.1  # Azithromycin's approximate pKa
concentration = 500  # mg

# Define environments
environment_data = [
    {'name': 'stomach', 'pH': 2.0, 'dissolution_rate_constant': 0.05},
    {'name': 'duodenum', 'pH': 5.0, 'dissolution_rate_constant': 0.1},
    {'name': 'jejunum', 'pH': 6.5, 'dissolution_rate_constant': 0.12},
    {'name': 'ileum', 'pH': 7.5, 'dissolution_rate_constant': 0.15}
]

# Run simulation
time_steps, solubility_profile = dissolution_profile(pKa, concentration, environment_data, 0.1)
optimal_env, max_solubility = find_optimal_solubility(solubility_profile)

# Plotting example (we can refine this for Streamlit later)
for env, solubility in solubility_profile.items():
    plt.plot(time_steps, solubility, label=f"{env} (pH {environment_data[0]['pH']})")
plt.xlabel("Time (minutes)")
plt.ylabel("Dissolved Amount (mg)")
plt.legend()
plt.title("Azithromycin Solubility Profile in Different Environments")
plt.show()

