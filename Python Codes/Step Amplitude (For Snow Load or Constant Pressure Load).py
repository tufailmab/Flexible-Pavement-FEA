import numpy as np
import matplotlib.pyplot as plt

# Ask for user input for the month and load step parameters
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Number of days in each month (not accounting for leap year)

# Ask the user for input values
load_step_month = int(input("Enter the month (1 for January, 2 for February, etc.) when the load step occurs: "))
load_step_day = int(input("Enter the day of the month when the load step occurs: "))
load_value = float(input("Enter the load value after the step (in N/m²): "))

# Calculate the total number of days for the year
total_days = sum(days_in_months)

# Create an array representing the days of the year
time = np.arange(1, total_days + 1)  # Day 1 to Day 365 (or 366 if leap year)

# Initialize the amplitude array
amplitude = np.zeros_like(time)

# Find the day of the year when the step occurs
step_day_of_year = sum(days_in_months[:load_step_month - 1]) + load_step_day

# Apply the load step after the specified day
amplitude[time >= step_day_of_year] = load_value

# Plot the amplitude curve
plt.plot(time, amplitude)
plt.title(f'Step Function for Snow Load (Load = {load_value} N/m² after Day {step_day_of_year})')
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
filename = "2. Step Amplitude (For Snow Load or Constant Pressure Load).txt"
with open(filename, 'w') as f:
    # Write the header
    f.write("Time (Seconds), Amplitude\n")  # Header line with "Time" and "Amplitude"
    
    # Write the time and amplitude data
    for t, a in zip(time, amplitude):
        f.write(f"{t}, {a}\n")  # Write time and amplitude data as comma-separated values

print(f"Step function data saved to {filename}")
	
