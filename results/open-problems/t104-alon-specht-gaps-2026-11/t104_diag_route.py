"""Route for D = 2, 3 with nonconstant diag Pi: replace tau_ij by the bounds
B1 = (sqrt Pi_ii + sqrt Pi_jj)^2 and B2 = 2(Pi_ii + Pi_jj) in 2 S5 and print the ratios
Y_B / (X1 + X2 + X3) on stratum points, next to the exact Y / (X1 + X2 + X3).
usage: python t104_diag_route.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

DIR = r"~/brain-repo/06_math_research/t104_alon_agent_2026_11_11/"
n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = DIR + "t104_sinf_stratum.py"
src = open(here, encoding="utf-8").read().split("\nrng = np.random")[0]
sys.argv = ["t104_sinf_stratum.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "sinf_mod"}
exec(compile(src, here, "exec"), g)
h, relgap = g["h"], g["relgap"]


def parts(w, tol=1e-6):
    w = w / w.sum()
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lam * (np.eye(n) - np.ones((n, n)) / n) - L
    d = np.diag(L)
    S1 = D * (2 * lam - np.trace(L @ L)); S2 = float(np.diag(Pi) @ np.diag(G))
    S3 = S5 = Y1 = Y2 = 0.0
    for wk, (i, j) in zip(w, h.pairs):
        ga = 2 * lam - d[i] - d[j] - 2 * wk
        S3 += wk * (Pi[i, i] * G[i, i] + Pi[j, j] * G[j, j] - 2 * Pi[i, j] * G[i, j])
        S5 += wk * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * ga
        Y1 += wk * (np.sqrt(Pi[i, i]) + np.sqrt(Pi[j, j])) ** 2 * ga
        Y2 += wk * 2 * (Pi[i, i] + Pi[j, j]) * ga
    S4 = D * ((n - 1) * lam - 2); c = 2 * n / (n - 2)
    X = S1 + c * (lam * S2 - S3) + (1 - lam) / (n - 2) * (S4 - c * S2)
    return D, lam, X, 2 * S5, 2 * Y1, 2 * Y2, np.diag(Pi).max() * n / D


rng = np.random.default_rng(SEED); kept = 0; worst = [0, 0, 0]
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    D, lam, X, Y, Y1, Y2, dmax = parts(w)
    rs = [Y / X, Y1 / X, Y2 / X]
    worst = [max(a, b) for a, b in zip(worst, rs)]
    print("pt %2d D %d lam %.4f max(n Pi_ii / D) %.3f   exact %.4f  sqrt-bound %.4f  sum-bound %.4f" % (kept, D, lam, dmax, *rs), flush=True)
print("n %d points %d  largest ratio: exact %.4f  sqrt-bound %.4f  sum-bound %.4f (bound route closes iff < 1)" % (n, kept, *worst))
