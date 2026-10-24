"""Maximise the SEL-13 ratio over 2x2 matrices with the objective evaluated in 30-digit mpmath
(float64 SVD/entropy is unreliable at the extreme scales where the supremum sits)."""
import numpy as np, mpmath as mp, time
from scipy.optimize import minimize
mp.mp.dps = 30

def ratio_mp(x, y, z):
    x, y, z = mp.mpf(x), mp.mpf(y), mp.mpf(z)
    nrm2 = 1 + x*x + y*y + z*z
    M = mp.matrix([[1, x], [y, z]]) / mp.sqrt(nrm2)
    U, S, V = mp.svd_r(M)
    s = [S[0]**2, S[1]**2]
    if s[1] < mp.mpf(10)**-26 or abs(s[0]-s[1]) < mp.mpf(10)**-20: return None
    H = lambda ps: -sum(p*mp.log(p, 2) for p in ps if p > 0)
    rhs = H(s) + sum(s[k]*(H([U[0,k]**2, U[1,k]**2]) + H([V[k,0]**2, V[k,1]**2])) for k in range(2))
    lhs = H([M[i,j]**2 for i in range(2) for j in range(2)])
    return (lhs - rhs) / sum(p*(1-p) for p in s)

def obj(v):
    # parametrise magnitudes on a log scale: x = sx*10^lx etc.
    x = v[0]; y = v[1]; z = v[2]
    if max(abs(x), abs(y), abs(z)) > 1: return 1.0
    r = ratio_mp(x, y, z)
    return 1.0 if r is None else -float(r)

rng = np.random.default_rng(42)
t0 = time.time(); best = (-1, None)
for st in range(60):
    x0 = rng.uniform(-1, 1, size=3) * (10.0 ** rng.uniform(-3, 0, size=3))
    res = minimize(obj, x0, method="Nelder-Mead", options={"maxiter": 1500, "xatol": 1e-13, "fatol": 1e-13})
    if -res.fun > best[0]: best = (-res.fun, res.x)
    if time.time() - t0 > 400: break
print("starts done:", st + 1, " best mp ratio %.12f at %s" % (best[0], best[1]))
x, y, z = best[1]
mp.mp.dps = 60
print("60-digit check:", mp.nstr(ratio_mp(x, y, z), 15))
