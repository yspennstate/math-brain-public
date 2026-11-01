from math import sqrt, exp, pi

C_indef = 1.0/(2.0*sqrt(2.0))
C_def = exp(-0.5)/sqrt(2.0*pi)
C_tail = sqrt(6.0)*exp(-1.5)/(2.0*sqrt(pi))
cap_one = 12.0*C_indef
fold_gaussian = 12.0/(2.0*sqrt(3.0))
partner_uniform_ceiling = 2.0*sqrt(6.0)

assert C_tail < C_def < C_indef
assert abs(cap_one - 3.0*sqrt(2.0)) < 1e-14
assert abs(fold_gaussian - 2.0*sqrt(3.0)) < 1e-14
assert abs(fold_gaussian*sqrt(2.0) - partner_uniform_ceiling) < 1e-14

# Deterministic grid check of the exact algebraic product-slack inequality
# r(r+c) >= 3 under r>=1, c>=1, r^2 c>=2.
for i in range(10001):
    r = 1.0 + 3.0*i/10000.0
    c = max(1.0, 2.0/(r*r))
    assert r*(r+c) >= 3.0 - 1e-12

print('PASS QFORM_GAUSSIAN_FULLTARGET_COMPARATOR')
print('indef_unit=', repr(C_indef))
print('def_unit=', repr(C_def))
print('tail_unit=', repr(C_tail))
print('cap_one_barrier=', repr(cap_one))
print('fold_gaussian_ceiling=', repr(fold_gaussian))
print('partner_uniform_ceiling=', repr(partner_uniform_ceiling))
print('ratio=', repr(fold_gaussian/partner_uniform_ceiling))
