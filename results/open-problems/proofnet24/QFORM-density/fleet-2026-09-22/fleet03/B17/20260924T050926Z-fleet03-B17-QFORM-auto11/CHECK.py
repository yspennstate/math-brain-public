#!/usr/bin/env python3
"""Deterministic sanity checks for QFORM-MONOTONE-CORE-MINUS-SQUARE-GLOBAL-v1.

The mathematical proof is in REPORT.md.  These checks verify the exact rational
comparisons used in the partner separation and numerical values of the two
closed-form constants.  Numerical evaluation is diagnostic, not the proof of
the theorem.
"""

from math import sqrt, pi, erf, exp
from fractions import Fraction

Cminus = sqrt(6*pi) * erf(sqrt(3/2))
partner = 3*sqrt(2)*exp(-3/100)

# Exact rational comparison used after the elementary transcendental bound
# C_- < 97/24.
assert 97**2 < 18 * 24**2

# e^{-3/100} > 97/100, then
# 3 sqrt(2) * 97/100 > 97/24 iff 18 sqrt(2) > 25,
# whose square is 648 > 625.
assert 18**2 * 2 > 25**2
partner_rational_lower = 3*sqrt(2)*Fraction(97,100)
assert partner_rational_lower > Fraction(97,24)

# Diagnostic direct evaluations.
assert Cminus < 97/24
assert partner > 97/24
assert partner > Cminus
assert Cminus < 3*sqrt(2)

# The exact negative-level optimizer value in the Gaussian endpoint is
# M(r)=12 int_0^{1/2} exp[-6(y^2+2 r y)]dy, which is pointwise decreasing in r.
# Verify on a deterministic grid as a sanity check only.
def simpson_M(r, n=20000):
    assert n % 2 == 0
    a, b = 0.0, 0.5
    h = (b-a)/n
    def f(y):
        return 12*exp(-6*(y*y+2*r*y))
    total = f(a)+f(b)
    total += 4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))
    total += 2*sum(f(a+2*k*h) for k in range(1,n//2))
    return total*h/3

vals = [simpson_M(r) for r in (0.0, 0.1, 0.5, 1.0, 2.0)]
assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))
assert abs(vals[0]-Cminus) < 1e-10

print("PASS QFORM_MONOTONE_CORE_MINUS_SQUARE_GLOBAL")
print(f"C_minus={Cminus:.15f}")
print(f"97/24={97/24:.15f}")
print(f"partner_theta_0.01={partner:.15f}")
print(f"partner_minus_C_minus={partner-Cminus:.15f}")
print("exact_square_checks: 9409 < 10368; 648 > 625")
print("negative_level_samples=" + ",".join(f"{v:.12f}" for v in vals))
