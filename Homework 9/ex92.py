import numpy as np
import matplotlib.pyplot as plt

n = 100

points = np.random.rand(n, 2)

distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)

colors = np.where(distances < 1, 'green', 'red')

marker_sizes = np.abs(points[:, 0]) + np.abs(points[:, 1])

plt.scatter(points[:, 0], points[:, 1], c=colors, s=50*marker_sizes)
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.show()
