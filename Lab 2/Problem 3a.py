import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
import scipy.special as sp

N = 30 #number of grid points
a = 0
b = 5
x,h = np.linspace(a,b,N,retstep = True)

y = (-4/sp.jv(1,5))*sp.jv(1,x)+x

A=np.zeros((N,N))
A[0,0] = 1
A[N-1,N-1] = 1

B=np.zeros((N))
B[0] = 0
B[-1] = 1


for n in range(1,N-1):
    A[n,n-1] = (1/h**2)-(1/(x[n]*2*h))
    A[n,n] = (-2/h**2)+1-(1/x[n]**2)
    A[n,n+1] = (1/h**2)+(1/(x[n]*2*h))
    
    B[n] = x[n]
    
yn = la.solve(A,B)

plt.figure()
plt.plot(x,y,x,yn,'r.')
plt.show()