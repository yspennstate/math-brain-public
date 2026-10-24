import math

# Exact-rank-three floating/L2 constants.
sqrt6 = math.sqrt(6.0)
delta = 2.0/5.0
alpha = 0.5 - 0.5*sqrt6*delta
C_float = 6.0/alpha
C_float_exact = 300.0 + 120.0*sqrt6
assert delta < 1.0/sqrt6
assert alpha > 0.0
assert abs(C_float-C_float_exact) < 1e-10
assert C_float < 594.0

# Collision refinement at max leverage 1/4.
C_collision = 12.0*(4.0**(1.0/6.0))
assert C_collision < 15.12

# Localized complement.
rho2 = 1.0/sqrt6 - 1.0/64.0
rho = math.sqrt(rho2)
C_diag = 128.0/math.sqrt(1.0/8.0)
assert rho > 0.6265
assert C_diag < 363.0

# account02/B08 grouped rank-two partner application.
C_grp = (2.0**(4.0/3.0)+1.0)*math.sqrt(3.0)*(2.0**0.25)
C_partner_h13 = C_grp*(3.0**0.25)
assert C_partner_h13 < 9.542

print('QFORM_B08_R21_CHECK_PASS')
print('1/sqrt(6)=',1.0/sqrt6)
print('alpha(delta=2/5)=',alpha)
print('C_float=',C_float)
print('C_collision(delta<=1/4)=',C_collision)
print('localized_cross_row_threshold=',rho)
print('C_diag=',C_diag)
print('C_grp=',C_grp)
print('C_partner_h>=1/3=',C_partner_h13)
