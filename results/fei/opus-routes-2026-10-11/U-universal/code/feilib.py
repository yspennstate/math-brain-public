"""Exact and floating tools for Fourier entropy / influence experiments.

Conventions
-----------
* A Boolean function on n bits is a length-2^n array of +-1 values, indexed by
  x in [0, 2^n); bit i of x equal to 1 means x_i = -1.
* chi_S(x) = (-1)^{popcount(S & x)}; S is also a bitmask.
* W[S] = sum_x f(x) chi_S(x) is an integer; fhat(S) = W[S] / 2^n and
  p_S = W[S]^2 / 4^n.  All identities below can be evaluated exactly with
  integers; logarithms are floating point (evidence only).
* Entropies are in bits unless a function name says _nat.
"""
from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache

import numpy as np

LOG2E = 1.0 / math.log(2.0)


def popcount(x: int) -> int:
    return bin(x).count("1")


@lru_cache(maxsize=None)
def hadamard(n: int) -> np.ndarray:
    """Integer Walsh-Hadamard matrix H[S, x] = (-1)^{|S & x|} (int64)."""
    N = 1 << n
    idx = np.arange(N)
    H = np.ones((N, N), dtype=np.int64)
    for i in range(n):
        bit = (idx >> i) & 1
        H *= np.where(np.outer(bit, bit) == 1, -1, 1)
    return H


def fwht_int(table) -> np.ndarray:
    """Exact integer fast Walsh-Hadamard transform: returns W[S] (object or int64)."""
    a = np.array(table, dtype=np.int64).copy()
    N = a.shape[-1]
    h = 1
    while h < N:
        a = a.reshape(a.shape[:-1] + (N // (2 * h), 2, h))
        x = a[..., 0, :].copy()
        y = a[..., 1, :].copy()
        a[..., 0, :] = x + y
        a[..., 1, :] = x - y
        a = a.reshape(a.shape[:-3] + (N,))
        h *= 2
    return a


def spectrum(table) -> np.ndarray:
    """Floating spectral law p_S (sums to 1)."""
    W = fwht_int(table).astype(np.float64)
    N = W.shape[-1]
    return (W / N) ** 2


def xlog2(p: np.ndarray) -> np.ndarray:
    out = np.zeros_like(p, dtype=np.float64)
    m = p > 0
    out[m] = p[m] * np.log2(p[m])
    return out


def entropy(p: np.ndarray) -> np.ndarray:
    """Shannon entropy in bits along the last axis."""
    return -xlog2(p).sum(axis=-1)


def binh(q: np.ndarray) -> np.ndarray:
    q = np.asarray(q, dtype=np.float64)
    return -(xlog2(q) + xlog2(1.0 - q))


def nbits(N: int) -> int:
    return N.bit_length() - 1


@lru_cache(maxsize=None)
def sizes(n: int) -> np.ndarray:
    return np.array([popcount(s) for s in range(1 << n)], dtype=np.int64)


def influences(p: np.ndarray, n: int) -> np.ndarray:
    """Inf_i = sum_{S containing i} p_S, shape (..., n)."""
    idx = np.arange(1 << n)
    return np.stack([p[..., (idx >> i) & 1 == 1].sum(axis=-1) for i in range(n)], axis=-1)


def total_influence(p: np.ndarray, n: int) -> np.ndarray:
    return (p * sizes(n)).sum(axis=-1)


def erasure_terms(p: np.ndarray, n: int) -> np.ndarray:
    """B_i = H(S_i | S_{-i}) in bits, shape (..., n)."""
    idx = np.arange(1 << n)
    out = []
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        hi = lo | (1 << i)
        a = p[..., lo]
        b = p[..., hi]
        m = a + b
        with np.errstate(divide="ignore", invalid="ignore"):
            q = np.where(m > 0, b / np.where(m > 0, m, 1.0), 0.0)
        out.append((m * binh(q)).sum(axis=-1))
    return np.stack(out, axis=-1)


def restrict(table: np.ndarray, n: int, i: int, val_bit: int) -> np.ndarray:
    """Restriction x_i fixed (val_bit 0 means x_i=+1); result on n-1 bits."""
    idx = np.arange(1 << n)
    keep = idx[((idx >> i) & 1) == val_bit]
    return table[..., keep]


def delta_terms(table: np.ndarray, n: int) -> np.ndarray:
    """Delta_i H = H(f) - (H(f_+)+H(f_-))/2, shape (..., n)."""
    H = entropy(spectrum(table))
    out = []
    for i in range(n):
        Hp = entropy(spectrum(restrict(table, n, i, 0)))
        Hm = entropy(spectrum(restrict(table, n, i, 1)))
        out.append(H - 0.5 * (Hp + Hm))
    return np.stack(out, axis=-1)


def all_tables(n: int) -> np.ndarray:
    """All 2^(2^n) Boolean tables on n bits as an int8 array (+-1)."""
    N = 1 << n
    M = 1 << N
    codes = np.arange(M, dtype=np.int64)
    bits = (codes[:, None] >> np.arange(N)[None, :]) & 1
    return (1 - 2 * bits).astype(np.int8)


def summary(table, n: int | None = None) -> dict:
    t = np.asarray(table)
    if n is None:
        n = nbits(t.shape[-1])
    p = spectrum(t)
    H = float(entropy(p))
    inf = influences(p, n)
    I = float(inf.sum())
    B_i = erasure_terms(p, n)
    B = float(B_i.sum())
    TC = float(binh(inf).sum() - H)
    return dict(n=n, H=H, I=I, B=B, DTC=H - B, TC=TC, Var=float(1 - p[0]), inf=inf, B_i=B_i)


# ---------- exact rational helpers ----------

def exact_spectrum(table) -> list[Fraction]:
    W = fwht_int(table)
    N = len(W)
    return [Fraction(int(w) * int(w), N * N) for w in W]


def exact_influences(table) -> list[Fraction]:
    p = exact_spectrum(table)
    n = nbits(len(p))
    return [sum((p[s] for s in range(len(p)) if (s >> i) & 1), Fraction(0)) for i in range(n)]


def exact_total_influence(table) -> Fraction:
    p = exact_spectrum(table)
    return sum((popcount(s) * ps for s, ps in enumerate(p)), Fraction(0))
