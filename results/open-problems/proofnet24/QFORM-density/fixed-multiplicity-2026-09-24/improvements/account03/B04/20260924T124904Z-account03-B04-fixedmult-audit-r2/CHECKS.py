from math import sqrt

eta = 1.0/100.0
kappa = 1.0/(80.0**2)
eps = sqrt(18.0*kappa)
c = 1.0-eps
d0 = 1.0-eps-eta
o0 = sqrt(eta*eta+eta)+eps
delta = d0*d0-o0*o0
omega_lb = c*c*kappa*kappa
xi_lb = 0.5*delta*delta*kappa*kappa
r1_diag = 39.0/40.0-eta
r1_off = sqrt(eta*eta+eta)+1.0/40.0

assert eta + sqrt(kappa) < 1.0
assert r1_diag > r1_off
assert delta > 0.0
assert omega_lb > 2.18e-8
assert xi_lb > 8.90e-9

print('QFORM_B04_FIXEDMULT_R2_EIGHT_COLLAR_CHECK_PASS')
print('epsilon_star', repr(eps))
print('c_star', repr(c))
print('d0', repr(d0))
print('o0', repr(o0))
print('delta_star', repr(delta))
print('omega1_lower', repr(omega_lb))
print('xi2_lower', repr(xi_lb))
print('r1_diag_lower', repr(r1_diag))
print('r1_off_upper', repr(r1_off))
