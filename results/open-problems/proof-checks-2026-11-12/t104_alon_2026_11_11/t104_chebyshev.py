"""Chebyshev route for the stratum target sum_l g_l (P_l - Q_l) >= 0 (g_l = lambda - mu_l, P_l, Q_l traces over Top as in
t104_per_l_seed11.py). If F_l = P_l - Q_l is ordered like g_l (non-increasing in mu_l), Chebyshev's sum inequality gives
sum g_l F_l >= (1/m)(sum g_l)(sum F_l), so it would suffice that the plain sum sum_l F_l (a trace over Top-perp in 1-perp,
basis-free) is >= 0 and the ordering holds. Checks both at random stratum points.
usage: python t104_chebyshev.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_chebyshev.py", "t104_trace_terms.py")
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


def F(w, tol=1e-6):
    w = w / w.sum()
    L = Bs.T @ np.diag(w) @ Bs
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    out = []
    for l in low:
        v, mu = U[:, l], ev[l]; P = Q = 0.0
        for k in top:
            u = U[:, k]; p = u * v
            P += mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2)
            Q += 2 * np.sum(w * (Bs @ u) ** 2 * (Bs @ v) ** 2)
        out.append((mu, lam - mu, P - Q, Q / P))
    return lam, out


rng = np.random.default_rng(SEED); kept = 0; minplain = np.inf; viol = 0; worst_rel = np.inf
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    lam, out = F(w)
    mus = np.array([o[0] for o in out]); gs = np.array([o[1] for o in out]); Fs = np.array([o[2] for o in out])
    order = np.argsort(mus)
    ordered = bool(np.all(np.diff(Fs[order]) <= 1e-12))
    viol += not ordered
    plain = Fs.sum(); weighted = gs @ Fs; cheb = gs.sum() * plain / len(Fs)
    minplain = min(minplain, plain / np.abs(Fs).sum())
    worst_rel = min(worst_rel, weighted / cheb if cheb > 0 else -np.inf)
    print("pt %2d lam %.4f  mu %s  F %s  ordered %s  plain %+.5f  weighted %+.5f  cheb bound %+.5f"
          % (kept, lam, np.round(mus, 4), np.round(Fs, 5), ordered, plain, weighted, cheb), flush=True)
print("n %d points %d  ordering fails at %d  smallest plain/sum|F| %.4f  smallest weighted/cheb %.4f"
      % (n, kept, viol, minplain, worst_rel), flush=True)
