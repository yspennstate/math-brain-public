from fractions import Fraction
from itertools import product, permutations, combinations
from math import isqrt, perm
import sympy as sp

# PROB20-17 exact finite certificate.
# All matrices are rational PSD Gram matrices A=B^T B / tr(B^T B).
# Spectral norms are enclosed using exact rational root isolation for
# charpoly(P^T P), followed by exact rational square-root enclosures.

x = sp.symbols('x')
EPS_POWER = 8
SQRT_DIGITS = 8

B_LIST = [
    [[0,1,0],[1,-1,-1],[1,-1,-1]],
    [[0,1,1],[1,-1,-1],[1,0,0]],
    [[1,-1,-1],[1,-1,0],[1,0,0]],
    [[0,1,1],[1,-1,-1],[1,0,-1]],
    [[1,0,-1],[1,0,1],[1,1,1]],
    [[1,0,1],[1,1,-1],[1,1,1]],
    [[0,0,1],[1,-1,0],[1,1,1]],
    [[1,-1,1],[1,0,0],[1,1,1]],
    [[0,0,1],[0,0,1],[1,1,1]],
]

def gram_normalized(B):
    B = sp.Matrix(B)
    G = B.T * B
    tr = sum(G[i,i] for i in range(3))
    assert tr > 0
    A = G / tr
    assert A == A.T
    # PSD is exact from the displayed Gram factorization.
    return A

MATS = [gram_normalized(B) for B in B_LIST]

# Ensure this is genuinely noncommutative, not a diagonal-only test family.
noncommuting_pairs = 0
for i in range(len(MATS)):
    for j in range(i+1, len(MATS)):
        if MATS[i]*MATS[j] != MATS[j]*MATS[i]:
            noncommuting_pairs += 1
assert noncommuting_pairs > 0


def q_to_fraction(q):
    q = sp.Rational(q)
    return Fraction(int(q.p), int(q.q))


def sqrt_fraction_bounds(q, digits=SQRT_DIGITS):
    """Exact decimal-rational enclosure of sqrt(q), q>=0."""
    assert q >= 0
    if q == 0:
        return Fraction(0), Fraction(0)
    D = 10**digits
    z_floor = (q.numerator * D * D) // q.denominator
    a = isqrt(z_floor)
    lo = Fraction(a, D)
    if a*a*q.denominator == q.numerator*D*D:
        hi = lo
    else:
        hi = Fraction(a+1, D)
    assert lo*lo <= q <= hi*hi
    return lo, hi


def spectral_norm_interval(P):
    S = P.T * P
    if S.is_zero_matrix:
        return Fraction(0), Fraction(0)
    poly = S.charpoly(x).as_poly()
    intervals = sp.polys.polytools.intervals(
        poly, eps=sp.Rational(1, 10**EPS_POWER)
    )
    # Exact ordering of rational interval endpoints.
    (a,b), mult = max(intervals, key=lambda item: item[0][1])
    fa, fb = q_to_fraction(a), q_to_fraction(b)
    assert 0 <= fa <= fb
    lo, _ = sqrt_fraction_bounds(fa)
    _, hi = sqrt_fraction_bounds(fb)
    assert 0 <= lo <= hi
    return lo, hi


def word_norm_cache(mats, length):
    cache = {}
    for idx in product(range(len(mats)), repeat=length):
        P = sp.eye(3)
        for i in idx:
            P = P * mats[i]
        cache[idx] = spectral_norm_interval(P)
    return cache


def ratio_interval_from_cache(cache, subset, m):
    n = len(subset)
    wr_lo = wr_hi = Fraction(0)
    for local in product(range(n), repeat=m):
        idx = tuple(subset[i] for i in local)
        lo, hi = cache[idx]
        wr_lo += lo
        wr_hi += hi
    wor_lo = wor_hi = Fraction(0)
    for local in permutations(range(n), m):
        idx = tuple(subset[i] for i in local)
        lo, hi = cache[idx]
        wor_lo += lo
        wor_hi += hi
    assert wr_lo > 0
    factor = Fraction(n**m, perm(n,m))
    r_lo = factor * wor_lo / wr_hi
    r_hi = factor * wor_hi / wr_lo
    return r_lo, r_hi

# m=4: exact exhaustive subset search over one fixed 9-matrix rational Gram library.
cache4 = word_norm_cache(MATS, 4)
assert len(cache4) == 9**4
configs4 = []
for n in range(4, 10):
    for sub in combinations(range(9), n):
        rlo, rhi = ratio_interval_from_cache(cache4, sub, 4)
        assert rhi < 1
        configs4.append((rlo, rhi, n, sub))
assert len(configs4) == sum(sp.binomial(9,n) for n in range(4,10)) == 382
best4 = max(configs4, key=lambda z: z[1])

# m=5: exact certified test of the strongest numerical five-matrix candidate
# retained from this library-selection pass (indices 4..8).
MATS5 = MATS[4:9]
cache5 = word_norm_cache(MATS5, 5)
assert len(cache5) == 5**5
r5lo, r5hi = ratio_interval_from_cache(cache5, tuple(range(5)), 5)
assert r5hi < 1

print('PROB20-17 exact 3x3 rational Gram certificate')
print('sympy_version', sp.__version__)
print('noncommuting_pairs', noncommuting_pairs)
print('m4_word_norms_certified', len(cache4))
print('m4_source_valid_configurations_certified', len(configs4))
print('m4_best_n', best4[2])
print('m4_best_subset', best4[3])
print('m4_ratio_lower', best4[0])
print('m4_ratio_upper', best4[1])
print('m4_ratio_lower_decimal', float(best4[0]))
print('m4_ratio_upper_decimal', float(best4[1]))
print('m5_word_norms_certified', len(cache5))
print('m5_n', 5)
print('m5_subset_global_indices', tuple(range(4,9)))
print('m5_ratio_lower', r5lo)
print('m5_ratio_upper', r5hi)
print('m5_ratio_lower_decimal', float(r5lo))
print('m5_ratio_upper_decimal', float(r5hi))
print('ALL ASSERTIONS PASSED')
