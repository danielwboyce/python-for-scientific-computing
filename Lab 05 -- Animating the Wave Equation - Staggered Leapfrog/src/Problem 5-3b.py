# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:47:54 2019

@author: dboyce5
"""

import numpy as np
#import scipy.linalg as la
#import matplotlib.pyplot as plt
#import scipy.special as sp

#constants
L = 1. #in m
N = 200. #number of cells; there should be N + 2 points, though

#boundary points
a = 0.
b = L

h = (b - a) / N #cell width

#more constants
c = 2. #m/s
tau = 0.2 * h / c

#x grid
x = np.arange(a - (h / 2.), b + (3. * h / 2.), h)

#initial displacement and velocity
y = 0.01 * np.exp(-(x-L/2)**2 / 0.02)
vy = np.zeros_like(x)

#yold initialization
yold = np.zeros_like(y)
yold[1:-1] = y[1:-1] - (tau * vy[1:-1]) + ((c * c * tau * tau)/(2 * h *h))*(y[2:] - 2 * y[1:-1] + y[:-2])