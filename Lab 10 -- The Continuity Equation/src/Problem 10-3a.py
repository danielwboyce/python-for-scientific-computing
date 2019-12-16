# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:56:16 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants (in SI units)
L = 10. #length of x grid


N = 400 #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

h = (b - a) / (N - 2) #cell width

#more constants
v0 = 1
tau = h * 0.9


#x grid (cell-edge)
x = np.arange(a - (h / 2.), b + (3. * h / 2.), h)


rho = np.zeros_like(x)
rho = 1 + np.exp(-200 * (x / L - 0.5)**2)
v = np.ones_like(x) * v0

#define A and B matrices
A = np.identity(N)
B = np.identity(N)
A[0,0] = 1
A[-1,-1] = 1
B[0,0] = 0
B[-1,-1] = 0
for n in range(1,N - 1):
    C1 = -tau * v[n + 1] / (4 * h)
    C2 = -tau * v[n - 1] / (4 * h)
    A[n,n - 1] = C2
    A[n,n] =  1
    A[n,n + 1] = -C1
    B[n,n - 1] = -C2
    B[n,n] = 1
    B[n,n + 1] = C1
    
    
#matrix multiplication to get the rhs 
r = B @ rho



# load r[1] and r[-1] as appropriate
# for the boundary conditions
r[0] = 2 - r[1]
r[-1] = 2 * r[-2] - r[-3]
#%%
# load the new T directly into T itself


k = 0
t = 0
tmax = 10
plt.figure(1) # Open the figure window
# the loop that steps the solution along

while t < tmax:
    k = k + 1
    t = t + tau
    
    rho = la.solve(A,r)
    
    #matrix multiplication to get the rhs 
    r = B @ rho

    # load r[1] and r[-1] as appropriate
    # for the boundary conditions
    r[0] = 2 - r[1]
    r[-1] = 2 * r[-2] - r[-3]
    
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps
    
    #Texact = np.sin(np.pi * x / L) * np.exp(-np.pi**2 * D * t / L**2)
    
    #error = np.sqrt( np.mean( (T - Texact)**2 ))
    
    if k % 10 == 0:
        plt.clf() # clear the figure window
        #plt.plot(x,Texact,'b-')
        plt.plot(x,rho,'b-')
        plt.xlabel('x')
        plt.ylabel('T')
        plt.title('time = {:1.3f}'.format(t))
        plt.ylim([0,2.5])
        plt.xlim([a,b])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw

