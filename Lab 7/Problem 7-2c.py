# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:46:21 2019

@author: dboyce5
"""


import numpy as np
#import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants (in SI units)
L = 10 #length of x grid

N = 40 #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

#stepping constants
h = (b - a) / N #cell width
#C = 1.1
#tau = C * h**2 #time constant
tau = 50

#x grid
x = np.arange(a - (h / 2.), b + (h / 2), h)


#initial displacement (y)
y = np.ones_like(x)

ynew = np.zeros_like(y)
j = 0
t = 0
tmax = 500
plt.figure(1) # Open the figure window
# the loop that steps the solution along

while t < tmax:
    j = j + 1
    t = t + tau
    
    ynew = y / (1 - tau)
    #enforcing boundary conditions on Tnew
    
    y = np.copy(ynew)
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps
    

    

    
    if j % 1 == 0:
        plt.clf() # clear the figure window
        plt.plot(x,y,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time = {:1.3f}'.format(t))
        plt.ylim([-50,50])
        plt.xlim([0,L])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw
