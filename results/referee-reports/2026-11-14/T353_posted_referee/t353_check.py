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
print("z1=2.5: I_A=%.13f I_S=%.13f" % (I(2, 1, *w2(2.5)), I(0, -1, *w2(2.5))))
print("z1=1.7 diff=%.4e" % diffT2(1.7))
pair = quad(lambda z: I(2, 1, *w2(z)), -15, 18, limit=400, epsabs=1e-13)[0]
best = quad(lambda z: max(I(2, 1, *w2(z)), I(0, -1, *w2(z))), -15, 18, points=[2.0, 2.005, 2.01], limit=400, epsabs=1e-13)[0]
print("T=2 H(P||Q)=%.6f best switch=%.6f gain=%.4e" % (pair, best, best - pair))
# reverse orientation of the pair: Q||P (swap roles: p <- q, q <- p)
def Irev(al, be, ga):
    f = lambda s: max(ga*phi(s) + be*phi(s-1) - E*(al*phi(s) + be*phi(s-2)), 0.0)
    return quad(f, -40, 40, points=[-5, 0, 1, 2, 4], limit=400, epsabs=1e-15)[0]
print("T=2 H(Q||P)=%.6f" % quad(lambda z: Irev(*w2(z)), -15, 18, limit=400, epsabs=1e-13)[0])
g = quad(diffT2, 2.1, 2.6, limit=200, epsabs=1e-14)[0]
zs = np.linspace(2.1, 2.6, 201); mn = min(diffT2(z) for z in zs)
print("int_{2.1}^{2.6} (I_S - I_A) = %.4e (claim >= 1.04e-4); min on grid %.4e (claim >= 2.0828e-4)" % (g, mn))
# where the switch starts to win
lo, hi = 1.9, 2.1
for _ in range(40):
    mid = (lo + hi)/2
    if diffT2(mid) > 0: hi = mid
    else: lo = mid
print("transition z1 = %.4f (paper: near 2.005)" % hi)
# T = 3 point value
def w3(y):
    y1, y2 = y; T = 3
    al = (phi(y1-2)*phi(y2) + phi(y1)*phi(y2-2))/T; ga = (phi(y1-1)*phi(y2) + phi(y1)*phi(y2-1))/T; be = phi(y1)*phi(y2)/T
    return al, be, ga
a = w3((-0.1, 2.25)); print("T=3 y=(-0.1,2.25) diff=%.9e (paper 1.535260930e-3)" % (I(0, -1, *a) - I(2, 1, *a)))
# corners and centre of B for the sign
for y in [(-0.3, 2.2), (-0.3, 2.3), (0.1, 2.2), (0.1, 2.3), (-0.1, 2.25)]:
    a = w3(y); print("  B point", y, "diff=%.4e" % (I(0, -1, *a) - I(2, 1, *a)))
# analytic region check at T=2: z1 in [3, 12]
print("T=2 z1>=3 min diff on grid: %.3e" % min(diffT2(z) for z in np.linspace(3, 12, 91)))
