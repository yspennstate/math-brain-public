# B14 lead checks (Claude), written for run 20261011T224500Z-claude-B14-granularity-neutralization.
# Independent implementation: numpy integer FWHT, superset-max DP, Python Fractions. No agent code imported.
# Convention: index b, bit i of b = 1  <=>  x_i = -1 ; chi_S(x) = (-1)^{popcount(S & b)} ; W[S] = sum_b f[b] chi_S.
import sys, json, math, time, random, itertools
from fractions import Fraction as Fr
import numpy as np

T0 = time.time()
OUT = {}
ASSERTS = [0]

def ok(cond, msg):
    ASSERTS[0] += 1
    if not cond:
        raise AssertionError(msg)

def fwht(f):
    a = np.array(f, dtype=np.int64).copy()
    n = a.shape[-1]
    h = 1
    while h < n:
        a = a.reshape(a.shape[:-1] + (-1, 2, h))
        x = a[..., 0, :].copy(); y = a[..., 1, :].copy()
        a[..., 0, :] = x + y; a[..., 1, :] = x - y
        a = a.reshape(a.shape[:-3] + (n,))
        h *= 2
    return a

def popcounts(m):
    idx = np.arange(1 << m, dtype=np.int64)
    pc = np.zeros(1 << m, dtype=np.int64)
    for i in range(m):
        pc += (idx >> i) & 1
    return pc

def upmax_degree(W, m):
    """d[S] = max{|T| : T superset of S, W[T] != 0}; -1 if none.  Works on last axis."""
    pc = popcounts(m)
    d = np.where(W != 0, pc, -1).astype(np.int64)
    for i in range(m):
        h = 1 << i
        shp = d.shape[:-1] + (-1, 2, h)
        dd = d.reshape(shp)
        dd[..., 0, :] = np.maximum(dd[..., 0, :], dd[..., 1, :])
        d = dd.reshape(d.shape)
    return d

def v2(x):
    x = abs(int(x)); return (x & -x).bit_length() - 1

def influences_edges(f, m):
    f = np.asarray(f); idx = np.arange(1 << m)
    return [Fr(int(np.count_nonzero(f != f[idx ^ (1 << i)])), 1 << m) for i in range(m)]

def spectral_data(f, m):
    W = fwht(f); pc = popcounts(m); D = 1 << (2 * m)
    q = [Fr(int(w) * int(w), D) for w in W]
    return W, pc, q

