from fractions import Fraction
import math

alpha = Fraction(157, 320)
sigma = Fraction(3, 16)
partner_tau = Fraction(1, 8)

pivot_onecross = 8 / math.sqrt(float(alpha * sigma))
partner_triangle = 2 * (3 + math.log(8)) * float(sigma * partner_tau * partner_tau) ** (-1/3)
triangle_prefactor = 2 * (3 + math.log(8))

S11 = Fraction(49, 100)
S12 = Fraction(1, 5)
S22 = Fraction(4, 49)
det = S11 * S22 - S12 * S12

print(f"onecross_heavy_pivot={pivot_onecross:.15f}")
print(f"partner_triangle_scale={partner_triangle:.15f}")
print(f"partner_triangle_prefactor={triangle_prefactor:.15f}")
print(f"regression_det={det}")
print(f"regression_diag1={float(S11):.15f}")
print(f"regression_diag2={float(S22):.15f}")
print(f"regression_cross={float(S12):.15f}")
print(f"3/16={3/16:.15f}")
