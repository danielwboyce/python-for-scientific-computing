# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:09:45 2019

@author: dboyce5
"""

from numpy import arange, sin, pi
from matplotlib import pyplot

N=500 #number of points or cells
a=0 #beginning of range
b=pi/2 #end of range

l= b-a #width of range
h=l/N #step size

x=arange(a-(h/2),b+(3*h/2),h)
b=len(x)

f=sin(x)

pyplot.figure()
pyplot.plot(x,f)
pyplot.show()

print(f)