import numpy as np

def maxRange(v0,theta):
    g = 9.8 #accelation due to gravity in m/s^2
    R = v0**2 * np.sin(2*theta) / g
    return R

def maxHeight(v0,theta):
    g = 9.8 #accelation due to gravity in m/s^2
    vy = v0*np.sin(theta)
    h = vy**2 / (2*g)
    return h