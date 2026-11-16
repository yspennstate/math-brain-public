"""The stratum target in trace form (no eigenvector basis). With Pi the projector onto Top (dimension D),
G = sum_{l below} (lambda - mu_l) v_l v_l' = lambda (I - J/n) - L (top terms vanish), tau_e = b_e' Pi b_e and
gamma_e = b_e' G b_e = 2 lambda - d_i - d_j - 2 w_ij for e = ij:
    S1 = sum g mu        = D (2 lambda - tr L^2)
    S2 = sum g |p|^2     = sum_i Pi_ii G_ii
    S3 = sum g p'Lp      = sum_e w_e (Pi_ii G_ii + Pi_jj G_jj - 2 Pi_ij G_ij)
    S4 = sum g           = D ((n-1) lambda - 2)
    S5 = sum g sum w q^2 = sum_e w_e tau_e gamma_e
and the target (n-2)(R - lambda) + (1 - lambda) >= 0 is
    T = S1 + 2n/(n-2) (lambda S2 - S3) + (1-lambda)/(n-2) (S4 - 2n/(n-2) S2) - 2 S5 >= 0.
Checks T against the pair sum of t104_R_closed.py and prints T / S4 (equal to s_inf - 1 over (n-2) times sum g|A|^2/S4).
usage: python t104_trace_form.py n points seed
"""
import sys
import numpy as np
from scipy.optimize import minimize

n, NPTS, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
here = __file__.replace("t104_trace_form.py", "t104_sinf_stratum.py")
src = open(here, encoding="utf-8").read().split("\nrng = np.random")[0]
sys.argv = ["t104_sinf_stratum.py", str(n), "0", "0"]
g = {"__file__": here, "__name__": "sinf_mod"}
exec(compile(src, here, "exec"), g)
h, relgap, sinf = g["h"], g["relgap"], g["sinf"]


def trace_T(w, tol=1e-6):
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
        tau = Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]
        S5 += wk * tau * (2 * lam - d[i] - d[j] - 2 * wk)
    S4 = D * ((n - 1) * lam - 2)
    T = S1 + 2 * n / (n - 2) * (lam * S2 - S3) + (1 - lam) / (n - 2) * (S4 - 2 * n / (n - 2) * S2) - 2 * S5
    A2 = S4 - 2 * n / (n - 2) * S2
    return lam, D, T, A2, S5


def pair_T(w, tol=1e-6):
    w = w / w.sum()
    L = h.E.T @ np.diag(w) @ h.E
    ev, U = np.linalg.eigh(L - h.ONES)
    lam = ev[-1]
    top = [k for k in range(1, n) if ev[k] > lam * (1 - tol)]
    low = [l for l in range(1, n) if ev[l] <= lam * (1 - tol)]
    T = 0.0
    for k in top:
        u = U[:, k]
        for l in low:
            v, mu = U[:, l], ev[l]
            p = u * v; pp = float(p @ p)
            q = np.array([(u[i] - u[j]) * (v[i] - v[j]) for (i, j) in h.pairs])
            aa = 1 - 2 * n / (n - 2) * pp
            P = mu + 2 * n / (n - 2) * (lam * pp - float(p @ L @ p)) + (1 - lam) / (n - 2) * aa
            T += (lam - mu) * (P - 2 * float((w * q * q).sum()))
    return T


rng = np.random.default_rng(SEED)
kept = 0; worst = 0.0; worst_s = 0.0
for t in range(NPTS * 20):
    if kept >= NPTS:
        break
    z0 = np.sqrt(h.starts(h.NK, rng)[t % h.NK] + 1e-3 * rng.random(h.m))
    r = minimize(relgap, z0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 20000})
    w = r.x ** 2; w /= w.sum()
    if relgap(r.x) > 1e-7 or np.abs(w - 1.0 / h.m).sum() < 0.05:
        continue
    kept += 1
    lam, D, T, A2, S5 = trace_T(w)
    Tp = pair_T(w)
    s, _, lam2, R = sinf(w)
    # s_inf - 1 = (n-2) (sum g <A,MA> - lambda sum g|A|^2)/sum g|A|^2 + 1 - lambda = (n-2) T / sum g|A|^2
    s_from_T = 1 + (n - 2) * T / A2
    worst = max(worst, abs(T - Tp)); worst_s = max(worst_s, abs(s_from_T - s))
    print("pt %2d  D %d  lam %.5f  T %+.6f  pair T %+.6f  s_inf from T %.6f  direct %.6f" % (kept, D, lam, T, Tp, s_from_T, s), flush=True)
print("points %d  |T - pair T| <= %.1e   |s_inf from T - direct| <= %.1e" % (kept, worst, worst_s), flush=True)
