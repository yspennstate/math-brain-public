"""Referee library (independent of the author's fei_lib.py).

Convention: a function on n sign bits is a numpy array T of length 2^n; T[i] is its value at the point x with
x_j = -1 iff bit j of i is set.  chi_S(x) = (-1)^{popcount(S & i)} for a set S encoded as a bitmask.
Unnormalised Walsh transform W[S] = sum_i T[i] chi_S(i)  (exact for integer input).  fhat(S) = W[S]/2^n.
For a multiplexer F(x,y) = g_x(y) on an a-bit selector (low bits) and n-bit data (high bits):
joint index = xi + 2^a * yi.
"""
from fractions import Fraction
import math
import numpy as np

LOG2E = 1.0 / math.log(2.0)


def wht(v):
    """Unnormalised Walsh-Hadamard transform along the last axis (works for stacked rows).
    Integer input stays exact (int64); float input is float64."""
    a = np.array(v, copy=True)
    if a.dtype.kind in "iub":
        a = a.astype(np.int64)
    else:
        a = a.astype(np.float64)
    shp = a.shape
    N = shp[-1]
    a = a.reshape(-1, N)
    h = 1
    while h < N:
        a = a.reshape(a.shape[0], -1, 2, h)
        x = a[:, :, 0, :].copy()
        y = a[:, :, 1, :].copy()
        a[:, :, 0, :] = x + y
        a[:, :, 1, :] = x - y
        a = a.reshape(a.shape[0], N)
        h *= 2
    return a.reshape(shp)


def popcount_table(n):
    idx = np.arange(1 << n, dtype=np.int64)
    pc = np.zeros(1 << n, dtype=np.int64)
    for j in range(n):
        pc += (idx >> j) & 1
    return pc


def ent(p, axis=-1):
    """Shannon entropy in bits of nonnegative weights p along axis (assumed to sum to 1)."""
    p = np.asarray(p, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0)
    return t.sum(axis=axis)


def h2(t):
    t = np.asarray(t, dtype=np.float64)
    return ent(np.stack([t, 1 - t], axis=-1), axis=-1)


def spectrum(T, n):
    """Exact integer Walsh transform and the float squared-coefficient law."""
    W = wht(np.asarray(T, dtype=np.int64))
    P = (W.astype(np.float64) ** 2) / float(4 ** n)
    return W, P


def H_of(T, n):
    _, P = spectrum(T, n)
    return float(ent(P))


def I_exact(T, n):
    W = wht(np.asarray(T, dtype=np.int64))
    pc = popcount_table(n)
    return Fraction(int(np.sum(W * W * pc)), 4 ** n)


def coord_inf_exact(T, n):
    """Inf_j as exact Fractions from the truth table (disagreement probability)."""
    T = np.asarray(T)
    idx = np.arange(1 << n)
    out = []
    for j in range(n):
        out.append(Fraction(int(np.sum(T != T[idx ^ (1 << j)])), 1 << n))
    return out


def mux_table(branches, a, n):
    """branches: shape (2^a, 2^n), row b = g_b. Returns F with joint index xi + 2^a*yi."""
    B = np.asarray(branches)
    assert B.shape == (1 << a, 1 << n)
    return B.T.reshape(-1).copy()


def sel_data_split(W, a, n):
    """Reshape a joint Walsh vector (length 2^(a+n)) into a matrix M[S, T] (S selector set, T data set)."""
    return np.asarray(W).reshape(1 << n, 1 << a).T


def K_of_c(c):
    c = float(c)
    if c <= 0:
        return float("inf")
    hc = float(h2(c))
    return min(2 * hc / c, hc / c + 2 * LOG2E)


def bits(i, n):
    return [(-1 if (i >> j) & 1 else 1) for j in range(n)]
