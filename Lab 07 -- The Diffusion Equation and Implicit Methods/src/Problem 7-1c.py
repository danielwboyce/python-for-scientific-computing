# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:14:10 2019

@author: dboyce5
"""

import numpy as np
#import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants (in SI units)
D = 0.5 #diffusion constant
L = 3 #length of x grid

N = 40 #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

#stepping constants
h = (b - a) / N #cell width
C = 0.25
tau = C * h**2 / D #time constant

#x grid
x = np.arange(a - (h / 2.), b + (h / 2), h)


#initial temperature (T)
T = np.zeros_like(x)
T = np.sin(np.pi * x / L)
T[0] = T[1]
T[-1] = T[-2]

Tnew = np.zeros_like(T)
j = 0
t = 0
tmax = 2
plt.figure(1) # Open the figure window
# the loop that steps the solution along

while t < tmax:
    j = j + 1
    t = t + tau
    
    Tnew[1:-1] = T[1:-1] + ((D * tau)/(h**2)) * (T[2:] - 2 * T[1:-1] + T[:-2])
    #enforcing boundary conditions on Tnew
    Tnew[0] = Tnew[1]
    Tnew [-1] = Tnew[-2]
    
    T = np.copy(Tnew)
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps

    

    
    if j % 50 == 0:
        plt.clf() # clear the figure window
        plt.plot(x,T,'b-')
        plt.xlabel('x')
        plt.ylabel('T')
        plt.title('time = {:1.3f}'.format(t))
        plt.ylim([0,1])
        plt.xlim([0,L])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw
