from fractions import Fraction as F
import sympy as sp

# Exact algebra for the weighted m-choice forbidden-pair selector benchmark.
m, lam, x = sp.symbols("m lam x")

# For one constraint and one selector: 0 if both forbidden coordinates are
# selected, lambda if exactly one is selected, and 1 if neither is selected.
A = (m - 1) * (2 * lam + m - 1) / m**2

# Exact two-selector one-constraint moment after averaging over whether the
# two selectors agree at each endpoint; x is their root-overlap fraction.
B = (
    2*lam**2*m*x + 4*lam**2*x**2 - 8*lam**2*x + 2*lam**2
    - 4*lam*m*x + 4*lam*m - 4*lam*x**2 + 12*lam*x - 8*lam
    + m**2 + 2*m*x - 4*m + x**2 - 4*x + 4
) / m**2

lam_star = (m - 1) / (m - 2)
R_star = sp.factor((B / A**2).subs(lam, lam_star))
R_target = 1 + (m*x - 1)**2 / (m - 1)**4
assert sp.simplify(R_star - R_target) == 0

# The derivative at the independent overlap x=1/m is a perfect square.
dB_typ = sp.factor(sp.diff(B, x).subs(x, 1/m))
dB_target = 2 * (lam*m - 2*lam - m + 1)**2 / m**3
assert sp.simplify(dB_typ - dB_target) == 0
# In particular m=2 cannot be balanced by any finite positive lambda.
assert sp.simplify(dB_typ.subs(m, 2) - sp.Rational(1, 4)) == 0

# Prior certified outward upper bounds from the 08:29 T04 report at alpha=3.6.
uU = F(197596486380699, 10**15)
SminU = F(1609550314021127, 10**15)
r1U = F(1026099170436126, 10**15)
r2U = F(508148367896451, 10**15)

# Three decorrelated near-optimal menus: c_3 = (3^2/2) u S_*^2.
c3U = F(9, 2) * uU * SminU * SminU
c3_simple = F(288, 125)  # 2.304
threshold3 = F(32, 9)    # 2(m-1)^4/m^2 for m=3
assert c3U < c3_simple < threshold3

a3 = c3_simple * F(9, 16)
p3 = (F(2) - a3) / (F(2) + a3)
assert a3 == F(162, 125)
assert p3 == F(22, 103)

# A generic root-candidate tree uses one specified root variable, then greedy
# minimum-break descendants. Its certified mean-cost upper bound is
# 1 + r1/(1-r2). Six decorrelated choices already tolerate this larger cost.
SindU = F(1) + r1U / (F(1) - r2U)
c6U = F(36, 2) * uU * SindU * SindU
c6_simple = F(33877, 1000)  # 33.877
threshold6 = F(625, 18)     # 2*5^4/6^2
assert c6U < c6_simple < threshold6

a6 = c6_simple * F(36, 625)
p6 = (F(2) - a6) / (F(2) + a6)
assert a6 < 2
assert p6 == F(7607, 617393)

print("balanced_identity =", sp.factor(R_star))
print("typical_overlap_derivative_B =", dB_typ)
print("m2_typical_derivative =", sp.simplify(dB_typ.subs(m, 2)))
print("u_upper =", float(uU))
print("S_min_upper =", float(SminU))
print("c3_upper =", float(c3U))
print("c3_simple_bound =", float(c3_simple))
print("m3_second_moment_threshold =", float(threshold3))
print("m3_Paley_Zygmund_lower_from_simple_bound =", str(p3), float(p3))
print("S_individual_upper =", float(SindU))
print("c6_upper =", float(c6U))
print("c6_simple_bound =", float(c6_simple))
print("m6_second_moment_threshold =", float(threshold6))
print("m6_Paley_Zygmund_lower_from_simple_bound =", str(p6), float(p6))
print("ALL_EXACT_CHECKS_PASS")
