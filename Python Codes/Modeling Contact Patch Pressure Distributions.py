import numpy as np
import matplotlib.pyplot as plt

# Function to generate a circular contact patch pressure distribution
def circular_contact_patch(length, width, grid_size):
    x = np.linspace(0, length, grid_size)
    y = np.linspace(0, width, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Pressure distribution in a circular pattern
    radius = min(length, width) / 2
    pressure = np.exp(-((X - length/2)**2 + (Y - width/2)**2) / (2 * radius**2))
    return X, Y, pressure

# Function to generate an elliptical contact patch pressure distribution
def elliptical_contact_patch(length, width, grid_size):
    x = np.linspace(0, length, grid_size)
    y = np.linspace(0, width, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Elliptical pressure distribution
    a = length / 2
    b = width / 2
    pressure = np.exp(-(((X - length/2)**2 / a**2) + ((Y - width/2)**2 / b**2)) / 2)
    return X, Y, pressure

# Function to generate a rectangular contact patch pressure distribution
def rectangular_contact_patch(length, width, grid_size):
    x = np.linspace(0, length, grid_size)
    y = np.linspace(0, width, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Rectangular pressure distribution (uniform)
    pressure = np.ones_like(X)  # Uniform pressure across the patch
    return X, Y, pressure

# Grid size and patch dimensions
contact_patch_length = 200  # mm
contact_patch_width = 150   # mm
grid_size = 100            # Number of grid points in each direction

# Circular Contact Patch
X, Y, pressure = circular_contact_patch(contact_patch_length, contact_patch_width, grid_size)
plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, pressure, cmap='viridis', levels=20)
plt.title('Circular Contact Patch')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.colorbar(cp, label='Pressure (kPa)')
plt.tight_layout()
plt.show()

# Elliptical Contact Patch
X, Y, pressure = elliptical_contact_patch(contact_patch_length, contact_patch_width, grid_size)
plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, pressure, cmap='viridis', levels=20)
plt.title('Elliptical Contact Patch')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.colorbar(cp, label='Pressure (kPa)')
plt.tight_layout()
plt.show()

# Rectangular Contact Patch
X, Y, pressure = rectangular_contact_patch(contact_patch_length, contact_patch_width, grid_size)
plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, pressure, cmap='viridis', levels=20)
plt.title('Rectangular Contact Patch')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.colorbar(cp, label='Pressure (kPa)')
plt.tight_layout()
plt.show()
