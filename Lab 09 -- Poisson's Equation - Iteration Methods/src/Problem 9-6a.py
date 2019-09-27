# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:17:10 2019

@author: daniel
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Make the grid
xmin = -2
xmax = 2
Nx = 100
hx = (xmax - xmin) / (Nx - 2)
x = np.arange(xmin - hx / 2,xmax + 3 * hx / 2,hx)
hx2 = hx**2
ymin = 0
Ly = 2
ymax = Ly
Ny = 100
hy = (ymax - ymin) / (Ny - 2)
y = np.arange(ymin - (hy / 2),ymax + (1 * hy / 2),hy)
hy2 = hy**2
X,Y = np.meshgrid(x,y,indexing='ij')


#iteration parameters
#R = (hy2 * np.cos(np.pi / Nx) + hx2 * np.cos(np.pi / Ny)) / (hx2 + hy2)
#w = 2 / (1 + np.sqrt(1 - R**2))
w = 1.5

# Initialize potential
V = 0.5*np.ones_like(X)

# Enforce boundary conditions
V0 = 1

V[0,:] = -2 * V0 - V[1,:] #x = xmin boundary
V[-1,:] = 2 * V0 - V[-2,:] #x = xmax boundary
V[:,0] = 0 #y = ymin boundary
V[:,-1] = 0 #y = ymax boundary

# Allow possibility of charge distribution
rho = np.zeros_like(X)

#error calculation
Vscale = 1 #a scaling voltage on the order of the biggest voltage in the problem; here literally the biggest voltage in the problem
xshort = np.zeros(Nx - 2)
yshort = np.zeros(Ny - 2)
lhs, rhs = np.meshgrid(xshort,yshort,indexing='ij')
eps = 1 #actual values of eps will be calculated in the loop

# Iterate
n = 0 #counter
denom = 2/hx2 + 2/hy2
fig = plt.figure(1)
while eps > (Ny**(-2)):
    # make plots every few steps
#    if n % 10 == 0:
#        plt.clf()
#        ax = Axes3D(fig)
#        surf = ax.plot_surface(X,Y,V, cmap = 'summer')
#        ax.set_zlim(-0.1, 2)
#        plt.xlabel('x')
#        plt.ylabel('y')
#        plt.draw()
#        plt.pause(0.01)
    # Iterate the solution
    for j in range(1,len(x)-1):
        for k in range(1,len(y)-1):
            V[j,k] = w * ((V[j+1,k] + V[j-1,k]) / hx2 + (V[j,k+1] + V[j,k-1]) / hy2 + rho[j,k]) / denom + (1 - w) * V[j,k]
            n = n + 1
    rhs = ((V[2:,1:-1] + V[:-2,1:-1]) / hx2 + (V[1:-1,2:] + V[1:-1,:-2]) / hy2 + rho[1:-1,1:-1]) / denom
    lhs = V[1:-1,1:-1]
    eps = np.max(np.abs(lhs - rhs) / Vscale)
    
plt.clf()
ax = Axes3D(fig)
surf = ax.plot_surface(X,Y,V, cmap = 'summer')
ax.set_zlim(-1, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.draw()