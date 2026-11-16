"""Which terms of the stratum trace target carry the bound? T = X1 + X2 + X3 - Y with
X1 = S1 = D(2 lambda - tr L^2), X2 = 2n/(n-2)(lambda S2 - S3), X3 = (1-lambda)/(n-2) sum g|A|^2, Y = 2 S5
(t104_trace_form.py). Prints, over stratum points, the largest Y/X for X = X1, X1+X2, X1+X3, X2+X3, X1+X2+X3
(a sub-sum with ratio below 1 everywhere is a candidate for the proof). Also tests Y <= 2 X1 ... nothing else.
usage: python t104_trace_terms.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_trace_terms.py", "t104_sinf_stratum.py")
src = open(here, encoding="utf-8").read().split("\nrng = np.random")[0]
sys.argv = ["t104_sinf_stratum.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "sinf_mod"}
exec(compile(src, here, "exec"), g)
h, relgap = g["h"], g["relgap"]


def terms(w, tol=1e-6):
    w = w / w.sum()
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lam * (np.eye(n) - np.ones((n, n)) / n) - L
    d = np.diag(L)
    S1 = D * (2 * lam - np.trace(L @ L))
    S2 = float(np.diag(Pi) @ np.diag(G))
    S3 = S5 = 0.0
    for wk, (i, j) in zip(w, h.pairs):
        S3 += wk * (Pi[i, i] * G[i, i] + Pi[j, j] * G[j, j] - 2 * Pi[i, j] * G[i, j])
        S5 += wk * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (2 * lam - d[i] - d[j] - 2 * wk)
    S4 = D * ((n - 1) * lam - 2)
    X1 = S1; X2 = 2 * n / (n - 2) * (lam * S2 - S3); X3 = (1 - lam) / (n - 2) * (S4 - 2 * n / (n - 2) * S2)
    return lam, D, X1, X2, X3, 2 * S5


names = ["X1", "X1+X2", "X1+X3", "X2+X3", "X1+X2+X3"]
worst = {k: 0.0 for k in names}; mins = [np.inf, np.inf, np.inf]
rng = np.random.default_rng(SEED); kept = 0
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    lam, D, X1, X2, X3, Y = terms(w)
    vals = {"X1": X1, "X1+X2": X1 + X2, "X1+X3": X1 + X3, "X2+X3": X2 + X3, "X1+X2+X3": X1 + X2 + X3}
    for k in names:
        worst[k] = max(worst[k], Y / vals[k] if vals[k] > 0 else np.inf)
    mins = [min(mins[0], X1), min(mins[1], X2), min(mins[2], X3)]
    print("pt %2d D %d lam %.4f  X1 %.4f X2 %.4f X3 %.4f  Y %.4f" % (kept, D, lam, X1, X2, X3, Y), flush=True)
print("n %d points %d  smallest X1 %.4f X2 %.4f X3 %.4f" % (n, kept, *mins), flush=True)
print("largest Y / sub-sum: " + "  ".join("%s %.4f" % (k, worst[k]) for k in names), flush=True)
