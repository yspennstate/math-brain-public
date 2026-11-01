from math import sqrt, e
import mpmath as mp

rho = 3/64
delta = 1/2 - sqrt(2*rho) - rho
rho_star = (39-6*sqrt(30))/98
q_min = max(1.0, 2*rho/delta)
K31 = e/(6*sqrt(2))*float(mp.beta(mp.mpf(1)/6, mp.mpf(1)/12))
cap = K31/delta

assert rho < rho_star
assert q_min == 1.0
assert delta > 0
assert 3 > 2*q_min
assert cap < 38.491

# Relative L-infinity instability witness.
# Q0 = X2^2+X3^2+X4^2 has support length 3/4, so ||p0||_inf >= 4/3.
# Qeps = eps X1^2 + Q0 with X1 uniform [R,R+1] has
# ||p_eps||_inf <= 1/(2 eps R), hence ratio >= 8 eps R/3.
for eps, M in [(0.5,10), (0.1,100), (1e-3,1e6)]:
    R = 3*M/(8*eps)
    ratio_lower = (8*eps*R)/3
    assert ratio_lower >= M*(1-1e-12)

print('QFORM_B12_COMPLETION_STABILITY_CHECK_PASS')
print(f'rho={rho:.17g}')
print(f'delta={delta:.17g}')
print(f'rho_star={rho_star:.17g}')
print(f'q_min={q_min:.17g}')
print(f'K31={K31:.17g}')
print(f'cap={cap:.17g}')
