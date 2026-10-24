"""Exact Walsh-transform utilities for the SEL route.

Truth tables are numpy int8/int64 arrays of +-1 of length 2^n.  Index i encodes the input x with
x_j = -1 iff bit j of i is 1.  The unnormalized Walsh transform W[S] = sum_x f(x) chi_S(x) is an exact
integer; fhat(S) = W[S] / 2^n.  Sets S are encoded as bitmasks.
"""
from fractions import Fraction
import math
import numpy as np

try:
    import mpmath
except ImportError:  # pragma: no cover
    mpmath = None


def fwht_int(a):
    """Unnormalized Walsh-Hadamard transform of an integer vector (exact, int64)."""
    a = np.array(a, dtype=np.int64).copy()
    n = a.shape[0]
    h = 1
    while h < n:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(-1)
        h *= 2
    return a


def fwht_float(a):
    a = np.array(a, dtype=np.float64).copy()
    n = a.shape[0]
    h = 1
    while h < n:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(-1)
        h *= 2
    return a


POPCOUNT_CACHE = {}


def popcounts(n):
    if n not in POPCOUNT_CACHE:
        idx = np.arange(1 << n, dtype=np.int64)
        pc = np.zeros(1 << n, dtype=np.int64)
        for j in range(n):
            pc += (idx >> j) & 1
        POPCOUNT_CACHE[n] = pc
    return POPCOUNT_CACHE[n]


def entropy_from_W(W, n):
    """Fourier entropy in bits, float, from exact integer Walsh coefficients."""
    W = np.asarray(W, dtype=np.float64)
    m = W * W
    nz = m > 0
    # p = m/4^n ; -p log p = p (2n - log2 m)
    p = m[nz] / float(4 ** n)
    return float(np.sum(p * (2 * n - np.log2(m[nz]))))


def entropy_probs(p):
    p = np.asarray(p, dtype=np.float64)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def influence_from_W(W, n):
    """Exact total influence as a Fraction."""
    pc = popcounts(n)
    W = np.asarray(W, dtype=np.int64)
    num = int(np.sum((W * W) * pc))
    return Fraction(num, 4 ** n)


def coord_influences_from_W(W, n):
    """Exact Inf_j as Fractions, j = 0..n-1."""
    W = np.asarray(W, dtype=np.int64)
    m = W * W
    idx = np.arange(1 << n)
    out = []
    for j in range(n):
        out.append(Fraction(int(np.sum(m[((idx >> j) & 1) == 1])), 4 ** n))
    return out


def H_interval(W, n, dps=60):
    """Rigorous-ish interval for H via mpmath interval arithmetic (outward rounding)."""
    if mpmath is None:
        raise RuntimeError("mpmath missing")
    iv = mpmath.iv
    iv.dps = dps
    vals, counts = np.unique(np.abs(np.asarray(W, dtype=np.int64)), return_counts=True)
    total = iv.mpf(0)
    four_n = 4 ** n
    for v, c in zip(vals, counts):
        v = int(v)
        if v == 0:
            continue
        m = v * v
        # contribution c * (m/4^n) * (2n - log2 m)
        term = iv.mpf(int(c) * m) / four_n * (2 * n - iv.log(iv.mpf(m)) / iv.log(2))
        total += term
    return total


def table_from_func(func, n):
    out = np.empty(1 << n, dtype=np.int64)
    for i in range(1 << n):
        x = [(-1 if (i >> j) & 1 else 1) for j in range(n)]
        out[i] = func(x)
    return out


def bits_of(i, n):
    return [(-1 if (i >> j) & 1 else 1) for j in range(n)]


def multiplexer_table(branches, a, n):
    """F(x,y) = g_x(y).  branches: array shape (2^a, 2^n) of +-1.  Selector bits are the LOW a bits
    of the joint index, data bits the HIGH n bits:  index = x_index + 2^a * y_index."""
    B = np.asarray(branches, dtype=np.int64)
    assert B.shape == (1 << a, 1 << n)
    # F[x + 2^a y] = B[x, y]
    return B.T.reshape(-1).copy()


def stats(table, n):
    W = fwht_int(table)
    return W, entropy_from_W(W, n), influence_from_W(W, n)
