# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:45:13 2019

@author: dboyce5
"""

from numpy import linspace, pi, sin, sinh
from matplotlib import pyplot

N=100 # the number of grid points
a=0
b=pi
x,h = linspace(a,b,N,retstep = True)

y=sin(x)*sinh(x)

pyplot.figure()
pyplot.plot(x,y)
pyplot.show()
