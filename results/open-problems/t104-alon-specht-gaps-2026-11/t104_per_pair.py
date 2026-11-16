"""Does the stratum target hold pair by pair? For u a unit vector in Top (D = 2: u = cos t u1 + sin t u2, 360 angles) and
v = v_l an eigenvector with mu_l < lambda (on 1-perp), with p = u * v, q_e = (b_e . u)(b_e . v), c = 2n/(n-2):
    P(u, v) = mu + c (lambda |p|^2 - p'Lp) + (1 - lambda) |A|^2 / (n - 2),   |A|^2 = 1 - c |p|^2,
    target summed: sum_l (lambda - mu_l) [P - 2 sum_e w_e q_e^2] >= 0 (push 117). Per pair: 2 sum w q^2 <= P ?
Prints the largest per-pair ratio 2 sum w q^2 / P over angles and l, per point, plus the summed ratio as a check.
usage: python t104_per_pair.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_per_pair.py", "t104_trace_terms.py")
src = open(here, encoding="utf-8").read().split("\nnames = ")[0]
sys.argv = ["t104_trace_terms.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "tt_mod"}
exec(compile(src, here, "exec"), g)
h, terms, relgap = g["h"], g["terms"], g["relgap"]
c = 2.0 * n / (n - 2)
Bs = []
for (i, j) in h.pairs:
    b = np.zeros(n); b[i], b[j] = 1, -1; Bs.append(b)
Bs = np.array(Bs)


def per_pair(w, tol=1e-6):
    w = w / w.sum()
    L = Bs.T @ np.diag(w) @ Bs
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    worst = -np.inf; where = None; num = den = 0.0
    angles = np.linspace(0, np.pi, 360, endpoint=False) if len(top) == 2 else [0.0]
    for t in angles:
        u = U[:, top[0]] * np.cos(t) + (U[:, top[1]] * np.sin(t) if len(top) == 2 else 0)
        for l in low:
            v, mu = U[:, l], ev[l]
            p = u * v
            P = mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2)
            Q = 2 * np.sum(w * (Bs @ u) ** 2 * (Bs @ v) ** 2)
            r = Q / P if P > 0 else np.inf
            if r > worst:
                worst, where = r, (t, l, mu, P, Q)
            if t == 0.0 or len(top) == 2 and abs(t - np.pi / 2) < 1e-12:
                num += (lam - mu) * Q; den += (lam - mu) * P
    return lam, len(top), worst, where, num / den


idx = {p: k for k, p in enumerate(h.pairs)}
if n == 5:
    w = np.zeros(h.m)
    for e in [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]:
        w[idx[e]] = 0.2
    lam, D, worst, where, summed = per_pair(w)
    print("C5   lam %.5f D %d  per-pair max %.4f (angle %.3f, mu %.4f)  summed %.4f" % (lam, D, worst, where[0], where[2], summed), flush=True)
rng = np.random.default_rng(SEED); kept = 0; gmax = 0.0
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    lam, D, worst, where, summed = per_pair(w)
    gmax = max(gmax, worst)
    print("pt %2d lam %.5f D %d  per-pair max %.4f (angle %.3f, mu %.4f, P %.4f)  summed %.4f"
          % (kept, lam, D, worst, where[0], where[2], where[3], summed), flush=True)
print("n %d points %d  largest per-pair ratio %.4f" % (n, kept, gmax), flush=True)
