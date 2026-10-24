from fractions import Fraction
from itertools import product

# Fixture 1: exact partition bound in Theorem 3.1(B).
lam = Fraction(3, 5)
a2 = [lam / 4] * 4
z2 = [Fraction(1, 4)] * 4
dstar = max(z2)
required = lam * (1 - dstar) / 4
best = Fraction(0)
best_mask = None
for mask in product([0, 1], repeat=4):
    ay = sum((a2[k] for k in range(4) if mask[k]), Fraction(0))
    zz = sum((z2[k] for k in range(4) if not mask[k]), Fraction(0))
    val = ay * zz
    if val > best:
        best, best_mask = val, mask
assert best == Fraction(3, 20)
assert required == Fraction(9, 80)
assert best >= required

# Fixture 2: exact coloop collar at eta=1/16.
eta = Fraction(1, 16)
c = h = Fraction(31, 32)
rho2 = Fraction(0)
P11 = 1 - c - rho2
P22 = 1 - h
lam2 = max(P11, P22)
pair_mass = c * h
assert lam2 == Fraction(1, 32) < eta
assert pair_mass == Fraction(961, 1024)
assert pair_mass > 1 - 4 * eta == Fraction(3, 4)

print("fixture1_best=", best, "required=", required, "mask=", best_mask)
print("fixture2_lambda=", lam2, "pair_mass=", pair_mass, "threshold=", 1 - 4 * eta)
