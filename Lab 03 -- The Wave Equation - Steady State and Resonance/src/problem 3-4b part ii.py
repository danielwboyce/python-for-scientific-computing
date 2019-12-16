# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:13:18 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

#we wish to solve the equation g''(x) = (-mu * omega**2 / T) * g(x) as an eigenvalue problem
# we will solve it in the form A g = lambda B g, where A is a matrix describing the linear operation (the second derivative) acting on g in the lhs of the equation, lambda is the eigenvalues, and B is an identity matrix with the endpoints made to be zero so that we are solving a generalized eigenvalue problem.

#some constants
mu = 0.003
T = 127

# two boundary conditions
a = 0 #far left x coordinate of boundary condition for g(x); g(a) = 0
L = 1.2 #far right x coordinate of boundary condition for g(x); g'(L) = 2*g(L)

N = 30 #number of grid points we wish to use
x,h = np.linspace(a,L,N,retstep = True)


#now we'll define the A and B matrices
A = np.zeros((N,N))
A[0,0] = 1
A[-1,-1] = -2 + 3/(2*h)
A[-1,-2] = (-2)/h
A[-1,-3] = 1/(2*h)
for n in range(1,N-1):
    A[n,n-1] = h**(-2)
    A[n,n] = -2 * h**(-2)
    A[n,n+1] = h**(-2)
B = np.identity(N)
B[0,0] = 0
B[-1,-1] = 0

#now we will find the eigenvalues and vectors of this problem
vals, vecs = la.eig(A,B)

#because lambda = (-mu * omega**2 / T), we can find omega (the eigenfrequencies)
omega = np.sqrt(-T * np.real(vals) / mu)

# now we'll sort the eigenvalues and eigenvectors
ind = np.argsort(omega)
omega=omega[ind]
vecs = vecs[:,ind]

plt.figure()
plt.plot(x,vecs[:,0])
plt.plot(x,vecs[:,1])
plt.plot(x,vecs[:,2])
plt.show()



