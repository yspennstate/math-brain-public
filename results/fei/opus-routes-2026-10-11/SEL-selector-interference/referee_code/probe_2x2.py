"""Probe the 2x2 landscape of the SEL-13 ratio gap/B with float64 search and 50-digit mpmath confirmation.
M = [[1, x], [y, z]] covers every 2x2 matrix up to scaling, row/column sign flips, permutations and transpose
(all of which leave gap and B unchanged), with |entries| <= 1 after choosing the largest |entry| as M_11."""
import numpy as np, mpmath as mp
from scipy.optimize import minimize
mp.mp.dps = 50

def ratio_f(x, y, z):
    M = np.array([[1.0, x], [y, z]]); M = M / np.linalg.norm(M)
    U, S, Vt = np.linalg.svd(M)
    if S[1] < 1e-7 * S[0] or abs(S[0]-S[1]) < 1e-9: return None
    s = S**2
    H = lambda p: float(-(p[p>0]*np.log2(p[p>0])).sum())
    rhs = H(s) + sum(s[k]*(H(U[:,k]**2)+H(Vt[k,:]**2)) for k in range(2))
    return (H((M**2).ravel()) - rhs) / float((s*(1-s)).sum())

def ratio_mp(x, y, z):
    x, y, z = mp.mpf(x), mp.mpf(y), mp.mpf(z)
    M = mp.matrix([[1, x], [y, z]]); nrm = mp.sqrt(1 + x*x + y*y + z*z); M = M / nrm
    U, S, V = mp.svd_r(M)
    s = [S[0]**2, S[1]**2]
    H = lambda ps: -sum(p*mp.log(p, 2) for p in ps if p > 0)
    rhs = H(s) + sum(s[k]*(H([U[0,k]**2, U[1,k]**2]) + H([V[k,0]**2, V[k,1]**2])) for k in range(2))
    lhs = H([M[i,j]**2 for i in range(2) for j in range(2)])
    B = sum(p*(1-p) for p in s)
    return (lhs - rhs)/B

rng = np.random.default_rng(0)
best = (-1, None)
for st in range(400):
    x0 = rng.uniform(-1, 1, size=3) * (10.0 ** rng.uniform(-3, 0, size=3))
    f = lambda v: -(ratio_f(*v) or 0.0) if np.all(np.abs(v) <= 1) else 1.0
    res = minimize(f, x0, method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-12, "fatol": 1e-14})
    if -res.fun > best[0]:
        best = (-res.fun, res.x)
print("float64 best ratio %.9f at (x,y,z) = %s" % (best[0], best[1]))
print("mpmath 50-digit ratio at that point:", mp.nstr(ratio_mp(*best[1]), 15))
# the author's family as t -> 0 in mpmath
for t in ("1e-2", "1e-3", "1e-4", "1e-6"):
    tt = mp.mpf(t); eta = mp.mpf("4.59112158874")
    # [[t,1],[t^2(1-eta),t]] -> permute to put 1 at M_11: [[1,t],[t,t^2(1-eta)]]
    print("author family t=%s ratio = %s" % (t, mp.nstr(ratio_mp(tt, tt, tt*tt*(1-eta)), 15)))
