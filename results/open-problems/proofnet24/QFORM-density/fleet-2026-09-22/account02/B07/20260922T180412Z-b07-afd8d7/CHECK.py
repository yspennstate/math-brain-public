import math


def density_bound(m, detC):
    assert m > 2 and detC > 0
    K = math.pi ** (m / 2) * detC ** (-0.5)
    t0 = K ** (2 / m)
    integral = 2 * (t0 + K * t0 ** (1 - m / 2) / (m / 2 - 1))
    return K, t0, integral / (2 * math.pi)


m = 3
detC = 1 / 256
K, t0, bound = density_bound(m, detC)
closed = 3 * 256 ** (1 / 3)

print("m=3 detC=1/256")
print(f"K={K:.15f}")
print(f"t0={t0:.15f}")
print(f"density_bound={bound:.15f}")
print(f"closed_form={closed:.15f}")
assert abs(bound - closed) < 1e-12
assert bound < 19.049
print("m=2 endpoint exponent=1 => tail integral diverges logarithmically")
print("STATUS=QFORM_DISJOINT_3CROSS_L2_CHECK_PASS")
