from fractions import Fraction as Q

# Exact arithmetic self-check for the R09 G0013 joint-slope relaxation report.
# This certifies only the rational algebra quoted in the report; it is not an
# independent audit of any theorem-sized claim.

m0 = Q(19, 48)
L0 = Q(19, 24)
u0 = Q(17, 12)
r = Q(6137, 6912)

# Lower-ramp scalar-envelope optimizer: a(m)=2*u0*m=(17/6)m.
a_coeff = 2 * u0
# h_min coefficient on this branch:
# ((a-2m)^3)/(12(6m-a)) = (125/8208)m^2.
h_coeff = (Q(5, 6) ** 3) / (12 * Q(19, 6))
var_coeff = a_coeff**2 / 12 + h_coeff

assert a_coeff == Q(17, 6)
assert h_coeff == Q(125, 8208)
assert var_coeff == Q(13, 19)

# rho_* = 2 int_0^{1/2} a(m) dm, xi_* = 12 int_0^{1/2} Var(q_m) dm.
# Keep only the exact lower branch for both, and a crude exact lower bound
# a(m) >= 6m-8m^2 on the tail m in [m0,1/2].
rho_low = a_coeff * m0**2
xi_low = 8 * var_coeff * m0**3  # 12*2*(m0^3/3)

# 2 * integral_{m0}^{1/2} (6m-8m^2) dm.
def F(m):
    return 3*m*m - Q(8, 3)*m*m*m
rho_tail_lb = 2 * (F(Q(1, 2)) - F(m0))

assert rho_low == Q(6137, 13824)
assert xi_low == Q(4693, 13824)
assert rho_tail_lb == Q(4645, 20736)

sum_lb = rho_low + xi_low + rho_tail_lb
assert sum_lb == Q(10445, 10368)
margin = sum_lb - 1
assert margin == Q(77, 10368) and margin > 0

# Anti-pairing of the preferred active slopes m <-> 1/2-m.
# On the middle interval both levels are in the lower-ramp branch and
# sigma(m)=2m/L0^2.  The product is maximized at m=1/4.
prod_mid_max = Q(1, 4) / (L0**4)
assert prod_mid_max == Q(82944, 130321)
assert prod_mid_max < 1

# On a tail/lower pair, m' <= 5/48, hence sigma(m') <= 120/361.
low_partner_max = (2 * Q(5, 48)) / (L0**2)
assert low_partner_max == Q(120, 361)

# The tail root L_m solves L(6m(1-m)-L^2/2)=r on [m0,1/2].
# At L=2/3 the left side is at most 23/27, while r exceeds 23/27 by 83/2304.
root_margin = r - Q(23, 27)
assert root_margin == Q(83, 2304) and root_margin > 0
# Since the relevant cubic branch is increasing up to L_m, L_m>2/3,
# so sigma_tail=1/L_m<3/2.
prod_tail_upper = Q(3, 2) * low_partner_max
assert prod_tail_upper == Q(180, 361)
assert prod_tail_upper < prod_mid_max < 1

print('rho_low =', rho_low, float(rho_low))
print('xi_low =', xi_low, float(xi_low))
print('rho_tail_lower_bound =', rho_tail_lb, float(rho_tail_lb))
print('rho_plus_xi_lower_bound =', sum_lb, float(sum_lb))
print('D4_contradiction_margin =', margin, float(margin))
print('middle_anti_pair_slope_product_max =', prod_mid_max, float(prod_mid_max))
print('tail_anti_pair_slope_product_upper =', prod_tail_upper, float(prod_tail_upper))
print('tail_root_margin_r_minus_23over27 =', root_margin, float(root_margin))
print('SELF_CHECK_ONLY / PASS')
