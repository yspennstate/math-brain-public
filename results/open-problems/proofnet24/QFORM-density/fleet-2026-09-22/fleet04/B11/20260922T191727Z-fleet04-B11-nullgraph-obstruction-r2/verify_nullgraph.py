import math


def lower_bound(K: int) -> float:
    return 0.5 * math.log(2.0) * sum(1.0 / k for k in range(1, K + 1))


def mass(N: int) -> float:
    return sum(2.0 ** (-k - 1) / k for k in range(1, N + 1))


assert abs(0.5 * math.log(2.0) - mass(200)) < 1e-15
vals = [lower_bound(K) for K in (10, 100, 1000, 10000)]
assert vals == sorted(vals)
assert vals[-1] > 3.0

print("rectangle_mass", mass(200))
for K, value in zip((10, 100, 1000, 10000), vals):
    print("K", K, "density_lower_bound", value)
print("QFORM_B11_NULLGRAPH_CHECK_PASS")
