from fractions import Fraction
import math

# Exact ledger for the concrete example in Section 4.
# On span(e1,e3), (I+4nn^T)D has matrix [[3,-2],[2,-3]].
trace = 3 + (-3)
det = 3*(-3) - (-2)*2
assert trace == 0 and det == -5

# Row caps: p=1/2 and q in {1/4,1/2}.
assert Fraction(1,2) + Fraction(1,4) <= 1
assert Fraction(1,2) + Fraction(1,2) <= 1

# Mixed score and constants.
r = 2.0
Z = 2*r
assert Z == 4.0
exact_constant = 3*math.e/Z**(1/3)
uniform_constant = 3*math.e*(5/4)**(1/3)
assert abs(exact_constant - 5.137230742833414) < 1e-12
assert uniform_constant < 8.785

print("checks passed", exact_constant, uniform_constant)
