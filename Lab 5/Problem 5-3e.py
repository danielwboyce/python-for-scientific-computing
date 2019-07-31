# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:34:01 2019

@author: dboyce5
"""

import numpy as np
#import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants
L = 1. #in m
N = 200. #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

h = (b - a) / N #cell width

#more constants
c = 2. #m/s
tau = 0.2 * h / c

#x grid
x = np.arange(a - (h / 2.), b + (3. * h / 2.), h)

#initial displacement and velocity
y = 0.01 * np.exp(-(x-L/2)**2 / 0.02)
vy = np.zeros_like(x)
#enforcing boundary conditions when initializing y
y[0] = y[1]
y[-1] = y[-2]

#yold initialization
yold = np.zeros_like(y)
yold[1:-1] = y[1:-1] - (tau * vy[1:-1]) + ((c * c * tau * tau)/(2 * h *h))*(y[2:] - 2 * y[1:-1] + y[:-2])
#enforcing boundary conditions when initializing yold
yold[0] = yold[1]
yold[-1] = yold[-2] 

ynew = np.zeros_like(y)
j = 0
t = 0
tmax = 2
plt.figure(1) # Open the figure window
# the loop that steps the solution along
while t < tmax:
    j = j + 1
    t = t + tau
    
    ynew[1:-1] = 2 * y[1:-1] - yold[1:-1] + ((c * tau / h)**2 )*(y[2:]-2*y[1:-1]+y[:-2])
    #enforcing boundary conditions on ynew
    ynew[0] = ynew[1]
    ynew [-1] = ynew[-2]
    
    yold = np.copy(y)
    y = np.copy(ynew)
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps
    if j % 50 == 0:
        plt.clf() # clear the figure window
        plt.plot(x,y,'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('time={:1.3f}'.format(t))
        plt.ylim([-0.03,0.03])
        plt.xlim([0,1])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw