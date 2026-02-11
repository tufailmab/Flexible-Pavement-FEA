import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv  # Bessel function of the first kind
from scipy.integrate import quad  # Numerical integration

# Biharmonic Function (Equation 1)
def biharmonic_function(m, A, B, C, D, r, z):
    # Limit the exponential terms to avoid overflow
    exp_mz = np.exp(m * z)
    exp_neg_mz = np.exp(-m * z)
    integrand = (A * exp_mz - B * exp_neg_mz + 
                 C * z * exp_neg_mz - D * z * exp_mz) * jv(0, m * r)
    return integrand

# Example parameters for biharmonic function
A = 1
B = 1
C = 1
D = 1
r = np.linspace(0.0, 0.3, 200)  # Extended range for r
z = 0.5

# Compute the biharmonic function values
Phi = np.zeros_like(r)
for i, r_val in enumerate(r):
    # Use a large but finite upper limit for integration
    result, error = quad(biharmonic_function, 0, 10, args=(A, B, C, D, r_val, z), epsabs=1e-6, epsrel=1e-6)
    Phi[i] = result

# Plot biharmonic function
plt.figure()
plt.title("Biharmonic Function")
plt.xlabel("r")
plt.ylabel("Phi")
plt.plot(r, Phi, label="Phi(r)")
plt.legend()
plt.grid(True)

# Set axis limits to start from 0
plt.xlim(0, max(r))
plt.ylim(0, max(Phi) * 1.1)  # Slightly above the maximum value of Phi

# Display the plot
plt.show()
