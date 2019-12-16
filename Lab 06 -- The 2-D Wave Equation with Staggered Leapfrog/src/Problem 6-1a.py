# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:07:32 2019

@author: dboyce5
"""

#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
#from matplotlib import cm
import numpy as np

# Make 1D x and y arrays
Nx=30
a=0
b=2
x,hx = np.linspace(a,b,Nx,retstep = True)
Ny=50
c=-1
d=3
y,hy = np.linspace(c,d,Ny,retstep = True)

# Make the 2D grid
X, Y = np.meshgrid(x, y)
