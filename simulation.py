import numpy as np
import matplotlib.pyplot as plt

def calculate_ionization(pKa, pH):
    ratio = 10 ** (pH - pKa)
    ionized = ratio / (1 + ratio) * 100
    return ionized

def run_simulation(pKa, concentration_mg, selected_env):
    concentration_molar = concentration_mg / 1000
    environments = {
        "Stomach": (1, 3),
        "Duodenum": (5, 6),
        "Jejunum": (6, 7),
        "Ileum": (7, 8)
    }

    time_range = np.linspace(0, 120, 100)
    fig, ax = plt.subplots(figsize=(12, 6))
    report_data = []
    max_solubility = 0  # Track the maximum solubility for dynamic y-axis scaling

    for env in selected_env:
        pH_min, pH_max = environments[env]
        pH_range = np.linspace(pH_min, pH_max, 50)
        ionized_percentages = [calculate_ionization(pKa, pH) for pH in pH_range]

        solubility_over_time = np.array([
            np.mean(ionized_percentages) * concentration_molar * (1 - np.exp(-t/40)) for t in time_range
        ])

        # Update maximum solubility for y-axis scaling
        max_solubility = max(max_solubility, solubility_over_time.max())

        # Plot the solubility curve
        line, = ax.plot(time_range, solubility_over_time, label=f"{env} (pH {pH_min}-{pH_max})", linewidth=2)
        
        # Calculate the peak solubility and the time to reach it
        peak_solubility = solubility_over_time.max()
        time_to_peak_solubility = time_range[np.argmax(solubility_over_time)]

        # Add annotation for peak solubility
        ax.annotate(
            f"Peak solubility\nat {time_to_peak_solubility:.1f} min",
            xy=(time_to_peak_solubility, peak_solubility),
            xytext=(time_to_peak_solubility +
