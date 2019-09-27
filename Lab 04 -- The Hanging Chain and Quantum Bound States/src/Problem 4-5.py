# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:34:31 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

# two boundary conditions
a = -5 #far left xi coordinate of boundary condition for psi(xi); psi(a) = 0
b = 5 #far right xi coordinate of boundary condition for psi(xi); psi(b) = 0

N = 500 #number of grid points we wish to use
xi,h = np.linspace(a,b,N,retstep = True)

#now we'll define the A and B matrices
A = np.zeros((N,N))
A[0,0] = 1
A[-1,-1] = 1
for n in range(1,N-1):
    A[n,n-1] = -1/(2*h**2)
    A[n,n] = (1/(h**2)) + (xi[n]**4)
    A[n,n+1] = -1/(2*h**2)
B = np.identity(N)
B[0,0] = 0
B[-1,-1] = 0

#now we will find the eigenvalues and vectors of this problem
vals, vecs = la.eig(A,B)

#because lambda = (-g * omega**2), we can find omega (the eigenfrequencies)
#omega = np.sqrt(-vals * g)

# now we'll sort the eigenvalues and eigenvectors
ind = np.argsort(vals)
vals = vals[ind]
vecs = vecs[:,ind]

plt.figure()
plt.plot(xi,np.abs(vecs[:,0])**2)
plt.plot(xi,np.abs(vecs[:,1])**2)
plt.plot(xi,np.abs(vecs[:,2])**2)
plt.plot(xi,np.abs(vecs[:,3])**2)
plt.show()