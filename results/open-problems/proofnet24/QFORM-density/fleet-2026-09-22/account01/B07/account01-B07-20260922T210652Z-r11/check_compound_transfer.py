from fractions import Fraction
from itertools import combinations
from math import exp, sqrt
import random


def e(xs, k):
    out = Fraction(0, 1)
    for I in combinations(range(len(xs)), k):
        p = Fraction(1, 1)
        for i in I:
            p *= xs[i]
        out += p
    return out

random.seed(20260922)
checks = 0
worst = None
for r in range(3, 11):
    coeff = Fraction(9, 2) * Fraction(r * (r - 1), (r - 2) ** 2)
    for _ in range(250):
        xs = [Fraction(random.randint(0, 11), random.randint(1, 9)) for _ in range(r)]
        e3 = e(xs, 3)
        if e3 == 0:
            continue
        e2 = e(xs, 2)
        assert e2 ** 3 >= coeff * e3 ** 2
        ratio = float(e2 ** 3 / (coeff * e3 ** 2))
        if worst is None or ratio < worst[0]:
            worst = (ratio, r)
        checks += 1

c2 = float(Fraction(9, 2) * Fraction(1, 256 ** 2)) ** (1 / 3)
Cstar = 48 * sqrt(exp(1)) * (24 / 23) ** 0.25
half_riesz = Cstar * c2 ** (-1 / 8)

print(f"exact_rational_checks={checks}")
print(f"worst_normalized_ratio={worst[0]:.15f} at rank={worst[1]}")
print(f"c2={c2:.15f}")
print(f"c2_over_2={c2/2:.15f}")
print(f"c2_over_8={c2/8:.15f}")
print(f"half_riesz_constant={half_riesz:.15f}")
assert c2 > 1 / 25
assert c2 / 2 > 1 / 50
assert c2 / 8 > 1 / 200
assert half_riesz < 120
print("STATUS=QFORM_COMPOUND_ORDER_TRANSFER_CHECK_PASS")
