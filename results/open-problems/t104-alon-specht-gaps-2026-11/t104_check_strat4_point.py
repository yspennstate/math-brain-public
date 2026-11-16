"""Evaluate Codex STRAT4's worst n=5 D=2 points with the definitions directly (independent of stratum.py)."""
import sys
import numpy as np
for f in sys.argv[1:]:
    z = np.load(f); a, b, U = float(z['a']), float(z['b']), z['U']
    n = 5; lam = (2 + a + b) / 4; H = np.eye(n) - np.ones((n, n)) / n
    G = a * np.outer(U[:, 0], U[:, 0]) + b * np.outer(U[:, 1], U[:, 1])
    L = lam * H - G; W = -L.copy(); np.fill_diagonal(W, 0)
    ev, V = np.linalg.eigh(L); top = np.where(ev > ev[-1] - 1e-8)[0]; D = len(top)
    Pi = V[:, top] @ V[:, top].T
    c = 2 * n / (n - 2); beta = (1 - lam) / (n - 2)
    X1 = D * (lam * np.trace(G) - np.trace(G @ G)); X2 = c * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - c * np.diag(Pi) @ np.diag(G))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j]) for i in range(n) for j in range(i + 1, n))
    T = X1 + X2 + X3 - 2 * S5
    print(f, "D", D, "eigs", np.round(ev, 6), "min w %.3e" % W[np.triu_indices(n, 1)].min(), "sum w %.6f" % W[np.triu_indices(n, 1)].sum())
    print("   T %.6e  X1+X2+X3 %.6e  T/den %.8f  2S5/den %.8f  codex terms %s" % (T, X1 + X2 + X3, T / (X1 + X2 + X3), 2 * S5 / (X1 + X2 + X3), z['terms']))
    print("   weights", np.round(W[np.triu_indices(n, 1)], 6))
