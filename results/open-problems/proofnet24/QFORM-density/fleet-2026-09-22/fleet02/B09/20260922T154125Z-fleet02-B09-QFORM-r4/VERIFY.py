from fractions import Fraction
import math

# Target-valid stress family effective 3x3 matrix:
# Q = 2(Z+U+V)^2 + 10 U V + V^2.
# Characteristic polynomial is x^3 - 7 x^2 - 41 x + 50.
def p(x):
    x = Fraction(x)
    return x**3 - 7*x**2 - 41*x + 50

for x in (-5, -4, 1, 2, 10, 11):
    print(f"p({x})={p(x)}")

# Signs certify roots in (-5,-4), (1,2), and (10,11), hence three |lambda|>1.
assert p(-5) < 0 < p(-4)
assert p(1) > 0 > p(2)
assert p(10) < 0 < p(11)

# New p=4 rank-one-one-sided-cross + dependent-square constant.
base = 2**(17/6) * math.sqrt(3)
new_stress = base / math.sqrt(10)  # outer pivot a=2, rank-one cross singular value s=5

# Named partner fleet03/B09, applied to no-shear baseline 10 U V + 2 Z^2.
partner_baseline = 8 * math.sqrt(2) / math.sqrt(5*2)

print(f"base_constant={base:.15f}")
print(f"new_stress_bound={new_stress:.15f}")
print(f"partner_baseline_bound={partner_baseline:.15f}")
print("PASS")
