import math
import random

TAU = 9 / 16
M0 = math.sqrt((1 - TAU * TAU) / 2)
KAPPA0 = M0 - TAU
SCALAR = 16 * math.sqrt(30) * TAU ** (-0.25)
PAIR = 8 * math.sqrt(5) * KAPPA0 ** (-0.25)
TARGET = 32 * math.sqrt(10)

print('tau=', TAU)
print('m0=', M0)
print('kappa0=', KAPPA0)
print('scalar_constant=', SCALAR)
print('pair_constant=', PAIR)
print('target_constant=', TARGET)

assert abs(SCALAR - TARGET) < 1e-12
assert PAIR < TARGET
assert KAPPA0 > 1 / 1024
assert abs(M0 * M0 - 175 / 512) < 1e-15
assert TAU * TAU == 81 / 256

random.seed(314159265)

def det3(B):
    a, b, c = B[0]
    d, e = B[1][1], B[1][2]
    f = B[2][2]
    return a*d*f + 2*b*e*c - a*e*e - d*c*c - f*b*b

checked = 0
for _ in range(10000):
    u = random.uniform(-2, 2)
    v = random.uniform(-2, 2)
    lower = math.sqrt(abs(u*v)) + 0.1
    m = random.choice((-1, 1)) * random.uniform(lower, lower + 4)
    e1 = random.uniform(-2, 2)
    e2 = random.uniform(-2, 2)
    w = random.uniform(-2, 2)
    detC = u*v - m*m
    if abs(detC) < 1e-12:
        continue
    B = [[u, m, e1], [m, v, e2], [e1, e2, w]]
    delta = det3(B)
    inv00 = v / detC
    inv01 = -m / detC
    inv11 = u / detC
    r = w - (e1*(inv00*e1 + inv01*e2) + e2*(inv01*e1 + inv11*e2))
    assert abs(delta - detC*r) < 1e-8*(1 + abs(delta))
    checked += 1

print('schur_identity_examples=', checked)
print('STATUS=PASS')
