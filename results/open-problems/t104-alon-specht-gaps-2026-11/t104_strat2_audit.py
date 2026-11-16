"""Independent numerical audit of two STRAT2 theorems (12-13 Nov).
(A) complete-graph neighbourhood: on random stratum graphs (top multiplicity D forced by averaging the top D eigenvalues
    on 1-perp, then a multiple of H for nonnegative weights, tr L = 2) check
      sum_{i<j} tau_ij gamma_ij = n S2 + D s,   max_{i!=j} G_ij <= kappa s,   S2 <= eta s,
      T >= D s/((D+1) n (n-2)^2) * (B(3n-8) - Z s)            (bound (2)),
    with T computed from the GAP_STATE_FORM definitions (X1, X2, X3, S5), and near-complete instances with s < eps_n.
(B) n = 5, D = 3: T = g/45 (7 + 16g + (70-200g) m4 + 120 g m3^2), m4 <= 13/20 on the unit zero-sum sphere.
usage: python t104_strat2_audit.py trials seed
"""
import sys
import numpy as np

TR, SEED = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(SEED)


def lap(W):
    return np.diag(W.sum(1)) - W


def stratum(n, D, scale):
    H = np.eye(n) - np.ones((n, n)) / n
    W = rng.random((n, n)) * (rng.random((n, n)) < rng.uniform(0.3, 1.0)); W = np.triu(W, 1); W = W + W.T
    W = W * scale + np.triu(np.ones((n, n)), 1) + np.triu(np.ones((n, n)), 1).T   # near complete when scale small
    L = lap(W)
    Q = np.linalg.qr(np.column_stack([np.ones(n), rng.standard_normal((n, n - 1))]))[0][:, 1:]
    ev, V = np.linalg.eigh(Q.T @ L @ Q)
    ev[-D:] = ev[-D:].mean()
    L = Q @ V @ np.diag(ev) @ V.T @ Q.T
    w = -L[np.triu_indices(n, 1)]
    if w.min() < 0:
        L = L + n * (-w.min()) * H
    L = L * 2 / np.trace(L)
    W = -L.copy(); np.fill_diagonal(W, 0); W[np.abs(W) < 1e-15] = 0
    return W


def terms(W, tol=1e-8):
    n = W.shape[0]; L = lap(W)
    Q = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, :n - 1]]))[0][:, 1:]
    ev, V = np.linalg.eigh(Q.T @ L @ Q); U = Q @ V
    lam = ev[-1]; top = np.where(ev > lam - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lam * (np.eye(n) - np.ones((n, n)) / n) - L
    d = np.diag(L); c = 2 * n / (n - 2)
    S1 = D * (2 * lam - np.trace(L @ L)); S2 = float(np.diag(Pi) @ np.diag(G)); S3 = S5 = 0.0; tg = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            tau = Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]; gam = G[i, i] + G[j, j] - 2 * G[i, j]
            tg += tau * gam
            w = W[i, j]
            if w <= 0:
                continue
            S3 += w * (Pi[i, i] * G[i, i] + Pi[j, j] * G[j, j] - 2 * Pi[i, j] * G[i, j])
            S5 += w * tau * (2 * lam - d[i] - d[j] - 2 * w)
    S4 = D * ((n - 1) * lam - 2)
    X1 = S1; X2 = c * (lam * S2 - S3); X3 = (1 - lam) / (n - 2) * (S4 - c * S2)
    s = (n - 1) * lam - 2
    Goff = G - np.diag(np.diag(G))
    np.fill_diagonal(Goff, -np.inf)
    return dict(n=n, D=D, lam=lam, s=s, T=X1 + X2 + X3 - 2 * S5, S2=S2, tg=tg, Gmax=Goff.max(), gap=ev[-1] - ev[-D - 1])


def eps(n, D=2):
    B = (D - 1) * n - 2 * D; Z = (n - 1) * (n - 2) ** 2 * (n + 2 * D) - B * (n - 4)
    return B * (3 * n - 8) / Z


