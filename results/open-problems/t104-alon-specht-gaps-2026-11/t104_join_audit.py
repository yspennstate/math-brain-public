"""Independent check of the uniform-join family (Codex STRAT2, step 4).
Blocks of sizes a_1..a_q, weight t on every cross pair, an arbitrary weighted graph inside each block with
largest internal Laplacian eigenvalue below a*t. Weights are scaled so tr L = 2. For each random instance:
  - D equals q-1 and lambda equals n*t;
  - T (trace form, as in t104_trace_form.py) is >= 0;
  - the block formulas X1 = D sum tr((lam I - G_a) G_a), X2 = c sum p_a tr(G_a^2),
    X3 = (1-lam)/(n-2) sum (D - c p_a) tr(G_a), 2 S5 = 2t sum (q-2+n/a) tr(G_a) agree with the direct sums;
  - for q = 3 the per-eigenvalue margin X1 + X2 - 2 S5 is >= 0.
usage: python t104_join_audit.py trials seed
"""
import sys
import numpy as np

TR, SEED = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(SEED)


def lap(W):
    return np.diag(W.sum(1)) - W


def instance(sizes):
    n = sum(sizes); q = len(sizes)
    W = np.zeros((n, n)); lab = np.repeat(np.arange(q), sizes)
    t = 1.0
    W[lab[:, None] != lab[None, :]] = t
    s = 0
    for a in sizes:
        if a >= 2:
            B = rng.random((a, a)) * (rng.random((a, a)) < rng.uniform(0.3, 1.0)); B = np.triu(B, 1); B = B + B.T
            lm = np.linalg.eigvalsh(lap(B))[-1]
            if lm > 0:
                frac = rng.choice([rng.uniform(0, 1), rng.uniform(0.95, 0.999)])
                B *= frac * a * t / lm
            W[s:s + a, s:s + a] = B
        s += a
    W /= W[np.triu_indices(n, 1)].sum()   # tr L = 2
    return W, lab


def terms(W, lab, sizes, tol=1e-9):
    n = W.shape[0]; q = len(sizes); L = lap(W)
    ev, U = np.linalg.eigh(L + np.ones((n, n)))   # constant vector moved to eigenvalue n
    ev[np.argmax(np.abs(U.T @ np.ones(n)))] = -1  # drop it
    order = np.argsort(ev); ev, U = ev[order], U[:, order]
    lam = ev[-1]; top = np.where(ev > lam - tol)[0]; D = len(top)
    Pi = U[:, top] @ U[:, top].T
    G = lam * (np.eye(n) - np.ones((n, n)) / n) - L
    d = np.diag(L); c = 2 * n / (n - 2)
    S1 = D * (2 * lam - np.trace(L @ L)); S2 = float(np.diag(Pi) @ np.diag(G)); S3 = S5 = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            w = W[i, j]
            if w == 0:
                continue
            S3 += w * (Pi[i, i] * G[i, i] + Pi[j, j] * G[j, j] - 2 * Pi[i, j] * G[i, j])
            S5 += w * (Pi[i, i] + Pi[j, j] - 2 * Pi[i, j]) * (2 * lam - d[i] - d[j] - 2 * w)
    S4 = D * ((n - 1) * lam - 2)
    X1 = S1; X2 = c * (lam * S2 - S3); X3 = (1 - lam) / (n - 2) * (S4 - c * S2)
    T = X1 + X2 + X3 - 2 * S5
    # block formulas
    t = W[lab[:, None] != lab[None, :]].max()
    bX1 = bX2 = bX3 = bQ = 0.0; s = 0; offblock = 0.0
    for k, a in enumerate(sizes):
        Ga = G[s:s + a, s:s + a]; pa = 1 / a - 1 / n
        bX1 += D * np.trace((lam * np.eye(a) - Ga) @ Ga); bX2 += c * pa * np.trace(Ga @ Ga)
        bX3 += (1 - lam) / (n - 2) * (D - c * pa) * np.trace(Ga); bQ += 2 * t * (q - 2 + n / a) * np.trace(Ga)
        s += a
    offblock = np.abs(G[lab[:, None] != lab[None, :]]).max()
    return dict(n=n, q=q, D=D, lam=lam, nt=n * t, T=T, X1=X1, X2=X2, X3=X3, Q=2 * S5,
                err=max(abs(bX1 - X1), abs(bX2 - X2), abs(bX3 - X3), abs(bQ - 2 * S5)), off=offblock)


worstT = np.inf; worst_m = np.inf; maxerr = 0.0; maxoff = 0.0; badD = 0; ratio = 0.0
for it in range(TR):
    q = rng.choice([3, 3, 3, 4])
    sizes = list(rng.integers(1, 6, size=q))
    if sum(sizes) < 4:
        continue
    W, lab = instance(sizes)
    r = terms(W, lab, sizes)
    if r["D"] != q - 1 or abs(r["lam"] - r["nt"]) > 1e-9:
        badD += 1; continue
    worstT = min(worstT, r["T"]); maxerr = max(maxerr, r["err"]); maxoff = max(maxoff, r["off"])
    ratio = max(ratio, r["Q"] / (r["X1"] + r["X2"] + r["X3"]))
    if q == 3:
        worst_m = min(worst_m, r["X1"] + r["X2"] - r["Q"])
print("trials %d  D != q-1 or lam != nt: %d" % (TR, badD))
print("min T %.3e   min (X1+X2-2S5) at q=3 %.3e   max 2S5/(X1+X2+X3) %.6f" % (worstT, worst_m, ratio))
print("block formulas vs direct sums: max err %.1e   max |G| off the blocks %.1e" % (maxerr, maxoff))
