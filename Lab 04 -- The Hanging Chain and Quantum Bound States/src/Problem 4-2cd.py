# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:18:45 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import scipy.special as sp

#some constants
L = 2 #length of the chain is 2m
g = 9.8 #acceleration due to gravity in m/(s**2)

# two boundary conditions
a = 0 #far left x coordinate of boundary condition for f(x); f'(a) = 0
b = L #far right x coordinate of boundary condition for f(x); f(b) = 0

N = 30 #number of grid points we wish to use
xcelledge,h = np.linspace(a,L,N,retstep = True)


xcenter = np.arange(a - h/2, b + 3*h/2, h)

#now we'll define the A and B matrices
A = np.zeros((N + 1,N + 1))
A[0,0] = -1/h
A[0,1] = 1/h
A[-1,-1] = 1/2
A[-1,-2] = 1/2
for n in range(1,N):
    A[n,n-1] = xcenter[n] * h**(-2)
    A[n,n] = ((-2 * xcenter[n])/(h**2)) - (1/h)
    A[n,n+1] = (xcenter[n]/(h**2)) + (1/h)
B = np.identity(N+1)
B[-1,-1] = 0

#now we will find the eigenvalues and vectors of this problem
vals, vecs = la.eig(A,B)

#because lambda = (-g * omega**2), we can find omega (the eigenfrequencies)
omega = np.sqrt(-vals * g)

# now we'll sort the eigenvalues and eigenvectors
ind = np.argsort(omega)
omega=omega[ind]
vecs = vecs[:,ind]

plt.figure()
plt.plot(xcenter,vecs[:,0])
plt.plot(xcenter,vecs[:,1])
plt.plot(xcenter,vecs[:,2])
plt.show()

x = 2
exactomegas=np.sqrt((sp.jn_zeros(0,10)**2)*g/(4*x))