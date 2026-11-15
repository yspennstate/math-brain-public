"""Black-box audit of STRAT5's new claims (n=5, D=2), with the same frame and term code as t104_audit_regions.py.
Modes: a <= 443/1000 (any r); r <= 3/25 (any a); equal gaps g <= 0.5491444; uniform complete graph added
(min w_ij >= (lam-a)/5). Also checks the moment bounds (13) on every sampled frame.
usage: python t104_audit_strat5.py trials seed"""
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
GSTAR = (209 + 3 * np.sqrt(305)) / 476
mom_bad = 0; mom_n = 0
for mode in ("a<=443/1000", "r<=3/25", "equal<=g*", "complete-added"):
    minT = np.inf; minr = np.inf; kept = 0; tries = 0
    while kept < TR and tries < 400 * TR:
        tries += 1
        Q = np.linalg.qr(rng.standard_normal((4, 2)) * rng.uniform(0.2, 3, (4, 1)))[0]
        u, w = B @ Q[:, 0], B @ Q[:, 1]
        if mode == "a<=443/1000":
            a = 0.443 * rng.uniform(0, 1) ** 0.2; b = a * rng.uniform(0, 1)
        elif mode == "r<=3/25":
            a = rng.uniform(0, 1); b = a * 0.12 * rng.uniform(0, 1)
        elif mode == "equal<=g*":
            a = b = GSTAR * rng.uniform(0, 1) ** 0.2
        else:
            # (23) holds when the endpoint graph splits: u constant on two blocks, w inside one block.
            k = rng.integers(1, 4); perm = rng.permutation(5); S, Tb = perm[:5 - k], perm[5 - k:]
            u = np.zeros(5); u[S] = k; u[Tb] = -(5 - k); u /= np.linalg.norm(u)
            blk = S if (len(S) >= 2 and (len(Tb) < 2 or rng.uniform() < 0.6)) else Tb
            v = np.zeros(5); v[blk] = rng.standard_normal(len(blk)); v[blk] -= v[blk].mean()
            w = v / np.linalg.norm(v)
            r = rng.uniform(0, 1); a = 2 / (3 - r) * rng.uniform(0, 1) ** 0.3; b = r * a
        lam = (2 + a + b) / 4
        G = a * np.outer(u, u) + b * np.outer(w, w)
        W = lam / 5 + G; np.fill_diagonal(W, 0)
        if W.min() < 0 or a > lam:
            continue
        if mode == "complete-added" and W[np.triu_indices(5, 1)].min() < (lam - a) / 5:
            continue
        A, Bm, C = (u ** 4).sum(), (w ** 4).sum(), (u * u * w * w).sum()
        mom_n += 1
        e = 1e-12
        if not (7/30 - e <= A <= 13/20 + e and 7/30 - e <= Bm <= 13/20 + e and -e <= C <= 0.3 + e
                and 0.25 - e <= A + C <= 0.8 + e and 0.25 - e <= Bm + C <= 0.8 + e
                and A + Bm + 2 * C <= 1.4 + e and 2 * C <= A + Bm + e):
            mom_bad += 1
        W /= W[np.triu_indices(5, 1)].sum()
        D, X1, X2, X3, Y = terms(W)
        if D != 2:
            continue
        kept += 1; T = X1 + X2 + X3 - Y
        minT = min(minT, T); minr = min(minr, T / (X1 + X2 + X3))
    print("%-15s kept %d of %d tries  min T %.4e  min ratio %.6f" % (mode, kept, tries, minT, minr))
print("moment bounds (13): %d violations in %d frames" % (mom_bad, mom_n))
