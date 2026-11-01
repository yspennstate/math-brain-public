from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
sqrt2 = D(2).sqrt()

gamma0 = D(28159)/(D(4194304)*sqrt2)
tau = D(2) ** D(-16)
eps = D(2) ** D(-12)
Gamma_C = gamma0/D(3) * (D(1)-D(3)/D(1024))**2
beta_C = D(1)/D(192)-tau
C_E3 = D('8.45302122552817687470491804598')
delta2 = Gamma_C**2 * eps**2 / D(3)
bound2 = C_E3 * delta2 ** (-D(1)/D(6))
c0 = D(1)/(D(1152)*sqrt2)-tau
delta3 = c0**2 * eps**4 / D(3)
bound3 = C_E3 * delta3 ** (-D(1)/D(6))
err = (tau+2*eps)/D(2)

print('gamma0', gamma0)
print('Gamma_C', Gamma_C)
print('beta_C', beta_C)
print('delta2', delta2)
print('bound2', bound2)
print('c0', c0)
print('delta3', delta3)
print('bound3', bound3)
print('skeleton_error', err)

assert beta_C == D(1021)/D(196608)
assert bound2 < D(1397)
assert bound3 < D(30838)
assert err == D(33)/D(131072)
print('QFORM_B20_R46_THREECUT_CHECK_PASS')
