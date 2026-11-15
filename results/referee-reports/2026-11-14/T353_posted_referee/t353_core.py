# Independent recomputation of the T=2 and T=3 values of the shuffled-ABLQ paper, written from the paper's statements only.
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm
E = np.exp(0.5)  # e^eps, eps = 1/2, sigma = 1
phi = norm.pdf
def I(a, c, al, be, ga):
    f = lambda s: max(al*phi(s) + be*phi(s-a) - E*(ga*phi(s) + be*phi(s-c)), 0.0)
    return quad(f, -40, 40, points=[-5, -2, 0, 1, 2, 4, 8], limit=400, epsabs=1e-15, epsrel=1e-13)[0]
def w2(z):  # T = 2 weights
    return 0.5*phi(z-2), 0.5*phi(z), 0.5*phi(z-1)
def diffT2(z):
    al, be, ga = w2(z); return I(0, -1, al, be, ga) - I(2, 1, al, be, ga)
