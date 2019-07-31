#import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la

#a = [[4,3,2],[1,2.5,9],[4.2,2.9,10.5],[39.4,1.4],[2.7,98,42,16.2]]
#a[1][2] = 'george'

#x = np.array([1,2,3])   # x is a NumPy array
#print(x+x)              # adding two NumPy arrays adds the values
#y = [1,2,3]             # y is a Python list
#print(y+y)              # adding lists concatenates the two lists

#a = [1,2,3,4,5,6,7,8,9,10]
#print(a[1:])
#print(a[1:3])
#print(a[:3])
#print(a[1:4:2])
#print(a[5:2:-1])

#b = a[[2,3,5,9]]

#a = range(10,20,2)
#b = range(3,9)
#c = range(10)

#s = 0
#for x in [3,42,1,9.9]:
#    s = s + x
#    print(s)
#    
#for y in range(5,50,3):
#    print(y)
   
#%% 

for n in np.arange(5,50,.1):
    print(n)

#%%
    
s = 0
for n in range(1,1001):
    s += 1/n**2
print(s)

#%%

p = 1
for n in range(1,21):
    p *= n # Multiply p by n
print(p)

#%%

a = 1
b = 3
if a > 0:
    c = 1
else:
    c = 0
if a >= 0 or b >= 0: # If condition 1 met
    c = a + b
elif a > 0 and b >= 0: # If condition 2 met
    c = a - b
else: # If neither condition is met.
    c = a * b
    
#%%
    
a = 0.1
b = 3 * a
c = 0.3
print(b==c) # Are they the same number?
print(b) # It sure looks like they are the same.
print(c) # It sure looks like they are the same.
print(" {:.45f} ".format(b)) #b--- out to 45 decimal places
print(" {:.45f} ".format(c)) #c--- out to 45 decimal places

#%%
a = 0.1
b = 3 * a
c = 0.3
print(abs(b - c) < 1e-10)

#%%

term = 1 # Load the first term in the sum
s = term # Initialize the sum
n = 1 # Set a counter
while term > 1e-10: # Loop while term is bigger than 1e-10
    n += 1 #Add 1 to n so that it will count: 2,3,4,5
    if n % 3 != 0:
        continue
    term = 1./n**2 # Calculate the next term to add
    s += term # Add 1/n^2 to the running total
    if n > 1000:
        print('This is taking too long. I''m outta here...')
        break

#%%
        
A = np.zeros((100,200))
s=A.shape
B=np.ones((100,200))
I=np.identity(100)

#%%

a = np.array([[1,2],[3,4]])     # Create 2 x 2 matrix
b = np.array([[5,6],[8,9]])     # Create 2 x 2 matrix
col = np.array([[3],[4]])       # Create 2 x 1 column vector

c = a.T                         # Transpose the matrix
e = a.conj().T                  # Find conjugate transpose of matrix
f = a @ b                       # Matrix multiplication
g = b @ col                     # Multiply matrix b to column vector
d = la.inv(a)                   # Find inverse of matrix

#%%

a = np.array([[3,1],[1,2]])
b = np.array([[9],[8]])
x = la.solve(a,b)


#%%
