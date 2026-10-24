from fractions import Fraction
from math import exp

# Deterministic regression checks for
# QFORM-PLUCKER-SCHUR-PROJECTED-CROSSING-v1.
# No external packages.

V_h2 = Fraction(1, 8)
V_3 = Fraction(1, 8)
det_lambda_sq = 900
S_sq = Fraction(1, 1)
Z_2 = Fraction(225, 16)

assert S_sq * Z_2 == det_lambda_sq * V_h2 * V_3

# Four nonzero hub-pair weights, each 1/32; every one of the four
# I-rows belongs to exactly two such pairs.
pair_weight = Fraction(1, 32)
V_total = 4 * pair_weight
assert V_total == V_h2
alpha = (2 * pair_weight) / V_total
assert alpha == Fraction(1, 2)

C1 = 3 * 2 ** (7 / 6) * exp(1 / 3)
C2 = 3 * 2 ** (5 / 6)
bound_example = C1 * 30 ** (-1 / 3) * float(V_h2 * V_3) ** (-1 / 6)
partner_bound = 9.2002740353 * (64 * 1728 / 61) ** (1 / 5)

assert C1 < 9.4
assert C2 < 5.346
assert bound_example < 6.05
assert partner_bound < 41.256

print(f"V_h2={V_h2} V_3={V_3} S2={S_sq} Z2={Z_2}")
print(f"identity={S_sq * Z_2} alpha={alpha}")
print(f"C1={C1:.12f} C2={C2:.12f}")
print(f"example_bound={bound_example:.12f}")
print(f"partner_bound={partner_bound:.12f}")
print("STATUS=PASS")
