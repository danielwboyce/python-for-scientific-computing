# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:22:26 2019

@author: daniel
"""

import numpy as np
#import scipy.linalg as la
#import matplotlib.pyplot as plt
#import scipy.special as sp

#max number of steps that the program will iterate
N = 1000

#starting point for solution
x = 0.5

#first guess
xguess = np.exp(-x)

#difference between new guess and previous one
difference = np.abs(xguess - x)

#counter for iterations
n = 1

#for n in range(N):
#    x = xguess
#    xguess = np.exp(-x)
#    difference = np.abs(xguess - x)
    
while difference > 1e-12:
    x = xguess
    xguess = np.exp(-x)
    difference = np.abs(xguess - x)
    n = n + 1