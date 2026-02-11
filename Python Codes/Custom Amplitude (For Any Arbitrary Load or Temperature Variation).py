import numpy as np
import matplotlib.pyplot as plt

# Ask for user input for the sawtooth wave parameters
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Number of days in each month (not accounting for leap year)

# Ask the user for input values for the sawtooth amplitude
start_amplitude = float(input("Enter the starting amplitude value (in N/m²): "))
end_amplitude = float(input("Enter the final amplitude value (in N/m²): "))
duration = float(input("Enter the duration of the time period (in units): "))

# Calculate the total number of days for the year
total_days = sum(days_in_months)

# Create time array for the sawtooth pattern
time = np.linspace(0, duration, 100)  # Time from 0 to duration

# Create the sawtooth pattern (increasing from start_amplitude to end_amplitude in a stepwise manner)
sawtooth_amplitude = np.tile(np.linspace(start_amplitude, end_amplitude, 10), 10)  # Replicating the linear increase in steps

# Ensure the length matches the time array
sawtooth_amplitude = sawtooth_amplitude[:len(time)]

# Plot the amplitude curve
plt.plot(time, sawtooth_amplitude)
plt.title('Sawtooth Pattern for Load Variation')
plt.xlabel('Time (Days of the Year)')
plt.ylabel('Load (N/m²)')
plt.grid(True)

# Format the x-axis labels to show months
month_ticks = []
month_labels = []
day_of_year = 1
for i, days_in_month in enumerate(days_in_months):
    month_ticks.append(day_of_year)
    month_labels.append(month_names[i])
    day_of_year += days_in_month

plt.xticks(month_ticks, month_labels, rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Save the amplitude data to a comma-separated text file (for ABAQUS input)
filename = "4. Custom Amplitude (For Any Arbitrary Load or Temperature Variation).txt"
with open(filename, 'w') as f:
    # Write the header
    f.write("Time, Amplitude\n")  # Header line with "Time" and "Amplitude"
    
    # Write the time and amplitude data
    for t, a in zip(time, sawtooth_amplitude):
        f.write(f"{t}, {a}\n")  # Write time and amplitude data as comma-separated values

print(f"Sawtooth amplitude data saved to {filename}")
