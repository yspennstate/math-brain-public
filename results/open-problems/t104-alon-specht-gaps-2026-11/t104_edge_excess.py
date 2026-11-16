"""X1 = D sum_e w_e gamma_e (gamma_e = 2 lambda - d_i - d_j - 2 w_e = b_e' G b_e, using tr L = 2, sum w = 1), so the
stratum target T = X1 + X2 + X3 - Y reads
    sum_e w_e gamma_e (2 tau_e - D) <= X2 + X3,        tau_e = |Pi b_e|^2 in [0, 2].
Checks X1 = D sum w gamma, and prints, per stratum point, the excess E = sum w gamma (2 tau - D), the share of it
from edges with 2 tau_e > D, and X2 + X3.
usage: python t104_edge_excess.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_edge_excess.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h, relgap, terms = g["h"], g["relgap"], g["terms"]

rng = np.random.default_rng(SEED); kept = 0; err = 0.0; worst = 0.0
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
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    top = [k for k in range(1, n) if ev[k] > lam * (1 - 1e-6)]
    Pi = U[:, top] @ U[:, top].T
    d = np.diag(L)
    gam = np.array([2 * lam - d[i] - d[j] - 2 * w[k] for k, (i, j) in enumerate(h.pairs)])
    tau = np.array([Pi[i, i] + Pi[j, j] - 2 * Pi[i, j] for (i, j) in h.pairs])
    err = max(err, abs(X1 - D * float(w @ gam)), abs(Y - 2 * float((w * tau * gam).sum())))
    E = float((w * gam * (2 * tau - D)).sum())
    pos = float((w * gam * np.clip(2 * tau - D, 0, None)).sum())
    worst = max(worst, E / (X2 + X3))
    print("pt %2d D %d lam %.4f  E %+.4f (from 2tau > D: %.4f, edges %d)  X2+X3 %.4f  min gamma %.2e"
          % (kept, D, lam, E, pos, int((2 * tau > D).sum()), X2 + X3, gam.min()), flush=True)
print("n %d points %d  identity error %.1e  largest E/(X2+X3) %.4f (target <= 1)" % (n, kept, err, worst), flush=True)
