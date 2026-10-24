from fractions import Fraction
from math import pow

L0 = Fraction(6221, 6450)
tail = Fraction(3, 200)
hprod = Fraction(4, 5)
c_minor = hprod * (L0 / 2 - tail)
assert c_minor == Fraction(2411, 6450)

outside_leverage = Fraction(1, 2) + (1 - L0)
assert outside_leverage == Fraction(1727, 3225)

C_square = 8 * pow(2.0, 0.25) / pow(3.0, 0.25) * pow(float(c_minor), -0.25)
assert C_square < 9.25

print(f"L0={float(L0):.15f}")
print(f"tail_ratio_bound={float(tail):.15f}")
print(f"physical_minor_coefficient={c_minor}={float(c_minor):.15f}")
print(f"wedge_diffuse_top2_outside_anchor_cap={outside_leverage}={float(outside_leverage):.15f}")
print(f"outer_square_constant={C_square:.15f}")
print("STATUS=PASS")
