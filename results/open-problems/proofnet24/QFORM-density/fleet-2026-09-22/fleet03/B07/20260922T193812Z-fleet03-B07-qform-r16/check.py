from fractions import Fraction
from math import factorial


def net_factor(k: int) -> Fraction:
    rainbow = Fraction(factorial(k), k**k) ** 2
    matching_divisor = factorial(k) ** 2
    return rainbow / matching_divisor

assert net_factor(2) == Fraction(1, 16)
assert net_factor(3) == Fraction(1, 729)
assert Fraction(1, 48) * net_factor(2) == Fraction(1, 768)
assert Fraction(1, 256) * net_factor(3) == Fraction(1, 186624)
assert Fraction(1, 186624) / Fraction(1, 3981312) == Fraction(64, 3)
assert Fraction(6, 27) ** 2 * Fraction(1, 256) == Fraction(1, 5184)

print("QFORM_B07_R16_CHECK_PASS")
print("k2_net", net_factor(2))
print("k3_net", net_factor(3))
print("S0_matching", Fraction(1, 768))
print("O0_matching", Fraction(1, 186624))
print("improvement_factor_vs_older_heavy_cascade", Fraction(64, 3))
