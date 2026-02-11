import numpy as np
import matplotlib.pyplot as plt

# Ask for the duration in hours for the amplitude generation
hours = int(input("Enter the duration in hours (for a single day): "))

# Define time (x-axis in seconds), save every 60 seconds (1 minute)
time = np.arange(0, hours * 3600, 60)  # Time increments of 60 seconds (every minute)

# Sinusoidal amplitude (full oscillation each 3600 seconds)
amplitude = 1 * np.sin(2 * np.pi * time / 3600)  # Sinusoidal fluctuation every hour (3600 seconds)

# Save as a .txt file
filename = f"1. Python Code to Generate a Sinusoidal Amplitude_{hours}_hours.txt"
with open(filename, 'w') as f:
    f.write("Time (seconds), Amplitude\n")  # Write header
    for t, a in zip(time, amplitude):
        f.write(f"{t}, {a}\n")  # Write time and amplitude data

print(f"Sinusoidal amplitude data for {hours} hours saved to {filename}")

# Plot the amplitude
plt.plot(time, amplitude)
plt.title(f'Sinusoidal Amplitude for {hours} Hours')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()  # Show the plot
