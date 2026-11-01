"""K x K Schur-complement family for the SEL-13 ratio: float64 Nelder-Mead search (as in stress_sel13.py),
then the best candidates re-evaluated at 60 digits with mpmath.  Question: does any float64 value above
kappa_0 = 0.756151564 survive high precision?"""
import numpy as np
import mpmath as mp
from scipy.optimize import minimize

KAPPA0 = 0.756151563992684
rng = np.random.default_rng(11)


def famK(params, K, t):
    a = params[:K - 1]; b = params[K - 1:2 * (K - 1)]
    X = np.asarray(params[2 * (K - 1):]).reshape(K - 1, K - 1)
    M = np.zeros((K, K))
    M[0, 0] = 1.0
    M[0, 1:] = t * b
    M[1:, 0] = t * a
    M[1:, 1:] = t * t * (np.outer(a, b) - X)
    return M


def ratio_f(M):
    M = M / np.linalg.norm(M)
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    if S[-1] < 1e-6 * S[0] or np.min(np.abs(np.diff(S))) < 1e-9 * S[0]:
        return None
    s = S ** 2
    H = lambda p: float(-(p[p > 0] * np.log2(p[p > 0])).sum())
    rhs = H(s) + sum(s[k] * (H(U[:, k] ** 2) + H(Vt[k, :] ** 2)) for k in range(len(s)))
    return (H((M ** 2).ravel()) - rhs) / float((s * (1 - s)).sum())


def ratio_mp(Mf, dps=60):
    mp.mp.dps = dps
    K = Mf.shape[0]
    M = mp.matrix([[mp.mpf(repr(float(Mf[i, j]))) for j in range(K)] for i in range(K)])
    nrm = mp.sqrt(sum(M[i, j] ** 2 for i in range(K) for j in range(K)))
    M = M / nrm
    U, S, V = mp.svd_r(M)
    s = [S[k] ** 2 for k in range(K)]
    H = lambda ps: -sum(p * mp.log(p, 2) for p in ps if p > 0)
    rhs = H(s) + sum(s[k] * (H([U[i, k] ** 2 for i in range(K)]) + H([V[k, j] ** 2 for j in range(K)])) for k in range(K))
    lhs = H([M[i, j] ** 2 for i in range(K) for j in range(K)])
    return (lhs - rhs) / sum(p * (1 - p) for p in s)


for K in (2, 3):
    cands = []
    npar = 2 * (K - 1) + (K - 1) ** 2
    for start in range(25):
        x0 = rng.normal(size=npar) * rng.uniform(0.5, 3)
        f = lambda v: -(ratio_f(famK(v, K, 1e-2)) or 0.0)
        res = minimize(f, x0, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-7, "fatol": 1e-10})
        cands.append((-res.fun, res.x))
    cands.sort(key=lambda c: -c[0])
    for val, x in cands[:4]:
        Mf = famK(x, K, 1e-2)
        hp = ratio_mp(Mf)
        print("K=%d  float64 %.7f  ->  60-digit %s   (above kappa_0 at 60 digits: %s)" % (
            K, val, mp.nstr(hp, 12), hp > KAPPA0))
