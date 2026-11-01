import math
import random


def beta(a, b):
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


def c_e2(q):
    return (2 ** 1.5 * math.sqrt(math.e) * 3 ** (-5 / 8) * q ** (-1 / 4)
            * math.sqrt(beta(1 / 4, 3 / (8 * q) - 1 / 4)))


C1 = c_e2(1.0)
C3 = 12 * math.sqrt(2) * 3 ** (1 / 8) * math.e ** (1 / 4)
SPLICE = C1 * (16 / 25) ** (-1 / 8)

assert C1 < 7.967
assert C3 < 25.0
assert SPLICE < 8.424

# q=2, rho=s/sqrt(24): each of three singular values >=s contributes >=24/25.
theta_floor = 3 * 24 / 25
assert theta_floor > 8 / 3
ratio = (3 * theta_floor) / (3 * theta_floor - 8)
assert abs(ratio - 13.5) < 1e-12

# Determinant/e2 lower bound sanity checks for arbitrary extra singular values.
# If x_i=sigma_i^2 and z=c*t^2, then prod(1+z*x_i)>=1+z^2*e2(x).
max_rel = 0.0
for _ in range(5000):
    m = random.randint(2, 12)
    xs = [10 ** random.uniform(-4, 2) for _ in range(m)]
    z = 10 ** random.uniform(-4, 2)
    det = 1.0
    for x in xs:
        det *= 1 + z * x
    e2 = sum(xs[i] * xs[j] for i in range(m) for j in range(i + 1, m))
    lower = 1 + z * z * e2
    assert det + 1e-12 * max(1.0, det) >= lower
    max_rel = max(max_rel, max(0.0, (lower - det) / det))

# log D >= theta for ridge eigenvalues x/(1+x).
max_gap = 0.0
for _ in range(5000):
    xs = [10 ** random.uniform(-8, 8) for _ in range(random.randint(1, 20))]
    logD = sum(math.log1p(x) for x in xs)
    theta = sum(x / (1 + x) for x in xs)
    assert logD + 1e-12 >= theta
    max_gap = max(max_gap, theta - logD)

print(f'C_e2_q1={C1:.12f}')
print(f'C_three_cross={C3:.12f}')
print(f'C_transverse_splice={SPLICE:.12f}')
print(f'theta_floor={theta_floor:.12f}')
print(f'ratio_3theta_over_gap={ratio:.12f}')
print(f'determinant_trials=5000 max_lower_violation_relative={max_rel:.3e}')
print(f'logD_trials=5000 max_violation={max_gap:.3e}')
print('QFORM_B06_R24_CHECK_PASS')
