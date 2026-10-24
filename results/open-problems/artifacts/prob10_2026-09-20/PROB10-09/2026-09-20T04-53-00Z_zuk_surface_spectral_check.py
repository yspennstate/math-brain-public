from fractions import Fraction

# Published spectral inputs in the standard surface-group normalization:
# ||M_3|| <= 0.552792 = 69099/125000 (Nagnibeda, as recorded in Bartholdi Thm 1.3)
# ||M_4|| < 1/2 (Zuk's all-genus bound ||M_g|| < 1/sqrt(g))
mu3 = Fraction(69099, 125000)
A3 = 12 * mu3
A4_bar = Fraction(8, 1)  # strict upper bound
Rbar = A3 + A4_bar

D = 28
Q = D - 1

# Proposed strict p_u floor.
p = Fraction(8020563, 100000000)
z = 1 / p

# If z>sqrt(Q) and z^2-Rbar*z+Q>0, then
# R_actual < Rbar < z+Q/z, hence beta_D(R_actual)<z and p<1/beta.
zsq_minus_Q = z*z - Q
quad_slack = z*z - Rbar*z + Q

pc_bar = Fraction(4540551, 100000000)
old_gap = Fraction(3123709, 100000000)
new_gap = p - pc_bar
delta = new_gap - old_gap

assert A3 == Fraction(207297, 31250)
assert Rbar == Fraction(457297, 31250)
assert zsq_minus_Q > 0
assert quad_slack > 0
assert new_gap == Fraction(870003, 25000000)
assert delta == Fraction(356303, 100000000)

# Zuk's g=4 bound beats the previous BCCH Section-3 factor bound
# 8 < 1 + 2*sqrt(14), because 14 > (7/2)^2.
assert Fraction(14,1) > Fraction(49,4)

print("A3_upper =", A3, "=", float(A3))
print("A4_strict_upper = 8")
print("Rbar =", Rbar, "=", float(Rbar))
print("p_u_floor_candidate =", p, "=", float(p))
print("z =", z, "=", float(z))
print("z^2-Q =", zsq_minus_Q, "=", float(zsq_minus_Q))
print("z^2-Rbar*z+Q =", quad_slack, "=", float(quad_slack))
print("p_c_upper =", pc_bar, "=", float(pc_bar))
print("old_gap =", old_gap, "=", float(old_gap))
print("new_gap =", new_gap, "=", float(new_gap))
print("gap_improvement =", delta, "=", float(delta))
print("ALL_EXACT_CHECKS_PASS")
