from fractions import Fraction

# Exact self-check for the rational constants in the R09 G0013
# higher-Jacobi-mode refinement.  The analytic inequalities themselves
# are proved in the accompanying immutable run report.

s0 = Fraction(2221, 20000)
L0 = Fraction(1663, 30000)
h0 = Fraction(11, 480000)
Crat = Fraction(97, 100)

# Bookkeeping identities used in the contradiction argument.
assert L0 == 2 * s0 - Fraction(1, 6)
assert s0 == Fraction(1, 9) - Fraction(8, 3) * h0

# C = (7/24) * 36^(1/3) < 97/100.
# Both sides are positive, so cubing is exact and order-preserving.
lhs_C3 = Fraction(7**3 * 36, 24**3)
rhs_C3 = Crat**3
assert lhs_C3 < rhs_C3

# Need
#   1/36 + (97/100) h0^(1/3) + h0 < L0.
# Rearrange to h0^(1/3) < R and cube (R>0).
R = (L0 - Fraction(1, 36) - h0) / Crat
assert R > 0
assert h0 < R**3

print("R09 G0013 HIGHER-MODE RATIONAL SELF-CHECK")
print(f"s0 = {s0} = {float(s0):.12f}")
print(f"1/9 - s0 = {Fraction(1,9)-s0} = {float(Fraction(1,9)-s0):.12f}")
print(f"L0 = 2*s0-1/6 = {L0}")
print(f"h0 = {h0}")
print(f"C^3 upper comparison: {lhs_C3} < {rhs_C3}")
print(f"R = {R}")
print(f"R^3 - h0 = {R**3-h0}")
print("SELF_CHECK_ONLY / PASS")
