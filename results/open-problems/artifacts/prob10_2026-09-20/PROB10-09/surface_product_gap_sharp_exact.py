#!/usr/bin/env python3
"""Final exact arithmetic certificate for PROB10-09 surface-product iteration.

The report proves the group-theoretic and percolation/operator lemmas. This
script checks only the finite rational/radical inequalities used by that proof.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

# Sharpened percolation comparison point, found after the idea-before-code pass.
p = Fraction(13, 251)
L = 1 - (1-p) * (1-p*p)**10
branch_margin = 13*L - 1
assert branch_margin > 0

# Uniform radical certificate retained from the exploratory check:
# beta = 5 + sqrt(13) + sqrt(11+10sqrt(13)) < 50/3.
# After two sign-safe squarings this is 13*300^2 < 1243^2.
beta_square_margin = 1243**2 - 13*(300**2)
assert beta_square_margin > 0

# Hence p*beta < (13/251)*(50/3)=650/753 < 1.
pbeta_rational_margin = 753 - 650
assert pbeta_rational_margin > 0

# Coarse method-isolation point p*=3/50: ordinary adjacency resolvent does not
# bridge this point, while beta<50/3 implies the NB lower bound does.
# (3/50)(10+2sqrt13)>1 <=> 3sqrt13>10.
allwalk_coarse_failure_margin = 9*13 - 10**2
assert allwalk_coarse_failure_margin > 0

# Optional check excluding the normalized-rho <1/2 sufficient class for the
# standard 28-regular product graph: 2(sqrt11+sqrt15)>14.
# Equivalent after sign-safe squaring to 4*165 > 23^2.
rho_half_exclusion_margin = 4*165 - 23**2
assert rho_half_exclusion_margin > 0

getcontext().prec = 70
s13 = Decimal(13).sqrt()
beta = Decimal(5) + s13 + (Decimal(11) + Decimal(10)*s13).sqrt()
inv_beta = Decimal(1) / beta
p_dec = Decimal(13)/Decimal(251)
gap = inv_beta - p_dec
rho_upper = Decimal(10) + Decimal(2)*s13
allwalk_lower = Decimal(1)/rho_upper

print("PROB10-09 sharp exact arithmetic certificate")
print(f"p0={p.numerator}/{p.denominator}")
print(f"L(p0)={L.numerator}/{L.denominator}")
print(f"13L(p0)-1={branch_margin.numerator}/{branch_margin.denominator}")
print("branching_strict=PASS")
print(f"beta_square_margin={beta_square_margin}")
print("beta_lt_50_over_3=PASS")
print(f"pbeta_rational_margin={pbeta_rational_margin}")
print("p0_times_beta_lt_1=PASS")
print(f"allwalk_coarse_failure_margin={allwalk_coarse_failure_margin}")
print("coarse_point_allwalk_fails=PASS")
print(f"rho_half_exclusion_square_margin={rho_half_exclusion_margin}")
print("normalized_rho_not_lt_half=PASS")
print(f"p0_decimal={p_dec}")
print(f"beta_decimal={beta}")
print(f"one_over_beta_decimal={inv_beta}")
print(f"certified_gap_decimal={gap}")
print(f"rho_upper_decimal={rho_upper}")
print(f"allwalk_lower_decimal={allwalk_lower}")
print("VERDICT=PASS_EXACT_ARITHMETIC_CORE_SHARP")
print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BENJAMINI_SCHRAMM")
