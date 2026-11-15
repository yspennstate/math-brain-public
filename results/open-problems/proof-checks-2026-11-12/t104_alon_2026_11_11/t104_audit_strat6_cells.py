"""Black-box check of STRAT6's strong moment cells (n=5, D=2): sample frames with r in [rlo, rhi] and
a in [alo, ahi] of each cell, evaluate T with the term code of the earlier audits, report the least T and quotient.
usage: python t104_audit_strat6_cells.py cells.json trials_per_cell seed"""
import sys, json
from fractions import Fraction as F
import numpy as np
cells = json.load(open(sys.argv[1])); TR = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]))


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
worst_all = np.inf
for c in cells:
    rlo, rhi, alo, ahi = (float(F(c[k])) for k in ("rlo", "rhi", "alo", "ahi"))
    minT = np.inf; minq = np.inf; kept = 0; tries = 0
    while kept < TR and tries < 300 * TR:
        tries += 1
        Q = np.linalg.qr(rng.standard_normal((4, 2)) * rng.uniform(0.2, 3, (4, 1)))[0]
        u, w = B @ Q[:, 0], B @ Q[:, 1]
        r = rng.uniform(rlo, rhi)
        # bias a toward the ceiling, where the cell is tight
        a = alo + (ahi - alo) * rng.uniform(0, 1) ** 0.25; b = r * a
        lam = (2 + a + b) / 4
        W = lam / 5 + a * np.outer(u, u) + b * np.outer(w, w); np.fill_diagonal(W, 0)
        if W.min() < 0 or a > lam:
            continue
        W /= W[np.triu_indices(5, 1)].sum()
        D, X1, X2, X3, Y = terms(W)
        if D != 2:
            continue
        kept += 1; T = X1 + X2 + X3 - Y
        minT = min(minT, T); minq = min(minq, T / (X1 + X2 + X3))
    worst_all = min(worst_all, minq)
    print("r [%s,%s] a [%s,%s]  kept %d of %d  min T %.4e  min q %.5f" % (c["rlo"], c["rhi"], c["alo"], c["ahi"], kept, tries, minT, minq))
print("least quotient over all cells %.5f" % worst_all)
