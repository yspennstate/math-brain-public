"""The beta -> infinity value on the double-top stratum. When lambda_1 = lambda_2 = lambda, letting beta -> infinity in
s_beta keeps only the pairs (k, l) with lambda_k = lambda (k in Top) and lambda_l < lambda, each weighted by its gap:

    s_inf = (n-2) sum_{k in Top, l} (lam - lam_l) a_kl' M a_kl / sum_{k in Top, l} (lam - lam_l) |a_kl|^2 - need,

with a_kl the V_[n-2,2] coordinates of sym(u_k (x) u_l). This is basis-free in Top (it is a trace over Top (x) e_l),
so it is well defined on the stratum, and H >= s_inf there. Question: is s_inf >= 1 on the whole stratum?

Points on the stratum: random starts, then Nelder-Mead on z (w = z^2) minimising gap12/lambda; kept if the relative
gap is below 1e-7 and the point is away from uniform K_n. For each kept point prints s_inf, H on the search grid
extended to 1e10, lambda, R - lambda (R the gap-weighted
average of M, so s_inf - 1 = (n-2)(R - lambda) + (1 - lambda), and lambda <= 1 on the stratum since 2 lambda <= tr L = 2),
and the support.
usage: python t104_sinf_stratum.py n points seed
"""
import importlib.util
import sys
import numpy as np
from scipy.optimize import minimize

here = __file__.replace("t104_sinf_stratum.py", "t104_np_hsearch.py")
n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
spec = importlib.util.spec_from_file_location("hs", here)
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
GRID = h.GRID + [1e7, 1e8, 1e9, 1e10]


def sinf(w, tol=1e-6):
    w = w / w.sum()
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    M = np.tensordot(w, h.SW, axes=1)
    num = den = 0.0
    for k in top:
        for l in low:
            a = h.B.T @ ((np.outer(U[:, k], U[:, l]) + np.outer(U[:, l], U[:, k])) / h.R2).ravel()
            num += (lam - ev[l]) * float(a @ M @ a); den += (lam - ev[l]) * float(a @ a)
    need = (n - 1) * lam - 2.0
    R = num / den if den > 1e-15 else float("nan")
    return ((n - 2) * R - need) if den > 1e-15 else -need, len(top), lam, R


def relgap(z):
    w = z * z + 1e-300
    w = w / w.sum()
    ev = np.linalg.eigvalsh(h.E.T @ np.diag(w) @ h.E)
    return (ev[-1] - ev[-2]) / ev[-1]


rng = np.random.default_rng(SEED)
best = (np.inf, None)
kept = 0
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    s, mult, lam, R = sinf(w)
    H = h.values(w[None, :] + 1e-300, GRID)[0][0]
    if s < best[0]:
        best = (s, w)
    print("pt %3d  mult %d  s_inf %+.6f  H %+.6f  H-s_inf %+.2e  lam %.6f  R-lam %+.6f  %s"
          % (kept, mult, s, H, H - s, lam, R - lam, h.fmt(w, 1e-4)),
          flush=True)
print("kept %d  smallest s_inf %+.6f at %s" % (kept, best[0], h.fmt(best[1], 1e-5) if best[1] is not None else "-"),
      flush=True)
