import numpy as np
import matplotlib.pyplot as plt

# Given time data and discharge values from the question
time_hours = np.array([0, 6, 12, 18, 24, 30, 36, 40, 44, 48, 52, 56, 60, 64])
discharge_cume = np.array([0, 40, 64, 215, 360, 405, 350, 270, 205, 145, 100, 70, 50, 42])

# The constant base flow of the river is 20 m3/s
constant_base_flow = 20  # m3/s

# Remove the base flow to find the direct runoff
direct_runoff = discharge_cume - constant_base_flow

# Calculate the 6-hour unit hydrograph (UH)
# The 6-hour UH is the direct runoff divided by the rainfall excess (6 hours of rainfall)
# Assuming 1 cm of rainfall excess over 6 hours
rainfall_excess = 1  # cm
six_hour_UH = direct_runoff / rainfall_excess

# Superpose the 6-hour UH to create the 12-hour UH using the superposition method
# Shift the 6-hour UH by 6 hours (1 time step) for superposition
six_hour_shifted = np.roll(six_hour_UH, 1)
six_hour_shifted[0] = 0  # No runoff at time 0

# Add the original and the shifted UHs to get the 12-hour UH
twelve_hour_UH = six_hour_UH + six_hour_shifted

# Plot the hydrographs
plt.figure(figsize=(14, 7))
plt.plot(time_hours, six_hour_UH, 'b-o', label='6-Hour Unit Hydrograph')
plt.plot(time_hours, twelve_hour_UH, 'r-s', label='12-Hour Unit Hydrograph', linestyle='--')

# Plot details
plt.title('6-Hour and 12-Hour Unit Hydrographs')
plt.xlabel('Time (hours)')
plt.ylabel('Discharge (cumecs per cm of runoff)')
plt.legend()
plt.grid(True)
plt.show()

# Print the calculated data for both hydrographs
print("6-Hour Unit Hydrograph Data:")
print(six_hour_UH)
print("12-Hour Unit Hydrograph Data:")
print(twelve_hour_UH)
