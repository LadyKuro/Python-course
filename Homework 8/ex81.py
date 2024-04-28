import numpy as np

arr_a = np.arange(0.0, 1.1, 0.1)
assert arr_a.shape == (11,)
print("arr_a")
print(arr_a)
print("")

arr_b = np.zeros((5, 6), dtype=np.int8)
assert arr_b.shape == (5, 6)
print("arr_b:")
print(arr_b)
print("")


x = 0+1j
arr_c = np.power(x, np.arange(9))
assert arr_c.shape == (9,)
print("arr_c:")
print(arr_c)
print("")

