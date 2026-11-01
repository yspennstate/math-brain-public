from fractions import Fraction

# Independent exact-arithmetic audit core for
# P19-AUDIT-P20-I0081-LOGUNIFORM-ENDTOEND-19.
# The analytic proof is written in the accompanying P19 run report; this
# executable checks only the finite rational inequalities used there.

# Elementary lower bound e > sum_{k=0}^5 1/k! = 163/60, then e^6 > 400.
e_lower = Fraction(163, 60)
e6_gap = e_lower**6 - 400
assert e6_gap > 0
assert e6_gap.numerator == 92969578009

# Uniform boundary-phase monotonicity margin for L >= 6.
phase_margin = 6 * Fraction(399, 401) - 1
assert phase_margin == Fraction(1993, 401)
assert phase_margin > 0

# Classical rational upper bound pi < 22/7 implies pi^2 < 10.
pi2_upper = Fraction(22, 7) ** 2
assert pi2_upper == Fraction(484, 49)
assert pi2_upper < 10

# Exact upper bound for the curvature error at L=6.
F6_upper = (
    Fraction(1, 400)
    * Fraction(46**2, 6)
    * Fraction(400, 399) ** 4
)
assert F6_upper == Fraction(67712000000, 76034875203)
assert F6_upper < 1
curvature_margin_lower = 1 - F6_upper
assert curvature_margin_lower == Fraction(8322875203, 76034875203)
assert curvature_margin_lower > 0

print(f"e6_lower_gap_numerator={e6_gap.numerator}")
print(f"phase_margin={phase_margin}")
print(f"pi2_upper={pi2_upper}")
print(f"F6_upper={F6_upper}")
print(f"curvature_margin_lower={curvature_margin_lower}")
print("P19-AUDIT-P20-I0081-LOGUNIFORM-ENDTOEND-19 PASS")