worst = dict(id=0.0, G=-np.inf, S2=-np.inf, b2=np.inf, near=np.inf); kept = 0; nearkept = 0
for it in range(TR):
    n = int(rng.integers(5, 11)); D = int(rng.choice([2, 2, 3, 3, 4])); D = min(D, n - 2)
    scale = rng.choice([10 ** rng.uniform(-4, -1), rng.uniform(0.2, 3.0)])
    W = stratum(n, D, scale)
    r = terms(W)
    if r["D"] != D or r["gap"] < 1e-6:
        continue
    kept += 1; s = r["s"]; Dd = D
    B = (Dd - 1) * n - 2 * Dd; Z = (n - 1) * (n - 2) ** 2 * (n + 2 * Dd) - B * (n - 4)
    rhs = Dd * s / ((Dd + 1) * n * (n - 2) ** 2) * (B * (3 * n - 8) - Z * s)
    kap = (n - 2) / (2 * n); eta = Dd * (n - 1) / (n * (Dd + 1))
    worst["id"] = max(worst["id"], abs(r["tg"] - (n * r["S2"] + Dd * s)))
    worst["G"] = max(worst["G"], r["Gmax"] - kap * s)
    worst["S2"] = max(worst["S2"], r["S2"] - eta * s)
    worst["b2"] = min(worst["b2"], r["T"] - rhs)
    if s < eps(n, 2):
        nearkept += 1; worst["near"] = min(worst["near"], r["T"])
print("(A) kept %d of %d, near-complete (s < eps_n) %d" % (kept, TR, nearkept))
print("    max |sum tau gamma - (n S2 + D s)| %.2e" % worst["id"])
print("    max (G_ij - kappa s) %.2e   max (S2 - eta s) %.2e   (both should be <= 0)" % (worst["G"], worst["S2"]))
print("    min (T - rhs(2)) %.3e (should be >= 0)   min T among s < eps_n %.3e" % (worst["b2"], worst["near"]))
from fractions import Fraction as F
print("    eps_n exact:", [(n, F((n - 4) * (3 * n - 8), (n - 1) * (n - 2) ** 2 * (n + 4) - (n - 4) ** 2)) for n in (5, 6, 7, 8, 9, 10, 12)])

# (B) n = 5, D = 3
n = 5; maxerr = 0.0; m4max = 0.0; minreg = np.inf; k5 = 0
for it in range(TR):
    v = rng.standard_normal(n); v -= v.mean(); v /= np.linalg.norm(v)
    m4max = max(m4max, (v ** 4).sum())
    g = rng.uniform(0.01, 1.2)
    # build L = lam H - g v v^T, lam = (2+g)/4; weights must be nonnegative to be a graph
    lam = (2 + g) / 4; L = lam * (np.eye(n) - np.ones((n, n)) / n) - g * np.outer(v, v)
    W = -L.copy(); np.fill_diagonal(W, 0)
    if W[np.triu_indices(n, 1)].min() < 0:
        continue
    r = terms(W)
    if r["D"] != 3:
        continue
    k5 += 1
    m3 = (v ** 3).sum(); m4 = (v ** 4).sum()
    f = g / 45 * (7 + 16 * g + (70 - 200 * g) * m4 + 120 * g * m3 ** 2)
    maxerr = max(maxerr, abs(f - r["T"]))
    if g <= 35 / 76:
        minreg = min(minreg, r["T"])
# m4 maximum by local optimisation from many starts
for it in range(2000):
    v = rng.standard_normal(n)
    for k in range(200):
        v -= v.mean(); v /= np.linalg.norm(v)
        v = v + 0.05 * (4 * v ** 3 - (4 * v ** 3).mean())
    v -= v.mean(); v /= np.linalg.norm(v); m4max = max(m4max, (v ** 4).sum())
print("(B) n=5 D=3 graphs %d   max |T - formula(4)| %.2e   max m4 %.6f (13/20 = 0.65)   min T at g <= 35/76 %.3e"
      % (k5, maxerr, m4max, minreg))
