#!/usr/bin/env python3
"""Deterministic arithmetic checks for QFORM B13 r13.

The proof is analytic and lives in REPORT.md.  This checker validates the beta-function
specializations and the stated numerical values; it is not used as a substitute for proof.
"""
import math


def log_beta(a, b):
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def chord_moment(m, q):
    # Exact analytic formula: integral_D ell(z)^q dz = q*m^((q+1)/2)*B(q,m).
    return q * m ** ((q + 1.0) / 2.0) * math.exp(log_beta(q, float(m)))


def conditional_moment(m, alpha=2.0 / 3.0):
    return chord_moment(m, 1.0 - alpha) ** 3


# q=1 and q=2 specializations.
for m in (2, 3, 4, 10, 100):
    assert abs(chord_moment(m, 1.0) - 1.0) < 2e-12
    target2 = 2.0 * math.sqrt(m) / (m + 1.0)
    assert abs(chord_moment(m, 2.0) - target2) < 2e-11

# At m=2, B(1/3,2)=9/4, hence M_2=27/16 exactly.
assert abs(conditional_moment(2) - 27.0 / 16.0) < 2e-12

expected = {
    4: 3.0987813411078717,
    10: 7.3633579283167905,
    100: 71.44517937398096,
    1000: 712.3103530824323,
}
for m, target in expected.items():
    got = conditional_moment(m)
    assert abs(got - target) <= 2e-10 * max(1.0, abs(target))

limit = math.gamma(4.0 / 3.0) ** 3
assert abs(limit - 0.7120729426887294) < 2e-15
# The exact ratio approaches the claimed positive asymptotic constant.
assert abs(conditional_moment(1000) / 1000.0 - limit) < 3e-4

print("QFORM_CONDITIONAL_2OVER3_MOMENT_CHECK_PASS")
for m in (2, 4, 10, 100, 1000):
    val = conditional_moment(m)
    print(f"m={m:4d} M_m={val:.15f} M_m/m={val/m:.15f}")
print(f"Gamma(4/3)^3={limit:.15f}")
