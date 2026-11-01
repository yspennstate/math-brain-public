"""Hill-climb B/I (and H/I) over general Boolean functions by single truth-table flips.

sup B/I sandwiches the FEI constant:  C_FEI - 2/ln2 <= sup B/I <= C_FEI.  Read-once families reach 3.698; the
question is whether a free search over all functions goes higher.  Flipping f at one point x shifts every Fourier
coefficient by -2 f(x) 2^-n chi_S(x), so a whole sweep of 2^n neighbours is one Hadamard product.
usage: bclimb.py <n> <restarts> <target BI|HI|rho> [seed]"""
import numpy as np, math, sys, time
import bexp
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

def hadamard_rows(n, xs):
    """X[j, S] = chi_S(x_j) for x_j in xs"""
    S = np.arange(1 << n, dtype=np.uint64)[None, :]
    x = np.asarray(xs, dtype=np.uint64)[:, None]
    par = np.zeros(( len(xs), 1 << n), dtype=np.uint64)
    v = x & S
    # popcount parity
    v = v ^ (v >> np.uint64(1)); v &= np.uint64(0x5555555555555555)
    # simpler: use bit_count via python-free trick
    return v

def chi_matrix(n, chunk):
    S = np.arange(1 << n, dtype=np.int64)
    out = np.empty((len(chunk), 1 << n), dtype=np.int8)
    for r, x in enumerate(chunk):
        a = np.bitwise_and(S, int(x))
        # popcount
        b = a.copy(); c = np.zeros_like(b)
        while b.any():
            c += (b & 1); b >>= 1
        out[r] = 1 - 2 * (c & 1).astype(np.int8)
    return out

_POP = None
def popcount_table(n):
    global _POP
    if _POP is None or len(_POP) < (1 << n):
        _POP = np.array([bin(i).count("1") for i in range(1 << n)], dtype=np.int8)
    return _POP

def chi_block(n, chunk):
    pop = popcount_table(n)
    S = np.arange(1 << n, dtype=np.int64)[None, :]
    a = np.bitwise_and(S, np.asarray(chunk, dtype=np.int64)[:, None])
    return (1 - 2 * (pop[a] & 1)).astype(np.float64)

def score(fh, n, key, sizes, idxlo, idxhi):
    """fh: (B, 2^n) Fourier coefficients -> objective"""
    mu = fh * fh
    I = (mu * sizes).sum(axis=1)
    if key == "HI":
        with np.errstate(divide="ignore", invalid="ignore"):
            H = -np.where(mu > 1e-300, mu * np.log2(np.maximum(mu, 1e-300)), 0.0).sum(axis=1)
        return np.where(I > 1e-12, H / np.maximum(I, 1e-300), 0.0)
    B = np.zeros(fh.shape[0])
    for lo, hi in zip(idxlo, idxhi):
        A = fh[:, lo] ** 2; Bb = fh[:, hi] ** 2; m = A + Bb
        with np.errstate(divide="ignore", invalid="ignore"):
            beta = np.where(m > 1e-300, Bb / np.maximum(m, 1e-300), 0.0)
        B += (m * bexp._h2(beta)).sum(axis=1)
    return np.where(I > 1e-12, B / np.maximum(I, 1e-300), 0.0)

def climb(n, key, f0, rng, max_sweeps=200, chunk=1024):
    N = 1 << n
    sizes = popcount_table(n)[:N].astype(float)
    idxlo = [np.array([s for s in range(N) if not (s >> i) & 1]) for i in range(n)]
    idxhi = [lo | (1 << i) for i, lo in enumerate(idxlo)]
    f = f0.copy()
    cur = float(score(bexp.fwht(f[None, :]) / N, n, key, sizes, idxlo, idxhi)[0])
    for sweep in range(max_sweeps):
        fh = bexp.fwht(f[None, :])[0] / N
        best, bestx = cur, -1
        for st in range(0, N, chunk):
            xs = np.arange(st, min(st + chunk, N))
            X = chi_block(n, xs)
            cand = fh[None, :] - (2.0 * f[xs] / N)[:, None] * X
            sc = score(cand, n, key, sizes, idxlo, idxhi)
            j = int(np.argmax(sc))
            if sc[j] > best:
                best, bestx = float(sc[j]), int(xs[j])
        if bestx < 0:
            break
        f[bestx] = -f[bestx]; cur = best
    return cur, f, sweep

if __name__ == "__main__":
    n = int(sys.argv[1]); restarts = int(sys.argv[2]); key = sys.argv[3]
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    rng = np.random.default_rng(seed)
    N = 1 << n
    best = (-1, None); t0 = time.time()
    for r in range(restarts):
        if r == 0:
            f0 = np.ones(N); f0[N - 1] = -1.0                       # AND_n
        elif r == 1:
            f0 = 1.0 - 2.0 * (popcount_table(n)[:N] >= (n + 1) // 2)  # majority
        else:
            f0 = 1.0 - 2.0 * (rng.random(N) < rng.uniform(0.05, 0.5))
            if np.all(f0 == f0[0]): f0[0] = -f0[0]
        v, f, sw = climb(n, key, np.asarray(f0, float), rng)
        s = bexp.stats(f[None, :], n)
        if v > best[0]:
            best = (v, f.copy())
            print("  n=%d r=%3d  %s=%.6f  (sweeps %d)  B/I=%.5f H/I=%.5f rho0=%.5f I=%.4f  %.0fs"
                  % (n, r, key, v, sw, s["BI"][0], s["HI"][0], s["rho0"][0], s["I"][0], time.time() - t0), flush=True)
    v, f = best
    s = bexp.stats(f[None, :], n)
    print("BEST n=%d %s=%.6f   B/I=%.6f  H/I=%.6f  rho0=%.6f  B=%.5f H=%.5f I=%.5f   (%.0f s)"
          % (n, key, v, s["BI"][0], s["HI"][0], s["rho0"][0], s["B"][0], s["H"][0], s["I"][0], time.time() - t0))
    np.save("bclimb_%s_n%d_s%d.npy" % (key, n, seed), f)
