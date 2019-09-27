# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:12:16 2019

@author: dboyce5
"""

#import numpy
from numpy import sin,arange
#from scipy.special import j0 # Bessel function of the 1st kind of
                             # order 0
from matplotlib import pyplot

#print('Hello, Jacob Michael Barker!')
#
#print(1+1)
#
#x=20
#
#x=x+1
#
#a = 2
#b = 4
#c = a * b
#
##a=input('What is your age?')
#
#a = 20
#b = 15
#c = a + b # add two numbers
#d = a/b # floating point division
#i = a//b # integer division
#r = a % b # return only the remainder(an integer) of the division
#e = a * b # multiply two numbers together
#f = c**4 # raise number to a power (use **, not ^)
#
#
#a = 20
#b = float(a)
#
#a = 0.1
#b = 3 * a #Integer multiplied by a float results in a float.
#
#y = 1.23e15
#
#q = True
#
#s='This is a string'
#t="Don't worry"
#
#a = 22
#b = 3.5
#print("I am {:d} years old and my GPA is: {:5.2f}".format(a, b))
##This style also works
#joe_string="My GPA is {:5.2f} and I am {:d} years old."
#print(joe_string.format(b,a))
#
#x=3.14
#y=round(x)
#
#x=3.14
#y=2
#b,c=divmod(x,y)
#
#x = numpy.pi # Get the value of pi
#y = numpy.sin(x) # Find the sine of pi radians
#z = numpy.sqrt(x) # Take the square root of pi
#
#z=sqrt(x)
#
#
#a = 5.5
#b = 6.2
#c = pi/2
#d = a * sin(b * c)
#e = a * j0(3.5 * pi/4)
#
#my_sum=sum((x-5)**3)
#
#
#a = array([1,2,3,4,5,6,7,8,9,10])
#b = arange(0,10,.1)
#
#myArray,mydx = linspace(0,10,10,retstep = True)
#
#xList = [2 , 3 , 5.2 , 2 , 6.7]
#xArray = array(xList) # Create first array
#yArray = array([4,8,9.8,2.1,8.2,4.5]) # Create second array
#c = xArray**2 # Square the elements of the first array
#d = xArray + 3 # Add 3 to every element of the first array
#e = xArray * 5 # Multipy every element of the first array by 5
#f = xArray + yArray # Add the elements of array one to the elements of
## array two
#g = xArray * yArray # Multiply the elements of array one by
## the elements of array two

x=arange(0,10,0.01)
y=sin(5*x)
pyplot.figure()
pyplot.plot(x,y)
pyplot.show()
#pyplot.savefig('filename.png')

nhalf = len(x)//2
pyplot.plot(x[0:nhalf],y[0:nhalf])
pyplot.plot(x[nhalf:],y[nhalf:])
pyplot.show()
