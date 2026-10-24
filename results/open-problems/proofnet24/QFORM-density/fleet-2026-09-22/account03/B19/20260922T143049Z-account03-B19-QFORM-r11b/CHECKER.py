from fractions import Fraction as F

# Exact rational regression for account03/B19 low-rank normal form.
theta = F(1, 8)

# Near-diagonal 7/16 branch.
h = F(7, 16)
det_near = (1-h)**2-h**2
assert det_near == F(1, 8)

# s2(H)<=1/8 branch.
det_same = (1-theta)**2-(2*theta)**2
assert det_same == F(45, 64)

det_third = (1-theta)*F(1, 7)-(2*theta)**2
assert det_third == F(1, 16)

lambda_lb = (1-theta)-F(1, 7)
assert lambda_lb == F(41, 56)

v2_ub = theta/lambda_lb
assert v2_ub == F(7, 41)

outside_mass_lb = 1-2*v2_ub
assert outside_mass_lb == F(27, 41)

normalized_w2_ub = v2_ub/outside_mass_lb
assert normalized_w2_ub == F(7, 27)

# Frobenius inverse bound for M0.
inv_frob_sq_ub = F(128, 49)+F(256, 189)+F(64, 9)
assert inv_frob_sq_ub == F(14656, 1323)
assert inv_frob_sq_ub < F(100, 9)
assert F(100, 9)-inv_frob_sq_ub == F(44, 1323)

# Full compression after R and small diagonal contamination.
compression_smin_gap = F(3, 10)-(F(1, 8)+F(1, 7))
assert compression_smin_gap == F(9, 280)

print('det_near=', det_near)
print('det_same=', det_same)
print('det_third=', det_third)
print('lambda_lb=', lambda_lb)
print('v_i_squared_ub=', v2_ub)
print('outside_mass_lb=', outside_mass_lb)
print('normalized_w_i_squared_ub=', normalized_w2_ub)
print('inverse_frobenius_squared_ub=', inv_frob_sq_ub)
print('compression_smin_gap=', compression_smin_gap)
print('QFORM_B19_ONE_EFFECTIVE_NORMAL_FORM_CHECK_PASS')
