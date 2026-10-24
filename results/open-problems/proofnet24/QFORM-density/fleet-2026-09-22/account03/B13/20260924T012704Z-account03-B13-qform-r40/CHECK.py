from fractions import Fraction
import math
import random

# Deterministic exact-arithmetic check of Theorem 3.1.
rng = random.Random(13040)
for _ in range(1000):
    ti, tj, tl, tm = [Fraction(rng.randint(-20, 20), rng.randint(1, 10)) for _ in range(4)]
    dk = Fraction(rng.randint(1, 10), rng.randint(1, 10))
    c = Fraction(rng.randint(1, 10), rng.randint(1, 10))
    ri, rj, rl, rm = [Fraction(rng.randint(-20, 20), rng.randint(1, 10)) for _ in range(4)]

    def G(a, b, ra, rb):
        return dk * (a - b) ** 2 + c * (ra + rb)

    lhs = G(ti, tj, ri, rj) + G(tl, tm, rl, rm) - G(ti, tl, ri, rl) - G(tj, tm, rj, rm)
    rhs = -2 * dk * (ti - tm) * (tj - tl)
    assert lhs == rhs

# Constant checks used in Sections 4-5.
CT = 759375 / 2
H0_sq = 1536 * math.e**2
H0 = math.sqrt(H0_sq)
K0 = 2 * CT / H0_sq
cluster_constant = 48 * math.sqrt(K0)

assert abs(K0 - 253125 / (512 * math.e**2)) < 1e-13
assert 106.5344 < H0 < 106.5345
assert 66.9077 < K0 < 66.9078
assert 392.6262 < cluster_constant < 392.6263

# The singular-value implication Delta=sigma1^2 sigma2^2 >= sigma2^4
# is checked over a deterministic grid with sigma1>=sigma2>=0.
for a in range(51):
    for b in range(a + 1):
        sigma1 = Fraction(a, 10)
        sigma2 = Fraction(b, 10)
        Delta = sigma1**2 * sigma2**2
        assert Delta >= sigma2**4

print(f"H0={H0:.15f}")
print(f"K0={K0:.15f}")
print(f"48sqrtK0={cluster_constant:.15f}")
print("QFORM_B13_R40_SLOPE_CLUSTER_CHECK_PASS")
