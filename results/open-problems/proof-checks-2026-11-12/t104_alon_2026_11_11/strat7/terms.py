"""Numerical reference for T = X1 + X2 + X3 - 2 S5 (floating point; for testing formulas only, never a proof).
terms(W) returns (D, X1, X2, X3, 2*S5). W: symmetric nonnegative, zero diagonal; normalised here to edge sum 1."""
import numpy as np


def terms(W, tol=1e-9):
    W = np.array(W, dtype=float)
    W = W / W[np.triu_indices(W.shape[0], 1)].sum()
    N = W.shape[0]
    L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L)
    lm = ev[-1]
    top = np.where(ev > lm - tol)[0]
    D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2)
    beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G))
    X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N) if W[i, j] > 0)
    return D, X1, X2, X3, 2 * S5


if __name__ == "__main__":
    # balanced triangle plus two isolated vertices (an n = 5 equality case): T should be 0
    W = np.zeros((5, 5)); W[0, 1] = W[1, 2] = W[0, 2] = 1; W = W + W.T
    D, X1, X2, X3, Y = terms(W)
    print("triangle+2 isolated: D", D, "T", X1 + X2 + X3 - Y)
