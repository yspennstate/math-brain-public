# Certified base-2 logarithms of primes and the exact sign of integer linear forms
# sum_p e_p log2 p.  Rational interval arithmetic (fractions) with a big-integer fallback.
# Used by census_n4.py, search_n56.py and b09_interval.py.
from fractions import Fraction
import numpy as np

def primes_upto(m):
    s = [True] * (m + 1); s[0] = s[1] = False
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, m + 1, i):
                s[j] = False
    return [i for i in range(m + 1) if s[i]]

def ln_enclosure(x, K=90):
    """x a Fraction in [1,2]. Returns rationals lo <= ln x <= hi from
    ln x = 2 atanh(z), z = (x-1)/(x+1) in [0,1/3]; all series terms are >= 0, so the
    partial sum is a lower bound and the tail is at most z^(2K+1)/((2K+1)(1-z^2))."""
    z = (x - 1) / (x + 1); z2 = z * z; s = Fraction(0); zp = z
    for k in range(K):
        s += zp / (2 * k + 1); zp *= z2
    tail = zp / ((2 * K + 1) * (1 - z2))
    return 2 * s, 2 * (s + tail)

LN2 = ln_enclosure(Fraction(2))
_cache = {}

def log2_enclosure(p):
    """Rational lo <= log2 p <= hi for an integer p >= 1."""
    if p in _cache:
        return _cache[p]
    k = p.bit_length() - 1
    if p == 1 << k:
        r = (Fraction(k), Fraction(k))
    else:
        lo, hi = ln_enclosure(Fraction(p, 1 << k))        # 0 <= lo <= ln(p/2^k) <= hi
        r = (k + lo / LN2[1], k + hi / LN2[0])
    _cache[p] = r
    return r

def factor(m):
    d = {}; x = m; p = 2
    while p * p <= x:
        while x % p == 0:
            d[p] = d.get(p, 0) + 1; x //= p
        p += 1
    if x > 1:
        d[x] = d.get(x, 0) + 1
    return d

SCALE_BITS = 320

def sign_form(coeffs):
    """Exact sign of sum_p coeffs[p] * log2 p (p distinct primes, integer coefficients).
    Interval test at 2^-320 resolution; if undecided, exact comparison of prod p^e.
    log2 of distinct primes are linearly independent over Q, so the form is 0 iff all
    coefficients vanish."""
    c = {p: int(e) for p, e in coeffs.items() if int(e) != 0}
    if not c:
        return 0
    S = 1 << SCALE_BITS; lo = 0; hi = 0
    for p, e in c.items():
        a, b = log2_enclosure(p)
        L = (a.numerator * S) // a.denominator
        U = -((-b.numerator * S) // b.denominator)
        if e > 0:
            lo += e * L; hi += e * U
        else:
            lo += e * U; hi += e * L
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    bits = sum(abs(e) * p.bit_length() for p, e in c.items())
    if bits > 20_000_000:
        raise RuntimeError('exact fallback too large: %d bits' % bits)
    A = 1; B = 1
    for p, e in c.items():
        if e > 0: A *= p ** e
        else: B *= p ** (-e)
    return (A > B) - (A < B)

def enclose_form(coeffs, const=Fraction(0)):
    """Rational enclosure [lo, hi] of const + sum_p coeffs[p] log2 p."""
    lo = Fraction(const); hi = Fraction(const)
    for p, e in coeffs.items():
        a, b = log2_enclosure(p)
        if e > 0:
            lo += e * a; hi += e * b
        elif e < 0:
            lo += e * b; hi += e * a
    return lo, hi

def add_mlogm(acc, m, mult):
    """acc += mult * (m log2 m) as prime exponents (0 log 0 = 0)."""
    if m <= 1:
        return
    for p, v in factor(m).items():
        acc[p] = acc.get(p, 0) + mult * m * v

class LinLog:
    """Vectorised screen for many forms over the primes <= maxval."""
    def __init__(self, maxval):
        self.P = primes_upto(maxval)
        self.idx = {p: k for k, p in enumerate(self.P)}
        self.lo = [log2_enclosure(p)[0] for p in self.P]
        self.logf = np.array([float(x) for x in self.lo])        # correctly rounded
        self.exact_calls = 0
    def vexp(self, m):
        v = [0] * len(self.P); x = m
        for k, p in enumerate(self.P):
            if x == 1:
                break
            while x % p == 0:
                v[k] += 1; x //= p
        assert x == 1, m
        return v
    def sign(self, e):
        self.exact_calls += 1
        return sign_form({self.P[k]: int(t) for k, t in enumerate(e) if int(t) != 0})
    def float_screen(self, E):
        """IEEE double screen. With integer entries < 2^50 and <= 600 terms the computed
        value differs from the true form by < 2^-46 * S, S = sum |e_k| log2 p_k; a row is
        decided only when |value| > 2^-40 * S.  Undecided rows return sign 0."""
        E = np.asarray(E)
        assert np.abs(E).max(initial=0) < 2 ** 50 and E.shape[-1] <= 600
        Ef = E.astype(np.float64)
        val = (Ef * self.logf).sum(axis=-1)
        S = (np.abs(Ef) * self.logf).sum(axis=-1)
        m = S * 2.0 ** -40
        sg = np.zeros(val.shape, dtype=np.int8)
        sg[val > m] = 1; sg[val < -m] = -1
        return sg, val
