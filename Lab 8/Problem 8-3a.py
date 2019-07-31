# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:03:17 2019

@author: dboyce5
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
#import scipy.special as sp

#constants (in SI units)
hbar = 1 #Planck's constant
L = 10 #length of x grid
sigma = 2
p = 2 * np.pi
m = 1
Eexpect = (p**2 /(2 * m)) + (hbar**2 / (4 * m * sigma**2))
V0 = Eexpect * 0.5

N = 500 #number of cells; there should be N + 2 points, though

#boundary points
a = -2 * L
b = 3 * L

#stepping constant
tau = 0.01

#x grid (cell-edge)
x,h = np.linspace(a, b,N,retstep = True,dtype=np.complex_)

barrierindices = []
#potential (zero inside well)
V = np.zeros_like(x,dtype=np.complex_)
for n in range(len(V)):
    if x[n] <= L and x[n] >= 0.95 * L:
        V[n] = V0
        barrierindices.append(n)

Psi = np.zeros_like(x,dtype=np.complex_)
Psi = np.exp(1j * p * x / hbar) * np.exp(-x**2 / (2 * sigma**2)) / (np.sqrt(sigma * np.sqrt(np.pi)))
#%%
#define A and B matrices
A = np.identity(N,dtype=np.complex_)
B = np.identity(N,dtype=np.complex_)
A[0,0] = 1
A[-1,-1] = 1
B[0:] = 0
B[-1:] = 0
for n in range(1,N - 1):
    A[n,n] = (1j * hbar / tau) - (hbar**2 / (2 * m * hbar**2)) - (V[n] / 2)
    B[n,n] = (1j * hbar / tau) + (hbar**2 / (2 * m * hbar**2)) + (V[n] / 2)
    A[n,n + 1] = hbar**2 / (4 * m * h**2)
    A[n,n - 1] = hbar**2 / (4 * m * h**2)
    B[n,n + 1] = -hbar**2 / (4 * m * h**2)
    B[n,n - 1] = -hbar**2 / (4 * m * h**2)
    
    
#matrix multiplication to get the rhs 
r = B @ Psi

# load r[1] and r[-1] as appropriate
# for the boundary conditions
r[0] = 0
r[-1] = 0

# load the new T directly into T itself


k = 0
t = 0
tmax = 25
plt.figure(1) # Open the figure window
# the loop that steps the solution along


#%%
while t < tmax:
    k = k + 1
    t = t + tau
    
    Psi = la.solve(A,r)
    PsiStar = np.conj(Psi)
    PsiSq = np.real(PsiStar * Psi)
    
    totalintegral = np.trapz(PsiSq,x,h)
    
    leftbarrier = np.trapz(np.real(np.conj(Psi[:barrierindices[0]]) * Psi[:barrierindices[0]]),x[:barrierindices[0]],h)
    
    rightbarrier = np.trapz(np.real(np.conj(Psi[barrierindices[-1] + 1:]) * Psi[barrierindices[-1] + 1:]),x[barrierindices[-1] + 1:],h)
    
    #matrix multiplication to get the rhs 
    r = B @ Psi

    # load r[1] and r[-1] as appropriate
    # for the boundary conditions
    r[0] = 0
    r[-1] = 0
    
    # Use leapfrog and the boundary conditions to load
    # ynew with y at the next time step using y and yold
    # update yold and y for next timestep
    # remember to use np.copy
    # make plots every 50 time steps
    
    #Texact = np.sin(np.pi * x / L) * np.exp(-np.pi**2 * D * t / L**2)
    
    #error = np.sqrt( np.mean( (T - Texact)**2 ))
    
    if k % 50 == 0:
        plt.clf() # clear the figure window
        #plt.plot(x,Texact,'b-')
        plt.plot(x,PsiSq,'b-')
        plt.plot(x,V / V0,'r-')
        plt.xlabel('x')
        plt.ylabel('T')
        plt.title('time = {:1.3f}, area under left side of barrier |Psi|**2 = {:1.6f}, area under right side of barrier |Psi|**2 = {:1.6f}, total area under |Psi|**2 = {:1.6f}'.format(t,leftbarrier,rightbarrier,totalintegral))
        plt.ylim([0,1.1])
        plt.xlim([a,b])
        plt.draw() # Draw the plot
        plt.pause(0.1) # Give the computer time to draw