"""Exact rational checks accompanying agents/008.md.

These checks are not a proof substitute. They validate arithmetic and the
explicit sharpness/cycle witnesses in the report. No external dependencies.
"""

from fractions import Fraction as F
import json


def f(s, lam):
    return (1 - lam) * s + lam * (1 - s) ** 2


def offspring_table(entries):
    return {(min(i, j), max(i, j)): k for (i, j), k in entries.items()}


def V(x, table):
    out = [F(0) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            k = table[min(i, j), max(i, j)]
            assert k not in (i, j)
            out[k] += x[i] * x[j]
    assert sum(out) == 1
    return out


def T(x, table, lam):
    return [(1 - lam) * xi + lam * vi for xi, vi in zip(x, V(x, table))]


def l1diff(x, y):
    return sum(abs(xi - yi) for xi, yi in zip(x, y))


sharp_table = offspring_table({
    (0, 0): 1, (0, 1): 2, (0, 2): 1, (0, 3): 1,
    (1, 1): 0, (1, 2): 3, (1, 3): 0,
    (2, 2): 3, (2, 3): 0, (3, 3): 0,
})
q = lam = F(2, 5)
eps = F(1, 1000)
a, b = q - eps, F(1, 2) - q + eps
x = [a + eps, b, a - eps, b]
y = [a - eps, b, a + eps, b]
assert max(x + y) <= q
observed_ratio = l1diff(T(x, sharp_table, lam), T(y, sharp_table, lam)) / l1diff(x, y)
expected_ratio = 1 - lam + 2 * lam * (q - eps)
assert observed_ratio == expected_ratio

bounds = [F(1)]
for _ in range(3):
    bounds.append(max(lam, f(bounds[-1], lam)))
assert bounds == [F(1), F(3, 5), F(53, 125), F(2, 5)]

cycle_table = {
    (i, j): min(k for k in range(4) if k not in (i, j))
    for i in range(4) for j in range(i, 4)
}
e1 = [F(1), F(0), F(0), F(0)]
e2 = [F(0), F(1), F(0), F(0)]
assert V(e1, cycle_table) == e2
assert V(e2, cycle_table) == e1

lam2 = F(9, 20)
r = F(55, 144)
q2 = F(3149, 8000)
assert f(1 - lam2, lam2) == q2
assert f(r, lam2) < q2
assert max(T(T(e1, cycle_table, lam2), cycle_table, lam2)) == q2
L2 = max(1 - lam2 + 2 * lam2 * q2, 2 * lam2)
assert L2 == F(72341, 80000)
assert lam2 / (1 - L2) == F(4000, 851)

# Sharp half-averaging two-step coordinate bound.
all_to_first = {
    (i, j): (0 if 0 not in (i, j) else min(k for k in range(1, 4) if k not in (i, j)))
    for i in range(4) for j in range(i, 4)
}
half_input = [F(1, 2), F(1, 2), F(0), F(0)]
half_output = T(T(half_input, all_to_first, F(1, 2)), all_to_first, F(1, 2))
assert half_output[0] == F(49, 128)

print(json.dumps({
    "status": "all exact assertions passed",
    "sharpness_ratio_for_epsilon_1_over_1000": str(observed_ratio),
    "sharpness_ratio_formula": str(expected_ratio),
    "two_fifths_global_coordinate_bounds": list(map(str, bounds)),
    "raw_V_vertex_cycle": "e1 -> e2 -> e1",
    "nine_twentieths_two_step_cap": str(q2),
    "nine_twentieths_composition_at_minimum": str(f(r, lam2)),
    "nine_twentieths_contraction_factor": str(L2),
    "nine_twentieths_residual_error_multiplier": str(lam2 / (1 - L2)),
    "half_averaging_sharp_two_step_coordinate": str(half_output[0]),
}, indent=2))
