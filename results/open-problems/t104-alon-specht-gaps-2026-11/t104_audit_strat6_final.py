"""Adversarial numerical audit of the FINAL STRAT6 cells (176 cells, ceiling 103/200), with my own term code.
For a fixed frame T/a = L(r) + a H(r) is affine in a, and a <= 443/1000 is already proved, so each cell's claim
reduces to T >= 0 at a = ahi; r is sampled at rlo, the midpoint and rhi. Frames are searched by Nelder-Mead
from random starts; frames outside the stratum (negative weight, D != 2, disconnected) are penalised.
Also sweeps the uniform ceiling a = 103/200 for r in [3/25, 1].
usage: python t104_audit_strat6_final.py celldir starts seed"""
import sys, json
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize

CD, ST, rng = sys.argv[1], int(sys.argv[2]), np.random.default_rng(int(sys.argv[3]))
B0 = np.linalg.qr(np.column_stack([np.ones(5), np.random.default_rng(1).standard_normal((5, 4))]))[0][:, 1:]


def frame(x):
    Q = np.linalg.qr(x.reshape(4, 2))[0]
    return B0 @ Q[:, 0], B0 @ Q[:, 1]


def T_of(W, tol=1e-9):
    N = W.shape[0]; L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N))
    return D, X1 + X2 + X3 - 2 * S5, ev


def objective(x, a, b):
    u, w = frame(x)
    lam = (2 + a + b) / 4
    W = lam / 5 + a * np.outer(u, u) + b * np.outer(w, w); np.fill_diagonal(W, 0)
    neg = -min(W.min(), 0.0)
    if neg > 0:
        return 10 + 100 * neg
    D, T, ev = T_of(W)
    if D != 2 or ev[1] < 1e-7:
        return 10.0
    return T


def search(a, b, starts):
    best = np.inf
    for _ in range(starts):
        r = minimize(objective, rng.standard_normal(8), args=(a, b), method="Nelder-Mead",
                     options=dict(maxiter=3000, xatol=1e-10, fatol=1e-13))
        best = min(best, r.fun)
    return best


worst = np.inf; wcell = None; n = 0
for name in ("strong_moment_cells.json", "enhanced_moment_cells.json", "directional_moment_cells.json"):
    cells = json.load(open(CD + "/" + name)); cw = np.inf
    for c in cells:
        rlo, rhi, ahi = float(F(c["rlo"])), float(F(c["rhi"])), float(F(c["ahi"]))
        for r in (rlo, (rlo + rhi) / 2, rhi):
            m = search(ahi, r * ahi, ST); n += 1
            cw = min(cw, m)
            if m < worst:
                worst, wcell = m, (name, c["rlo"], c["rhi"], c["ahi"], r)
    print("%-32s cells %3d  least min T at a = ahi: %.4e" % (name, len(cells), cw), flush=True)
print("cell points %d  overall least %.4e at %s" % (n, worst, wcell), flush=True)
print("uniform ceiling a = 103/200")
uw = np.inf
for r in np.linspace(0.12, 1.0, 23):
    m = search(103 / 200, r * 103 / 200, ST); uw = min(uw, m)
print("   least min T over 23 ratios %.4e" % uw, flush=True)
