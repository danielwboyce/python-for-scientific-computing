# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:31:41 2019

@author: dboyce5
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#constants
sigma = 2. #in N/m
mu = 0.3 #in kg/m**2
cspeed = np.sqrt(sigma/mu)

# Make 1D x and y arrays
Nx = 50
a = -5
b = 5
x,hx = np.linspace(a,b,Nx,retstep = True)
Ny = Nx
c = -5
d = 5
y,hy = np.linspace(c,d,Ny,retstep = True)

# Make the 2D grid
X, Y = np.meshgrid(x, y)

print(hx/cspeed)

f = 0.71

tfinal = 10
tau = f * hx / cspeed
t=np.arange(0,tfinal,tau)
skip = 10

Z = np.exp(-5 * (X**2 + Y**2))
Z[0,:] = np.zeros_like(Z[0,:]) #row
Z[-1,:] = np.zeros_like(Z[-1,:])
Z[:,0] = np.zeros_like(Z[:,0]) #column
Z[:,-1] = np.zeros_like(Z[:,-1])

Zold = np.zeros_like(Z)
Zold[1:-1,1:-1] = (1 - (sigma * tau**2 / mu)*((1/(hx**2)) + (1/(hy**2)))) * Z[1:-1,1:-1] + ((sigma * tau**2)/(2 * mu * hx**2)) * (Z[1:-1,2:] + Z[1:-1,:-2]) + ((sigma * tau**2)/(2 * mu * hy**2)) * (Z[2:,1:-1] + Z[:-2,1:-1])

Znew = np.zeros_like(Z)

fig = plt.figure(1)
# here is the loop that steps the solution along
for m in range(len(t)):

    Znew[1:-1,1:-1] = 2 * (1 - (sigma * tau**2 / mu)*((1/(hx**2)) + (1/(hy**2)))) * Z[1:-1,1:-1] - Zold[1:-1,1:-1]+ ((sigma * tau**2)/(mu * hx**2)) * (Z[1:-1,2:] + Z[1:-1,:-2]) + ((sigma * tau**2)/(mu * hy**2)) * (Z[2:,1:-1] + Z[:-2,1:-1])
    
    Zold = np.copy(Z)
    Z = np.copy(Znew)
    
    # make plots every skip time steps
    if m % skip == 0:
        plt.clf()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X,Y,Z)
        ax.set_zlim(-0.5, 0.5)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.draw()
        plt.pause(0.1)