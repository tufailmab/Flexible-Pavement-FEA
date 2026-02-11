import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv  # Bessel function of the first kind
from scipy.integrate import quad  # Numerical integration

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
d2Phi_dr2 = np.gradient(np.gradient(Phi, r), r)

# Compute the Laplacian of Phi (nabla^2 Phi)
nabla2Phi = np.gradient(np.gradient(Phi, r), r) + np.gradient(np.gradient(Phi, z), z)

# Calculate radial stress in the horizontal plane (Equation 5)
sigma_ri = np.gradient(mu * nabla2Phi - d2Phi_dr2, z)

# Plot radial stress in the horizontal plane
plt.figure()
plt.title("Radial Stress in the Horizontal Plane")
plt.xlabel(r"Radial Distance, \( r \)")
plt.ylabel(r"Radial Stress in Horizontal Plane, \( \sigma_{ri} \)")
plt.plot(r, sigma_ri, label="Radial Stress in Horizontal Plane")
plt.legend()
plt.grid(True)
plt.show()
