import numpy as np
import matplotlib.pyplot as plt

n = 100

# Generate random points
points = np.random.rand(n, 2)

# Calculate distances from (0,0)
distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)

# Set colors based on distances
colors = np.where(distances < 1, 'green', 'red')

# Set marker sizes based on |x|+|y|
marker_sizes = np.abs(points[:, 0]) + np.abs(points[:, 1])

# Plot the points
plt.scatter(points[:, 0], points[:, 1], c=colors, s=50*marker_sizes)

# Set plot limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# Show the plot
plt.show()
