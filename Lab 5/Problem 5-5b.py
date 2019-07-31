# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:49:34 2019

@author: dboyce5
"""

import numpy as np
#import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants (in SI units)
T = 127
mu = 0.003
L = 1.2
c = np.sqrt(T / mu)
gamma = 60
omega = 400

N = 200 #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

#stepping constants
h = (b - a) / N #cell width
tau = 0.2 * h / c #time constant

#x grid
x = np.arange(a - (h / 2.), b + (3. * h / 2.), h)

#forcing function
f = np.zeros_like(x)
    
for n in range(N+2):
    left = 0.8
    right = 1
    height = 0.73
    if (x[n] >= left) and (x[n] <= right):
        f[n] = height

#initial displacement (y) and yold
y = np.zeros_like(x)
yold = np.zeros_like(y)

ynew = np.zeros_like(y)
j = 0
t = 0
tmax = 2
plt.figure(1) # Open the figure window
# the loop that steps the solution along

while t < tmax:
    j = j + 1
    t = t + tau
    
    ynew[1:-1] = (1/(2 + gamma * tau))*((2 * tau**2 * f[1:-1] * np.cos(omega * t) / mu) + 4 * y[1:-1] + (gamma * tau - 2) * yold[1:-1] + (2 * c**2 * tau**2 / (h**2))*(y[2:] - 2 * y[1:-1] + y[:-2]))
    #enforcing boundary conditions on ynew
    ynew[0] = -ynew[1]
    ynew [-1] = -ynew[-2]
    
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
        plt.ylim([-0.0025,0.0025])
        plt.xlim([0,L])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw
