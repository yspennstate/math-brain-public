# Corrected search: a in the sorted chamber, b = (chamber point) permuted by each of the 24 perms (my first search kept b in a's chamber).
import itertools
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as Fr
import cert_b1e as C
V = np.array(C.VERT, dtype=float)
def phi24(a, b, m):
    A = a @ a; B = b @ b; return A * B * (A + B) - m * (A * A + B * B)
def bary(x):
    Mx = np.vstack([V.T, np.ones(4)]); return np.linalg.lstsq(Mx, np.append(x, 1), rcond=None)[0]
rng = np.random.default_rng(5)
res = []
for m in (0.0, float(C.M_END)):
    for pi in itertools.permutations(range(4)):
        pi = list(pi)
        def f(y):
            la, lb = np.abs(y[:4]) + 1e-15, np.abs(y[4:]) + 1e-15
            a = (la / la.sum()) @ V; b = ((lb / lb.sum()) @ V)[pi]; p = phi24(a, b, m)
            return float(C.K_direct(list(a), list(b), m)) / p if p > 1e-9 else 9e9
        best = (9e9, None)
        for t in range(4):
            r = minimize(f, rng.random(8), method='Nelder-Mead', options=dict(maxiter=2500, xatol=1e-10, fatol=1e-13))
            if r.fun < best[0]: best = (r.fun, r.x)
        res.append((best[0], m, pi, best[1]))
res.sort(key=lambda r: r[0])
for r in res[:4]:
    y = r[3]; la, lb = np.abs(y[:4]) / np.abs(y[:4]).sum(), np.abs(y[4:]) / np.abs(y[4:]).sum()
    a = la @ V; b = (lb @ V)[r[2]]
    print('K/phi24 %.5f m=%s pi=%s  K=%.4g  K(-1/10)=%.4g  a=%s b=%s' % (r[0], r[1], r[2], float(C.K_direct(list(a), list(b), r[1])),
          float(C.K_direct(list(a), list(b), r[1], Fr(-1, 10))), np.round(a, 4), np.round(b, 4)))
