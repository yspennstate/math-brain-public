"""Largest H/I among regular (shifted) monotone functions: simulated annealing over shifted up-sets.

A shifted up-set on n coordinates with order 0 >= 1 >= ... >= n-1 is an up-set closed under moving an
element to a smaller index.  Moves toggle one point while preserving both properties.
Compared with the best AND/OR chain (the conjectured LTF extremisers): 3.93519 (n=10), 3.96225 (n=12).
Usage: python regular_search.py N STEPS RESTARTS SEED
"""
import sys, math, time
import numpy as np
import numba as nb
from monolib import setup_process


@nb.njit(cache=True)
def wht_HI(f, n):
    N = 1 << n
    a = np.empty(N)
    for x in range(N):
        a[x] = -1.0 if f[x] else 1.0
    h = 1
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                u = a[j]
                v = a[j + h]
                a[j] = u + v
                a[j + h] = u - v
        h *= 2
    H = 0.0
    I = 0.0
    for S in range(N):
        c = a[S] / N
        p = c * c
        if p > 1e-300:
            H -= p * math.log2(p)
            cnt = 0
            s = S
            while s:
                s &= s - 1
                cnt += 1
            I += cnt * p
    return H, I


@nb.njit(cache=True)
def can_add(f, n, x):
    if f[x]:
        return False
    for k in range(n):
        if not (x >> k) & 1:
            if not f[x | (1 << k)]:
                return False
    # shifted: every left shift of x must be present
    for j in range(n):
        if (x >> j) & 1:
            for i in range(j):
                if not (x >> i) & 1:
                    y = (x & ~(1 << j)) | (1 << i)
                    if not f[y]:
                        return False
    return True


@nb.njit(cache=True)
def can_remove(f, n, x):
    if not f[x]:
        return False
    for k in range(n):
        if (x >> k) & 1:
            if f[x & ~(1 << k)]:
                return False
    # no member may shift onto x: for i < j with x_i = 1, x_j = 0, the point with i moved to j must be absent
    for i in range(n):
        if (x >> i) & 1:
            for j in range(i + 1, n):
                if not (x >> j) & 1:
                    y = (x & ~(1 << i)) | (1 << j)
                    if f[y]:
                        return False
    return True


@nb.njit(cache=True)
def anneal(n, steps, seed, T0, T1, start):
    np.random.seed(seed)
    N = 1 << n
    # start: AND of the first k coordinates for random k, which is shifted
    f = np.zeros(N, dtype=np.bool_)
    if start.size == N:
        for x in range(N):
            f[x] = start[x]
    else:
        k = np.random.randint(1, n + 1)
        mask = (1 << k) - 1
        for x in range(N):
            if (x & mask) == mask:
                f[x] = True
    H, I = wht_HI(f, n)
    cur = H / I if I > 0 else 0.0
    best = cur
    bestf = f.copy()
    for t in range(steps):
        T = T0 * (T1 / T0) ** (t / steps)
        found = False
        for _try in range(4000):
            x = np.random.randint(0, N)
            if f[x]:
                if can_remove(f, n, x):
                    f[x] = False
                    found = True
                    break
            else:
                if can_add(f, n, x):
                    f[x] = True
                    found = True
                    break
        if not found:
            continue
        H, I = wht_HI(f, n)
        val = H / I if I > 1e-12 else 0.0
        if val >= cur or np.random.random() < math.exp((val - cur) / T):
            cur = val
            if cur > best:
                best = cur
                bestf = f.copy()
        else:
            f[x] = not f[x]
    return best, bestf


@nb.njit(cache=True)
def best_lex(n):
    # lexicographic (initial segment) functions in the order where coordinate 0 is most significant:
    # f(x) = 1 iff rev(x) >= 2^n - a, an up-set that is shifted for the order 0 >= 1 >= ... >= n-1
    N = 1 << n
    best = 0.0
    besta = 0
    for a in range(1, N):
        f = np.zeros(N, dtype=np.bool_)
        for x in range(N):
            r = 0
            for b in range(n):
                if (x >> b) & 1:
                    r |= 1 << (n - 1 - b)
            f[x] = r >= N - a
        H, I = wht_HI(f, n)
        if I > 0 and H / I > best:
            best = H / I
            besta = a
    f = np.zeros(N, dtype=np.bool_)
    for x in range(N):
        r = 0
        for b in range(n):
            if (x >> b) & 1:
                r |= 1 << (n - 1 - b)
        f[x] = r >= N - besta
    return best, besta, f


def main():
    setup_process()
    n = int(sys.argv[1]); steps = int(sys.argv[2]); R = int(sys.argv[3]); seed = int(sys.argv[4])
    t0 = time.time()
    lb, la, lf = best_lex(n)
    print(f"n={n}: best lexicographic (AND/OR chain) H/I = {lb:.6f} at a = {la}", flush=True)
    overall = 0.0
    empty = np.zeros(0, dtype=np.bool_)
    for r in range(R):
        start = lf if r % 2 == 1 else empty
        T0 = 0.01 if r % 2 == 1 else 0.05
        best, bestf = anneal(n, steps, seed + r, T0, 0.0005, start)
        pts = int(bestf.sum())
        print(f"n={n} restart {r} ({'from best chain' if r % 2 == 1 else 'from AND_k'}): best H/I = {best:.6f} (|f^-1(1)| = {pts})", flush=True)
        if best > overall:
            overall = best
            np.save(f"../logs/regular_best_n{n}.npy", bestf.astype(np.uint8))
    print(f"n={n}: overall best H/I over regular found = {overall:.6f} ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
