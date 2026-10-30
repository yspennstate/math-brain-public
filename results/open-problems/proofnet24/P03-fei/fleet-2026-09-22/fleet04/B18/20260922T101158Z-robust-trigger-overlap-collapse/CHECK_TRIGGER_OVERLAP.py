from fractions import Fraction
import math

eta = Fraction(1, 16)
trigger_factor = Fraction(1, 1) / (2 * (1 - 2 * eta))
weight_floor = Fraction(44, 7)
visible = trigger_factor * 2 / weight_floor
hidden = trigger_factor / weight_floor
mass_visible = visible / 3
mass_hidden = hidden / 3

assert trigger_factor == Fraction(4, 7)
assert visible == Fraction(2, 11)
assert hidden == Fraction(1, 11)
assert mass_visible == Fraction(2, 33)
assert mass_hidden == Fraction(1, 33)

j_coefficient = 4.0 / (33.0 * math.log(2.0))

print(f"trigger_factor={trigger_factor}")
print(f"address_visible={visible}")
print(f"address_hidden={hidden}")
print(f"mass_visible={mass_visible}")
print(f"mass_hidden={mass_hidden}")
print(f"J_coefficient={j_coefficient:.15f}")
print("PASS")
