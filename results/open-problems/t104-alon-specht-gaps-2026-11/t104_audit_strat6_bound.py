"""Tests the derivation behind STRAT6's strong cells: for a frame (u, w, a, r) inside a cell, T/a must be >= value(A, B, C, a, r)
with that cell's multipliers, where A = sum u^4, B = sum w^4, C = sum u^2 w^2 and T comes from my own term code.
A violation would mean the lower bound is wrong even though check() passes at the polytope vertices.
usage: python t104_audit_strat6_bound.py cells.json trials_per_cell seed"""
import sys, json
from fractions import Fraction as F
import numpy as np
from strat6_moment_bounds import value

cells = json.load(open(sys.argv[1])); TR = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]))


def T_of(W, tol=1e-9):
    N = W.shape[0]; L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N) if W[i, j] > 0)
    return D, X1 + X2 + X3 - 2 * S5


B0 = np.linalg.qr(np.column_stack([np.ones(5), rng.standard_normal((5, 4))]))[0][:, 1:]
worst = np.inf; nviol = 0; ntot = 0
for c in cells:
    rlo, rhi, alo, ahi = (float(F(c[k])) for k in ("rlo", "rhi", "alo", "ahi"))
    mult = [float(F(c[k])) for k in ("theta_n", "theta_j", "theta_d", "tangent", "shift")]
    kept = 0; tries = 0; cw = np.inf
    while kept < TR and tries < 300 * TR:
        tries += 1
        Q = np.linalg.qr(rng.standard_normal((4, 2)) * rng.uniform(0.2, 3, (4, 1)))[0]
        u, w = B0 @ Q[:, 0], B0 @ Q[:, 1]
        r = rng.uniform(rlo, rhi); a = alo + (ahi - alo) * rng.uniform(0, 1) ** 0.25; b = r * a
        lam = (2 + a + b) / 4
        W = lam / 5 + a * np.outer(u, u) + b * np.outer(w, w); np.fill_diagonal(W, 0)
        if W.min() < 0 or a > lam:
            continue
        D, T = T_of(W)
        if D != 2:
            continue
        kept += 1; ntot += 1
        A, Bm, C = float((u ** 4).sum()), float((w ** 4).sum()), float((u * u * w * w).sum())
        gap = T / a - value((A, Bm, C), a, r, *mult)
        cw = min(cw, gap)
        if gap < -1e-9:
            nviol += 1
    worst = min(worst, cw)
    print("r [%s,%s]  kept %d  least T/a - value %.4e" % (c["rlo"], c["rhi"], kept, cw))
print("frames %d  violations %d  least gap %.4e" % (ntot, nviol, worst))
