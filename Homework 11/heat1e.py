#!/usr/bin/python3
#
# 1D heat/diffusion equation

import math
import numpy as np
import matplotlib.pyplot as plt

#D, Nx, Nt, L, T = 1.0, 14, 100, 1.0, 0.1
D, Nx, Nt, L, T = 1.0, 20, 250, 1.0, 0.1
#D, Nx, Nt, L, T = 1.0, 40, 500, 1.0, 0.1
t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = D*dt / (dx*dx)
print ( "r = {}".format(r) )
assert r < 0.5

#u = np.zeros( (Nx+1,Nt+1), dtype=float )  # macierz na wszystkie wyniki
u = np.empty( (Nx+1,Nt+1), dtype=float )  # macierz na wszystkie wyniki

# initial condition, t=0
#u[:,0] = 4.0 * x * (1-x)   # arc
#u[:,0] = 0.5*(np.sign(x-0.4) + np.sign(0.6 - x)) # step
#u[:,0] = np.where(x < 0.5, 2*x, 2*(1-x))
u[:,0] = np.where( x < 0.8, 0, 1) + np.where( x < 0.2, 1, 0)
#u[:,0] = 0.0   # cold rod

# boundary condition, x=0 and x=L=1
u[0,:] = 1.0   # both hot ends (cold middle)
#u[Nx,:] = 0.0   # cold end
u[Nx,:] = 1.0   # hot end

# iteration/solution the linear algebraic equations
for j in range(Nt):
    #for i in range(1,Nx):
    #    u[i,j+1] = r*u[i-1,j] + (1-2*r)*u[i,j] + r*u[i+1,j]
    # vectorization
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

# visualization
print ( u )
plt.title("1D heat equation")
plt.xlabel("time") # odwrotnie!
plt.ylabel("x")

plt.imshow(u, cmap='hot', interpolation='nearest')
#plt.imshow(u[:,::3], cmap='hot', interpolation='nearest')
#plt.imshow(u[:,::3], cmap='hot', interpolation='bilinear')
#plt.imshow(u[:,::3], cmap='hot', interpolation='hamming')
#plt.imshow(u[:,::5], cmap='hot', interpolation='nearest')

plt.colorbar()
plt.savefig("heat1e.pdf")
plt.show()


# EOF
