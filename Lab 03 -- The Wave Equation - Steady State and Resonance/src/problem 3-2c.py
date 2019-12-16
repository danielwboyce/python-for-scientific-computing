# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:30:30 2019

@author: dboyce5
"""

import numpy as np
import Lab3Funcs as lab3
from matplotlib import pyplot as plt

#we are attempting to solve the equation T * g''(x) + mu * omega**2 * g(x) = -f(x)

N = 100 #number of grid points
mu = 0.003
T = 127
omega = 400
a = 0 #far left x coordinate of boundary condition for g(x)
b = 0.8 #left coordinate for change in step function for f(x)
c = 1 #right coordinate for change in step function for f(x)
L = 1.2 #far right x coordinate of boundary condition for g(x)
x,h = np.linspace(a,L,N,retstep = True)

#f is a step function such if b<x<c then f(x)=0.73, else f(x)=0
#lab3.force creates this function
f = lab3.force(x, N, b, c, 0.73)

#defining a list of omegas from 400 to 1700 with 200 steps
omegas = np.linspace(400,1700,200)

#now, for each value of omega, we're going to find the amplitude of the solution of g(x) there and save and plot the amplitude at each value of omega
amplitudes = np.zeros_like(omegas) #creating container for amplitudes
for n in range(len(omegas)): 
    #lab3.steadyState accepts the force function f(x) and the other constants that go into the  differential equation and returns the solution to the equation g(x)
    gn = lab3.steadyState(f, N, h, T, mu, omegas[n])
    
    amplitudes[n] = np.amax(gn)
    
plt.figure()
plt.plot(omegas,amplitudes)
plt.show()
