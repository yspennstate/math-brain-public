"""Black-box search for a counterexample in the 5+1 class at N = 6 (connected five-vertex component carrying the
double top, plus one isolated vertex), with my own term code. The component is the STRAT6 frame
omega_ij = lambda/5 + a u_i u_j + b w_i w_j (b = r a, lambda = (2 + a + b)/4, edge sum 1); the sixth vertex is
isolated, so the top pair and the edge sum are unchanged and T is evaluated with N = 6 constants.
Nelder-Mead over (frame, a, r) from random starts; a in [amin, 2/(3 - r)] through a sigmoid, r in [rmin, 1].
Frames with a negative weight, D != 2 or a disconnected component are penalised. Also reports least T/a^2.
usage: python t104_audit_strat9_51.py starts seed [amin]"""
import sys
import numpy as np
from scipy.optimize import minimize

ST, rng = int(sys.argv[1]), np.random.default_rng(int(sys.argv[2]))
AMIN = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
RMIN = 0.02
B0 = np.linalg.qr(np.column_stack([np.ones(5), np.random.default_rng(1).standard_normal((5, 4))]))[0][:, 1:]


def T_of(W, tol=1e-9):
    N = W.shape[0]; L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    E = (np.diag(Pi)[:, None] + np.diag(Pi)[None, :] - 2 * Pi) * (np.diag(G)[:, None] + np.diag(G)[None, :] - 2 * G)
    S5 = 0.5 * float((W * E).sum())
    return D, X1 + X2 + X3 - 2 * S5, ev


def unpack(x):
    Q = np.linalg.qr(x[:8].reshape(4, 2))[0]
    u, w = B0 @ Q[:, 0], B0 @ Q[:, 1]
    r = RMIN + (1 - RMIN) / (1 + np.exp(-x[9]))
    amax = 2 / (3 - r)
    a = AMIN + (amax - AMIN) / (1 + np.exp(-x[8]))
    return u, w, a, r


def build(x):
    u, w, a, r = unpack(x); b = r * a; lam = (2 + a + b) / 4
    W5 = lam / 5 + a * np.outer(u, u) + b * np.outer(w, w); np.fill_diagonal(W5, 0)
    W = np.zeros((6, 6)); W[:5, :5] = W5
    return W, a, r


def obj(x, scaled):
    W, a, r = build(x)
    neg = -min(W[:5, :5][np.triu_indices(5, 1)].min(), 0.0)
    if neg > 0:
        return 10 + 100 * neg
    D, T, ev = T_of(W)
    if D != 2 or ev[2] < 1e-7:      # ev[0] = 0 twice (isolated vertex + component), ev[2] > 0 iff component connected
        return 10.0
    return T / a ** 2 if scaled else T


for scaled in (False, True):
    best, arg = np.inf, None
    for _ in range(ST):
        res = minimize(obj, rng.standard_normal(10), args=(scaled,), method="Nelder-Mead",
                       options=dict(maxiter=6000, xatol=1e-11, fatol=1e-14))
        if res.fun < best:
            best, arg = res.fun, res.x
    W, a, r = build(arg)
    print("%s least %.4e at a %.5f r %.5f min weight %.3e" % ("T/a^2" if scaled else "T    ", best, a, r,
          W[:5, :5][np.triu_indices(5, 1)].min()), flush=True)
# padding check: same component at N = 5 (STRAT6 quantity) next to N = 6
W, a, r = build(arg)
print("check same frame: T(N=5) %.4e  T(N=6) %.4e" % (T_of(W[:5, :5])[1], T_of(W)[1]), flush=True)
