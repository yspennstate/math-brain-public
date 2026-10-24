import math
import random

r_star = math.sqrt(3/10) * (math.sqrt(7/800) * math.sqrt(1 - 1e-4) - 1e-2)
A_star = math.sqrt(math.pi * math.sqrt(2) / r_star)

assert r_star > 0
assert abs(A_star * A_star - math.pi * math.sqrt(2) / r_star) < 1e-12

for p in (2.5, 3.0, 4.0, 6.0, 10.0):
    t0 = A_star * A_star
    split = 2 * (t0 + A_star**p * t0**(1-p/2) / (p/2 - 1))
    closed = 2 * A_star * A_star * p / (p - 2)
    assert abs(split - closed) <= 1e-10 * closed

for _ in range(100000):
    n = random.randint(2, 8)
    weights = [random.random() for _ in range(n)]
    total = sum(weights)
    weights = [x / total for x in weights]
    z = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(n)]
    p = random.choice((1.0, 1.5, 2.0, 3.0, 4.0, 7.0))
    lhs = abs(sum(w * q for w, q in zip(weights, z)))**p
    rhs = sum(w * abs(q)**p for w, q in zip(weights, z))
    assert lhs <= rhs + 1e-10 * (1 + rhs)

print('QFORM_B13_COPY_CHECK_PASS')
print(f'r_star={r_star:.16g}')
print(f'A_star={A_star:.16g}')
print(f'A_star_sq={A_star*A_star:.16g}')
print(f'four_copy_Linf={2*math.sqrt(2)/r_star:.16g}')
print(f'two_copy_epslog_prefactor={math.exp(0.5)*A_star*A_star/math.sqrt(2*math.pi):.16g}')
print('jensen_tests=100000')
