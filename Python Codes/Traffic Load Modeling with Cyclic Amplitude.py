import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
duration = 10  # Duration in seconds
sampling_rate = 100  # Sampling rate (samples per second)
time_interval = 1 / sampling_rate  # Time between samples

# Generate time array (x values)
time = np.arange(0, duration, time_interval)

# Generate amplitude array (y values)
amplitude = np.floor(time) % 2

# Plot the data (simplified style)
plt.figure(figsize=(10, 5))
plt.step(time, amplitude, where='post', label='Cyclic Loading Protocol', color='b')

# Add title and labels
plt.title('Cyclic Loading Protocol', fontsize=14)
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

# Add legend with the updated text
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# Optional: Save data to a CSV file
data = pd.DataFrame({'Time': time, 'Amplitude': amplitude})
data.to_csv('static_load_amplitude.csv', index=False)
