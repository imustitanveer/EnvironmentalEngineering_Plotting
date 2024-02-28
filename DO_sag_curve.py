import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Given data for DO concentration at various distances
DO_concentrations = np.array([6.9492, 7.8168, 8.5697, 9.35193, 9.5993])  # DO in mg/L
distances_km = np.array([0, 58.512, 110, 200, 250])  # Distance in km

# Given DO saturation level
DO_sat = 10  # DO saturation in mg/L

# Plotting the DO Sag Curve
plt.figure(figsize=(10, 6))

# Fit a spline curve to the data
spl = make_interp_spline(distances_km, DO_concentrations, k=3)
smooth_dist = np.linspace(distances_km.min(), distances_km.max(), 500)
smooth_DO = spl(smooth_dist)

# Plot the smoothed DO data points
plt.plot(smooth_dist, smooth_DO, label='DO Concentration')

# Plot the original DO data points
plt.plot(distances_km, DO_concentrations, 'o', color='red')

# Plot the DO saturation line
plt.hlines(y=DO_sat, xmin=0, xmax=220, colors='grey', linestyles='dotted', label='DO$_{sat}$')

# Annotate the points
labels = ['DO$_{mix}$', 'D$_{c}$', 'D$_{t,100}$', 'D$_{t,220}$']
for i, label in enumerate(labels):
    plt.annotate(f"{label} ({DO_concentrations[i]:.2f})", (distances_km[i], DO_concentrations[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Labels and title
plt.title('DO Sag Curve')
plt.xlabel('Distance (km)')
plt.ylabel('DO (mg/L)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
