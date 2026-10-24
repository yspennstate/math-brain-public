#!/usr/bin/env python3
from fractions import Fraction

# Exact-arithmetic self-check for NM13-11 / P0257.
# Certifies the adaptive outward-sector correction and its compactified u>=1 tail.
# The geometric/calculus lemmas are proved in the accompanying immutable run report;
# every numerical endpoint and rational gate used there is checked here exactly.

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
sqrtpi_lo = Fraction(17, 10)
assert sqrtpi_lo**2 < 3 < pi_lo

# Carried equal-radius envelope at rho=2:
# q(2)=4*pi + 12*asin(1/4) + (3/4)*sqrt(15) + sqrt(3)/4.
# asin(x) <= x/sqrt(1-x^2), so asin(1/4) <= 1/sqrt(15) < 17/64.
assert 4096 < 289 * 15
asin_quarter_hi = Fraction(17, 64)
q2_hi = 4 * Fraction(22, 7) + 12 * asin_quarter_hi + 3 + Fraction(1, 2)
assert q2_hi == Fraction(2157, 112)
assert q2_hi < 20
assert 20 < 25
qneg_near = Fraction(1, 40000)  # q(2)^(-7/2) > 20^(-7/2) > 1/40000.

# Radial-shape exact integrals with d=1/2-s:
# J = integral_0^(1/2) s(1-d)d(3-d) ds = 83/1920.
# K = integral_0^(1/2) s(1-d)d ds = 1/64.
half = Fraction(1, 2)
J = (
    -half**5 / 5
    - Fraction(5, 8) * half**4
    + Fraction(1, 12) * half**3
    + Fraction(5, 16) * half**2
)
K = -half**4 / 4 + half**2 / 8
assert J == Fraction(83, 1920)
assert K == Fraction(1, 64)

# Near range 0<=u<=1. The adaptive angular-sector lemma gives
# integral_0^1 h_d(1+u)du >= (pi/3)(1-d)d(3-d).
# With dW=3*pi^2*s ds this yields pi^3*J for the radial family.
radial_near = Fraction(5, 16) * sqrtpi_lo * 27 * J * qneg_near
assert radial_near == Fraction(12699, 819200000)

# Disjoint cap: W_cap > 9/32 and d>=1/10. Its integrated near-range saving is
# (pi/3)*(9/10)*(1/10)*(29/10) > 261/1000.
cap_near_h = Fraction(261, 1000)
cap_near = (
    Fraction(5, 16)
    * Fraction(9, 32)
    * sqrtpi_lo
    * cap_near_h
    * qneg_near
)
assert cap_near == Fraction(39933, 40960000000)

# Tail gate for rho>=2.
# For x<=1/4, asin(x) <= (16/15)x because
# 1/sqrt(1-x^2) <= 4/sqrt(15) < 16/15.
assert Fraction(225, 16) < 15  # sqrt(15) > 15/4.

# Hence q(rho) < pi*rho^2 + (31/10)rho + 1/2.
# The lower-order term is <= (13/7)rho^2 for rho>=2.
poly_at_2 = Fraction(13, 7) * 4 - Fraction(31, 10) * 2 - Fraction(1, 2)
deriv_at_2 = Fraction(26, 7) * 2 - Fraction(31, 10)
assert poly_at_2 == Fraction(51, 70) and poly_at_2 > 0
assert deriv_at_2 > 0
assert Fraction(22, 7) + Fraction(13, 7) == 5

# Thus q(rho)<5 rho^2. Since sqrt(5)<9/4,
# q(rho)^(-7/2) > 4/(1125*rho^7).
assert Fraction(5) < Fraction(81, 16)

# For rho>=2 and 0<=d<=1/2, 2rho-d >= (7/4)rho.
# Together with pi/3>1, h_d(rho) >= (7/4)(1-d)d*rho.
assert Fraction(2) - Fraction(1, 4) == Fraction(7, 4)

# integral_2^infinity rho^(-6)dr = 1/160, hence the complete tail kernel is 7/180000.
tail_kernel = Fraction(7, 4) * Fraction(4, 1125) * Fraction(1, 160)
assert tail_kernel == Fraction(7, 180000)

radial_tail = Fraction(5, 16) * sqrtpi_lo * 27 * K * tail_kernel
cap_tail = (
    Fraction(5, 16)
    * sqrtpi_lo
    * Fraction(9, 32)
    * Fraction(9, 100)
    * tail_kernel
)
assert radial_tail == Fraction(357, 40960000)
assert cap_tail == Fraction(1071, 2048000000)

near_total = radial_near + cap_near
tail_total = radial_tail + cap_tail
shape_total = near_total + tail_total
assert near_total == Fraction(674883, 40960000000)
assert tail_total == Fraction(18921, 2048000000)
assert shape_total == Fraction(1053303, 40960000000)

# Previous run's continuous-radial-plus-cap correction, now strictly replaced.
old_shape = Fraction(56457, 8192000000)
gain = shape_total - old_shape
assert gain == Fraction(385509, 20480000000)
assert gain > 0

# Exact equal-radius-envelope endpoint carried from the 08:03 run.
base_cert = Fraction(
    4915876313217460292927478863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
previous_endpoint = base_cert + old_shape
expected_previous = Fraction(
    4915930154808341640583728863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
assert previous_endpoint == expected_previous

new_endpoint = base_cert + shape_total
expected_new = Fraction(
    4916077214821159023396228863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
assert new_endpoint == expected_new
assert new_endpoint > previous_endpoint
assert new_endpoint > Fraction(6292578, 10000000)

print("P0257 adaptive-sector + compactified-tail exact certificate")
print("PI_GT_3 =", pi_lo > 3)
print("PI_LT_22_OVER_7 =", pi_hi < Fraction(22, 7))
print("Q2_UPPER =", q2_hi)
print("Q2_UPPER_LT_20 =", q2_hi < 20)
print("RADIAL_NEAR_J =", J)
print("RADIAL_TAIL_K =", K)
print("TAIL_Q_LT_5_RHO2_GATE =", poly_at_2 > 0 and deriv_at_2 > 0)
print("TAIL_KERNEL_EXACT =", tail_kernel)
print("RADIAL_NEAR_DELTA =", radial_near)
print("CAP_NEAR_DELTA =", cap_near)
print("RADIAL_TAIL_DELTA =", radial_tail)
print("CAP_TAIL_DELTA =", cap_tail)
print("TOTAL_SHAPE_DELTA =", shape_total)
print("GAIN_OVER_PREVIOUS_EXACT =", gain)
print("GAIN_OVER_PREVIOUS_DECIMAL =", fixed_decimal(gain, 24))
print("PREVIOUS_ENDPOINT_DECIMAL =", fixed_decimal(previous_endpoint, 24))
print("NEW_ENDPOINT_EXACT =", new_endpoint)
print("NEW_ENDPOINT_DECIMAL =", fixed_decimal(new_endpoint, 24))
print("NEW_ENDPOINT_GT_0.6292578 =", new_endpoint > Fraction(6292578, 10000000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
