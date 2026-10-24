"""Hunt for sign matrices beating the ratio 5/3 in Open Problem 11 of the Randomstrasse 2024 list.

disc(A) >= v exactly when the n rows and their complements cover every sign vector within Hamming
distance (n-v)/2, so a hit is a certificate and is verified exhaustively before being believed.  The
published covering-code bounds leave n = 12, 15, 17, 18, 20, 21 and beyond undecided at levels that would
beat 5/3, which is where this looks.

Annealing on the number of uncovered sign vectors, with a coverage count so one row change costs two
passes.
"""
import numpy as np, sys, time


def sign_vectors(n):
    m = 1 << (n - 1)
    b = ((np.arange(m, dtype=np.int64)[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int8)
    b[:, n - 1] = 0
    return (1 - 2 * b)


def hunt(n, v, iters=20000, restarts=8, seed=0, verbose=True):
    V = sign_vectors(n)
    m = V.shape[0]
    rng = np.random.default_rng(seed)
    Vi = V.astype(np.int16)
    def cov_of(r): return (np.abs(Vi @ r.astype(np.int16)) >= v)
    best_overall = None
    for rs in range(restarts):
        idx = rng.integers(0, m, n)
        cov = np.zeros(m, dtype=np.int16)
        for j in idx: cov += cov_of(V[j])
        unc = int((cov == 0).sum()); best = unc
        for it in range(iters):
            if unc == 0:
                return idx, V
            j = int(rng.integers(0, n))
            u = np.flatnonzero(cov == 0)
            # propose a row near an uncovered vector, with a few bits flipped
            cand = V[u[rng.integers(0, len(u))]].copy()
            for f in rng.integers(0, n, size=int(rng.integers(0, 4))): cand[f] = -cand[f]
            if cand[-1] < 0: cand = -cand
            newc = cov_of(cand); oldc = cov_of(V[idx[j]])
            cov2 = cov - oldc + newc
            unc2 = int((cov2 == 0).sum())
            if unc2 <= unc or rng.random() < 0.03:
                k = int(np.packbits((1 - cand[:-1]) // 2, bitorder='little').view(np.uint8)[0]) if n <= 9 else None
                # recover the index by bit arithmetic on the first n-1 coordinates
                bits = ((1 - cand[:-1]) // 2).astype(np.int64)
                k = int((bits << np.arange(n - 1)).sum())
                idx[j] = k; cov = cov2; unc = unc2
                best = min(best, unc)
        if verbose:
            print(f"    restart {rs}: {best} sign vectors left uncovered", flush=True)
    return None, V


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        n, v = (int(x) for x in arg.split(','))
        t0 = time.time()
        print(f"n = {n}, target discrepancy {v}  (ratio {v/np.sqrt(n):.4f}, beats 5/3: "
              f"{'yes' if v/np.sqrt(n) > 5/3 else 'no'})", flush=True)
        idx, V = hunt(n, v)
        if idx is None:
            print(f"  no covering found in the budget  [{time.time()-t0:.0f}s]", flush=True)
        else:
            A = V[idx]
            real = int(np.abs(V.astype(np.int16) @ A.T.astype(np.int16)).max(axis=1).min())
            print(f"  FOUND, verified discrepancy {real}, ratio {real/np.sqrt(n):.4f}  "
                  f"[{time.time()-t0:.0f}s]", flush=True)
            for r in A: print('   ', ''.join('+' if t > 0 else '-' for t in r), flush=True)
            np.save(f'hunt_n{n}_v{real}.npy', A)
