import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Current Discharge Condition
DO_concentrations_current = np.array([6.94918, 3.1, 3.077933, 4.215, 7.434])  # DO in mg/L
distances_km_current = np.array([0, 51.735, 58.512, 110, 220])  # Distance in km

# Management Scenario 1
DO_concentrations_scenario1 = np.array([6.949180328, 7.385, 7.4656, 8.247, 9.314])  # DO in mg/L
distances_km_scenario1 = np.array([0, 51.735, 58.512, 110, 220])  # Distance in km

# Management Scenario 2
DO_concentrations_scenario2 = np.array([6.949180328, 7.7281, 7.8168, 8.5697, 9.4644])  # DO in mg/L
distances_km_scenario2 = np.array([0, 51.735, 58.512, 110, 220])  # Distance in km

# Management Scenario 3
DO_concentrations_scenario3 = np.array([6.94918, 4.6422, 4.6573, 5.667, 8.1104])  # DO in mg/L
distances_km_scenario3 = np.array([0, 51.735, 58.512, 110, 220])  # Distance in km

# Given DO saturation level
DO_sat = 10  # DO saturation in mg/L

# Plotting the DO Sag Curve
plt.figure(figsize=(14, 7))

# Interpolation and plotting for each scenario
for scenario, DO_concentrations, distances_km, color, label in zip(
        ["Current Discharge", "Management Scenario 1", "Management Scenario 2", "Management Scenario 3"],
        [DO_concentrations_current, DO_concentrations_scenario1, DO_concentrations_scenario2,
         DO_concentrations_scenario3],
        [distances_km_current, distances_km_scenario1, distances_km_scenario2, distances_km_scenario3],
        ['orange', 'green', 'blue', 'purple'],
        ['Current Discharge', 'Management Scenario 1', 'Management Scenario 2', 'Management Scenario 3']
):
    # Fit a spline curve to the data
    spl = make_interp_spline(distances_km, DO_concentrations, k=3)
    smooth_dist = np.linspace(distances_km.min(), distances_km.max(), 500)
    smooth_DO = spl(smooth_dist)

    # Plot the smoothed DO data points for each scenario
    plt.plot(smooth_dist, smooth_DO, label=label, linestyle='-', color=color)

    # Plot the original DO data points for each scenario
    plt.plot(distances_km, DO_concentrations, 'o', color=color)

# Plot the DO saturation line
plt.hlines(y=DO_sat, xmin=0, xmax=250, colors='grey', linestyles='dotted', label='DO Saturation Level')

# Labels and title
plt.title('DO Sag Curve Comparison')
plt.xlabel('Distance (km)')
plt.ylabel('DO (mg/L)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
