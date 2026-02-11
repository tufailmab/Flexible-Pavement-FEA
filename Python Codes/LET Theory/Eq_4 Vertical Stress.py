import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv  # Bessel function of the first kind
from scipy.integrate import quad  # Numerical integration
from scipy.ndimage import gaussian_filter1d  # For smoothing

# Example parameters
A = 1
B = 1
C = 1
D = 1
E = 30000  # Young's modulus
mu = 0.35  # Poisson's ratio
r = np.linspace(0.001, 0.3, 800)  # Increased resolution for r
z = 0.5  # Depth

# Biharmonic Function (Equation 1)
def biharmonic_function(m, A, B, C, D, r, z):
    integrand = (A * np.exp(m * z) - B * np.exp(-m * z) + 
                 C * z * np.exp(-m * z) - D * z * np.exp(m * z)) * jv(0, m * r)
    return integrand

# Compute the biharmonic function values
Phi = np.zeros_like(r)
for i, r_val in enumerate(r):
    result, _ = quad(biharmonic_function, 0, 10, args=(A, B, C, D, r_val, z), epsabs=1e-6, epsrel=1e-6)
    Phi[i] = result

# Compute the second derivative of Phi with respect to r
dPhi_dr = np.gradient(Phi, r)

# Since Phi is a function of r only, we approximate the derivative with respect to z using finite differences
dz = 0.01
Phi_plus_dz = np.zeros_like(Phi)
Phi_minus_dz = np.zeros_like(Phi)
for i, r_val in enumerate(r):
    Phi_plus_dz[i], _ = quad(biharmonic_function, 0, 10, args=(A, B, C, D, r_val, z + dz), epsabs=1e-6, epsrel=1e-6)
    Phi_minus_dz[i], _ = quad(biharmonic_function, 0, 10, args=(A, B, C, D, r_val, z - dz), epsabs=1e-6, epsrel=1e-6)

# Compute the second derivative with respect to z
d2Phi_dz2 = (Phi_plus_dz - 2 * Phi + Phi_minus_dz) / (dz ** 2)

# Compute the mixed second derivative with respect to z and r
d2Phi_dzdr = np.gradient(d2Phi_dz2, r)

# Calculate radial displacement (Equation 2)
u_radial = (1 + mu) / E * d2Phi_dzdr

# Compute the Laplacian of Phi (nabla^2 Phi)
nabla2Phi = np.gradient(np.gradient(Phi, r), r) + np.gradient(np.gradient(Phi, z), z)

# Calculate vertical displacement (Equation 3)
w_vertical = (1 + mu) / E * (2 * (1 - mu) * nabla2Phi - d2Phi_dz2)

# Apply Gaussian smoothing to vertical displacement
w_vertical_smooth = gaussian_filter1d(w_vertical, sigma=20)  # Increase sigma for more smoothing

# Calculate vertical stress (Equation 4)
sigma_zi = np.gradient((2 - mu) * nabla2Phi - d2Phi_dz2, z)

# Plot radial displacement
plt.figure()
plt.title("Radial Displacement")
plt.xlabel("Radial Distance, \( r \)")
plt.ylabel(r"Radial Displacement, \( u_i \)")
plt.plot(r, u_radial, label="Radial Displacement")
plt.legend()
plt.grid(True)
plt.show()

# Plot vertical displacement (smoothed)
plt.figure()
plt.title("Vertical Displacement (Smoothed)")
plt.xlabel("Radial Distance, \( r \)")
plt.ylabel(r"Vertical Displacement, \( w_i \)")
plt.plot(r, w_vertical_smooth, label="Vertical Displacement (Smoothed)", color='red')
plt.legend()
plt.grid(True)
plt.show()

# Plot vertical stress
plt.figure()
plt.title("Vertical Stress")
plt.xlabel("Radial Distance, \( r \)")
plt.ylabel(r"Vertical Stress, \( \sigma_{zi} \)")
plt.plot(r, sigma_zi, label="Vertical Stress")
plt.legend()
plt.grid(True)
plt.show()
