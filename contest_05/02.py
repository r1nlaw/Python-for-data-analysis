import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)

plt.figure(figsize=(6, 4))

plt.scatter(x, y, c='red', label='red')
plt.scatter(x + 0.1, y + 0.1, c='green', label='green')
plt.scatter(x + 0.2, y + 0.2, c='blue', label='blue')

plt.legend(loc='upper right', fontsize=10)

plt.xlim([-0.2, 1.2])
plt.ylim([-0.2, 1.2])

plt.show()

print('1')
