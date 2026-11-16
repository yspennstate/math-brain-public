"""Equitable partitions with the block contrasts on top. q blocks of sizes a_1..a_q; between blocks a and b a nonnegative
a x b matrix C_ab with every row sum lam*b/n and every column sum lam*a/n (Sinkhorn on a random sparse positive matrix),
so each block-constant vector orthogonal to 1 has eigenvalue lam. Random interior graphs, scaled down until lam is the
top eigenvalue with multiplicity exactly q-1. Weights scaled to tr L = 2. Uniform cross weights are the join family
(t104_join_audit.py), where G is block diagonal; here it is not. Prints min T, max 2S5/(X1+X2+X3), and min of
X1 + X2 - 2S5 (the join proof's inequality) over the instances.
usage: python t104_equitable_test.py q trials seed [minsize]
"""
import sys
import numpy as np

Q, TR, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
MINSIZE = int(sys.argv[4]) if len(sys.argv) > 4 else 1
rng = np.random.default_rng(SEED)


def lap(W):
    return np.diag(W.sum(1)) - W


def sinkhorn(M, r, c, it=3000):
    for _ in range(it):
        M *= (r / M.sum(1))[:, None]; M *= (c / M.sum(0))[None, :]
    return M


def build(sizes):
    n = sum(sizes); q = len(sizes); lam = 1.0
    W = np.zeros((n, n)); off = np.cumsum([0] + sizes)
    for x in range(q):
        for y in range(x + 1, q):
            a, b = sizes[x], sizes[y]
            M = rng.random((a, b)) * (rng.random((a, b)) < rng.uniform(0.4, 1.0)) + 1e-9
            M = sinkhorn(M, np.full(a, lam * b / n), np.full(b, lam * a / n))
            W[off[x]:off[x + 1], off[y]:off[y + 1]] = M
    W = W + W.T
    for x in range(q):
        a = sizes[x]
        if a >= 2:
            B = rng.random((a, a)) * (rng.random((a, a)) < rng.uniform(0.3, 1.0)); B = np.triu(B, 1); B = B + B.T
            W[off[x]:off[x + 1], off[x]:off[x + 1]] = B * rng.uniform(0.05, 1.0)
    lab = np.repeat(np.arange(q), sizes)
    Ybasis = np.array([(lab == x) - sizes[x] / n for x in range(q)], float).T   # block contrasts span
    for shrink in range(60):
        L = lap(W); ev = np.linalg.eigvalsh(L)
        # eigenvalues of L on the orthogonal complement of the block-constant vectors
        P = Ybasis @ np.linalg.pinv(Ybasis); P1 = np.ones((n, n)) / n
        Rp = np.eye(n) - P - P1 + P1 @ P   # projector onto complement of span(block indicators)
        Rp = np.eye(n) - np.linalg.qr(np.column_stack([np.ones(n), Ybasis]))[0] @ np.linalg.qr(np.column_stack([np.ones(n), Ybasis]))[0].T
        evc = np.linalg.eigvalsh(Rp @ L @ Rp)
        if evc.max() < lam * (1 - 1e-6):
            break
        for x in range(q):   # shrink interiors
            W[off[x]:off[x + 1], off[x]:off[x + 1]] *= 0.8
    else:
        return None
    s = W[np.triu_indices(n, 1)].sum(); return W / s


def terms(W, tol=1e-8):
    n = W.shape[0]; L = lap(W)
    ev, U = np.linalg.eigh(L)
    lam = ev[-1]; top = np.where(ev > lam - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lam * (np.eye(n) - np.ones((n, n)) / n) - L
    d = np.diag(L); c = 2 * n / (n - 2)
    S1 = D * (2 * lam - np.trace(L @ L)); S2 = float(np.diag(Pi) @ np.diag(G)); S3 = S5 = 0.0
    iu = np.triu_indices(n, 1)
    for i, j in zip(*iu):
        w = W[i, j]
        if w <= 0:
            continue
        S3 += w * (Pi[i, i] * G[i, i] + Pi[j, j] * G[j, j] - 2 * Pi[i, j] * G[i, j])
        S5 += w * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (2 * lam - d[i] - d[j] - 2 * w)
    S4 = D * ((n - 1) * lam - 2)
    X1 = S1; X2 = c * (lam * S2 - S3); X3 = (1 - lam) / (n - 2) * (S4 - c * S2)
    return D, lam, X1, X2, X3, 2 * S5, np.diag(Pi)


minT = np.inf; maxr = 0.0; minm = np.inf; kept = 0; worst_sizes = None; worst_m_sizes = None; diagspread = 0.0
for it in range(TR):
    sizes = [int(v) for v in rng.integers(MINSIZE, 6, size=Q)]
    if sum(sizes) < 5 or len(set(sizes)) == 1:
        continue
    W = build(sizes)
    if W is None:
        continue
    D, lam, X1, X2, X3, Y, dg = terms(W)
    if D != Q - 1:
        continue
    kept += 1
    T = X1 + X2 + X3 - Y; r = Y / (X1 + X2 + X3); m = X1 + X2 - Y
    diagspread = max(diagspread, dg.max() - dg.min())
    if T < minT:
        minT = T
    if r > maxr:
        maxr = r; worst_sizes = sizes
    if m < minm:
        minm = m; worst_m_sizes = sizes
print("q %d  kept %d of %d  max diag(Pi) spread %.3f" % (Q, kept, TR, diagspread))
print("min T %.4e   max 2S5/(X1+X2+X3) %.6f at sizes %s" % (minT, maxr, worst_sizes))
print("min (X1+X2-2S5) %.4e at sizes %s" % (minm, worst_m_sizes))
