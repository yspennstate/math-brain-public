from fractions import Fraction

# Exact finite arithmetic used in the canonical disconnected-fan example.
# The analytic inputs (OU Rayleigh formula, lambda_0(-1,1)=1, strict domain
# monotonicity) are proved/cited in the accompanying R07 report and are not
# replaced by this checker.

A = Fraction(5, 1)
lower_bound = A*A/Fraction(8, 1) - Fraction(1, 4)
expected = Fraction(23, 8)

assert lower_bound == expected
assert lower_bound > 1
assert lower_bound - 1 == Fraction(15, 8)

# The convex hull of [-6,-5] U [5,6] is [-6,6], which strictly contains
# the critical source interval [-1,1]. These integer comparisons are exact.
assert Fraction(-6,1) < Fraction(-1,1) < Fraction(1,1) < Fraction(6,1)

print("PASS")
print(f"component_OU_lower_bound={lower_bound}")
print(f"gap_above_1={lower_bound - 1}")
print("convex_hull_strictly_contains_source_critical_interval=True")
