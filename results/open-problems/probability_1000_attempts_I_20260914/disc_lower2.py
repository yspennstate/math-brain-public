"""Lower bounds for Open Problem 11 of the Randomstrasse 2024 list at larger n.

disc(A) >= v exactly when the n rows of A and their complements cover every sign vector within Hamming
distance (n-v)/2.  Search for such a set of rows by annealing on the number of uncovered sign vectors,
keeping a coverage count so that changing one row costs a single pass, and verify any hit exhaustively
before believing it.
"""
import numpy as np, sys


def sign_vectors(n):
    m = 1 << (n - 1)
    b = ((np.arange(m, dtype=np.int64)[:, None] >> np.arange(n)[None, :]) & 1)
    b[:, n - 1] = 0
    return (1 - 2 * b).astype(np.int8)


def covers(V, r, v):
    return (np.abs(V @ r.astype(np.int16)) >= v)


def search(n, v, V, rng, iters=6000, restarts=6):
    m = V.shape[0]
    for _ in range(restarts):
        idx = rng.integers(0, m, n)
        cov = np.zeros(m, dtype=np.int16)
        for j in idx: cov += covers(V, V[j], v)
        unc = int((cov == 0).sum())
        best = unc
        for it in range(iters):
            if unc == 0: return idx
            j = int(rng.integers(0, n))
            # propose a row that covers some currently uncovered vector
            u = np.flatnonzero(cov == 0)
            pivot = V[u[rng.integers(0, len(u))]]
            cand = pivot.copy()
            flip = rng.integers(0, n, size=int(rng.integers(0, 3)))
            cand[flip] = -cand[flip]
            newc = covers(V, cand, v); oldc = covers(V, V[idx[j]], v)
            cov2 = cov - oldc + newc
            unc2 = int((cov2 == 0).sum())
            if unc2 <= unc or rng.random() < 0.02:
                # store the candidate by finding its index (rows are the sign vectors themselves)
                k = int(np.flatnonzero((V == cand).all(axis=1))[0]) if cand[-1] > 0 else \
                    int(np.flatnonzero((V == -cand).all(axis=1))[0])
                idx[j] = k; cov = cov2; unc = unc2
                best = min(best, unc)
    return None


if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(5)
    print(f"{'n':>3} {'v found':>8} {'ratio':>8} {'vs 5/3':>7}", flush=True)
    for n in range(lo, hi + 1):
        V = sign_vectors(n)
        got = 0; rows = None
        vtop = n if n % 2 else n - 1
        for v in range(vtop, 0, -2):
            idx = search(n, v, V, rng)
            if idx is not None:
                real = int(np.abs(V @ V[idx].T.astype(np.int16)).max(axis=1).min())
                if real >= v:
                    got, rows = real, V[idx].copy(); break
        r = got / np.sqrt(n)
        print(f"{n:>3} {got:>8} {r:>8.4f} {'BEATS' if r > 5/3 + 1e-12 else '':>7}", flush=True)
        if rows is not None: np.save(f'disc_rows_n{n}.npy', rows)
