from fractions import Fraction
from math import factorial


def exp_upper(q, n):
    q = Fraction(q)
    partial = sum((q**j) / factorial(j) for j in range(n + 1))
    first = (q**(n + 1)) / factorial(n + 1)
    ratio = q / Fraction(n + 2, 1)
    assert ratio < 1
    return partial + first / (1 - ratio)


c = Fraction(7, 100)
ec_up = exp_upper(c, 12)

checks = [
    ("exp(7/100)<43/40", Fraction(43, 40) - ec_up),
    (
        "two-cap capacity margin",
        2 * (1 - 17 * Fraction(3, 200)) - Fraction(41, 40),
    ),
    ("N12 second-heavy lower minus 250", Fraction(3272, 13) - 250),
    ("N13 second-heavy lower minus 250", Fraction(3749, 13) - 250),
    (
        "e^c Umax < 121s/100 margin coefficient",
        Fraction(121, 100) - Fraction(43, 40) * Fraction(9, 8),
    ),
    (
        "case r<=e margin",
        1
        - 4
        * Fraction(121, 100)
        * Fraction(3, 200)
        * Fraction(41, 5),
    ),
    (
        "A^5 > 20s^4 at s=3/200",
        Fraction(2, 25) ** 5 - 20 * Fraction(3, 200) ** 4,
    ),
    ("40/19 > 121/100", Fraction(40, 19) - Fraction(121, 100)),
]

print("exp_upper_7_100 =", ec_up)
for name, margin in checks:
    assert margin > 0, (name, margin)
    print("PASS", name, "margin =", margin)

print("ALL_EXACT_CHECKS_PASS")
