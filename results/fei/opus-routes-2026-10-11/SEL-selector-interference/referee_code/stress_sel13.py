"""Stress test of CONJECTURE SEL-13 (not a verdict item):
  H(|M|^2) <= H(s) + sum_k s_k [H(u_k^2) + H(v_k^2)] + kappa sum_k s_k (1 - s_k),  ||M||_F = 1,
claimed numerically sharp at kappa_0 = 0.756151564 (near-rank-one 2x2 limit [[t,1],[t^2(1-eta),t]]).
We look for larger ratios gap/B in (i) the author's family, (ii) its K x K generalisation
M = [[1, t b^T], [t a, t^2 (a b^T - X)]] (Schur complement -t^2 X), optimised over (a, b, X),
(iii) random and multi-scale random matrices.
"""
import math
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(11)


def H(p):
    p = np.asarray(p, dtype=np.float64)
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def ratio(M):
    M = np.asarray(M, dtype=np.float64)
    M = M / np.linalg.norm(M)
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    s = S ** 2
    if np.min(np.abs(np.diff(S))) < 1e-9 * S[0]:
        return None                     # degenerate: SVD not unique, skip
    rhs = H(s) + sum(s[k] * (H(U[:, k] ** 2) + H(Vt[k, :] ** 2)) for k in range(len(s)))
    gap = H((M ** 2).ravel()) - rhs
    B = float((s * (1 - s)).sum())
    if S[-1] < 1e-6 * S[0]:
        return None                     # second singular value not resolved in float64: skip
    return gap / B if B > 0 else None


def fam2(eta, t):
    return np.array([[t, 1.0], [t * t * (1 - eta), t]])


print("(i) author's family, t = 1e-2, 3e-3:")
for eta in (2.0, 4.0, 4.5911, 5.0, 8.0):
    print("   eta=%.4f  ratio(t=1e-2)=%.6f  ratio(t=3e-3)=%.6f" % (eta, ratio(fam2(eta, 1e-2)), ratio(fam2(eta, 3e-3))))


def famK(params, K, t):
    a = params[:K - 1]; b = params[K - 1:2 * (K - 1)]
    X = params[2 * (K - 1):].reshape(K - 1, K - 1)
    M = np.zeros((K, K))
    M[0, 0] = 1.0
    M[0, 1:] = t * b
    M[1:, 0] = t * a
    M[1:, 1:] = t * t * (np.outer(a, b) - X)
    return M


def neg_ratio(params, K, t):
    r = ratio(famK(params, K, t))
    return 0.0 if r is None else -r


print("(ii) K x K Schur-complement family, maximise over (a, b, X):")
for K in (2, 3, 4):
    best = -1e9
    bestp = None
    for start in range(25 if K < 4 else 12):
        npar = 2 * (K - 1) + (K - 1) ** 2
        x0 = rng.normal(size=npar) * rng.uniform(0.5, 3)
        res = minimize(neg_ratio, x0, args=(K, 1e-2), method="Nelder-Mead",
                       options={"maxiter": 6000, "xatol": 1e-7, "fatol": 1e-10})
        if -res.fun > best:
            best, bestp = -res.fun, res.x
    r_small = ratio(famK(bestp, K, 3e-3))
    print("   K=%d  best ratio at t=1e-2: %.6f   same params at t=3e-3: %s" % (K, best, "%.6f" % r_small if r_small else "degenerate"))

print("(iii) random multi-scale matrices:")
best = -1e9
for trial in range(40000):
    m = int(rng.integers(2, 6)); n = int(rng.integers(2, 6))
    M = rng.normal(size=(m, n)) * (10.0 ** rng.uniform(-4, 0, size=(m, n)))
    r = ratio(M)
    if r is not None and r > best:
        best = r
print("   max ratio over 40,000 random multi-scale matrices: %.6f" % best)
