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
d2Phi_dr2 = np.gradient(dPhi_dr, r)

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

# Calculate radial stress in the horizontal plane (Equation 5)
sigma_ri = np.gradient(mu * nabla2Phi - d2Phi_dr2, z)

# Calculate tangential stress in the horizontal plane (Equation 6)
sigma_thetai = np.gradient(mu * nabla2Phi - (1 / r) * dPhi_dr, z)

# Calculate shear stress in the vertical plane (Equation 7)
tau_zi = np.gradient((1 - mu) * nabla2Phi - d2Phi_dz2, r)

# Plot shear stress in the vertical plane
plt.figure()
plt.title("Shear Stress in the Vertical Plane")
plt.xlabel(r"Radial Distance, \( r \)")
plt.ylabel(r"Shear Stress in Vertical Plane, \( \tau_{zi} \)")
plt.plot(r, tau_zi, label="Shear Stress in Vertical Plane")
plt.legend()
plt.grid(True)
plt.show()
