import numpy as np
import matplotlib.pyplot as plt

# Given data for the discharge following a 6-hour rainfall event
time_hours = np.array([0, 6, 12, 18, 24, 30, 36, 40, 44, 48, 52, 56, 60, 64])
discharge_cume = np.array([0, 40, 64, 215, 360, 405, 350, 270, 205, 145, 100, 70, 50, 42]) - 20  # subtracting the base flow

# Create the S-curve by cumulatively summing the discharge
S_curve = np.cumsum(discharge_cume)

# Create a 6-hour unit hydrograph by subtracting the S-curve shifted by 6 hours from the original S-curve
six_hour_UH = S_curve - np.roll(S_curve, 1)
six_hour_UH[0] = 0  # Correct the first value that was wrapped around due to the roll

# Create a 12-hour unit hydrograph by subtracting the S-curve shifted by 12 hours from the original S-curve
twelve_hour_UH = S_curve - np.roll(S_curve, 2)
twelve_hour_UH[:2] = 0  # Correct the first two values that were wrapped around due to the roll

# Plot the 6-hour and 12-hour unit hydrographs
plt.figure(figsize=(14, 7))

# 6-hour unit hydrograph
plt.plot(time_hours, six_hour_UH, 'b-o', label='6-Hour Unit Hydrograph')

# 12-hour unit hydrograph from S-curve method
plt.plot(time_hours, twelve_hour_UH, 'g-s', label='12-Hour Unit Hydrograph (S-curve method)')

# S-curve
plt.plot(time_hours, S_curve, 'r--', label='S-curve')

# Plot details
plt.title('Unit Hydrographs and S-curve')
plt.xlabel('Time (hours)')
plt.ylabel('Discharge (cumecs per cm of runoff)')
plt.legend()
plt.grid(True)
plt.show()

# Print the S-curve data
print("S-curve Data:")
print(S_curve)

# Print the 6-hour unit hydrograph data
print("6-Hour Unit Hydrograph Data:")
print(six_hour_UH)

# Print the 12-hour unit hydrograph data
print("12-Hour Unit Hydrograph Data (S-curve method):")
print(twelve_hour_UH)
