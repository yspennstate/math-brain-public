from fractions import Fraction
import math

sqrt3_upper = Fraction(26, 15)
assert sqrt3_upper**2 > 3

stage2_upper = (
    Fraction(1, 9)
    + Fraction(1, 64)
    + 4 * (Fraction(13, 45) + Fraction(1, 64)) ** 2
)
assert stage2_upper < Fraction(1, 2)

two_leaf_mass = Fraction(31, 64) + Fraction(1, 9)
assert two_leaf_mass == Fraction(343, 576)

one_hub_bound = 12 * 128 ** (1 / 3)
two_hub_bound = 12 * 512 ** (1 / 3)
partner_bound = 128 / math.sqrt(1 / 4096)

assert one_hub_bound < 60.477
assert abs(two_hub_bound - 96) < 1e-10
assert partner_bound == 8192

print(f"sqrt3 upper square = {float(sqrt3_upper**2):.12f} > 3")
print(f"stage2 upper = {stage2_upper} = {float(stage2_upper):.12f} < 1/2")
print(f"two-leaf longitudinal mass > {two_leaf_mass} = {float(two_leaf_mass):.12f}")
print(f"one-hub medium-collar bound = {one_hub_bound:.12f} < 60.477")
print(f"two-hub moderate bound = {two_hub_bound:.12f} = 96")
print(f"partner diagonal-threshold bound = {partner_bound:.1f}")
print("STATUS=PASS")
