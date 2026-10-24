import math

H = math.sqrt(1536 * math.e**2)
L = 3072 * math.e**2
C5 = 2 * math.sqrt(30 * math.pi)

print('H', H)
print('sqrtH', math.sqrt(H))
print('L', L)
print('sqrtL', math.sqrt(L))
print('C5', C5)

for m in range(2, 5):
    amin = m / 12
    amax = m / 4
    print('alpha_range', m, amin, amax)
    assert 0 < amin <= amax <= 1

beta = 1 / (2 * (1 + 1/6))
gamma = (1/2) / (1 + 1/2)
print('beta_max', beta)
print('gamma_max', gamma)
assert abs(beta - 3/7) < 1e-15
assert abs(gamma - 1/3) < 1e-15

for k in range(1001):
    a = 1/6 + (1/2 - 1/6) * k / 1000
    assert 1 / (2 * (1 + a)) <= 3/7 + 1e-15
    assert a / (1 + a) <= 1/3 + 1e-15

print('QFORM_B13_R45_EXPONENT_CHECK_PASS')
