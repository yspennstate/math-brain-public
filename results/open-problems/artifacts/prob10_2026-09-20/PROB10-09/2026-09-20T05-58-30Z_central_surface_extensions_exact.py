#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext

# PROB10-09 exact finite core:
# standard non-split Z-central extensions of closed surface groups.
# This checks the genus-2 numerical/rational certificate and the elementary
# all-genus comparison. The direct-integral/magnetic domination and subgroup
# splitting arguments are written proofs in the substantive report.

# Genus 2 critical-side witness from T_6 square Z.
p0 = Fraction(31, 200)
phi_z = 1 - (1 - p0) ** 3 / (1 - p0 + p0 * p0) ** 2
offspring_excess = 5 * phi_z - 1

# Published rigorous Nagnibeda upper bound ||M_2|| <= 0.662816.
rho2 = Fraction(662816, 10**6)
A_surface2 = 8 * rho2
R2 = A_surface2 + 2
D2 = 10
Q2 = D2 - 1
disc2 = R2 * R2 - 4 * Q2

# Reduce discriminant to N / 15625^2.
N = 4230203904
assert disc2 == Fraction(N, 15625**2)

# beta^{-1} = (R - sqrt(R^2-4Q))/(2Q)
# = (114102 - sqrt(N))/281250.
# Certify p0 < beta^{-1} by positive-side squaring:
# sqrt(N) < 282033/4.
square_margin = 282033**2 - 16 * N

# All-g>=3 comparison:
# p_c <= 1/(4g-3), while p_2->2 > 1/(4 sqrt(g)+2)
# from Zuk ||M_g|| <= 1/sqrt(g).
# Need 4 sqrt(g)+2 < 4g-3, i.e. 4 sqrt(g) < 4g-5.
# Squaring gives f(g)=(4g-5)^2-16g >0.
f3 = (4*3 - 5)**2 - 16*3
# General difference f(g+1)-f(g)=32g-40, positive for g>=3.
general_diff_at_3 = 32*3 - 40

getcontext().prec = 80
sqrtN = Decimal(N).sqrt()
p2_lower = (Decimal(114102) - sqrtN) / Decimal(281250)
gap_lower = p2_lower - Decimal(31) / Decimal(200)

checks = {
    "fiber_offspring_excess_positive": offspring_excess > 0,
    "surface_adj_bound_identity": A_surface2 == Fraction(82852, 15625),
    "central_adj_bound_identity": R2 == Fraction(114102, 15625),
    "disc_identity": disc2 == Fraction(N, 15625**2),
    "p0_lt_p2_floor_square_margin_positive": square_margin > 0,
    "genus3_squared_margin_positive": f3 > 0,
    "all_genus_margin_increasing_from_g3": general_diff_at_3 > 0,
    "display_gap_positive": gap_lower > 0,
}

print("PROB10-09 CENTRAL SURFACE EXTENSION EXACT CORE")
print("p0 =", p0, "decimal =", f"{float(p0):.12f}")
print("phi_Z(p0) =", phi_z)
print("5*phi_Z(p0)-1 =", offspring_excess)
print("rho2_upper =", rho2, "decimal =", f"{float(rho2):.6f}")
print("A_surface2_upper =", A_surface2)
print("R2_upper =", R2, "decimal =", f"{float(R2):.12f}")
print("disc2 =", disc2)
print("disc_numerator_N =", N)
print("p0_lt_p2_square_margin =", square_margin)
print("p2_lower_numeric =", p2_lower)
print("gap_lower_numeric =", gap_lower)
print("gap_exact_form = (282033 - 4*sqrt(4230203904))/1125000")
print("f(3) =", f3)
print("f(g+1)-f(g) = 32g-40; at g=3 =", general_diff_at_3)
print("checks =", checks)
print("VERDICT =", "ALL_EXACT_CHECKS_PASS" if all(checks.values()) else "FAIL")
