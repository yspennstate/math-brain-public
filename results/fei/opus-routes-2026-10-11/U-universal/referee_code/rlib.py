"""Referee library for route U-universal (independent of the author's code/).

Conventions (my own): a Boolean function on n bits is a +-1 array of length N = 2^n; bit i of the
index x is 1 iff x_i = -1.  chi_S(x) = (-1)^{|S & x|}.  The integer Walsh transform
W[S] = sum_x f(x) chi_S(x) is exact; fhat(S) = W[S]/N and p_S = W[S]^2/N^2.

Everything that is an integer identity is done in integers; logarithms are float64 (evidence)
unless a function name ends in _mp (mpmath, 50 digits).
"""
from __future__ import annotations

import math
import numpy as np

LOG2E = 1.0 / math.log(2.0)


def nbits(N: int) -> int:
    n = N.bit_length() - 1
    assert 1 << n == N
    return n


def popcounts(n: int) -> np.ndarray:
    idx = np.arange(1 << n)
    c = np.zeros(1 << n, dtype=np.int64)
    for i in range(n):
        c += (idx >> i) & 1
    return c


def walsh(T: np.ndarray) -> np.ndarray:
    """Exact integer Walsh transform along the last axis (batch allowed).  Butterfly in int64."""
    a = np.array(T, dtype=np.int64, copy=True)
    N = a.shape[-1]
    n = nbits(N)
    shp = a.shape[:-1]
    for i in range(n):
        h = 1 << i
        a = a.reshape(shp + (N // (2 * h), 2, h))
        x = a[..., 0, :].copy()
        y = a[..., 1, :]
        a[..., 0, :] = x + y
        a[..., 1, :] = x - y
        a = a.reshape(shp + (N,))
    return a


def superset_sum(P: np.ndarray) -> np.ndarray:
    """Pi[S] = sum_{T superset of S} P[T] along the last axis (works for ints and floats)."""
    a = np.array(P, copy=True)
    N = a.shape[-1]
    n = nbits(N)
    idx = np.arange(N)
    for i in range(n):
        lo = idx[((idx >> i) & 1) == 0]
        a[..., lo] = a[..., lo] + a[..., lo | (1 << i)]
    return a


def plogq(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    """elementwise p*log2(q) with the convention 0*log(anything) = 0."""
    out = np.zeros(np.broadcast(p, q).shape, dtype=np.float64)
    m = (p > 0)
    m = np.broadcast_to(m, out.shape)
    pp = np.broadcast_to(p, out.shape)
    qq = np.broadcast_to(q, out.shape)
    out[m] = pp[m] * np.log2(qq[m])
    return out


def entropy(p: np.ndarray) -> np.ndarray:
    return -plogq(p, p).sum(axis=-1)


def h2(x):
    x = np.asarray(x, dtype=np.float64)
    return -(plogq(x, x) + plogq(1 - x, 1 - x))


class Spec:
    """Spectral data of a batch of laws p (shape (B, N)), float64, with optional exact integer numerators."""

    def __init__(self, p: np.ndarray):
        self.p = np.asarray(p, dtype=np.float64)
        if self.p.ndim == 1:
            self.p = self.p[None, :]
        self.N = self.p.shape[-1]
        self.n = nbits(self.N)
        self.size = popcounts(self.n)
        self.pi = superset_sum(self.p)

    @classmethod
    def from_tables(cls, T):
        T = np.asarray(T)
        if T.ndim == 1:
            T = T[None, :]
        W = walsh(T)
        N = T.shape[-1]
        s = cls((W.astype(np.float64) / N) ** 2)
        s.W = W
        return s

    def H(self):
        return entropy(self.p)

    def I(self):
        return (self.p * self.size).sum(-1)

    def Var(self):
        return 1.0 - self.p[:, 0]

    def U(self):
        # U = sum_S p_S log2(pi(S)/p_S)
        with np.errstate(divide="ignore", invalid="ignore"):
            r = np.where(self.p > 0, self.pi / np.where(self.p > 0, self.p, 1.0), 1.0)
        return plogq(self.p, r).sum(-1)

    def infl(self):
        idx = np.arange(self.N)
        return np.stack([self.p[:, ((idx >> i) & 1) == 1].sum(-1) for i in range(self.n)], -1)

    def B_i(self):
        idx = np.arange(self.N)
        out = []
        for i in range(self.n):
            lo = idx[((idx >> i) & 1) == 0]
            hi = lo | (1 << i)
            m = self.p[:, lo] + self.p[:, hi]
            with np.errstate(divide="ignore", invalid="ignore"):
                s = np.where(m > 0, self.p[:, hi] / np.where(m > 0, m, 1.0), 0.0)
            out.append((m * h2(s)).sum(-1))
        return np.stack(out, -1)

    def Gamma_i(self):
        """Gamma_i = sum_{S contains i} p_S log2(pi(S minus i)/pi(S))."""
        idx = np.arange(self.N)
        out = []
        for i in range(self.n):
            lo = idx[((idx >> i) & 1) == 0]
            hi = lo | (1 << i)
            with np.errstate(divide="ignore", invalid="ignore"):
                r = np.where(self.p[:, hi] > 0, self.pi[:, lo] / np.where(self.pi[:, hi] > 0, self.pi[:, hi], 1.0), 1.0)
            out.append(plogq(self.p[:, hi], r).sum(-1))
        return np.stack(out, -1)

    def L_down(self):
        """L = sum_S p_S sum_{i in S} log2(1 + p_{S-i}/p_S)."""
        idx = np.arange(self.N)
        tot = np.zeros(self.p.shape[0])
        for i in range(self.n):
            lo = idx[((idx >> i) & 1) == 0]
            hi = lo | (1 << i)
            with np.errstate(divide="ignore", invalid="ignore"):
                r = np.where(self.p[:, hi] > 0, 1.0 + self.p[:, lo] / np.where(self.p[:, hi] > 0, self.p[:, hi], 1.0), 1.0)
            tot += plogq(self.p[:, hi], r).sum(-1)
        return tot


def restrict_tables(T: np.ndarray, i: int, xi: int) -> np.ndarray:
    """physical restriction x_i = xi (+1 or -1) of a batch of tables; result on n-1 bits."""
    T = np.asarray(T)
    N = T.shape[-1]
    idx = np.arange(N)
    bit = 0 if xi == 1 else 1
    keep = idx[((idx >> i) & 1) == bit]
    return T[..., keep]


def all_tables(n: int) -> np.ndarray:
    N = 1 << n
    M = 1 << N
    codes = np.arange(M, dtype=np.int64)
    out = np.empty((M, N), dtype=np.int8)
    for x in range(N):
        out[:, x] = 1 - 2 * ((codes >> x) & 1)
    return out
