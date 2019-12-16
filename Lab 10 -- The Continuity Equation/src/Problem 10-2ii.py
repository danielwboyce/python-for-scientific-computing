# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:08:29 2019

@author: dboyce5
"""


import numpy as np
#import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants
L = 10. #in m
N = 400. #number of cells; there should be N + 2 points, though


#boundary points
a = 0.
b = L

h = (b - a) / (N - 2) #cell width

#more constants
v0 = 1
tau = h * 0.9

#x grid
x = np.arange(a - (h / 2.), b + (3. * h / 2.), h)

#initial displacement and velocity
rho = 1 + np.exp(-200 * (x / L - 0.5)**2)
v = np.ones_like(x) * v0
#enforcing boundary conditions when initializing y
rho[0] = 2 * 1 - rho[1]
rho[-1] = 2 * rho[-2] - rho[-3]

rhonew = np.zeros_like(rho)
peakdensity = []
times = []
j = 0 #counter
t = 0
#%%
tmax = 10
plt.figure(1) # Open the figure window
# the loop that steps the solution along
while t < tmax:
    times.append(t)
    peakdensity.append(np.max(rho))
    j = j + 1
    t = t + tau
    
    rhonew[1:-1] = rho[1:-1] - ((v0 * tau) / (2 * h)) * (rho[2:] - rho[:-2]) + ((v0**2 * tau**2) / (2 * h**2)) * (rho[2:] - 2 * rho[1:-1] + rho[:-2])
    #enforcing boundary conditions on ynew
    rhonew[0] = 2 * 1 - rhonew[1]
    rhonew[-1] = 2 * rhonew[-2] - rhonew[-3]
    
    rho = np.copy(rhonew)
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps
    if j % 25 == 0:
        plt.clf() # clear the figure window
        plt.plot(x,rho,'b-')
        plt.xlabel('x')
        plt.ylabel('rho')
        plt.title('time={:1.3f}'.format(t))
        plt.ylim([0.9,2.5])
        plt.xlim([a,b])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw
        
plt.figure(2)
plt.plot(times,peakdensity)