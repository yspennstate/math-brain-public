"""Referee utilities (independent of the author's code/).

Conventions: coordinate i <-> bit i of the table index; bit 0 means x_i = +1, bit 1 means x_i = -1.
Boolean outputs in {-1,+1}, true = +1.  fhat(S) = 2^-n sum_x f(x) chi_S(x), chi_S(x) = prod_{i in S} x_i.
All Walsh transforms are exact integer transforms (numpy int64, |values| <= 2^n, n <= 24 here).
Logs base 2 unless stated.
"""
from fractions import Fraction
import math
import numpy as np

LOG2E = 1.0 / math.log(2.0)
A_EXP = 1.2  # the paper's a = 6/5


def log2(x):
    return math.log2(x)


def coords(n):
    """X[i] = array of x_i over all 2^n inputs (values +-1, int8)."""
    idx = np.arange(1 << n, dtype=np.int64)
    return [(1 - 2 * ((idx >> i) & 1)).astype(np.int8) for i in range(n)]


def fwht_int(f):
    """Exact integer Walsh-Hadamard transform: F[S] = sum_x f(x) (-1)^{popcount(S & x)}."""
    a = np.array(f, dtype=np.int64).copy()
    n = a.size.bit_length() - 1
    assert a.size == 1 << n
    h = 1
    while h < a.size:
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(-1)
        h *= 2
    return a


def spectrum(f):
    """Return (n, dict S -> integer F(S)) for the nonzero coefficients; fhat(S) = F(S)/2^n."""
    F = fwht_int(f)
    n = F.size.bit_length() - 1
    nz = np.nonzero(F)[0]
    return n, {int(S): int(F[S]) for S in nz}


def popcount(x):
    return bin(x).count("1")


def bits_of(S):
    out = []
    i = 0
    while S:
        if S & 1:
            out.append(i)
        S >>= 1
        i += 1
    return out


def stats_exact(n, spec):
    """Exact v, I as Fractions; H as float (from exact masses)."""
    den = Fraction(1, 1 << (2 * n))
    v = Fraction(0)
    I = Fraction(0)
    H = 0.0
    for S, c in spec.items():
        m = c * c * den
        if S != 0:
            v += m
            I += popcount(S) * m
        mf = float(m)
        H -= mf * math.log2(mf)
    return v, I, H


def h2(v):
    v = float(v)
    if v <= 0 or v >= 1:
        return 0.0
    return -v * math.log2(v) - (1 - v) * math.log2(1 - v)


def elem_sym(ws, s):
    """e_s of the list ws (floats), by the standard DP."""
    e = [1.0] + [0.0] * s
    for w in ws:
        for k in range(min(s, len(ws)), 0, -1):
            e[k] += e[k - 1] * w
    return e[s]


def elem_sym_all(ws):
    """Return list e_0..e_m of the list ws."""
    m = len(ws)
    e = [1.0] + [0.0] * m
    cnt = 0
    for w in ws:
        cnt += 1
        for k in range(cnt, 0, -1):
            e[k] += e[k - 1] * w
    return e


def theta(s, r, a=A_EXP):
    return min(1.0, (s / r) ** a)


def influences_from_table(f, n):
    X = None
    inf = []
    idx = np.arange(1 << n, dtype=np.int64)
    for i in range(n):
        g = f[idx ^ (1 << i)]
        inf.append(Fraction(int(np.count_nonzero(g != f)), 1 << n))
    return inf
