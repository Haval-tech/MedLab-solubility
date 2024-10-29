# plot_settings.py

import matplotlib.pyplot as plt

def apply_plot_settings():
    # Set a dark background theme for matplotlib plots
    plt.style.use('dark_background')
    
    # Optionally set specific colors or other style properties for consistency
    plt.rcParams.update({
        "axes.facecolor": "#333333",  # Dark gray for axes background
        "axes.edgecolor": "white",    # White edges
        "text.color": "white",
        "xtick.color": "white",
        "ytick.color": "white",
    })
