import numpy as np

m1 = np.arange(20).reshape(4, 5)
print("m1:")
print(m1)
print("")

m2 = np.flip(m1, axis=1)
print("m2:")
print(m2)
print("")

m3 = np.flip(m1, axis=0)
print("m3:")
print(m3)
print("")

m4 = m1[1:-1, 1:-1]
print("m4:")
print(m4)
print("")