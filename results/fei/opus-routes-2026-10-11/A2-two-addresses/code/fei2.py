"""Exact utilities for the two-spectral-address class K2.

Conventions: a point x of {-1,1}^n is an integer 0..2^n-1; bit i of x set means x_i = -1.
chi_S(x) = (-1)^{popcount(S & x)}.  Walsh coefficients are kept as integers
W_S = sum_x f(x) chi_S(x) = 2^n fhat(S), so p(S) = W_S^2 / 4^n exactly.
"""
from fractions import Fraction
import itertools, math

def wht_int(vals):
    """In-place style integer Walsh-Hadamard transform of a list of length 2^n (returns new list)."""
    a = list(vals)
    h = 1
    N = len(a)
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a

def popcount(x):
    return bin(x).count("1")

def spectrum(f, n):
    """f: list of +-1 of length 2^n.  Returns integer W with W_S = 2^n fhat(S)."""
    W = wht_int(f)
    assert sum(w * w for w in W) == 4 ** n, "not Boolean"
    return W

def H_I_float(W, n):
    N2 = 4 ** n
    H = 0.0
    I = 0.0
    for S, w in enumerate(W):
        if w:
            p = w * w / N2
            H -= p * math.log2(p)
            I += p * popcount(S)
    return H, I

def I_exact(W, n):
    N2 = 4 ** n
    return Fraction(sum(w * w * popcount(S) for S, w in enumerate(W)), N2)

def law_is_product_int(q, m):
    """q: list of nonnegative integers indexed by subsets of an m-set (bitmask).
    Product iff for every coordinate i the 2 x 2^(m-1) matrix [q(U), q(U+i)] (U not containing i)
    has rank <= 1.  (Coordinatewise independence from the rest for every i is equivalent to
    mutual independence.)"""
    for i in range(m):
        bit = 1 << i
        rows = [(q[U], q[U | bit]) for U in range(1 << m) if not U & bit]
        # rank <= 1: all 2x2 minors vanish
        ref = None
        for a, b in rows:
            if a or b:
                ref = (a, b)
                break
        if ref is None:
            continue
        a0, b0 = ref
        for a, b in rows:
            if a * b0 != b * a0:
                return False
    return True

def rows_of(W, n, A):
    """Split integer spectrum by address set A (tuple of coordinates).  Returns dict T -> list over
    U (bitmask over C in increasing order of C coordinates) of W values; and the C coordinate list."""
    C = [i for i in range(n) if i not in A]
    rows = {}
    for Tbits in range(1 << len(A)):
        Tmask = 0
        for k, a in enumerate(A):
            if Tbits >> k & 1:
                Tmask |= 1 << a
        row = []
        for Ubits in range(1 << len(C)):
            Umask = 0
            for k, c in enumerate(C):
                if Ubits >> k & 1:
                    Umask |= 1 << c
            row.append(W[Tmask | Umask])
        rows[Tbits] = row
    return rows, C

def conditionally_product(W, n, A):
    rows, C = rows_of(W, n, A)
    m = len(C)
    for T, row in rows.items():
        q = [w * w for w in row]
        if sum(q) == 0:
            continue
        if not law_is_product_int(q, m):
            return False
    return True

def address_sets(n, kmax=2):
    for k in range(0, kmax + 1):
        for A in itertools.combinations(range(n), k):
            yield A

def in_K2(W, n):
    """Return the first address set A (|A|<=2) making all conditional laws product, else None."""
    for A in address_sets(n, 2):
        if conditionally_product(W, n, A):
            return A
    return None

def row_decomposition(W, n, A):
    """Exact per-row data: weight (Fraction), marginals (Fractions), for a K2 witness."""
    rows, C = rows_of(W, n, A)
    m = len(C)
    out = {}
    N2 = 4 ** n
    for T, row in rows.items():
        q = [w * w for w in row]
        tot = sum(q)
        if tot == 0:
            out[T] = None
            continue
        wT = Fraction(tot, N2)
        marg = []
        for i in range(m):
            s = sum(q[U] for U in range(1 << m) if U >> i & 1)
            marg.append(Fraction(s, tot))
        out[T] = (wT, marg)
    return out, C

def h2(t):
    t = float(t)
    if t <= 0 or t >= 1:
        return 0.0
    return -t * math.log2(t) - (1 - t) * math.log2(1 - t)
