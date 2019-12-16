# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:13:18 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

#we wish to solve the equation g''(x) = (-mu(x) * omega**2 / T) * g(x) as an eigenvalue problem
# we will solve it in the form A g = lambda B g, where A is a matrix describing the linear operation (the second derivative) acting on g in the lhs of the equation, lambda is the eigenvalues, and B is an identity matrix with the endpoints made to be zero so that we are solving a generalized eigenvalue problem.

#some constants
mu = 0.003
T = 127

# two boundary conditions
a = 0 #far left x coordinate of boundary condition for g(x); g(a) = 0
L = 1.2 #far right x coordinate of boundary condition for g(x); g(L) = 0

N = 30 #number of grid points we wish to use
x,h = np.linspace(a,L,N,retstep = True)


#now we'll define the A and B matrices
A = np.zeros((N,N))
A[0,0] = 1
A[-1,-1] = 1
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

#now we'll compare the exact analytical solutions and our eigenvectors and compare their graphs
g01 = np.amax(vecs[:,0])
gexact1 = g01 * np.sin(omega[0] * x * np.sqrt(mu / T))

g02 = np.amax(vecs[:,1])
gexact2 = g01 * np.sin(omega[1] * x * np.sqrt(mu / T))

g03 = np.amax(vecs[:,2])
gexact3 = g01 * np.sin(omega[2] * x * np.sqrt(mu / T))

plt.figure()
plt.plot(x,gexact1,x,vecs[:,0],'r.')
plt.plot(x,gexact2,x,vecs[:,1],'r.')
plt.plot(x,gexact3,x,vecs[:,2],'r.')
plt.show()

#and finally we'll compare our omega approximations and the exact values
omegaexact1 = 1 * (np.pi / L) * np.sqrt(T / mu)
omegaexact2 = 2 * (np.pi / L) * np.sqrt(T / mu)
omegaexact3 = 3 * (np.pi / L) * np.sqrt(T / mu)


