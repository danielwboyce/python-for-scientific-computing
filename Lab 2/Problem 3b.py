import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
#import scipy.special as sp

N = 5000 #number of grid points
a = 0
b = 5
x,h = np.linspace(a,b,N,retstep = True)

A=np.zeros((N,N))
A[0,0] = 1
A[-1,-1] = 1

B=np.zeros((N))
B[0] = 0
B[-1] = 3


for n in range(1,N-1):
    A[n,n-1] = (1/h**2)-(np.sin(x[n])/(2*h))
    A[n,n] = np.exp(x[n])-2/(h**2)
    A[n,n+1] = (1/h**2)+(np.sin(x[n])/(2*h))
    
    B[n] = x[n]**2
    
yn = la.solve(A,B)

iterator = 1

while abs(x[iterator] - 4.5)>1e-3:
    iterator = iterator + 1

y45=8.720623277763513

print(yn[iterator])
print(abs(y45-yn[iterator])<1e-3)

plt.figure()
plt.plot(x,yn,'r.')
plt.show()