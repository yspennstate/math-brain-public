"""Exact finite algebra supporting the analytic raw-cycle proof in agents/011.md.

This verifies the tensor, vertex transitions, zero return derivatives, and
rational constants. The uniform derivative estimates are proved in the report.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def mv(a, x):
    return [sum((v * t for v, t in zip(row, x)), F(0)) for row in a]


def jac(p, x):
    return [[2 * sum((p[i][j][k] * x[i] for i in range(4)), F(0))
             for j in range(4)] for k in range(4)]


offspring = {(0, 0): 1, (1, 1): 0, (2, 2): 0, (3, 3): 0,
             (0, 1): 2, (0, 2): 1, (0, 3): 1,
             (1, 2): 0, (1, 3): 0, (2, 3): 0}
p = [[[F(0) for k in range(4)] for j in range(4)] for i in range(4)]
e = [[[F(0) for k in range(4)] for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        p[i][j][offspring[min(i, j), max(i, j)]] = F(1)
        allowed = [k for k in range(4) if k not in (i, j)]
        for k in allowed:
            e[i][j][k] = F(1, len(allowed))
        for tensor in (p, e):
            assert sum(tensor[i][j]) == 1
            assert all(tensor[i][j][k] == 0 for k in (i, j))

vertex1, vertex2 = [F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)]
assert p[0][0] == vertex2
assert p[1][1] == vertex1
j1, j2 = jac(p, vertex1), jac(p, vertex2)
for j in range(1, 4):
    tangent = [F(0)] * 4
    tangent[0], tangent[j] = F(-1), F(1)
    assert mv(j2, mv(j1, tangent)) == [0] * 4
    assert mv(j1, mv(j2, tangent)) == [0] * 4

r, epsilon_max = F(1, 100), F(49, 5000)
assert epsilon_max + 2 * r * r == r
escape = 1 - (1 - epsilon_max) * (1 - r * r) ** 2
assert escape < r
rate = 24 * (epsilon_max + r)
assert rate == F(297, 625) < F(1, 2)
assert r * r < 1 - r
for i in range(4):
    for j in range(4):
        for k in range(4):
            mixed = (1 - epsilon_max) * p[i][j][k] + epsilon_max * e[i][j][k]
            if k not in (i, j):
                assert mixed >= epsilon_max / 3

result = {
    "all_exact_checks_passed": True,
    "epsilon_upper": str(epsilon_max),
    "cap_escape_r": str(r),
    "actual_escape_bound_at_endpoint": str(escape),
    "uniform_return_contraction_upper": str(rate),
    "jacobian_at_vertex1": [[str(z) for z in row] for row in j1],
    "jacobian_at_vertex2": [[str(z) for z in row] for row in j2],
    "zero_return_derivatives_on_full_tangent": True,
    "scope": "Finite algebra only; the uniform estimates and Banach argument are analytic proofs in agents/011.md."
}
target = Path(__file__).with_name("011_raw_cycle_exact_output.json")
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
