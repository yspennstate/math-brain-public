"""Exact optimal binary count-splitting tree by subset dynamic programming (cost about 5^n / 2 operations).

marg[B] = law of S cap B (compressed index over the bits of B), computed top-down in 3^n total work.
node cost of a split B = B1 + B2:  H(|S cap B1|, |S cap B2|) - H(|S cap B|).
CSopt = H(|S|) + best[[n]].
"""
import math
import numpy as np
import numba as nb
import wlib as W


@nb.njit(cache=True)
def _popc(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@nb.njit(cache=True)
def _expand(a, B):
    """pdep: place the bits of a into the set-bit positions of B."""
    out = 0
    j = 0
    b = B
    while b:
        low = b & (-b)
        if (a >> j) & 1:
            out |= low
        j += 1
        b ^= low
    return out


@nb.njit(cache=True)
def _compress(A, B):
    """pext: gather the bits of A at the set-bit positions of B."""
    out = 0
    j = 0
    b = B
    while b:
        low = b & (-b)
        if A & low:
            out |= (1 << j)
        j += 1
        b ^= low
    return out


@nb.njit(cache=True)
def build_marginals(p, n):
    N = 1 << n
    sizes = np.zeros(N, dtype=np.int64)
    for B in range(N):
        sizes[B] = 1 << _popc(B)
    off = np.zeros(N + 1, dtype=np.int64)
    for B in range(N):
        off[B + 1] = off[B] + sizes[B]
    marg = np.zeros(off[N], dtype=np.float64)
    full = N - 1
    for a in range(N):
        marg[off[full] + a] = p[a]  # compress(a, full) == a
    # descending order of popcount: process masks from full downward by removing the highest missing bit
    for B in range(N - 2, -1, -1):
        # pick j = lowest bit not in B; B | j > B so already computed
        comp = full ^ B
        j = comp & (-comp)
        Bj = B | j
        k = _popc(B)
        for a in range(1 << k):
            A = _expand(a, B)
            i0 = _compress(A, Bj)
            i1 = _compress(A | j, Bj)
            marg[off[B] + a] = marg[off[Bj] + i0] + marg[off[Bj] + i1]
    return marg, off


@nb.njit(cache=True)
def _xlog(x):
    if x <= 0.0:
        return 0.0
    return -x * math.log(x) / 0.6931471805599453


@nb.njit(cache=True)
def cs_dp(marg, off, n):
    N = 1 << n
    best = np.zeros(N)
    arg = np.zeros(N, dtype=np.int64)
    joint = np.zeros((n + 1, n + 1))
    for B in range(1, N):
        if (B & (B - 1)) == 0:
            continue
        k = _popc(B)
        low = B & (-B)
        rest = B ^ low
        # H(|S cap B|)
        tot = np.zeros(n + 1)
        for a in range(1 << k):
            tot[_popc(a)] += marg[off[B] + a]
        Htot = 0.0
        for c in range(k + 1):
            Htot += _xlog(tot[c])
        bv = 1e300
        ba = 0
        s = rest
        while True:
            B1 = low | s
            B2 = B ^ B1
            if B2 != 0:
                m1 = _compress(B1, B)  # B1 as a mask within the compressed index space of B
                for c1 in range(k + 1):
                    for c2 in range(k + 1):
                        joint[c1, c2] = 0.0
                for a in range(1 << k):
                    pa = marg[off[B] + a]
                    if pa > 0.0:
                        c1 = _popc(a & m1)
                        c2 = _popc(a) - c1
                        joint[c1, c2] += pa
                Hj = 0.0
                for c1 in range(k + 1):
                    for c2 in range(k + 1 - c1):
                        Hj += _xlog(joint[c1, c2])
                c = Hj - Htot + best[B1] + best[B2]
                if c < bv:
                    bv = c
                    ba = B1
            if s == 0:
                break
            s = (s - 1) & rest
        best[B] = bv
        arg[B] = ba
    return best, arg


def cs_opt(p, n):
    marg, off = build_marginals(np.asarray(p, dtype=np.float64), n)
    best, arg = cs_dp(marg, off, n)
    pc = W.popcounts(1 << n)
    Hsize = W.H_of(np.bincount(pc, weights=p, minlength=n + 1))
    return Hsize + float(best[(1 << n) - 1]), W.tree_from_arg(arg, (1 << n) - 1)
