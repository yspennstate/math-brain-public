"""An explicit form of R - lambda on the double-top stratum.

For u in Top (eigenvalue lambda), v = e_l (eigenvalue mu < lambda), X = (u v' + v u')/sqrt 2 and A its component in
V_[n-2,2] (symmetric, zero diagonal, zero row sums). On symmetric matrices M Y = sum_e w_e (Y - P_e Y P_e), and
Y - P Y P = (L (x) I + I (x) L - E (x) E) restricted, E_e = b_e b_e', so
    M X = (lambda + mu) X - sqrt2 sum_e w_e (b_e.u)(b_e.v) E_e.
V_[n-2,2] occurs once in Sym^2, so M maps A into V_[n-2,2] and the other components away from it, hence
    <A, M A> = <A, M X> = (lambda + mu) |A|^2 + 2 sqrt2 sum_{e = ij} w_e (u_i - u_j)(v_i - v_j) A_ij
(<A, E_e> = -2 A_ij since A has zero diagonal). Summing with weights g = lambda - mu over Top (x) e_l:
    (R - lambda) sum g |A|^2 = sum g [ mu |A|^2 + 2 sqrt2 sum_e w_e (b_e.u)(b_e.v) A_ij ] =: sum g T_l.
This script checks the identity against the code's M and prints, per pair, mu |A|^2 and the edge term, at random
points of the stratum (same generator as t104_sinf_stratum.py) and at 2K_2, the triangle and C_5.
usage: python t104_R_identity.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_R_identity.py", "t104_sinf_stratum.py")
src = open(here, encoding="utf-8").read().split("\nrng = np.random")[0]
sys.argv = ["t104_sinf_stratum.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "sinf_mod"}
exec(compile(src, here, "exec"), g)
h, sinf, relgap = g["h"], g["sinf"], g["relgap"]


def pieces(w, tol=1e-6):
    w = w / w.sum()
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    Mb = np.tensordot(w, h.SW, axes=1)
    err = 0.0; num = den = 0.0; out = []
    for k in top:
        u = U[:, k]
        for l in low:
            v, mu = U[:, l], ev[l]
            X = (np.outer(u, v) + np.outer(v, u)) / h.R2
            a = h.B.T @ X.ravel(); A = (h.B @ a).reshape(n, n)
            q = float(a @ Mb @ a); aa = float(a @ a)
            edge = 0.0
            for wk, (i, j) in zip(w, h.pairs):
                edge += wk * (u[i] - u[j]) * (v[i] - v[j]) * A[i, j]
            edge *= 2 * h.R2
            err = max(err, abs(q - ((lam + mu) * aa + edge)))
            gg = lam - mu
            num += gg * (mu * aa + edge); den += gg * aa
            out.append((k, l, mu, mu * aa, edge, gg))
    return lam, err, num / den, out


idx = {p: k for k, p in enumerate(h.pairs)}
named = [("2K2", [(0, 3), (1, 2)]), ("triangle", [(0, 1), (0, 2), (1, 2)])]
if n >= 5:
    named.append(("C5", [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]))
for name, es in named:
    w = np.zeros(h.m)
    for p in es:
        w[idx[p]] = 1.0
    lam, err, rl, out = pieces(w)
    s, _, lam2, R = sinf(w)
    print("%-9s lam %.6f  identity err %.1e  R-lam %+.6f (direct %+.6f)" % (name, lam, err, rl, R - lam2), flush=True)
    for k, l, mu, t1, t2, gg in out:
        print("    pair %d,%d  mu %.4f  gap %.4f  mu|A|^2 %+.5f  edge %+.5f" % (k, l, mu, gg, t1, t2), flush=True)

rng = np.random.default_rng(SEED)
kept = 0; worst = 0.0; pos_edge = 0; tot = 0
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    lam, err, rl, out = pieces(w)
    s, _, lam2, R = sinf(w)
    worst = max(worst, err, abs(rl - (R - lam2)))
    for k, l, mu, t1, t2, gg in out:
        tot += 1; pos_edge += t2 > 0
    print("pt %2d  lam %.5f  R-lam %+.6f  sum g mu|A|^2 %+.5f  sum g edge %+.5f"
          % (kept, lam, rl, sum(o[5] * o[3] for o in out), sum(o[5] * o[4] for o in out)), flush=True)
print("points %d  largest identity / R-lam discrepancy %.1e  pairs with positive edge term %d of %d"
      % (kept, worst, pos_edge, tot), flush=True)
