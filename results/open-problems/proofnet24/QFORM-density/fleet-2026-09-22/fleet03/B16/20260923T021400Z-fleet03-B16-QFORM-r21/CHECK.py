import math

C_cross = 3 * 2**(8/3)
C_rank2 = 16 * 2**(3/4)
tau = 3/7
near = C_cross * 2**(2/3) * (1-tau)**(-1/6)
far = C_rank2 * tau**(-1/4)

print('C_cross =', repr(C_cross))
print('C_rank2 =', repr(C_rank2))
print('near_tau_3_7 =', repr(near))
print('far_tau_3_7 =', repr(far))
print('max =', repr(max(near, far)))

assert C_cross < 19.049
assert near < 33.195
assert far < 33.258
assert max(near, far) < 34
print('STATUS=PASS')
