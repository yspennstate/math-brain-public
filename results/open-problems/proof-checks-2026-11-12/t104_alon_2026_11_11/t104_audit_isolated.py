"""Black-box audit of STRAT4's isolated-vertex theorem (n=5, D=2, one isolated vertex).
Vertex 4 isolated; on 0..3, L4 = lam(I - J/4) - (lam - mu) u u' with u unit zero-sum, so lam has multiplicity 2
on the 5-vertex graph. Weights w_ij = lam/4 + (lam-mu) u_i u_j >= 0 force s = (lam-mu)/lam <= 1/(4p), p = max(-u_i u_j).
Sum of weights scaled to 1. Computes T = X1+X2+X3-2S5 with the same term code as t104_strat3_audit.py.
usage: python t104_audit_isolated.py trials seed"""
import sys
import numpy as np
TR, SEED = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(SEED)

def terms(W, tol=1e-9):
    N = W.shape[0]; L = np.diag(W.sum(1)) - W
    ev, U = np.linalg.eigh(L); lm = ev[-1]; top = np.where(ev > lm - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T; G = lm * (np.eye(N) - np.ones((N, N)) / N) - L
    cc = 2 * N / (N - 2); beta = (1 - lm) / (N - 2)
    X1 = D * (lm * np.trace(G) - np.trace(G @ G)); X2 = cc * np.trace(G @ (Pi * G))
    X3 = beta * (D * np.trace(G) - cc * float(np.diag(Pi) @ np.diag(G)))
    S5 = sum(W[i, j] * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (G[i, i] + G[j, j] - 2 * G[i, j])
             for i in range(N) for j in range(i + 1, N) if W[i, j] > 0)
    return D, X1, X2, X3, 2 * S5

minT = np.inf; minr = np.inf; kept = 0; arg = None
for k in range(TR):
    u = rng.standard_normal(4) * rng.uniform(0.1, 3, 4); u -= u.mean(); u /= np.linalg.norm(u)
    p = max(-u[i] * u[j] for i in range(4) for j in range(i + 1, 4))
    smax = 1 / (4 * p)
    s = smax * (1.0 if k % 4 == 0 else rng.uniform(0, 1) ** 0.3)
    W = np.zeros((5, 5))
    for i in range(4):
        for j in range(i + 1, 4):
            W[i, j] = W[j, i] = max(0.0, 0.25 + s * u[i] * u[j])
    W /= W[np.triu_indices(5, 1)].sum()
    D, X1, X2, X3, Y = terms(W)
    if D != 2:
        continue
    kept += 1; T = X1 + X2 + X3 - Y; r = T / (X1 + X2 + X3)
    if T < minT: minT = T
    if r < minr: minr = r; arg = (np.round(u, 4), round(s / smax, 4))
print("kept %d of %d  min T %.6e  min T/(X1+X2+X3) %.10f at u,s/smax %s" % (kept, TR, minT, minr, arg))
