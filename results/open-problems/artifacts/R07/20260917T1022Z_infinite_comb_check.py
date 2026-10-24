from fractions import Fraction

# Exact finite self-check for the canonical normalized comb
# D = union_{k in Z} [3k-1/4, 3k+1/4].
# Each component has length d=1/2 and each gap has length 5/2.
# The analytic proof uses the ground-state/Poincare bound
#   lambda_0(a,b) >= pi^2/(2 d^2) - 1/4.
# With the classical rational inequality pi^2 > 9, this gives
#   lambda_0 > 9/(2 d^2) - 1/4 = 71/4 > 1.

d = Fraction(1, 2)
gap = Fraction(5, 2)
lambda_lower_using_pi2_gt_9 = Fraction(9, 1) / (2 * d * d) - Fraction(1, 4)

assert d == Fraction(1, 2)
assert gap == Fraction(5, 2)
assert lambda_lower_using_pi2_gt_9 == Fraction(71, 4)
assert lambda_lower_using_pi2_gt_9 > 1

print(f"component_length={d}")
print(f"gap_length={gap}")
print(f"lambda_lower_using_pi2_gt_9={lambda_lower_using_pi2_gt_9}")
print("PASS")
