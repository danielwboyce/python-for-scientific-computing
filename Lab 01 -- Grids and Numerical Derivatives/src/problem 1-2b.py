# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:50:43 2019

@author: dboyce5
"""

from numpy import arange, cos, sin
from matplotlib import pyplot

N=100   #number of points or cells
a=0     #beginning of range
b=2     #end of range

l= b-a  #width of range
h=l/N   #step size

x=arange(a+(h/2),b+(h/2),h) #cell-center grid
b=len(x)

f=cos(x)

pyplot.figure()
pyplot.plot(x,f)
pyplot.show()

print("The area under the grid is {:f} and the real value of sin(2) is {:f}".format(sum(f)*h,sin(2)))