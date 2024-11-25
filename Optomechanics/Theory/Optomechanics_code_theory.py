#II.3B
import numpy as np
from scipy.optimize import brentq

def f(alpha):
    return np.cos(alpha) * np.cosh(alpha) + 1

def roots(f):
    roots = []
    alpha_range = np.linspace(0,30,1000)

    # since there are multiple roots we can't use brentq immidiatelly but must split it in for example multiple intervals, and check if these contain a 0
    for i in range(len(alpha_range)-1):
        alpha0 = alpha_range[i]
        alpha1 = alpha_range[i+1]


        # just to chech if it went through the zero-line
        if f(alpha0)*f(alpha1) < 0:
            root = brentq(f,alpha0,alpha1)
            roots.append(root)
    
    return roots


alpha_roots = roots(f)
print(alpha_roots)

##II.B6
def frequency(kn,E,rho,L,h):
    f = np.round((kn**2 / (2 * np.pi)) * np.sqrt((E * h**2) / (12 * rho * L**4)))
    return f

alpha_roots= alpha_roots[0:5]
w = 20e-6       #micro m 
L = 200e-6      #micro m
h = 0.5e-6      #micro m
E = 285e9       #Pa
rho = 3440      #kg/m3

frequencies = frequency(np.array(alpha_roots),E,rho,L,h)
print(frequencies)