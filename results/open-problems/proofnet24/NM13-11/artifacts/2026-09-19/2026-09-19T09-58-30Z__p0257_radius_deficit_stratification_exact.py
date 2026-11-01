#!/usr/bin/env python3
from fractions import Fraction

# Exact-arithmetic self-check for NM13-11 / P0257.
# This certifies the coarse rational endpoint produced by the
# continuous radius-deficit stratification plus a disjoint perpendicular cap.
# All assertions are exact rational/integer statements.

def arctan_interval_recip(m: int, n: int):
    x = Fraction(1, m)
    x2 = x * x
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

def fixed_decimal(x: Fraction, places: int = 24):
    assert x >= 0
    scale = 10 ** places
    z = (x.numerator * scale) // x.denominator
    return f"{z // scale}.{z % scale:0{places}d}"

# Machin bounds certify 3 < pi < 22/7.
a5_lo, a5_hi = arctan_interval_recip(5, 50)
a239_lo, a239_hi = arctan_interval_recip(239, 12)
pi_lo = 4 * (4*a5_lo - a239_hi)
pi_hi = 4 * (4*a5_hi - a239_lo)
assert pi_lo > 3
assert pi_hi < Fraction(22, 7)

# sqrt(pi) > 17/10 because (17/10)^2 < 3 < pi.
assert Fraction(17, 10) ** 2 < 3
sqrtpi_lo = Fraction(17, 10)

# Carried equal-radius envelope:
# q(2)=4*pi + 12*asin(1/4) + (3/4)*sqrt(15) + sqrt(3)/4.
# asin(x) <= x/sqrt(1-x^2), hence asin(1/4) <= 1/sqrt(15) < 17/64.
assert 4096 < 289 * 15
asin_quarter_hi = Fraction(17, 64)
q2_hi = 4 * Fraction(22, 7) + 12 * asin_quarter_hi + 3 + Fraction(1, 2)
assert q2_hi == Fraction(2157, 112)
assert q2_hi < 20

# Since sqrt(20)<5, q(2)^(-7/2) > 20^(-7/2) > 1/40000.
assert 20 < 25
qneg_lo = Fraction(1, 40000)

# Continuous radial-core stratification.
# For normalized midpoint radius s in [0,1/2], the guaranteed radius deficit is
# d(s)=1/2-s, and the shell-volume coefficient is dW=3*pi^2*s ds.
# The annular-sector saving at rho=1 is h_d(1)=pi*d(2-d)/6.
# The elementary shape integral is:
# I = integral_0^(1/2) s*(1/2-s)*(3/2+s) ds = 7/192.
I = (
    Fraction(3, 8) * Fraction(1, 2) ** 2
    - Fraction(1, 3) * Fraction(1, 2) ** 3
    - Fraction(1, 4) * Fraction(1, 2) ** 4
)
# The previous line is intentionally expanded from the antiderivative
# (3/8)s^2 - (1/3)s^3 - (1/4)s^4.
assert I == Fraction(7, 192)

# Delta_radial = (5/16)*sqrt(pi)*qneg*(pi^3/2)*I
#              = 35*pi^(7/2)/(6144)*qneg.
# Use pi^3 > 27 and sqrt(pi) > 17/10.
radial_lo = Fraction(35, 6144) * Fraction(27) * sqrtpi_lo * qneg_lo
assert radial_lo == Fraction(1071, 163840000)

# Disjoint perpendicular cap outside |w|<=D/2:
# |a|<=1/8 and 1/2<|b|<=5/8 has normalized w-area 1/16.
# Then both short sides are <=5/sqrt(32) < 9/10, so deficit d>=1/10.
assert Fraction(25, 32) < Fraction(81, 100)
# Three longest-side choices give W_cap = 3*pi/32 > 9/32.
Wcap_lo = Fraction(9, 32)
# h_{1/10}(1) = 19*pi/600 > 19/200.
hcap_lo = Fraction(19, 200)
cap_lo = Fraction(5, 16) * Wcap_lo * sqrtpi_lo * hcap_lo * qneg_lo
assert cap_lo == Fraction(2907, 8192000000)

total_shape_lo = radial_lo + cap_lo
assert total_shape_lo == Fraction(56457, 8192000000)

# The previous run's one-core correction, which the present stratification replaces.
prev_shape_lo = Fraction(3213, 1310720000)
increment_over_prev = total_shape_lo - prev_shape_lo
assert increment_over_prev == Fraction(145503, 32768000000)
assert increment_over_prev > 0

# Exact equilateral-envelope endpoint carried from the 08:03 run.
base_cert = Fraction(
    4915876313217460292927478863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
previous_endpoint = base_cert + prev_shape_lo
expected_previous = Fraction(
    4915895464189826625935291363546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
assert previous_endpoint == expected_previous

new_endpoint = base_cert + total_shape_lo
expected_new = Fraction(
    4915930154808341640583728863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
assert new_endpoint == expected_new
assert new_endpoint > previous_endpoint
assert new_endpoint > Fraction(629239, 1000000)

print("P0257 continuous radius-deficit stratification exact certificate")
print("PI_GT_3 =", pi_lo > 3)
print("PI_LT_22_OVER_7 =", pi_hi < Fraction(22, 7))
print("Q2_UPPER =", q2_hi)
print("Q2_UPPER_LT_20 =", q2_hi < 20)
print("SHAPE_INTEGRAL_I =", I)
print("RADIAL_DELTA_LO_EXACT =", radial_lo)
print("RADIAL_DELTA_LO_DECIMAL =", fixed_decimal(radial_lo, 24))
print("CAP_DELTA_LO_EXACT =", cap_lo)
print("CAP_DELTA_LO_DECIMAL =", fixed_decimal(cap_lo, 24))
print("TOTAL_SHAPE_DELTA_LO_EXACT =", total_shape_lo)
print("TOTAL_SHAPE_DELTA_LO_DECIMAL =", fixed_decimal(total_shape_lo, 24))
print("INCREMENT_OVER_PREVIOUS_EXACT =", increment_over_prev)
print("INCREMENT_OVER_PREVIOUS_DECIMAL =", fixed_decimal(increment_over_prev, 24))
print("PREVIOUS_ENDPOINT_DECIMAL =", fixed_decimal(previous_endpoint, 24))
print("NEW_ENDPOINT_EXACT =", new_endpoint)
print("NEW_ENDPOINT_DECIMAL =", fixed_decimal(new_endpoint, 24))
print("NEW_ENDPOINT_GT_0.629239 =", new_endpoint > Fraction(629239, 1000000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
