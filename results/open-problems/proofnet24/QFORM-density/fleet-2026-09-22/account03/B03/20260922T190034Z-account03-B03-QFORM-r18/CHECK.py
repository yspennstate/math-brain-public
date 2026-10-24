import math


def ball_volume(r):
    return math.pi ** (r / 2) / math.gamma(r / 2 + 1)


def C_r(r):
    v = ball_volume(r)
    return (4 * r / (2 * r - 1)) * math.sqrt(math.e) * v ** (1 / (2 * r))


def radial_bathtub_constant(r, K):
    # K r v_r \int_0^R rho^(r-3/2) d rho, where K v_r R^r = 1.
    v = ball_volume(r)
    R = (1 / (K * v)) ** (1 / r)
    direct = K * r * v * R ** (r - 0.5) / (r - 0.5)
    closed = (2 * r / (2 * r - 1)) * (K * v) ** (1 / (2 * r))
    return direct, closed

for r in (1, 2, 3, 4):
    for K in (0.125, 1.0, 7.0):
        a, b = radial_bathtub_constant(r, K)
        assert abs(a - b) <= 1e-12 * max(1.0, abs(a), abs(b))

c1 = C_r(1)
c2 = C_r(2)
c3 = C_r(3)
assert abs(c1 - 4 * math.sqrt(2 * math.e)) < 1e-12
assert abs(c2 - (8 / 3) * math.sqrt(math.e) * math.pi ** 0.25) < 1e-12

# Exact rank-one control: U,V iid Uniform[-1/2,1/2], R=2UV.
# E|U|^-1/2 = 2 sqrt(2), so E|2UV|^-1/2 = 4 sqrt(2).
rank1_control = 4 * math.sqrt(2)
assert rank1_control < c1

print('QFORM_B03_R18_CHECK_PASS')
print(f'C1={c1:.15f}')
print(f'C2={c2:.15f}')
print(f'C3={c3:.15f}')
print(f'RANK1_CONTROL={rank1_control:.15f}')
