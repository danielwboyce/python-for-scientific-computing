# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:12:21 2019

@author: dboyce5
"""
import numpy as np
import numpy.linalg as la
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
#we are initializing the container for f here and will initialize its values below
f = np.zeros_like(x)

#A is the matrix defining the linear operators acting on g(x)
A=np.zeros((N,N))
A[0,0] = 1 #endpoint definition: g_0 = 0
A[-1,-1] = 1 #endpoint definition: g_(N-1) = 0

#initializing -f and A
for n in range(1,N-1):
    if (x[n] >= b) and (x[n] <= c):
        f[n] = -0.73
    
    A[n,n-1] = T * h**(-2)
    A[n,n] = mu * omega**2 - 2 * T * h**(-2)
    A[n,n+1] = T * h**(-2)
    
#solving for g(x)
gn = la.solve(A,f)

#plotting
plt.figure()
plt.plot(x,gn)
plt.show()