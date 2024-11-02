import matplotlib.pyplot as plt
import numpy as np

degrees = np.arange(1, 8)
error_sigma_01 = 10**np.linspace(-2, -11, len(degrees))  # blue
error_sigma_05 = 10**np.linspace(-1, -7, len(degrees))   # green
error_sigma_09 = 10**np.linspace(-1, -3, len(degrees))   # red

plt.figure(figsize=(8, 6))
plt.loglog(degrees, error_sigma_01, 'b^-', label=r'$\sigma = 0.1$', markersize=10, linewidth=2)
plt.loglog(degrees, error_sigma_05, 'g^-', label=r'$\sigma = 0.5$', markersize=10, linewidth=2)
plt.loglog(degrees, error_sigma_09, 'rs-', label=r'$\sigma = 0.9$', markersize=10, linewidth=2)

plt.title('Convergence plot', fontsize=16)
plt.xlabel('Highest Degree of Polynomials P', fontsize=14)
plt.ylabel(r'$L_2$ error', fontsize=14)

plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend(loc='lower left', fontsize=12)
plt.ylim([1e-13, 1e-1])

plt.show()

print('1')
