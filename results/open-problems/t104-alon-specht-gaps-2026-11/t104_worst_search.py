"""Worst case of the stratum target ratio J = sum_l g_l F_l / sum_l g_l |F_l| (F_l = P_l - Q_l, traces over Top; target
<=> J >= 0). Top is forced to the top two eigenvectors and the relative top gap is penalised (K * relgap), so the search
walks on and near the double-top stratum. Starts: the seed-11 point and stratum points from the usual generator.
Each finish is polished back onto the stratum (relgap < 1e-7) by a short constrained step and J is reported there.
usage: python t104_worst_search.py n starts seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NST, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_worst_search.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h, relgap = g["h"], g["relgap"]
c = 2.0 * n / (n - 2)
Bs = []
for (i, j) in h.pairs:
    b = np.zeros(n); b[i], b[j] = 1, -1; Bs.append(b)
Bs = np.array(Bs)


def J(z):
    w = z ** 2; s = w.sum()
    if s <= 0:
        return 10.0
    w = w / s
    L = Bs.T @ np.diag(w) @ Bs
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]; top = [n - 2, n - 1]; low = list(range(1, n - 2))
    num = den = 0.0
    for l in low:
        v, mu = U[:, l], ev[l]; P = Q = 0.0
        for k in top:
            u = U[:, k]; p = u * v
            P += mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2)
            Q += 2 * np.sum(w * (Bs @ u) ** 2 * (Bs @ v) ** 2)
        gl = lam - mu; num += gl * (P - Q); den += gl * abs(P - Q)
    return num / den if den > 0 else 10.0


rng = np.random.default_rng(SEED)
starts = []
if n == 5:
    W11 = [0.12518221, 0.34344950, 0.02497551, 0.00149480, 0.13304193, 0.32605611, 0.00032333, 0.04149927, 0.00055063, 0.00342672]
    idx = {p: k for k, p in enumerate(h.pairs)}
    order = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    w0 = np.zeros(h.m)
    for wv, p in zip(W11, order):
        w0[idx[p]] = wv
    starts.append(np.sqrt(w0))
t = 0
while len(starts) < NST and t < NST * 40:
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m)); t += 1
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    starts.append(r.x)
best = np.inf
for si, z0 in enumerate(starts):
    K = 50.0
    r = minimize(lambda z: J(z) + K * relgap(z), z0, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
    # polish onto the stratum: minimise relgap starting from the finish, then evaluate
    r2 = minimize(relgap, r.x, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    on = relgap(r2.x) < 1e-7
    j0, j1 = J(z0), J(r2.x)
    if on:
        best = min(best, j1)
    w = r2.x ** 2; w /= w.sum()
    print("start %2d  J start %.4f  J after %.4f  relgap %.1e  on stratum %s  weights %s"
          % (si, j0, j1, relgap(r2.x), on, " ".join("%.4f" % x for x in w)), flush=True)
print("n %d starts %d  smallest J on the stratum %.4f" % (n, len(starts), best), flush=True)
