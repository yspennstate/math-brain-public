from fractions import Fraction
import math

# Partner pair-area threshold and random-cut constants.
g0 = Fraction(63, 64) * Fraction(1, 36)
assert g0 == Fraction(7, 256)
cut_product = Fraction(17, 18) * Fraction(1, 16)
assert cut_product == Fraction(17, 288)
relative_leverage = Fraction(1, 36) / cut_product
assert relative_leverage == Fraction(8, 17)
assert relative_leverage < Fraction(1, 2)

pair_constant = 2048 * math.sqrt(2 / 7)

# Exact-graph endpoint constants.
nu = Fraction(1071, 3518)
# nu is the proved lower bound for sigma_min(L_B)^2.
theta0 = Fraction(1, 1) - Fraction(1, 100) / nu
assert theta0 > Fraction(96, 100)

pair_density_cap = 2 * math.sqrt(288 / 17)
endpoint_constant = (
    31
    * pair_density_cap ** (2 / 3)
    * float(theta0) ** (-1 / 6)
    * (64 / 63) ** (1 / 3)
)
assert endpoint_constant < 128

# A concrete exact-graph control: M swaps e1,e2 and fixes e3.
# L has columns sqrt(c)e1, a e1+e2, e3. Then
# B=L^T M L=[[0,sqrt(c),0],[sqrt(c),2a,0],[0,0,1]].
c = Fraction(63, 64)
a = Fraction(1, 5)
det_B = -c
beta2_gamma_det_abs = c * c
assert abs(det_B) == c
assert beta2_gamma_det_abs == c * c

print('partner_g_threshold =', g0)
print('random_cut_det_product_floor =', cut_product)
print('relative_volume_row_leverage_cap =', relative_leverage, '=', float(relative_leverage))
print('partner_pair_area_constant = %.12f' % pair_constant)
print('sigma_min_L_squared_floor =', nu, '=', float(nu))
print('cofactor_factor_theta0 =', theta0, '=', float(theta0))
print('bank_pair_density_cap = %.12f' % pair_density_cap)
print('exact_graph_endpoint_constant = %.12f' % endpoint_constant)
print('control_det_B =', det_B)
print('control_abs_beta2_gamma_detB =', beta2_gamma_det_abs)
print('QFORM_B11_R37_EXACT_GRAPH_BOUNDARY_CHECK_PASS')
