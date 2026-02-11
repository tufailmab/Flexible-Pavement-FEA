import numpy as np
import matplotlib.pyplot as plt

# Ask for user input for the ramp parameters
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Number of days in each month (not accounting for leap year)

# Ask the user for input values for ramp duration and ramp load
ramp_duration = float(input("Enter the duration of the ramp (in units): "))
ramp_end_load = float(input("Enter the final load value after the ramp (in N/m²): "))

# Calculate the total number of days for the year
total_days = sum(days_in_months)

# Create an array representing the days of the year
time = np.linspace(0, ramp_duration, 100)  # Time from 0 to ramp_duration units
amplitude = (ramp_end_load / ramp_duration) * time  # Linear ramp from 0 to ramp_end_load

# Plot the amplitude curve
plt.plot(time, amplitude)
plt.title(f'Linear Ramp Function for Load (Ramp from 0 to {ramp_end_load} N/m²)')
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
filename = "3. Ramp or Linear Amplitude (For Gradual Changes in Load or Temperature).txt"
with open(filename, 'w') as f:
    # Write the header
    f.write("Time (Seconds), Amplitude\n")  # Header line with "Time" and "Amplitude"
    
    # Write the time and amplitude data
    for t, a in zip(time, amplitude):
        f.write(f"{t}, {a}\n")  # Write time and amplitude data as comma-separated values

print(f"Ramp function data saved to {filename}")
