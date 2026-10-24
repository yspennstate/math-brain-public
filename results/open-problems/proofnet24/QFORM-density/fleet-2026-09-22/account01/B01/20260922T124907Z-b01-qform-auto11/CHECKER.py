import math


def cross_bound(k, D):
    K = math.pi ** (k / 2.0) * D ** (-0.5)
    T = K ** (2.0 / k)
    l1 = 2.0 * T + 4.0 * K / (k - 2.0) * T ** (1.0 - k / 2.0)
    density = l1 / (2.0 * math.pi)
    closed = k / (k - 2.0) * D ** (-1.0 / k)
    return K, T, l1, density, closed


for k, D in [(3, 1.0), (4, 16.0), (5, 0.125)]:
    K, T, l1, density, closed = cross_bound(k, D)
    print(f"k={k} D={D} K={K:.15g} T={T:.15g} L1={l1:.15g} density={density:.15g} closed={closed:.15g}")
    assert abs(density - closed) <= 1e-12 * max(1.0, abs(closed))

hybrid_constant = 7.0 * 2.0 ** (-1.0 / 7.0) * 3.0 ** (-3.0 / 7.0)
print(f"hybrid_constant={hybrid_constant:.15g}")

# Direct numerical check of the k=3 hybrid minimizer for a=D=1.
a = 1.0
D = 1.0
L = (16.0 * math.pi / a) ** (1.0 / 3.0)
K = math.pi ** 1.5 * D ** (-0.5)
A0 = 2.0 ** (2.0 / 3.0) * L
T = (3.0 * K / A0) ** (6.0 / 7.0)
hybrid_density = (A0 * T ** (2.0 / 3.0) + 4.0 * K * T ** (-0.5)) / (2.0 * math.pi)
print(f"hybrid_T={T:.15g} hybrid_density={hybrid_density:.15g}")
assert abs(hybrid_density - hybrid_constant) <= 1e-12

print("STATUS=PASS")
