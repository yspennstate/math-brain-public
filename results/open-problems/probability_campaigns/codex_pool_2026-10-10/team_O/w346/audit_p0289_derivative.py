"""Independent numerical control for the P0289 derivative identity."""

import math


def integrate(fn, upper, n=20000):
    h = upper / n
    return h / 3 * (fn(0) + fn(upper)
                    + 4 * sum(fn(h * i) for i in range(1, n, 2))
                    + 2 * sum(fn(h * i) for i in range(2, n, 2)))


delta = math.tan(math.pi / 1024)
R = lambda v: 0.5 * math.exp(-delta * v) * math.cos(v)
psi = lambda c: integrate(lambda u: (1 - u) * R(c * u), 1)
rhs = lambda c: integrate(lambda v: (2 * v - c) * R(v), c) / c**3

for c in [0.25, 1.2, 7.5, 20.0]:
    numerical = (psi(c + 1e-4) - psi(c - 1e-4)) / 2e-4
    exact_integral = rhs(c)
    assert abs(numerical - exact_integral) < 2e-8
    print(f"c={c}: finite_difference={numerical:.12g}, integral={exact_integral:.12g}")
