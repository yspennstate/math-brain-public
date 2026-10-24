"""Independent check: build the density of mu box+ S(0,t) from Biane's description and count its modes,
without using the level-set criterion at all.

For each u, v_t(u) is the positive root of  int dmu(x)/((x-u)^2+v^2) = 1/t  (when one exists), the
density at psi_t(u) = u + t*int (u-x) dmu/((x-u)^2+v^2) equals v_t(u)/(pi t), and psi_t is increasing.
So counting local maxima of v_t(u) counts the modes of the density.
"""
import numpy as np
from scipy.optimize import brentq

def vt(u, x, w, t):
    f = lambda v: (w / ((x - u) ** 2 + v * v)).sum() - 1.0 / t
    if f(1e-12) <= 0: return 0.0
    hi = 1.0
    while f(hi) > 0: hi *= 2
    return brentq(f, 1e-12, hi, xtol=1e-14)

def modes(x, w, t, n=20001):
    x = np.asarray(x, float); w = np.asarray(w, float)
    u = np.linspace(x.min() - 6, x.max() + 6, n)
    v = np.array([vt(uu, x, w, t) for uu in u])
    d = v / (np.pi * t)                       # density along the (increasing) reparametrisation
    k = 0
    for i in range(1, n - 1):
        if d[i] > d[i - 1] and d[i] >= d[i + 1] and d[i] > 1e-9: k += 1
    return k

print("symmetric Bernoulli on {-1,1}: diameter 2, theorem says unimodal from t = 4")
for t in (3.0, 3.8, 3.95, 4.05, 4.3, 6.0):
    print(f"   t = {t:>5.2f}   modes = {modes([-1, 1], [.5, .5], t)}")
print("\nasymmetric pair 0.3 at -1/2, 0.7 at +1/2: diameter 1, theorem says unimodal from t = 1")
print("   (the criterion puts the true threshold at 0.548, well inside the guarantee)")
for t in (0.3, 0.5, 0.55, 0.6, 1.0, 1.5):
    print(f"   t = {t:>5.2f}   modes = {modes([-.5, .5], [.3, .7], t)}")
print("\nthree atoms -1/2, 0, +1/2 with weights 0.45, 0.10, 0.45: diameter 1")
for t in (0.3, 0.5, 0.7, 1.0):
    print(f"   t = {t:>5.2f}   modes = {modes([-.5, 0, .5], [.45, .10, .45], t)}")
