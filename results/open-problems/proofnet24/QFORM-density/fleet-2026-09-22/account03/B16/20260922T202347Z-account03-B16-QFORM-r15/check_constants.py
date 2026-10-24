from fractions import Fraction
from math import sqrt

# Determinant contradiction in Case B.
coef = Fraction(1, 8) + 2 * Fraction(9, 16) ** 3 + 3 * Fraction(1, 2) * Fraction(9, 16) ** 2
assert coef == Fraction(1957, 2048)
assert coef < 1

# The selected 2x2 physical pair is indefinite.
pair_margin = Fraction(1, 4) - Fraction(81, 256)
assert pair_margin == -Fraction(17, 256)
assert pair_margin < 0

# Constants after the scalar-pivot and pair branches.
C_main = 16 * sqrt(30) * 2 ** 0.25
C_pair = 16 * sqrt(5)
assert C_main < 105
assert C_pair < 36
assert C_pair < C_main

print(f"determinant_coefficient={coef}={float(coef):.12f}")
print(f"pair_determinant_margin={pair_margin}={float(pair_margin):.12f}")
print(f"C_main={C_main:.15f}")
print(f"C_pair={C_pair:.15f}")
print("STATUS=PASS")
