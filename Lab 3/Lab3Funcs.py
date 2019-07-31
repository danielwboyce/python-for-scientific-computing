# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:03:21 2019

@author: dboyce5
"""

import numpy as np
import numpy.linalg as la

#definition of a function force that along a coordinate axis x with N points, it creates a step function such that between a and b it has magnitude -h
def force(x, N, a, b, h):
    f = np.zeros_like(x)
    
    for n in range(1,N-1):
        if (x[n] >= a) and (x[n] <= b):
            f[n] = -h
    
    return f

#definition of a function that finds the steady state solution g(x) for the differential equation
#T * g''(x) + mu * omega**2 * g(x) = -f(x)
#where f(x) is defined elsewhere and passed into the function. T, mu, and omega are also passed into the function, as well as the number of points N and the spacing between x coordinates h that are in f(x)
def steadyState(f, N, h, T, mu, omega):
    #A is the matrix defining the linear operators acting on g(x)
    A = np.zeros((N,N))
    A[0,0] = 1 #endpoint definition: g_0 = 0
    A[-1,-1] = 1 #endpoint definition: g_(N-1) = 0
    
    #initializing -f and A
    for n in range(1,N-1):    
        A[n,n-1] = T * h**(-2)
        A[n,n] = mu * omega**2 - 2 * T * h**(-2)
        A[n,n+1] = T * h**(-2)
        
    gn = la.solve(A,f)
    
    #this function returns the solution g(x)
    return gn
