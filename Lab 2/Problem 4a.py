import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
#import scipy.special as sp

N = 30 #number of grid points
a = 0
b = 2
x,h = np.linspace(a,b,N,retstep = True)

A=np.zeros((N,N))
A[0,0] = 1
A[-1,-1] = 1
A[-1,-2] = -1

B=np.zeros((N))
B[0] = 0
B[-1] = 0


for n in range(1,N-1):
    A[n,n-1] = h**(-2)
    A[n,n] = 9 - 2*h**(-2)
    A[n,n+1] = h**(-2)
    
    B[n] = x[n]
    
yn = la.solve(A,B)
yexact = (x/9)-(np.sin(3*x)/(27*np.cos(6)))

plt.figure()
plt.plot(x,yexact,x,yn,'r.')
plt.show()

print(np.sqrt(np.mean((yn-yexact)**2)))