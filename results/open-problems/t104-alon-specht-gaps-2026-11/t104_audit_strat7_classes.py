"""Black-box check of STRAT7's disconnected N = 6, D = 2 classes with my own term code.
Each class is a list of component sizes; two components are carriers. Edge weights inside a component are exp(x),
carriers are rescaled to top Laplacian eigenvalue 1 (so the top is shared, D = 2 when each carrier's top is simple),
inactive components to top eigenvalue sigmoid(y) < 1, and the whole graph to edge sum 1. Nelder-Mead minimises T
from random starts; frames with D != 2 are penalised. A value below -1e-8 would refute the class.
Classes with a single component carrying a double top (4 with 1+1, 5+1) need the tie inside one component and are
not sampled here, except the balanced triangle 3+1+1+1 by construction.
usage: python t104_audit_strat7_classes.py starts seed"""
import sys
import numpy as np
from scipy.optimize import minimize

ST, rng = int(sys.argv[1]), np.random.default_rng(int(sys.argv[2]))
N = 6


def T_of(W, tol=1e-9):
    L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N))
    return D, X1 + X2 + X3 - 2 * S5


def build(sizes, carriers, x):
    W = np.zeros((N, N)); k = 0; start = 0; yk = len(x) - 1
    blocks = []
    for c, s in enumerate(sizes):
        idx = list(range(start, start + s)); start += s
        B = np.zeros((N, N))
        for i in range(len(idx)):
            for j in range(i + 1, len(idx)):
                B[idx[i], idx[j]] = B[idx[j], idx[i]] = np.exp(np.clip(x[k], -12, 6)); k += 1
        if s >= 2:
            top = np.linalg.eigvalsh(np.diag(B.sum(1)) - B)[-1]
            target = 1.0 if c in carriers else 1 / (1 + np.exp(-x[yk]))
            B *= target / top
        W += B
    tot = W[np.triu_indices(N, 1)].sum()
    return W / tot


def nparams(sizes):
    return sum(s * (s - 1) // 2 for s in sizes) + 1


def obj(x, sizes, carriers):
    W = build(sizes, carriers, x)
    D, T = T_of(W)
    return T if D == 2 else 10.0


classes = [((4, 2), (0, 1)), ((3, 3), (0, 1)), ((3, 2, 1), (0, 1)), ((2, 2, 2), (0, 1)), ((2, 2, 1, 1), (0, 1)),
           ((3, 2, 1), (1, 0)), ((4, 2), (0, 1))]
overall = np.inf
for sizes, carriers in classes:
    best = np.inf
    for _ in range(ST):
        r = minimize(obj, rng.standard_normal(nparams(sizes)) * 1.5, args=(sizes, carriers), method="Nelder-Mead",
                     options=dict(maxiter=4000, xatol=1e-10, fatol=1e-13))
        best = min(best, r.fun)
    overall = min(overall, best)
    print("%-14s carriers %s  starts %d  least T %.4e" % ("+".join(map(str, sizes)), carriers, ST, best), flush=True)
# balanced triangle + three isolates, and two half edges + two isolates (claimed equality cases)
W = np.zeros((N, N)); W[0, 1] = W[1, 2] = W[0, 2] = 1 / 3; W = W + W.T
print("balanced triangle + 3 isolates: D %d T %.3e" % T_of(W))
W = np.zeros((N, N)); W[0, 1] = W[2, 3] = 1 / 2; W = W + W.T
print("two half edges + 2 isolates:    D %d T %.3e" % T_of(W))
print("overall least T %.4e" % overall)
