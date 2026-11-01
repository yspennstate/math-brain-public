"""Independent helper library for the review of route A2 (two spectral addresses).

Conventions (my own, written from the definitions, not copied from the route's code):
  * a point x of {-1,1}^n is an integer 0 <= x < 2^n; bit i of x is 1 iff x_i = -1.
  * a spectral set S is an integer bitmask; chi_S(x) = (-1)^popcount(x & S).
  * f is a +-1 integer vector of length 2^n; W[S] = sum_x f(x) chi_S(x) (integers), fhat = W / 2^n.
  * H(f) = sum_S fhat^2 log2(1/fhat^2) (bits), I(f) = sum_S |S| fhat^2.

Exact sign decisions: every quantity of the form  sum_S fhat(S)^2 log2(1/fhat(S)^2) - c I  with
c = 16/3 - (3/2) log2 3 is written as q0 + sum_{odd primes l} q_l log2 l with rational q's
(log2 of distinct odd primes and 1 are linearly independent over Q by unique factorisation), so its sign
is decided exactly: all q_l = 0 -> sign(q0); otherwise an mpmath interval evaluation at rising precision.
"""
from fractions import Fraction
from functools import lru_cache
import numpy as np
import mpmath
from mpmath import iv

POP = np.array([bin(i).count("1") for i in range(1 << 12)], dtype=np.int64)


def walsh_int(F):
    """F: integer array (..., 2^n). Returns sum_x F(x) chi_S(x) for every S (fast WHT, exact ints)."""
    A = np.array(F, dtype=np.int64, copy=True)
    N = A.shape[-1]
    h = 1
    while h < N:
        A = A.reshape(A.shape[:-1] + (N // (2 * h), 2, h))
        a = A[..., 0, :].copy()
        b = A[..., 1, :].copy()
        A[..., 0, :] = a + b
        A[..., 1, :] = a - b
        A = A.reshape(A.shape[:-3] + (N,))
        h *= 2
    return A


@lru_cache(maxsize=None)
def factor_small(k):
    """prime factorisation of a positive integer (small), as dict prime -> exponent"""
    out = {}
    d = 2
    while d * d <= k:
        while k % d == 0:
            out[d] = out.get(d, 0) + 1
            k //= d
        d += 1
    if k > 1:
        out[k] = out.get(k, 0) + 1
    return out


class LogLin:
    """q0 + sum_l q_l log2(l), l odd primes, rationals."""

    def __init__(self, q0=Fraction(0), ql=None):
        self.q0 = Fraction(q0)
        self.ql = dict(ql or {})

    def add_log2_int(self, coef, k):
        """add coef * log2(k) for a positive integer k"""
        coef = Fraction(coef)
        for l, e in factor_small(int(k)).items():
            if l == 2:
                self.q0 += coef * e
            else:
                self.ql[l] = self.ql.get(l, Fraction(0)) + coef * e
        return self

    def add(self, other, scale=1):
        scale = Fraction(scale)
        self.q0 += scale * other.q0
        for l, v in other.ql.items():
            self.ql[l] = self.ql.get(l, Fraction(0)) + scale * v
        return self

    def clean(self):
        self.ql = {l: v for l, v in self.ql.items() if v != 0}
        return self

    def interval(self, dps=50):
        old = iv.dps
        iv.dps = dps
        try:
            s = iv.mpf(self.q0.numerator) / self.q0.denominator
            for l, v in self.ql.items():
                s += iv.mpf(v.numerator) / v.denominator * iv.log(l) / iv.log(2)
            return s
        finally:
            iv.dps = old

    def sign(self):
        self.clean()
        if not self.ql:
            return (self.q0 > 0) - (self.q0 < 0)
        dps = 50
        while dps < 2000:
            s = self.interval(dps)
            if s.a > 0:
                return 1
            if s.b < 0:
                return -1
            dps *= 2
        raise RuntimeError("sign undecided")

    def __float__(self):
        return float(self.interval(30).mid)


def c_star_loglin():
    """c* = 16/3 - (3/2) log2 3"""
    return LogLin(Fraction(16, 3), {3: Fraction(-3, 2)})


def H_minus_cI_exact(W, n, c_rational=None, c_is_cstar=True):
    """W: integer Walsh vector of a Boolean function on n variables. Returns LogLin of H - c I
    (c = c* when c_is_cstar, else the rational c_rational)."""
    D = 4 ** n
    out = LogLin()
    Itot = Fraction(0)
    for S, w in enumerate(W):
        w = int(w)
        if w == 0:
            continue
        p = Fraction(w * w, D)
        # p log2(1/p) = p (2n - 2 log2 |w|)
        out.q0 += p * 2 * n
        out.add_log2_int(-2 * p, abs(w))
        Itot += p * bin(S).count("1")
    if c_is_cstar:
        # - c* I = -(16/3) I + (3/2) I log2 3
        out.q0 -= Fraction(16, 3) * Itot
        out.ql[3] = out.ql.get(3, Fraction(0)) + Fraction(3, 2) * Itot
    else:
        out.q0 -= Fraction(c_rational) * Itot
    return out.clean(), Itot


def H_float(W, n):
    p = (np.asarray(W, dtype=np.float64) / 2 ** n) ** 2
    nz = p > 0
    return float(-(p[nz] * np.log2(p[nz])).sum())


def I_exact(W, n):
    D = 4 ** n
    return sum(Fraction(int(w) * int(w), D) * bin(S).count("1") for S, w in enumerate(W))


def is_product_law_int(a, m):
    """a: nonnegative integer weights indexed by U in [0, 2^m). Exact test that a / sum(a) is a product law."""
    a = [int(t) for t in a]
    Z = sum(a)
    if Z == 0:
        return None  # absent row
    s = [sum(a[U] for U in range(1 << m) if (U >> i) & 1) for i in range(m)]
    Zp = Z ** (m - 1)
    for U in range(1 << m):
        rhs = 1
        for i in range(m):
            rhs *= s[i] if (U >> i) & 1 else (Z - s[i])
        if a[U] * Zp != rhs:
            return False
    return True


def rows_of(W, n, A):
    """Partial Walsh rows for the address set A (tuple of coordinates).
    Returns dict T(bitmask over A, as a subset of positions in A) -> integer vector over U in [0, 2^m)
    of W[T u U] where U ranges over subsets of C = complement (re-indexed by the order of C)."""
    C = [i for i in range(n) if i not in A]
    m = len(C)
    out = {}
    k = len(A)
    for t in range(1 << k):
        Tmask = 0
        for j in range(k):
            if (t >> j) & 1:
                Tmask |= 1 << A[j]
        vec = []
        for u in range(1 << m):
            Umask = 0
            for j in range(m):
                if (u >> j) & 1:
                    Umask |= 1 << C[j]
            vec.append(int(W[Tmask | Umask]))
        out[t] = vec
    return out, C


def in_K(W, n, A):
    """f in the class with address set A: every positive-weight conditional law of S_C given S_A is product."""
    rows, C = rows_of(W, n, A)
    m = len(C)
    for t, vec in rows.items():
        r = is_product_law_int([v * v for v in vec], m)
        if r is False:
            return False
    return True
