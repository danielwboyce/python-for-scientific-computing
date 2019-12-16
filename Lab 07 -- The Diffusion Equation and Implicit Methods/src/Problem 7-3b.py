# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:29:44 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants (in SI units)
D = 2 #diffusion constant
L = 3 #length of x grid

N = 200 #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

#stepping constants
h = (b - a) / N #cell width
#C = 1.1
#tau = C * h**2 #time constant
tau = 0.1

#x grid
x = np.arange(a - (h / 2.), b + (3*h / 2), h)

T = np.zeros_like(x)
T = np.sin(np.pi * x / L)

#define A and B matrices
A = np.identity(N + 2)
B = np.identity(N + 2)
A[0,0] = -1
A[0,1] = 1
A[-1,-1] = 1
A[-1,-2] = -1
B[0:] = 0
B[-1:] = 0
for n in range(1,N + 1):
    A[n,n] = 2 + ((2 * h**2) / (tau * D))
    B[n,n] = -2 + ((2 * h**2) / (tau * D))
    A[n,n + 1] = -1
    A[n,n - 1] = -1
    B[n,n + 1] = 1
    B[n,n - 1] = 1
    
    
#matrix multiplication to get the rhs 
r = B@T

# load r[1] and r[-1] as appropriate
# for the boundary conditions
r[0] = 0
r[-1] = 0

# load the new T directly into T itself


j = 0
t = 0
tmax = 5
plt.figure(1) # Open the figure window
# the loop that steps the solution along

while t < tmax:
    j = j + 1
    t = t + tau
    
    T = la.solve(A,r)
    
    #matrix multiplication to get the rhs 
    r = B@T

    # load r[1] and r[-1] as appropriate
    # for the boundary conditions
    r[0] = 0
    r[-1] = 0
    
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps
    
    #Texact = np.sin(np.pi * x / L) * np.exp(-np.pi**2 * D * t / L**2)
    
    #error = np.sqrt( np.mean( (T - Texact)**2 ))
    
    if j %   1 == 0:
        plt.clf() # clear the figure window
        #plt.plot(x,Texact,'b-')
        plt.plot(x,T,'r.')
        plt.xlabel('x')
        plt.ylabel('T')
        #plt.title('time = {:1.3f}, error = {:6f}'.format(t,error))
        plt.title('time = {:1.3f}'.format(t))
        plt.ylim([0,0.8])
        plt.xlim([0,L])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw

