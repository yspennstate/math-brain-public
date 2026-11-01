from fractions import Fraction

# Exact finite core for P20 I0081 rectangular log-uniform counterexample family.
# All comparisons are rational/integer; transcendental steps in the proof are
# reduced analytically to these finite inequalities.

e_partial = Fraction(163, 60)  # sum_{n=0}^5 1/n!
e6_gap = e_partial**6 - 400

pi2_upper = Fraction(22, 7)**2
assert pi2_upper < 10

poisson_lower = Fraction(399, 401)
phase_lower = Fraction(1, 2) * 12 * poisson_lower - 1

# Universal curvature-envelope upper bound for L,M >= 6:
# csc^4(t_*) < (1 + pi^2/36)^2 < (1 + 10/36)^2 = (23/18)^2,
# E(X) <= E(6) < 216*(1/400)*(400/399)^4.
csc4_upper = Fraction(23, 18)**2
E6_upper = Fraction(216, 400) * Fraction(400, 399)**4
curvature_ratio_upper = csc4_upper * E6_upper

assert e6_gap > 0
assert phase_lower > 0
assert curvature_ratio_upper < 1

print("P20 I0081 rectangular L,M>=6 exact finite core: PASS")
print("e lower partial =", e_partial)
print("(163/60)^6 - 400 =", e6_gap, "> 0")
print("(22/7)^2 =", pi2_upper, "< 10")
print("phase derivative lower bound =", phase_lower, "> 0")
print("csc^4 envelope upper =", csc4_upper)
print("E(6) rational upper =", E6_upper)
print("curvature ratio upper =", curvature_ratio_upper, "< 1")
print("curvature margin =", 1 - curvature_ratio_upper, "> 0")
print("monotonic E(X): d log E/dX < 3/X - 1 <= -1/2 for X>=6 (analytic)")
