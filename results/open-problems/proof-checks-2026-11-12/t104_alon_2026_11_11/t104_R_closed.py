"""Closed form of the stratum target. For orthonormal u, v with Lu = lambda u, Lv = mu v (both orthogonal to 1),
p_i = u_i v_i (sum p = u.v = 0), q_e = (u_i - u_j)(v_i - v_j) for e = ij, and A the V_[n-2,2] part of
sym(u (x) v):
    |A|^2      = 1 - 2n/(n-2) |p|^2,
    <A, M A>   = lambda + mu - 2n/(n-2) p'Lp - 2 sum_e w_e q_e^2.
(Row sums of the off-diagonal part are -sqrt2 p_i; sum_j w_ij q_ij = (lambda + mu) p_i - (Lp)_i.) So per pair
    <A,MA> - lambda|A|^2 + (1-lambda)/(n-2)|A|^2 = P - 2 sum_e w_e q_e^2, with
    P = mu + 2n/(n-2)(lambda|p|^2 - p'Lp) + (1-lambda)/(n-2) |A|^2,
every term of P nonnegative on the stratum (p'Lp <= lambda |p|^2 as p is orthogonal to 1). The stratum target
(n-2)(R-lambda) + (1-lambda) >= 0 reads sum_pairs g P >= 2 sum_pairs g sum_e w_e q_e^2, g = lambda - mu.
Checks both identities against the operator and prints the ratio Q = 2 sum g sum w q^2 / sum g P (target: Q <= 1).
usage: python t104_R_closed.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_R_closed.py", "t104_sinf_stratum.py")
src = open(here, encoding="utf-8").read().split("\nrng = np.random")[0]
sys.argv = ["t104_sinf_stratum.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "sinf_mod"}
exec(compile(src, here, "exec"), g)
h, relgap = g["h"], g["relgap"]


def check(w, tol=1e-6):
    w = w / w.sum()
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    Mb = np.tensordot(w, h.SW, axes=1)
    err = 0.0; SP = SQ = 0.0
    for k in top:
        u = U[:, k]
        for l in low:
            v, mu = U[:, l], ev[l]
            X = (np.outer(u, v) + np.outer(v, u)) / h.R2
            a = h.B.T @ X.ravel()
            p = u * v; pp = float(p @ p)
            q = np.array([(u[i] - u[j]) * (v[i] - v[j]) for (i, j) in h.pairs])
            aa = 1 - 2 * n / (n - 2) * pp
            qq = float((w * q * q).sum())
            ama = (lam + mu) - 2 * n / (n - 2) * float(p @ L @ p) - 2 * qq
            err = max(err, abs(aa - float(a @ a)), abs(ama - float(a @ Mb @ a)))
            P = mu + 2 * n / (n - 2) * (lam * pp - float(p @ L @ p)) + (1 - lam) / (n - 2) * aa
            gg = lam - mu
            SP += gg * P; SQ += gg * 2 * qq
    return lam, err, SQ / SP


idx = {p: k for k, p in enumerate(h.pairs)}
for name, es in [("2K2", [(0, 3), (1, 2)]), ("triangle", [(0, 1), (0, 2), (1, 2)]),
                 ("C5", [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)])][: 3 if n >= 5 else 2]:
    w = np.zeros(h.m)
    for e in es:
        w[idx[e]] = 1.0
    lam, err, Q = check(w)
    print("%-9s lam %.6f  err %.1e  Q %.6f" % (name, lam, err, Q), flush=True)
rng = np.random.default_rng(SEED)
kept = 0; worst = 0.0; Qmax = 0.0
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    lam, err, Q = check(w)
    worst = max(worst, err); Qmax = max(Qmax, Q)
    print("pt %2d  lam %.5f  err %.1e  Q %.6f" % (kept, lam, err, Q), flush=True)
print("points %d  largest identity error %.1e  largest Q %.6f (target Q <= 1)" % (kept, worst, Qmax), flush=True)
