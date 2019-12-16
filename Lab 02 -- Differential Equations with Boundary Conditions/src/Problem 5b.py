import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
#import scipy.special as sp

N = 250 #number of grid points
a = 0
b = 3
x,h = np.linspace(a,b,N,retstep = True)

A=np.zeros((N,N))
A[0,0] = 1
A[-1,-1] = 1

B=np.ones((N))
B[0] = 0
B[-1] = 0
#%%
yguess=np.zeros_like(x)

for n in range(1,N-1):
    A[n,n-1] = h**(-2)
    A[n,n] = -2*h**(-2)
    A[n,n+1] = h**(-2)
    yguess[n]=x[n]
    B[n] = 1-np.sin(yguess[n])
#%%

yn = la.solve(A,B)   

lhs = np.matmul(A,yguess)
rmserror = np.sqrt(np.mean((lhs-B)**2))
#%%
counter = 1
rmserrorthreshhold = 1e-11
while rmserror > rmserrorthreshhold:
    for n in range(1,N-1):
        yguess[n]=yn[n]
        B[n] = 1-np.sin(yguess[n])
    yn = la.solve(A,B)
    lhs = np.matmul(A,yguess)
    rmserror = np.sqrt(np.mean((lhs-B)**2))
    counter = counter + 1
    if counter > 1000:
        print('This is taking too long; I''ll just print what I''ve got')
        break

plt.figure()
plt.plot(x,yn,'r.')
plt.show()