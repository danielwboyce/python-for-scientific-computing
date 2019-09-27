# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:43:27 2019

@author: dboyce5
"""

import numpy as np
from scipy.special import jv
import matplotlib as mpl

N=20 #number of grids, add one for number of points
a=0
b=5

l=b-a
h=l/(N-1)

x=np.linspace(a,b,N)

f=jv(0,x)

fp = np.zeros_like(f)
fp[1:N-1]=(f[2:N]-f[0:N-2])/(2*h)
fp[0]=2*fp[1]-fp[2]
fp[N-1]=2*fp[N-2]-fp[N-3]


fpp = np.zeros_like(f)
fpp[1:N-1]=(f[2:N]-2*f[1:N-1]+f[0:N-2])/h**2
fpp[0]=2*fpp[1]-fpp[2]
fpp[N-1]=2*fpp[N-2]-fpp[N-3]


fpactual=-jv(1,x)
fppactual=(1/2)*(jv(2,x)-jv(0,x))

mpl.pyplot.figure()
mpl.pyplot.plot(x,f,x,fp,x,fpp)
mpl.pyplot.show()

mpl.pyplot.figure()
mpl.pyplot.plot(x,f,x,fpactual,x,fppactual)
mpl.pyplot.show()