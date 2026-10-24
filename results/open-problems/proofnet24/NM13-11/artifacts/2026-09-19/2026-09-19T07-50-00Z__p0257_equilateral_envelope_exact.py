#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt, comb

# Exact-arithmetic numerical certificate for the improved P0257
# equilateral-envelope closed-triple lower bound.
# No floating-point arithmetic is used in any assertion.

def arctan_interval_recip(m: int, n: int):
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

def asin_upper_half(x: Fraction, n_terms: int):
    # asin(x)=sum_{j>=0} binom(2j,j)x^(2j+1)/(4^j(2j+1)).
    # For 0<=x<=1/2, every coefficient is <=1, so after j=n_terms
    # the omitted positive tail is <= x^(2*n_terms+3)/(1-x^2).
    assert 0 <= x <= Fraction(1, 2)
    s = Fraction(0)
    for j in range(n_terms + 1):
        c = Fraction(comb(2*j, j), (4**j) * (2*j + 1))
        s += c * x**(2*j + 1)
    tail = x**(2*n_terms + 3) / (1 - x*x)
    return s + tail

def fixed_decimal(x: Fraction, places: int = 24):
    assert x >= 0
    scale = 10**places
    z = (x.numerator * scale) // x.denominator
    return f"{z//scale}.{z%scale:0{places}d}"

# Machin enclosure for pi.
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

# V = pi(4pi-3sqrt(3))/4 and prefactor V*sqrt(pi)/4.
GRID = 10**24
pref_raw_lo = pi_lo * (4*pi_lo - 3*sqrt3_hi) * sqrtpi_lo / 16
pref_lo = floor_grid(pref_raw_lo, GRID)
assert pref_lo > 0

# Equilateral-envelope normalized union area for rho>=1:
# q_delta(rho)=pi*rho^2+3*rho^2*asin(1/(2rho))
#              +(3/4)*sqrt(4rho^2-1)+sqrt(3)/4.
# Geometry gives q_delta increasing in rho; analytically
# q_delta'(rho)=2*pi*rho+6*rho*asin(1/(2rho))>0.
# Therefore q_delta(1+u)^(-5/2) is decreasing in u.
#
# We take an exact right Riemann lower sum on [0,20] with h=1/1000.
N = 20000
U_MAX = 20
ASIN_N = 20
TERM_SCALE = 10**24
SQRT_SCALE = 10**24
sum_term_grid = 0

for k in range(1, N + 1):
    u = Fraction(U_MAX * k, N)
    rho = 1 + u
    x = Fraction(1, 1) / (2*rho)
    asin_hi = asin_upper_half(x, ASIN_N)
    _, s_hi = sqrt_bounds(4*rho*rho - 1, SQRT_SCALE)

    q_hi = (
        pi_hi*rho*rho
        + 3*rho*rho*asin_hi
        + Fraction(3, 4)*s_hi
        + sqrt3_hi/4
    )

    _, sqrt_q_hi = sqrt_bounds(q_hi, SQRT_SCALE)
    # Lower bound q_hi^(-5/2)=1/(q_hi^2*sqrt(q_hi)).
    term_raw_lo = Fraction(
        q_hi.denominator*q_hi.denominator*sqrt_q_hi.denominator,
        q_hi.numerator*q_hi.numerator*sqrt_q_hi.numerator,
    )
    term_grid_lo = (term_raw_lo.numerator * TERM_SCALE) // term_raw_lo.denominator
    sum_term_grid += term_grid_lo

I_lo = Fraction(sum_term_grid * U_MAX, TERM_SCALE * N)
C_lo = pref_lo * I_lo
b_lo = Fraction(5, 8) + C_lo/2

old_cert = Fraction(
    15726690474745880958345733429927955202801271874129,
    25000000000000000000000000000000000000000000000000,
)

assert b_lo > old_cert
assert b_lo > Fraction(629232, 1000000)
assert b_lo > Fraction(6289, 10000)

print("P0257 equilateral-envelope exact certificate")
print("PI_LO_GRID =", pi_lo)
print("PI_HI_GRID =", pi_hi)
print("PREF_LO =", pref_lo)
print("ASIN_TERMS_THROUGH_J =", ASIN_N)
print("RIEMANN_N =", N)
print("RIEMANN_H = 1/1000")
print("RIEMANN_U_MAX =", U_MAX)
print("SUM_TERM_GRID =", sum_term_grid)
print("I_LO_DECIMAL =", fixed_decimal(I_lo, 24))
print("C_LO_DECIMAL =", fixed_decimal(C_lo, 24))
print("B_LO_EXACT =", b_lo)
print("B_LO_DECIMAL =", fixed_decimal(b_lo, 24))
print("B_LO_GT_PREVIOUS_CERT =", b_lo > old_cert)
print("B_LO_GT_0.629232 =", b_lo > Fraction(629232, 1000000))
print("B_LO_GT_0.6289 =", b_lo > Fraction(6289, 10000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
