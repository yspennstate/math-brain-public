"""Toeplitz aggregate lattice counts L_k(N), vectorized.

Same scan as aggregate_lattice.py: state (height, multiset of open chord
values), a slot opens a chord with value t (step +t) or closes an open chord
of value t (step -t, weight = multiplicity).  Multisets of each size are
ranked; adding or removing one value is injective on multisets, so each
(h, value) transition is a collision-free gather/scatter.  Counts are kept
modulo three primes near 2^58 and recovered by CRT.

Run: python -u lattice_np.py K [K ...]   (prints L_k(0..floor(k/2)), h*, m_2k)
"""
import sys, time
from itertools import combinations_with_replacement as cwr
from fractions import Fraction as F
from math import comb, factorial
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _primes_below(n, count):
    out = []
    c = n - 1
    while len(out) < count:
        if is_prime(c):
            out.append(c)
        c -= 1
    return out


PRIMES = _primes_below(1 << 58, 3)   # sums of 13 terms below 2^62 stay inside int64


def multisets(V, s):
    """count vectors (n, V) int8 of all multisets of size s, and sorted keys."""
    if s == 0:
        cnt = np.zeros((1, V), dtype=np.int8)
    else:
        arr = np.array(list(cwr(range(V), s)), dtype=np.int8)
        cnt = np.zeros((arr.shape[0], V), dtype=np.int8)
        for v in range(V):
            cnt[:, v] = (arr == v).sum(1)
        del arr
    B = np.int64(V)  # counts <= 12 < 13 <= V when V = 13; use base max(V, 13)
    return cnt


def keys_of(cnt, base):
    w = base ** np.arange(cnt.shape[1], dtype=np.int64)
    return (cnt.astype(np.int64) * w).sum(1)


def L_mod(k, N):
    V = 2 * N + 1
    smax = k
    base = np.int64(max(V, k + 1))
    cnts, keys, order = {}, {}, {}
    for s in range(smax + 1):
        c = multisets(V, s)
        kk = keys_of(c, base)
        o = np.argsort(kk)
        cnts[s] = c[o]
        keys[s] = kk[o]
    pw = base ** np.arange(V, dtype=np.int64)
    add, sub, subsel = {}, {}, {}
    for s in range(smax):
        a = np.empty((len(keys[s]), V), dtype=np.int64)
        for v in range(V):
            a[:, v] = np.searchsorted(keys[s + 1], keys[s] + pw[v])
        add[s] = a
    for s in range(1, smax + 1):
        sub[s], subsel[s] = {}, {}
        for v in range(V):
            sel = np.nonzero(cnts[s][:, v] > 0)[0]
            subsel[s][v] = sel
            sub[s][v] = np.searchsorted(keys[s - 1], keys[s][sel] - pw[v])
    P = np.array(PRIMES, dtype=np.int64).reshape(-1, 1)
    npr = len(PRIMES)
    # layer arrays: dict s -> array (npr, N+1, n_s)
    cur = {0: np.ones((npr, N + 1, 1), dtype=np.int64)}
    n = 2 * k
    for l in range(1, n + 1):
        rem = n - l
        nxt = {}
        for s, A in cur.items():
            # open: s -> s+1, needs s+1 <= rem
            if s + 1 <= rem:
                T = nxt.get(s + 1)
                if T is None:
                    T = np.zeros((npr, N + 1, len(keys[s + 1])), dtype=np.int64)
                    nxt[s + 1] = T
                for h in range(N + 1):
                    src = A[:, h, :]
                    if not src.any():
                        continue
                    for vi in range(V):
                        h2 = h + (vi - N)
                        if 0 <= h2 <= N:
                            idx = add[s][:, vi]
                            T[:, h2, idx] += src
                            T[:, h2, idx] %= P
            # close: s -> s-1, needs s-1 <= rem
            if s >= 1 and s - 1 <= rem:
                T = nxt.get(s - 1)
                if T is None:
                    T = np.zeros((npr, N + 1, len(keys[s - 1])), dtype=np.int64)
                    nxt[s - 1] = T
                for vi in range(V):
                    sel = subsel[s][vi]
                    if len(sel) == 0:
                        continue
                    idx = sub[s][vi]
                    mult = cnts[s][sel, vi].astype(np.int64)
                    for h in range(N + 1):
                        h2 = h - (vi - N)
                        if 0 <= h2 <= N:
                            src = A[:, h, sel]
                            T[:, h2, idx] += (src * mult) % P
                            T[:, h2, idx] %= P
        cur = nxt
    tot = cur[0].sum(axis=(1, 2)) % P[:, 0]
    return [int(x) for x in tot]


def crt(res):
    x, M = 0, 1
    for r, p in zip(res, PRIMES):
        t = ((r - x) * pow(M, -1, p)) % p
        x += M * t
        M *= p
    return x


def hstar_from(vals, d):
    hs = []
    for n, v in enumerate(vals):
        hs.append(v - sum(hs[i] * comb(n + d - i, d) for i in range(len(hs))))
    return hs


if __name__ == "__main__":
    assert all(is_prime(p) for p in PRIMES), "prime list"
    ks = [int(a) for a in sys.argv[1:]] or [4, 5, 6]
    for k in ks:
        t0 = time.time()
        half = k // 2 + 1
        vals = []
        for N in range(half):
            t1 = time.time()
            vals.append(crt(L_mod(k, N)))
            print(f"  k={k} N={N}: L={vals[-1]} ({time.time()-t1:.0f}s)", flush=True)
        hs = hstar_from(vals, k + 1)
        full = hs + [hs[k - i] for i in range(half, k + 1)]
        m = F(sum(full), factorial(k + 1))
        print(f"k={k}: L(0..{half-1}) = {vals}  h* = {full}  m_{2*k} = {m} = {float(m):.10e}  ({time.time()-t0:.0f}s)", flush=True)
