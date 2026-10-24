#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

# Exact-arithmetic finite certificate for the numerical endpoint in
# NM13-11 / P0257 closed-2-nearest-triple lower bound.
# No floating-point arithmetic is used in any assertion.

def arctan_interval_recip(m: int, n: int):
    # Alternating series for arctan(1/m); consecutive partial sums bracket.
    x = Fraction(1, m)
    x2 = x*x
    s = Fraction(0)
    xpow = x
    prev = None
    for j in range(n + 1):
        term = xpow / Fraction(2*j + 1)
        s += term if j % 2 == 0 else -term
        if j == n - 1:
            prev = s
        if j < n:
            xpow *= x2
    return min(prev, s), max(prev, s)

def floor_grid(x: Fraction, scale: int):
    return Fraction((x.numerator * scale) // x.denominator, scale)

def ceil_grid(x: Fraction, scale: int):
    return Fraction((x.numerator * scale + x.denominator - 1) // x.denominator, scale)

def sqrt_bounds(x: Fraction, scale: int):
    # exact rational lo <= sqrt(x) <= hi, denominator = scale
    assert x > 0
    p, q = x.numerator, x.denominator
    a_floor = (p * scale * scale) // q
    lo = Fraction(isqrt(a_floor), scale)
    a_ceil = (p * scale * scale + q - 1) // q
    c = isqrt(a_ceil)
    if c*c < a_ceil:
        c += 1
    hi = Fraction(c, scale)
    assert lo*lo <= x <= hi*hi
    return lo, hi

def fixed_decimal(x: Fraction, places: int = 18):
    # exact truncation toward zero for x>=0, only for human-readable output
    assert x >= 0
    scale = 10**places
    z = (x.numerator * scale) // x.denominator
    return f"{z//scale}.{z%scale:0{places}d}"

# Machin: pi/4 = 4 arctan(1/5) - arctan(1/239).
a5_lo, a5_hi = arctan_interval_recip(5, 50)
a239_lo, a239_hi = arctan_interval_recip(239, 12)
pi_lo_raw = 4 * (4*a5_lo - a239_hi)
pi_hi_raw = 4 * (4*a5_hi - a239_lo)
CONST_SCALE = 10**30
pi_lo = floor_grid(pi_lo_raw, CONST_SCALE)
pi_hi = ceil_grid(pi_hi_raw, CONST_SCALE)
assert pi_lo <= pi_lo_raw < pi_hi_raw <= pi_hi
assert pi_hi - pi_lo <= Fraction(2, CONST_SCALE)

sqrt3_lo, sqrt3_hi = sqrt_bounds(Fraction(3), CONST_SCALE)
sqrtpi_lo, sqrtpi_hi = sqrt_bounds(pi_lo, CONST_SCALE)

# V = pi(4pi-3sqrt(3))/4, and prefactor V*sqrt(pi)/4.
# Lower bound: pi_lo for positive pi factors, sqrt3_hi for subtraction,
# sqrtpi_lo for sqrt(pi).
GRID = 10**24
pref_raw_lo = pi_lo * (4*pi_lo - 3*sqrt3_hi) * sqrtpi_lo / 16
pref_lo = floor_grid(pref_raw_lo, GRID)
assert pref_lo > 0

# q(u)=alpha+beta*u+pi*u^2,
# alpha=pi+3+sqrt(3)/4, beta=2pi+3.
# f(u)=q(u)^(-5/2) is decreasing for u>=0.
# Right Riemann sum on [0,10] with h=1/100 is therefore a lower bound.
TERM_SCALE = 10**24
SQRT_SCALE = 10**24
sum_term_grid = 0
for k in range(1, 1001):
    u = Fraction(k, 100)
    q_hi = pi_hi + 3 + sqrt3_hi/4 + (2*pi_hi + 3)*u + pi_hi*u*u
    _, sqrt_q_hi = sqrt_bounds(q_hi, SQRT_SCALE)
    # q_hi >= q and sqrt_q_hi >= sqrt(q_hi), hence this is <= q^(-5/2).
    term_raw_lo = Fraction(
        q_hi.denominator*q_hi.denominator*sqrt_q_hi.denominator,
        q_hi.numerator*q_hi.numerator*sqrt_q_hi.numerator
    )
    term_grid_lo = (term_raw_lo.numerator * TERM_SCALE) // term_raw_lo.denominator
    sum_term_grid += term_grid_lo

I_lo = Fraction(sum_term_grid, TERM_SCALE * 100)  # multiply sum by h=1/100
C_lo = pref_lo * I_lo
b_lo = Fraction(5, 8) + C_lo/2

# Certified targets.
assert b_lo > Fraction(629, 1000)
assert b_lo > Fraction(62906, 100000)
# Also records the literature lower endpoint this improves upon.
assert b_lo > Fraction(6289, 10000)

print("PI_LO_GRID =", pi_lo)
print("PI_HI_GRID =", pi_hi)
print("PREF_LO =", pref_lo)
print("RIEMANN_N = 1000")
print("RIEMANN_H = 1/100")
print("RIEMANN_U_MAX = 10")
print("SUM_TERM_GRID =", sum_term_grid)
print("I_LO_DECIMAL =", fixed_decimal(I_lo, 24))
print("C_LO_DECIMAL =", fixed_decimal(C_lo, 24))
print("B_LO_EXACT =", b_lo)
print("B_LO_DECIMAL =", fixed_decimal(b_lo, 24))
print("B_LO_GT_0.6290 =", b_lo > Fraction(629,1000))
print("B_LO_GT_0.62906 =", b_lo > Fraction(62906,100000))
print("B_LO_GT_0.6289 =", b_lo > Fraction(6289,10000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
