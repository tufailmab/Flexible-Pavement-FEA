# Import all required libraries
# Current Version: Python 3.12.3
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.signal import argrelextrema
import numpy as np
import time

# Load the Excel sheet (You need to import the results from ABAQUS before working on this code)
# The Excel sheet should be in current directory
# The Excel sheet should contain 3 columns, Column A: Cycle numbers, Column B: ABAQUS Step Time & Column C: Rutting Depth
# Please check the current one, as i have provided with this project
# You must update the sheet in the format, that i have included in this course, so that you get the graphs accordingly
file_path = './Rutting Depth.xlsx'  # Adjust this path as needed (This is from the post processing of ABAQUS)
sheet_name = 'xyToExcel' #Just in case if you are using other names, you need to make sure to change this name here as well

# Read the Excel file and ensure header rows are not affected
# This only keep the headers safe
# This code seciton here read the ABAQUS output of what we covered in this lecture (Rutting depth profile)
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Find local maxima and minima for Column A (vs Column C - Loading/Unloading)
# Local maxima: Active Rutting Depth when the tyre load is applied
# Local manima: Incative Rutting Depth when the tyre load is removed
x_A = df.iloc[:, 0]  # Column A: Cycles number (assumes headers A1, B1, and C1 are intact)
y_C_A = df.iloc[:, 2]  # Rutting depth

# Get indices of rutting depth from curve exported from ABAQUS (Same excel file: Rutting Depth.xlsx)
maxima_A = argrelextrema(y_C_A.values, np.greater)[0]  # Rutting depth on active tyre contact area
minima_A = argrelextrema(y_C_A.values, np.less)[0]  # Rutting depth after the active tyre contact area

# Repeat for Total step time (vs Rutting depth - Loading/Unloading)
x_B = df.iloc[:, 1]  # Total step time from ABAQUS
y_C_B = df.iloc[:, 2]  # Rutting depth (same column as above)
maxima_B = argrelextrema(y_C_B.values, np.greater)[0]  # Rutting depth on active tyre contact area
minima_B = argrelextrema(y_C_B.values, np.less)[0]  # Rutting depth after the active tyre contact area

# Convert negative values to positive for better visualization
# There is only one purpose of it, which is actually to convert it to positive graph only
y_C_A_pos = np.abs(y_C_A) # Rutting Depth
y_C_B_pos = np.abs(y_C_B) # Rutting Depth

# Create a directory for output plots if it doesn't exist
# It will create a folder for you to save plots it generate from ABAQUS results
output_dir = './All Results from Post Processing Rutting Depth.xlsx file'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Plotting Rutting depth on active tyre contact area
plt.figure(figsize=(8, 6))
plt.plot(x_A[maxima_A], y_C_A_pos[maxima_A], color='red', linewidth=2.5, label='Loading (Cycle Number Vs Rutting Depth)')
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[2])
plt.title('Loading (Cycle Number Vs Rutting Depth)')
plt.legend()

# Set the axes to start from 0,0
plt.xlim(0, max(x_A))
plt.ylim(0, max(y_C_A_pos))

plt.savefig(os.path.join(output_dir, 'Loading (Cycle Number Vs Rutting Depth).png'))
plt.close()

# Plotting Rutting depth after the active tyre contact area
plt.figure(figsize=(8, 6))
plt.plot(x_A[minima_A], y_C_A_pos[minima_A], color='orange', linewidth=2.5, label='Unloading (Cycle Number Vs Rutting Depth)')
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[2])
plt.title('Unloading (Cycle Number Vs Rutting Depth)')
plt.legend()

# Set the axes to start from 0,0
plt.xlim(0, max(x_A))
plt.ylim(0, max(y_C_A_pos))

plt.savefig(os.path.join(output_dir, 'Unloading (Cycle Number Vs Rutting Depth).png'))
plt.close()
