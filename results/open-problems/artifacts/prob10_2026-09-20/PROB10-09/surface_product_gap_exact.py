#!/usr/bin/env python3
"""Exact arithmetic certificate for PROB10-09 surface-group product route.

Finite arithmetic only. This does not certify the group-theoretic Magnus
Freiheitssatz input or the archived percolation/operator lemmas; those are
proved on the report page. It certifies the rational/radical inequalities used
there.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

p = Fraction(3, 50)
L = 1 - (1-p) * (1-p*p)**10
branch_margin = 13*L - 1
assert branch_margin > 0

# beta = 5 + sqrt(13) + sqrt(11+10*sqrt(13)) < 50/3.
# Since 35/3-sqrt(13)>0, squaring reduces this exactly to
# 300*sqrt(13) < 1243, which follows after another positive squaring from:
radical_beta_margin = 1243**2 - 13*(300**2)
assert radical_beta_margin > 0

# The coarse all-walk bound 1/(10+2*sqrt(13)) is BELOW p=3/50.
# Equivalently (3/50)(10+2sqrt(13))>1, or 3sqrt(13)>10.
allwalk_failure_margin = 9*13 - 10**2
assert allwalk_failure_margin > 0

# Optional exact exclusion of the normalized-spectral-radius < 1/2 sufficient
# class for this standard product graph. Infinite 12- and 16-regular factors
# have adjacency norms at least 2sqrt(11), 2sqrt(15), so the product norm is
# at least 2(sqrt(11)+sqrt(15)) > 14. The final inequality is equivalent to
# 4*165 > 23^2 after one positive squaring.
rho_half_exclusion_margin = 4*165 - 23**2
assert rho_half_exclusion_margin > 0

getcontext().prec = 60
s13 = Decimal(13).sqrt()
beta = Decimal(5) + s13 + (Decimal(11) + Decimal(10)*s13).sqrt()
inv_beta = Decimal(1) / beta
gap = inv_beta - Decimal(3)/Decimal(50)
rho_upper = Decimal(10) + Decimal(2)*s13
allwalk_lower = Decimal(1)/rho_upper

print("PROB10-09 exact arithmetic certificate")
print(f"p0={p.numerator}/{p.denominator}")
print(f"L(p0)={L.numerator}/{L.denominator}")
print(f"13L(p0)-1={branch_margin.numerator}/{branch_margin.denominator}")
print("branching_strict=PASS")
print(f"beta_radical_square_margin={radical_beta_margin}")
print("beta_lt_50_over_3=PASS")
print(f"allwalk_failure_square_margin={allwalk_failure_margin}")
print("one_over_rho_upper_lt_3_over_50=PASS")
print(f"rho_half_exclusion_square_margin={rho_half_exclusion_margin}")
print("normalized_rho_not_lt_half=PASS")
print(f"beta_decimal={beta}")
print(f"one_over_beta_decimal={inv_beta}")
print(f"certified_gap_decimal={gap}")
print(f"rho_upper_decimal={rho_upper}")
print(f"allwalk_lower_decimal={allwalk_lower}")
print("VERDICT=PASS_EXACT_ARITHMETIC_CORE")
print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BENJAMINI_SCHRAMM")
