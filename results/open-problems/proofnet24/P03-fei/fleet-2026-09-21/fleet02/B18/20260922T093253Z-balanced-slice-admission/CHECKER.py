from fractions import Fraction

Cdag = Fraction(6521851214, 10**9)
eta_star_center = Fraction(35, 288)
eta4_center = Fraction(1, 8)

# Strong-source data from completed peer reports.
Deta_star = Fraction(7405187762554608605, 58643094782223581184)
old_deficit_lb = Fraction(38023, 10**6)
T_old_lb = old_deficit_lb / Deta_star
C_old_lb = Cdag + eta_star_center * T_old_lb

L4 = Fraction(211575825297187673, 1628974855061766144)
q4_deficit_lb = Fraction(38023734, 10**9)
q4_center_lb = Cdag + q4_deficit_lb / (8 * L4)
lambda_q = Fraction(58551, 200000)
Cq = Cdag + lambda_q * eta4_center
q4_repair_slack = -Fraction(38023735, 10**9) + lambda_q * L4

assert eta_star_center == Fraction(1, 8) * (1 - Fraction(1, 36))
assert eta4_center == Fraction(1, 8)
assert Cq == Fraction(6558445589, 10**9)
assert T_old_lb > Fraction(301111, 10**6)
assert C_old_lb > Fraction(6558444, 10**6)
assert q4_center_lb > Fraction(6558445, 10**6)
assert q4_repair_slack > 0

print('PASS')
print('eta_star_center =', eta_star_center)
print('eta4_center =', eta4_center)
print('old_safe_ray_T_lower =', float(T_old_lb))
print('old_safe_ray_center_lower =', float(C_old_lb))
print('Q4_center_lower_in_safe_cone =', float(q4_center_lb))
print('C_Q =', float(Cq))
print('Q4_strong_witness_slack_lower =', float(q4_repair_slack))
