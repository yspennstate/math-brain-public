from fractions import Fraction
from math import sqrt, e
import random

c3 = Fraction(11907, 16384)
x2_lb = c3 / 64
a = Fraction(1, 4096)
kappa0 = x2_lb / (x2_lb + a)
top2_lb = 2 * kappa0
eta0 = Fraction(9, 4) - top2_lb
T0 = a * eta0 / (1 - eta0)
lev0 = Fraction(1, 2) - eta0
ratio0 = T0 / x2_lb

assert kappa0 == Fraction(11907, 12163)
assert top2_lb == Fraction(23814, 12163)
assert eta0 == Fraction(14211, 48652)
assert T0 == Fraction(14211, 141070336)
assert lev0 == Fraction(10115, 48652)
assert ratio0 == Fraction(404224, 45565443)

# Pairwise ridge-sum superadditivity used in Lemma 5.1.
for _ in range(10000):
    aa = 10 ** random.uniform(-5, 2)
    x = 10 ** random.uniform(-8, 3)
    y = 10 ** random.uniform(-8, 3)
    lhs = x/(aa+x) + y/(aa+y)
    rhs = (x+y)/(aa+x+y)
    assert lhs + 1e-14 >= rhs

# Random tail packs: whenever total ridge contribution is below eta0,
# the total tail energy must be below T0. This tests the exact inversion.
eta0f = float(eta0)
T0f = float(T0)
af = float(a)
for _ in range(10000):
    m = random.randint(1, 25)
    ys = [10 ** random.uniform(-10, -2) for _ in range(m)]
    eta = sum(y/(af+y) for y in ys)
    if eta < eta0f:
        assert sum(ys) < T0f * (1 + 1e-12)

print("QFORM_B06_R39_RIDGE_TAIL_CHECK_PASS")
print("c3", float(c3))
print("x2_lb", float(x2_lb))
print("kappa0", float(kappa0))
print("top2_trace_lb", float(top2_lb))
print("eta0", float(eta0))
print("tail_energy_cap", float(T0))
print("rank2_F_distance_cap", sqrt(float(T0)))
print("low_trace_top2_physical_leverage_lb", float(lev0))
print("tail_to_x2_ratio_cap", float(ratio0))
print("q2_density_constant", 288*sqrt(e))
print("q1_density_constant", 288*sqrt(2*e))
