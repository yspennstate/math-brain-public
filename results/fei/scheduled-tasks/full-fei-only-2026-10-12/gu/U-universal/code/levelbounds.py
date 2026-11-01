import numpy as np
from math import comb, log2
from feilib import *
from families import tribes, maj, pointdefect
from upward import Uprime
def bounds(t):
    t = np.asarray(t); n = nbits(len(t)); p = spectrum(t); H = float(entropy(p)); I = float(total_influence(p, n)); Var = 1 - p[0]
    sz = sizes(n); W = np.array([p[sz == k].sum() for k in range(n + 1)])
    m = [sum(W[j] * comb(j, k) for j in range(n + 1)) for k in range(n + 1)]
    G1 = 2 * (I - Var) + 2 * (float(entropy(W)) + sum(W[k] * log2(m[k]) for k in range(1, n + 1) if W[k] > 0))
    best = min(2 * (I - Var) + 2 * (log2(sum(W[j] * (1 + lam) ** j for j in range(n + 1))) - I * log2(lam)) for lam in np.geomspace(1e-3, 1e3, 400))
    return H / I, G1 / I, best / I, (2 * (I - Var) + 2 * float(Uprime(p, n))) / I
for name, t in [('tribes3x4', tribes(3, 4)), ('tribes4x4', tribes(4, 4)), ('tribes2x8', tribes(2, 8)), ('maj13', maj(13)), ('pd12', pointdefect(12))]:
    print(name, 'H/I=%.3f  G1/I=%.3f  G2/I=%.3f  ThmG/I=%.3f' % bounds(t))
