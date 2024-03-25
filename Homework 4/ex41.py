import numpy as np

list_gen = lambda N: np.round(np.random.uniform(-1, 1, N), 3)
n = 3
point_list = [(x,y) for x in list_gen(n) for y in list_gen(n)]

a = list(filter((lambda p: True if p[0]**2 + p[1]**2 <= 1 else False), point_list))
print(a)

b = list(filter((lambda p: True if p[0]>0 and p[1] > 0 else False), point_list))
print(b)

point_list.sort(key = lambda p: (-p[1], p[0]))
print(point_list)

point_list.sort(key = lambda p: abs(p[0])+abs(p[1]))
print(point_list)