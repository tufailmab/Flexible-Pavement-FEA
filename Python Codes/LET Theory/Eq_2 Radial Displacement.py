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
r = np.linspace(0.0, 0.3, 200)  # Range for r
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

# Plot radial displacement
plt.figure()
plt.title("Radial Displacement")
plt.xlabel("Radial Distance, r")
plt.ylabel("Radial Displacement, u_radial")
plt.plot(r, u_radial, label="u_radial(r)")
plt.legend()
plt.grid(True)
plt.show()
