from fractions import Fraction

# Independent P26 exact finite-core audit for Hasebe--Ueda--Wang
# Problem 4.3, using the P20 log-uniform counterexample family.

e_partial = Fraction(163, 60)
e6_gap = e_partial**6 - 400
pi2_upper = Fraction(22, 7)**2
phase_lower = Fraction(6 * 399, 401) - 1
csc4_upper = Fraction(23, 18)**2
E6_upper = Fraction(216, 400) * Fraction(400, 399)**4
curvature_ratio_upper = csc4_upper * E6_upper
curvature_margin = 1 - curvature_ratio_upper

assert e6_gap > 0
assert pi2_upper < 10
assert phase_lower == Fraction(1993, 401)
assert phase_lower > 0
assert csc4_upper == Fraction(529, 324)
assert E6_upper == Fraction(512000000, 938702163)
assert curvature_ratio_upper == Fraction(67712000000, 76034875203)
assert curvature_ratio_upper < 1
assert curvature_margin == Fraction(8322875203, 76034875203)
assert curvature_margin > 0

print("P26 independent exact audit: Hasebe-Ueda-Wang Problem 4.3")
print("e6_gap =", e6_gap)
print("pi2_upper =", pi2_upper)
print("phase_lower =", phase_lower)
print("csc4_upper =", csc4_upper)
print("E6_upper =", E6_upper)
print("curvature_ratio_upper =", curvature_ratio_upper)
print("curvature_margin =", curvature_margin)
print("P26_I0081_EXACT_AUDIT_PASS")
