#!/usr/bin/env python3
from fractions import Fraction

# Exact-arithmetic self-check for NM13-11 / P0257.
# It certifies the coarse positive improvement produced by the asymmetric
# closed-triple core. No floating-point arithmetic is used in any assertion.


def arctan_interval_recip(m: int, n: int):
    x = Fraction(1, m)
    x2 = x * x
    s = Fraction(0)
    xpow = x
    prev = None
    for j in range(n + 1):
        term = xpow / Fraction(2 * j + 1)
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


# Certified classical pi bracket from Machin's identity.
a5_lo, a5_hi = arctan_interval_recip(5, 50)
a239_lo, a239_hi = arctan_interval_recip(239, 12)
pi_lo = 4 * (4 * a5_lo - a239_hi)
pi_hi = 4 * (4 * a5_hi - a239_lo)
assert pi_lo > 3
assert pi_hi < Fraction(22, 7)

# Shape-core volume W0 = 3*pi^2/32 and sector loss h(1)=7*pi/96.
W0_lo = Fraction(27, 32)             # pi > 3
sqrtpi_lo = Fraction(17, 10)         # (17/10)^2 < 3 < pi
h1_lo = Fraction(7, 32)              # 7*pi/96 > 7/32
assert Fraction(17, 10) ** 2 < 3

# q_Delta(2) = 4*pi + 12*asin(1/4) + (3/4)*sqrt(15) + sqrt(3)/4.
# asin(x) <= x/sqrt(1-x^2), so asin(1/4) <= 1/sqrt(15) < 17/64.
assert 4096 < 289 * 15               # 1/sqrt(15) < 17/64
asin_quarter_hi = Fraction(17, 64)
q2_hi = 4 * Fraction(22, 7) + 12 * asin_quarter_hi + 3 + Fraction(1, 2)
assert q2_hi == Fraction(2157, 112)
assert q2_hi < 20

# q_Delta(2)^(-7/2) > 20^(-7/2) > 1/40000 because sqrt(20)<5.
assert 20 < 25
qneg_lo = Fraction(1, 40000)

# From f(x)=x^(-5/2), f(q-h)-f(q) >= (5/2) h q^(-7/2).
# Integrate only u in [0,1], where h(1+u)>=h(1) and q(1+u)<=q(2).
delta_lo = Fraction(5, 16) * W0_lo * sqrtpi_lo * h1_lo * qneg_lo
assert delta_lo == Fraction(3213, 1310720000)

old_cert = Fraction(
    4915876313217460292927478863546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
new_cert = old_cert + delta_lo
expected_new = Fraction(
    4915895464189826625935291363546259379089219326781,
    7812500000000000000000000000000000000000000000000,
)
assert new_cert == expected_new
assert new_cert > old_cert
assert new_cert > Fraction(6292346, 10_000_000)

print("P0257 asymmetric closed-triple core exact certificate")
print("PI_GT_3 =", pi_lo > 3)
print("PI_LT_22_OVER_7 =", pi_hi < Fraction(22, 7))
print("Q2_UPPER =", q2_hi)
print("Q2_UPPER_LT_20 =", q2_hi < 20)
print("DELTA_LO_EXACT =", delta_lo)
print("DELTA_LO_DECIMAL =", fixed_decimal(delta_lo, 24))
print("OLD_CERT_DECIMAL =", fixed_decimal(old_cert, 24))
print("NEW_CERT_EXACT =", new_cert)
print("NEW_CERT_DECIMAL =", fixed_decimal(new_cert, 24))
print("NEW_CERT_GT_0.6292346 =", new_cert > Fraction(6292346, 10_000_000))
print("ALL_EXACT_FINITE_CHECKS_PASS")
