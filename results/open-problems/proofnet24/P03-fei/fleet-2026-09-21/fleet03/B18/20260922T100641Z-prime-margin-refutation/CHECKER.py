#!/usr/bin/env python3
"""Exact arithmetic checker for the source-exact prime-margin separation.

Inputs are the certified coarse defect bracket and exact Poincare currency from
the source-bound Numaro report, plus the certified c=0.01 read-once margin.
"""

from fractions import Fraction

A0 = Fraction(268204856, 10**9)
M = Fraction(62098577, 239075328)
# Certified: -0.038023735 < D_dagger < -0.038023734.
DELTA_LO = Fraction(38023734, 10**9)  # -D_dagger > this
DELTA_HI = Fraction(38023735, 10**9)  # -D_dagger < this
AND_CERT = Fraction(1, 100)
C0 = Fraction(64548, 10000)

c_lo = A0 + DELTA_LO / M
c_hi = A0 + DELTA_HI / M
center_lo = C0 + c_lo / 4

print("PRIME_MARGIN_REFUTATION_CHECK")
print("M_exact=", M)
print("c_Numaro_lower_exact=", c_lo)
print("c_Numaro_lower_decimal=", f"{float(c_lo):.15f}")
print("c_Numaro_upper_from_coarse_bracket=", f"{float(c_hi):.15f}")
print("AND_readonce_cert_upper=", f"{float(AND_CERT):.15f}")
print("separation_factor_lower=", f"{float(c_lo / AND_CERT):.12f}")
print("quadratic_center_lower=", f"{float(center_lo):.15f}")

assert c_lo > Fraction(4145936641982, 10**13)
assert c_lo > AND_CERT
assert c_lo / AND_CERT > 41
assert center_lo > Fraction(6558448416049, 10**12)
print("PASS")
