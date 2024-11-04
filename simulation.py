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

    for env in selected_env:
        pH_min, pH_max = environments[env]
        pH_range = np.linspace(pH_min, pH_max, 50)
        ionized_percentages = [calculate_ionization(pKa, pH) for pH in pH_range]

        solubility_over_time = np.array([
            np.mean(ionized_percentages) * concentration_molar * (1 - np.exp(-t/40)) for t in time_range
        ])

        # Plot the solubility curve
        line, = ax.plot(time_range, solubility_over_time, label=f"{env} (pH {pH_min}-{pH_max})", linewidth=2)
        
        # Calculate milestones
        avg_solubility = solubility_over_time[-1]
        time_to_50_solubility = time_range[np.argmax(solubility_over_time >= 0.5 * avg_solubility)]

        # Add annotation for 50% solubility
        ax.annotate(
            f"50% solubility\nat {time_to_50_solubility:.1f} min",
            xy=(time_to_50_solubility, 0.5 * avg_solubility),
            xytext=(time_to_50_solubility + 5, 0.5 * avg_solubility + 5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10
        )

        # Add milestone data
        report_data.append((env, pH_min, pH_max, avg_solubility, time_to_50_solubility))

    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Solubility (%)")
    ax.set_ylim(0, 100)  # Assuming solubility percentage maxes at 100%
    ax.set_title("Dynamic Solubility Graph")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    return report_data, fig
