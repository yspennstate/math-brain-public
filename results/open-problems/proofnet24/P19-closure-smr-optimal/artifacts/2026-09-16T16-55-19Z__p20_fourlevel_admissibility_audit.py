from fractions import Fraction

# Independent exact-arithmetic audit of P20 claim
# P20-I0081-FOURLEVEL-ADMISSIBLE-06.
# Scope: normalization and the exact symmetric log-unimodal staircase only.
# This does NOT audit P20's interval-certified eight-mode conclusion,
# physical subordination branch, or current-prior-art claim.

weights = [500, 1500, 500, 1]
radii = [10, 20, 28, 50]
den = 98100

# Indicator representation:
# h(y) = sum_j weights[j]/den * 1_{[-radii[j],radii[j]]}(y).
indicator_mass_numerator = 2 * sum(r*w for r, w in zip(radii, weights))
assert indicator_mass_numerator == den

# The four plateau heights obtained by summing nested indicators.
plateau_nums = [
    sum(weights),
    sum(weights[1:]),
    sum(weights[2:]),
    sum(weights[3:]),
]
assert plateau_nums == [2501, 2001, 501, 1]
assert plateau_nums[0] > plateau_nums[1] > plateau_nums[2] > plateau_nums[3] > 0

# Direct plateau-width normalization: widths are 20,20,16,44.
widths = [20, 20, 16, 44]
plateau_mass = sum(Fraction(width*n, den) for width, n in zip(widths, plateau_nums))
assert plateau_mass == 1

# Evenness is built into the nested symmetric intervals; strict decrease in |y|
# proves log-unimodality with mode 0. Exponentiation then gives multiplicative
# symmetry and mode 1 for the positive-line input law.

print(f"indicator_mass_numerator={indicator_mass_numerator}")
print(f"denominator={den}")
print(f"plateau_numerators={plateau_nums}")
print(f"plateau_mass={plateau_mass}")
print("strict_decrease=True")
print("P19-AUDIT-P20-FOURLEVEL-ADMISSIBILITY-16 PASS")
