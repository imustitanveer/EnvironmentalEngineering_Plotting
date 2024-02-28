import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data from the image provided by the user
data = {
    "Time (hr)": np.arange(0, 42, 3),
    "Stream flow (cumec)": [10, 14, 18, 32, 46, 54, 58, 49, 36, 25, 17, 12, 11, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

base_flow = 10
df['Direct runoff (cumec)'] = df['Stream flow (cumec)'] - base_flow

area_sq_km = 45.4  # area in square kilometers

# First, we will calculate the excess rainfall for the 6-hour unit hydrograph considering the constant base flow and storm loss
excess_rainfall = (3.5 - 0.25 * 6) / 100  # Convert cm to m
excess_rainfall_volume = excess_rainfall * area_sq_km * 1e6  # area in m^2
direct_runoff_volume = df['Direct runoff (cumec)'].sum() * 3 * 3600  # total volume in m^3
uh_6_hour = (df['Direct runoff (cumec)'] / direct_runoff_volume) * excess_rainfall_volume  # 6-hour UH in m^3 per cm of rainfall

# Now, let's calculate the S-curve which is a cumulative sum of the unit hydrograph ordinates
s_curve = uh_6_hour.cumsum() * 3  # every step is 3 hours, so we multiply by 3 to get cumulative volume

# For the 3-hour UH, we will take the differences of the S-curve at every step
uh_3_hour = s_curve.diff().fillna(s_curve[0]) / 3  # divide by 3 to get the UH in m^3 per cm of rainfall

# For the 9-hour UH, we will take the differences of the S-curve at every third step
uh_9_hour = s_curve.diff(periods=3).fillna(s_curve[0]) / 9  # divide by 9 to get the UH in m^3 per cm of rainfall

# Plot the 6-hour, 3-hour, and 9-hour unit hydrographs together with the S-curve
plt.figure(figsize=(10, 6))
plt.plot(df['Time (hr)'], uh_6_hour, label='6-hour UH', marker='o')
plt.plot(df['Time (hr)'], uh_3_hour, label='3-hour UH', marker='x')
plt.plot(df['Time (hr)'], uh_9_hour, label='9-hour UH', marker='^')
plt.plot(df['Time (hr)'], s_curve, label='S-curve', linestyle='--')
plt.xlabel('Time (hours)')
plt.ylabel('Discharge (m^3/s per cm of rainfall)')
plt.title('Unit Hydrographs and S-Curve')
plt.legend()
plt.grid(True)
plt.show()

# Now let's plot the storm events with the 6-hour unit hydrograph
# Since we are given 3 storm events, we will assume they are sequential and separate
# We will create a combined hydrograph by summing the direct runoff from all storms

# Create a DataFrame for the combined hydrograph
df_combined = pd.DataFrame({
    'Time (hr)': df['Time (hr)'],
    'Storm 1 (cumec)': uh_6_hour * excess_rainfall_volume,
    'Storm 2 (cumec)': uh_6_hour * excess_rainfall_volume,
    'Storm 3 (cumec)': uh_6_hour * excess_rainfall_volume,
})

# Calculate combined hydrograph by shifting storm 2 and storm 3 appropriately and then summing
df_combined['Storm 2 (cumec)'] = df_combined['Storm 2 (cumec)'].shift(2)  # Shift by 6 hours
df_combined['Storm 3 (cumec)'] = df_combined['Storm 3 (cumec)'].shift(4)  # Shift by 12 hours
df_combined.fillna(0, inplace=True)
df_combined['Combined (cumec)'] = df_combined.sum(axis=1)

# Plot the storm events and the combined hydrograph
plt.figure(figsize=(10, 6))
plt.plot(df_combined['Time (hr)'], df_combined['Storm 1 (cumec)'], label='Storm 1', marker='o')
plt.plot(df_combined['Time (hr)'], df_combined['Storm 2 (cumec)'], label='Storm 2', marker='x')
plt.plot(df_combined['Time (hr)'], df_combined['Storm 3 (cumec)'], label='Storm 3', marker='^')
plt.plot(df_combined['Time (hr)'], df_combined['Combined (cumec)'], label='Combined Storm', marker='s')
plt.xlabel('Time (hours)')
plt.ylabel('Discharge (cumec)')
plt.title('Storm Event Hydrographs')
plt.legend()
plt.grid(True)
plt.show()
