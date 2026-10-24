from fractions import Fraction
from math import factorial

# R07 / I0077: exact rational arithmetic supporting the canonical
# two-width log-periodic Floquet-budget example.
#
# Analytic inputs proved on the report page:
#   lambda_c >= pi^2 exp(-c^2/2)/(8 c^2),
#   lambda_c <= pi^2 exp(c^2/2)/(8 c^2),
#   pi^2 > 493/50, pi^2 < 10,
#   exp(-x) > sum_{k=0}^5 (-x)^k/k! for 0<x<1,
#   exp(1/8) < 1/(1-1/8)=8/7.

pi2_lb = Fraction(493, 50)
a = Fraction(1, 2)
b = Fraction(6, 5)
x = Fraction(18, 25)  # b^2/2

exp_b_lb = sum(
    (Fraction(-1, 1) ** k) * x**k / Fraction(factorial(k), 1)
    for k in range(6)
)

# exp(-1/8) > 1-1/8 = 7/8.
lambda_a_lb = pi2_lb * Fraction(7, 8) / (8 * a * a)
lambda_b_lb = pi2_lb * exp_b_lb / (8 * b * b)

narrow = Fraction(3, 20)
rest = Fraction(17, 20)
weighted_lb = narrow * lambda_a_lb + rest * lambda_b_lb

# Old single-threshold pulse route: for any threshold c<6/5 the
# longest below-threshold phase interval is at most 17/100, while
# lambda_c <= lambda_{1/2} < 40/7.
lambda_half_ub = Fraction(40, 7)
max_subwide_duty = Fraction(17, 100)
old_route_ub = max_subwide_duty * lambda_half_ub

# Profile pieces: narrow plateau, up-ramp, wide plateau, down-ramp.
assert narrow + Fraction(1, 100) + Fraction(83, 100) + Fraction(1, 100) == 1
assert exp_b_lb == Fraction(23758643, 48828125)
assert lambda_a_lb == Fraction(3451, 800)
assert lambda_b_lb == Fraction(11713010999, 28125000000)
assert weighted_lb == Fraction(563093843233, 562500000000)
assert weighted_lb - 1 == Fraction(593843233, 562500000000)
assert weighted_lb > 1
assert old_route_ub == Fraction(34, 35)
assert old_route_ub < 1

print(f"exp(-18/25) rational lower bound = {exp_b_lb}")
print(f"lambda_(1/2) rational lower bound = {lambda_a_lb}")
print(f"lambda_(6/5) rational lower bound = {lambda_b_lb}")
print(f"weighted spectral budget lower bound = {weighted_lb}")
print(f"exact gap above 1 = {weighted_lb - 1}")
print(f"old single-threshold route upper bound below width 6/5 = {old_route_ub}")
print("SELF-CHECK PASS")
