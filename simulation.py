import numpy as np
import matplotlib.pyplot as plt

def calculate_ionization(pKa, pH):
    """Calculate the ionization percentage based on pKa and pH."""
    ratio = 10 ** (pH - pKa)
    ionized = ratio / (1 + ratio) * 100
    return ionized

def run_simulation(pKa, concentration_mg, selected_env):
    """Run the drug solubility simulation for selected environments."""
    concentration_molar = concentration_mg / 1000
    time_range = np.linspace(0, 120, 100)
    fig, ax = plt.subplots(figsize=(12, 6))
    report_data = []
    max_solubility = 0  # Track the maximum solubility for dynamic y-axis scaling

    for env, selected_pH in selected_env.items():
        ionized_percentages = [calculate_ionization(pKa, selected_pH)]

        solubility_over_time = np.array([
            np.mean(ionized_percentages) * concentration_molar * (1 - np.exp(-t/40)) for t in time_range
        ])

        # Update maximum solubility for y-axis scaling
        max_solubility = max(max_solubility, solubility_over_time.max())

        # Plot the solubility curve
        line, = ax.plot(time_range, solubility_over_time, label=f"{env} (pH {selected_pH:.1f})", linewidth=2)
        
        # Find the peak solubility and time to reach 50% of it
        peak_solubility = solubility_over_time.max()
        time_to_50_peak_solubility = time_range[np.argmax(solubility_over_time >= 0.5 * peak_solubility)]

        # Add annotation for 50% of peak solubility
        if peak_solubility > 0:
            ax.annotate(
                f"50% peak solubility\nat {time_to_50_peak_solubility:.1f} min",
                xy=(time_to_50_peak_solubility, 0.5 * peak_solubility),
                xytext=(time_to_50_peak_solubility + 5, 0.5 * peak_solubility + 5),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=8,
                ha='center'
            )

        # Add milestone data
        report_data.append((env, selected_pH, peak_solubility, time_to_50_peak_solubility))

    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Solubility (%)")
    ax.set_ylim(0, max(max_solubility * 1.2, 10))  # Dynamic scaling with some padding
    ax.set_title("Dynamic Solubility Graph")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    return report_data, fig
