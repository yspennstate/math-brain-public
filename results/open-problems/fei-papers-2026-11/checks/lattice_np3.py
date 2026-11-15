"""Toeplitz aggregate lattice counts L_k(N): low-memory version of lattice_np2.

Same states and scan; the transition index arrays are rebuilt per layer
(searchsorted) instead of being stored for every layer, so the peak is about
two layers of counts plus the state table.  Runs one (N, h0) per call so the
pieces can go to different machines; prints residues mod the three primes.

Run: python -u lattice_np3.py K N H0         -> one run, residues
     python -u lattice_np3.py K               -> all N, h0, then m_2K
"""
import sys, time
from fractions import Fraction as F
from math import factorial
import numpy as np
from lattice_np2 import states, PRIMES, crt, hstar_from


def L_run(k, N, h0):
    LO, HI = -h0, N - h0
    V = 2 * N + 1
    base = np.int64(max(V, k + 1))
    pw = base ** np.arange(V, dtype=np.int64)
    vals = np.arange(V, dtype=np.int64) - N
    st = states(N, k, LO, HI)
    cnts, keys, sums = {}, {}, {}
    for s in range(k + 1):
        c = st[s]
        kk = (c.astype(np.int64) * pw).sum(1)
        o = np.argsort(kk)
        cnts[s] = c[o]
        keys[s] = kk[o]
        sums[s] = (cnts[s].astype(np.int64) * vals).sum(1)
    del st
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
                for vi in range(V):
                    ok = np.nonzero((sums[s] + vals[vi] >= LO) & (sums[s] + vals[vi] <= HI))[0]
                    if len(ok) == 0:
                        continue
                    dst = np.searchsorted(keys[s + 1], keys[s][ok] + pw[vi])
                    T[:, dst] += A[:, ok]
                    T[:, dst] %= P
            if s >= 1 and s - 1 <= rem:
                T = nxt.get(s - 1)
                if T is None:
                    T = nxt[s - 1] = np.zeros((npr, len(keys[s - 1])), dtype=np.int64)
                for vi in range(V):
                    ok = np.nonzero((cnts[s][:, vi] > 0) & (sums[s] - vals[vi] >= LO) & (sums[s] - vals[vi] <= HI))[0]
                    if len(ok) == 0:
                        continue
                    dst = np.searchsorted(keys[s - 1], keys[s][ok] - pw[vi])
                    mult = cnts[s][ok, vi].astype(np.int64)
                    T[:, dst] += (A[:, ok] * mult) % P
                    T[:, dst] %= P
        cur = nxt
    return [int(x) for x in cur[0][:, 0] % P[:, 0]]


if __name__ == "__main__":
    k = int(sys.argv[1])
    if len(sys.argv) == 4:
        N, h0 = int(sys.argv[2]), int(sys.argv[3])
        t = time.time()
        r = L_run(k, N, h0)
        print(f"k={k} N={N} h0={h0} res={r} ({time.time()-t:.0f}s)", flush=True)
        sys.exit(0)
    half = k // 2 + 1
    vals = []
    for N in range(half):
        tot = [0, 0, 0]
        for h0 in range(N // 2 + 1):
            w = 1 if 2 * h0 == N else 2
            tot = [(a + w * b) % p for a, b, p in zip(tot, L_run(k, N, h0), PRIMES)]
        vals.append(crt(tot))
        print(f"  k={k} N={N}: L={vals[-1]}", flush=True)
    hs = hstar_from(vals, k + 1)
    full = hs + [hs[k - i] for i in range(half, k + 1)]
    m = F(sum(full), factorial(k + 1))
    print(f"k={k}: L(0..{half-1}) = {vals}  h* = {full}  m_{2*k} = {m} = {float(m):.10e}", flush=True)
