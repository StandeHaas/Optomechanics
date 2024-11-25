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

a3 = -1
a1 = -a3
def _a4(a3, k, L):

    a4 = -a3 * (np.cosh(k*L) + np.cos(k*L))/(np.sinh(k*L) + np.sin(k*L))
    return a4,-a4


def _u(a1,a2,a3,a4, k, x):

    u = a1*np.cosh(k*x) + a2*np.sinh(k*x) + a3*np.cos(k*x) + a4*np.sin(k*x)
    return u 

k_n = np.array(alpha_roots[0:4]) / L

color = ['navy', 'blue', 'royalblue', 'lightblue']

for i in range(len(k_n)):
    k = k_n[i]
    a4, a2 = _a4(a3,k,L)
    x = np.linspace(0,L,1000)
    u = _u(a1,a2,a3,a4, k, x)
    plt.plot(x,u, color[i], label='Mode {}'.format(i))


plt.xlabel('Length (m)')
plt.ylabel('Deflection')
plt.ylim(-2,2)
plt.xlim(0,0.0002)
plt.legend()
plt.grid(True)
plt.savefig('Images\dheory_mode.eps', format='eps')
plt.show()
