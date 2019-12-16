# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:17:29 2019

@author: daniel
"""

import numpy as np

#max number of steps that the program will iterate
N = 1000

#starting point for solution
x = 0.5

#defined parameter
w = 0.635

#first guess
xguess = w * np.exp(-x) + (1 - w) * x

#difference between new guess and previous one
difference = np.abs(xguess - x)

#counter for iterations
n = 1

   
while difference > 1e-12:
    x = xguess
    xguess = w * np.exp(-x) + (1 - w) * x
    difference = np.abs(xguess - x)
    n = n + 1