"""Tests STRAT7's padding identities: for a graph W0 on n vertices padded with N - n isolated vertices,
X1 and S5 do not depend on N, X2 = 2N B/(N-2), X3 = (1-lam)[D(N-1)(N-4)lam - 2D(N-2) + 2N h]/(N-2)^2,
with B = sum_ij Pi_ij (lam I - L)_ij^2 and h = sum_i Pi_ii L_ii (computed on the padded graph).
usage: python t104_audit_strat7_padding.py trials seed"""
import sys
import numpy as np
TR, rng = int(sys.argv[1]), np.random.default_rng(int(sys.argv[2]))


def parts(W, tol=1e-9):
    N = W.shape[0]; L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N) if W[i, j] > 0)
    M = lm * np.eye(N) - L
    B = float((Pi * M * M).sum()); h = float(np.diag(Pi) @ np.diag(L))
    return D, lm, X1, X2, X3, S5, B, h


worst = dict(X1=0, S5=0, X2=0, X3=0); count = 0
for t in range(TR):
    n = int(rng.integers(3, 6))
    W0 = rng.uniform(0, 1, (n, n)) * (rng.uniform(0, 1, (n, n)) < 0.7)
    if t % 3 == 0:  # force a double top eigenvalue sometimes: a triangle with equal weights inside
        W0 = np.zeros((n, n)); W0[0, 1] = W0[1, 2] = W0[0, 2] = 1.0
    W0 = np.triu(W0, 1); W0 = W0 + W0.T
    if W0.sum() == 0:
        continue
    W0 /= W0[np.triu_indices(n, 1)].sum()
    ref = None
    for N in range(max(n, 5), 10):
        W = np.zeros((N, N)); W[:n, :n] = W0
        D, lm, X1, X2, X3, S5, B, h = parts(W)
        if ref is None:
            ref = (D, X1, S5)
        else:
            worst["X1"] = max(worst["X1"], abs(X1 - ref[1])); worst["S5"] = max(worst["S5"], abs(S5 - ref[2]))
        worst["X2"] = max(worst["X2"], abs(X2 - 2 * N * B / (N - 2)))
        X3f = (1 - lm) * (D * (N - 1) * (N - 4) * lm - 2 * D * (N - 2) + 2 * N * h) / (N - 2) ** 2
        worst["X3"] = max(worst["X3"], abs(X3 - X3f))
        count += 1
print("graphs %d, padded cases %d" % (TR, count))
for k, v in worst.items():
    print("max |%s difference| %.3e" % (k, v))
