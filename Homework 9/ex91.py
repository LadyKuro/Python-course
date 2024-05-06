import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.plot(x, y1, 'r-', label='sin(x)')
plt.plot(x, y2, 'g--', label='cos(x)')
plt.plot(x, y3, 'b:', label='exp(-x)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.show()
