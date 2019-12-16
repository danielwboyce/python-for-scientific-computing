import numpy as np
import scipy.linalg as la

# Physical Constants
gamma = 1.4     # Adiabatic Exponent
kappa = 2.4e-2  # Thermal conductivity originally 0.024
kB = 1.38e-23   # Boltzman Constant
M = 29*1.67e-27 # Mass of air molecule (Average)
mu = 1.82e-5  # Coefficient of viscosity originally 1.82e-5
F = (gamma-1)*M*kappa/kB   # a useful constant


def Srho(rho,v,vp,tau,h):
    # Step rho forward in time by using Crank-Nicolson
    # on the continuity equation

    N = len(rho)
    A = np.zeros((N,N))
    B = np.zeros_like(A)

    # Load interior points
    const = -tau/8/h
    for j in range(1,N-1):
        C1 = const * (v[j+1] + vp[j+1])
        C2 = const * (v[j-1] + vp[j-1])
        A[j,j-1] = C2
        A[j,j] = 1
        A[j,j+1] = -C1
        B[j,j-1] = -C2
        B[j,j] = 1
        B[j,j+1] = C1

    # Apply boundary condition

    # Write your code here
    
    A[0,0] = (1/(2 * tau)) + (1/(4 * h)) * (vp[1] + v[1] - vp[0] - v[0])
    A[0,1] = (1/(2 * tau)) + (1/(4 * h)) * (vp[1] + v[1] - vp[0] - v[0])
    A[-1,-2] = (1/(2 * tau)) + (1/(4 * h)) * (vp[-1] + v[-1] - vp[-2] - v[-2])
    A[-1,-1] = (1/(2 * tau)) + (1/(4 * h)) * (vp[-1] + v[-1] - vp[-2] - v[-2])
    
    B[0,0] = (1/(2 * tau)) - (1/(4 * h)) * (vp[1] + v[1] - vp[0] - v[0])
    B[0,1] = (1/(2 * tau)) - (1/(4 * h)) * (vp[1] + v[1] - vp[0] - v[0])
    B[-1,-2] = (1/(2 * tau)) - (1/(4 * h)) * (vp[-1] + v[-1] - vp[-2] - v[-2])
    B[-1,-1] = (1/(2 * tau)) - (1/(4 * h)) * (vp[-1] + v[-1] - vp[-2] - v[-2])

    # Crank Nicolson solve to step rho in time
    r = B@rho

    return la.solve(A,r)


def ST(T,v,vp,rho,rhop,tau,h):

    N = len(T)
    A = np.zeros((N,N))
    B = np.zeros_like(A)

    # Load interior points
    for j in range(1,N-1):
        D1 = (v[j] + vp[j])/(4*h) + 2*F/(rho[j]+rhop[j])/h**2
        D2 = (-(gamma-1) * (v[j+1] + vp[j+1] - v[j-1] - vp[j-1] )/(4*h)
              - 4*F/(rho[j] + rhop[j])/h**2 )
        D3 = -(v[j] + vp[j])/(4*h) + 2*F/(rho[j]+rhop[j])/h**2

        A[j,j-1] = -0.5*D1
        A[j,j] = 1/tau - 0.5*D2
        A[j,j+1] = -0.5*D3
        B[j,j-1] = 0.5*D1
        B[j,j] = 1/tau + 0.5*D2
        B[j,j+1] = 0.5*D3

    # Apply boundary condition
    # Insulating: dt/dx = 0

    # Write your code here
    A[0,0] = -1
    A[0,1] = 1
    A[-1,-2] = -1
    A[-1,-1] = 1
    
    B[0,0] = 1
    B[0,1] = -1
    B[-1,-2] = 1
    B[-1,-1] = -1

    # Crank Nicolson solve to step rho in time
    r = B@T
    return la.solve(A,r)


def Sv(v,vbar,vbarp,rho,rhop,T,Tp,tau,h):

    N = len(rho)
    A = np.zeros((N,N))
    B = np.zeros_like(A)
    E0 = np.zeros_like(v)

    # Load interior points
    for j in range(1,N-1):
        E0[j] = (-kB/4/h/M/(rho[j]+rhop[j]) *
                 ( (rho[j+1] + rhop[j+1]) * (T[j+1] + Tp[j+1])
                 - (rho[j-1] + rhop[j-1]) * (T[j-1] + Tp[j-1])) )
        E1 = (vbar[j] + vbarp[j])/(4*h)+8*mu/3/h**2/(rho[j]+rhop[j])
        E2 =-16*mu/3/h**2/(rho[j]+rhop[j])
        E3 =-(vbar[j] + vbarp[j])/(4*h) +8*mu/3/h**2/(rho[j]+rhop[j])

        A[j,j-1] = -0.5*E1
        A[j,j] = 1/tau - 0.5*E2
        A[j,j+1] = -0.5*E3
        B[j,j-1] = 0.5*E1
        B[j,j] = 1/tau + 0.5*E2
        B[j,j+1] = 0.5*E3

    # Apply boundary condition
    # Fixed: v = 0
    
    # Write your code here
    A[0,0] = 1
    A[0,1] = 1
    A[-1,-2] = 1
    A[-1,-1] = 1
    
    B[0,0] = -1
    B[0,1] = -1
    B[-1,-2] = -1
    B[-1,-1] = -1

    # Crank Nicolson solve to step rho in time
    r = B@v + E0
    return la.solve(A,r)
