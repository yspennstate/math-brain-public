"""Black-box audit of STRAT4's connected-region claims (n=5, D=2): T >= 0 when g1 <= 4/11, and when g1 = g2 <= 7/16.
Frame: orthonormal zero-sum u, w in R^5; G = a uu' + b ww'; lam = (2+a+b)/4; w_ij = lam/5 + G_ij (must be >= 0).
Rejection-samples feasible frames, evaluates T with the term code of t104_strat3_audit.py, records min T and min ratio.
usage: python t104_audit_regions.py trials seed"""
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

B = np.linalg.qr(np.column_stack([np.ones(5), rng.standard_normal((5, 4))]))[0][:, 1:]
out = {}
for mode in ("g1<=4/11", "equal<=7/16", "free"):
    minT = np.inf; minr = np.inf; kept = 0; tries = 0
    while kept < TR and tries < 200 * TR:
        tries += 1
        Q = np.linalg.qr(rng.standard_normal((4, 2)) * rng.uniform(0.2, 3, (4, 1)))[0]
        u, w = B @ Q[:, 0], B @ Q[:, 1]
        if mode == "g1<=4/11":
            a = 4 / 11 * rng.uniform(0, 1) ** 0.3; b = a * rng.uniform(0, 1)
        elif mode == "equal<=7/16":
            a = b = 7 / 16 * rng.uniform(0, 1) ** 0.3
        else:
            a = rng.uniform(0, 1); b = a * rng.uniform(0, 1)
        lam = (2 + a + b) / 4
        G = a * np.outer(u, u) + b * np.outer(w, w)
        W = lam / 5 + G; np.fill_diagonal(W, 0)
        if W.min() < 0 or a > lam:
            continue
        W /= W[np.triu_indices(5, 1)].sum()
        D, X1, X2, X3, Y = terms(W)
        if D != 2:
            continue
        kept += 1; T = X1 + X2 + X3 - Y
        minT = min(minT, T); minr = min(minr, T / (X1 + X2 + X3))
    out[mode] = (kept, tries, minT, minr)
    print("%-12s kept %d of %d tries  min T %.4e  min ratio %.6f" % (mode, kept, tries, minT, minr))
