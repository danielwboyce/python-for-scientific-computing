import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt

N = 30 #number of grid points
a = 0
b = 2
x,h = np.linspace(a,b,N,retstep = True)

y = (16*np.sin(3*x) + np.cos(6-x) - np.cos(6+x) + np.cos(2 + 3*x) - np.cos(2 - 3*x))/(16*np.sin(6))

A=np.zeros((N,N))
A[0,0] = 1
A[N-1,N-1] = 1

b=np.zeros(N)
b[N-1] = 1

for n in range(N-2):
    A[n+1,n] = h**(-2)
    A[n+1,n+1] = 9 - 2*h**(-2)
    A[n+1,n+2] = h**(-2)
    
    b[n+1] = np.sin(x[n+1])
    
yn = la.solve(A,b)

plt.figure()
plt.plot(x,y,x,yn,'r.')
plt.show()