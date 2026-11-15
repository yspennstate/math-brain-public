"""Toeplitz aggregate lattice counts L_k(N), on the reduced state space.

Same scan as lattice_np.py, but the height is not stored: it equals the sum
of the values of the open chords, so a state is a multiset of open values
whose sum lies in [0, N].  Only those multisets are enumerated.  Counts are
kept modulo three primes near 2^58 and recovered by CRT.

Run: python -u lattice_np2.py K [N0,N1,...]
"""
import sys, time
from fractions import Fraction as F
from math import comb, factorial
import numpy as np
from lattice_np import PRIMES, crt, hstar_from, is_prime


def states(N, k, LO, HI):
    """count matrices (int8, V columns) of multisets of size <= k over
    values -N..N whose sum is in [LO, HI], grouped by size."""
    V = 2 * N + 1
    cnt = np.zeros((1, V), dtype=np.int8)
    size = np.zeros(1, dtype=np.int64)
    tot = np.zeros(1, dtype=np.int64)
    for vi in range(V):
        v = vi - N
        parts_c, parts_s, parts_t = [], [], []
        for c in range(k + 1):
            ok = size + c <= k
            if not ok.any():
                break
            s2 = size[ok] + c
            t2 = tot[ok] + c * v
            nxt_min = min(0, v + 1) if vi + 1 < V else 0
            lo = t2 + (k - s2) * nxt_min           # smallest reachable sum
            hi = t2 + (k - s2) * (N if vi + 1 < V else 0)
            keep = (lo <= HI) & (hi >= LO)
            if vi + 1 == V:
                keep &= (t2 >= LO) & (t2 <= HI)
            if not keep.any():
                continue
            cc = cnt[ok][keep].copy()
            cc[:, vi] = c
            parts_c.append(cc); parts_s.append(s2[keep]); parts_t.append(t2[keep])
        cnt = np.concatenate(parts_c); size = np.concatenate(parts_s); tot = np.concatenate(parts_t)
    return {s: cnt[size == s] for s in range(k + 1)}


def L_run(k, N, h0):
    LO, HI = -h0, N - h0
    V = 2 * N + 1
    base = np.int64(max(V, k + 1))
    pw = base ** np.arange(V, dtype=np.int64)
    vals = np.arange(V, dtype=np.int64) - N
    st = states(N, k, LO, HI)
    cnts, keys = {}, {}
    for s in range(k + 1):
        c = st[s]
        kk = (c.astype(np.int64) * pw).sum(1)
        o = np.argsort(kk)
        cnts[s] = c[o]
        keys[s] = kk[o]
    del st
    sums = {s: (cnts[s].astype(np.int64) * vals).sum(1) for s in range(k + 1)}
    add, sub = {}, {}
    for s in range(k):
        a = {}
        for vi in range(V):
            ok = np.nonzero((sums[s] + vals[vi] >= LO) & (sums[s] + vals[vi] <= HI))[0]
            if len(ok) == 0:
                continue
            tgt = keys[s][ok] + pw[vi]
            idx = np.searchsorted(keys[s + 1], tgt)
            assert (keys[s + 1][idx] == tgt).all()
            a[vi] = (ok.astype(np.int32), idx.astype(np.int32))
        add[s] = a
    for s in range(1, k + 1):
        b = {}
        for vi in range(V):
            ok = np.nonzero((cnts[s][:, vi] > 0) & (sums[s] - vals[vi] >= LO) & (sums[s] - vals[vi] <= HI))[0]
            if len(ok) == 0:
                continue
            tgt = keys[s][ok] - pw[vi]
            idx = np.searchsorted(keys[s - 1], tgt)
            assert (keys[s - 1][idx] == tgt).all()
            b[vi] = (ok.astype(np.int32), idx.astype(np.int32), cnts[s][ok, vi].astype(np.int64))
        sub[s] = b
    del sums
    P = np.array(PRIMES, dtype=np.int64).reshape(-1, 1)
    npr = len(PRIMES)
    cur = {0: np.ones((npr, 1), dtype=np.int64)}
    n = 2 * k
    for l in range(1, n + 1):
        rem = n - l
        nxt = {}
        for s, A in cur.items():
            if s + 1 <= rem and s < k:
                T = nxt.get(s + 1)
                if T is None:
                    T = nxt[s + 1] = np.zeros((npr, len(keys[s + 1])), dtype=np.int64)
                for vi, (src, dst) in add[s].items():
                    T[:, dst] += A[:, src]
                    T[:, dst] %= P
            if s >= 1 and s - 1 <= rem:
                T = nxt.get(s - 1)
                if T is None:
                    T = nxt[s - 1] = np.zeros((npr, len(keys[s - 1])), dtype=np.int64)
                for vi, (src, dst, mult) in sub[s].items():
                    T[:, dst] += (A[:, src] * mult) % P
                    T[:, dst] %= P
        cur = nxt
    return [int(x) for x in cur[0][:, 0] % P[:, 0]]


def L_mod(k, N):
    # the start height h0 is conserved as height - sum; h0 and N - h0 are
    # mirror images under negating every value
    tot = [0, 0, 0]
    for h0 in range(N // 2 + 1):
        w = 1 if 2 * h0 == N else 2
        r = L_run(k, N, h0)
        tot = [(a + w * b) % p for a, b, p in zip(tot, r, PRIMES)]
    return tot


if __name__ == "__main__":
    assert all(is_prime(p) for p in PRIMES)
    k = int(sys.argv[1])
    half = k // 2 + 1
    Ns = [int(t) for t in sys.argv[2].split(",")] if len(sys.argv) > 2 else list(range(half))
    t0 = time.time()
    vals = []
    for N in Ns:
        t1 = time.time()
        vals.append(crt(L_mod(k, N)))
        print(f"  k={k} N={N}: L={vals[-1]} ({time.time()-t1:.0f}s)", flush=True)
    if Ns == list(range(half)):
        hs = hstar_from(vals, k + 1)
        full = hs + [hs[k - i] for i in range(half, k + 1)]
        m = F(sum(full), factorial(k + 1))
        print(f"k={k}: L(0..{half-1}) = {vals}  h* = {full}  m_{2*k} = {m} = {float(m):.10e}  ({time.time()-t0:.0f}s)", flush=True)
