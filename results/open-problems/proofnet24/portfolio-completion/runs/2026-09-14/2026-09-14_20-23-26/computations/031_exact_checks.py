"""Exact arithmetic checks for worker 031's integrated QSO manuscript audit.

These checks validate displayed constants and explicit witnesses. The universal
theorems are justified by the analytic audit in agents/031.md, not by sampling.
Uses only the Python standard library. Run from any working directory.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import json


# An element (a,b) denotes a+b*sqrt(5). Arithmetic is exact in Q(sqrt(5)).
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def inv(x):
    denominator = x[0] ** 2 - 5 * x[1] ** 2
    assert denominator != 0
    return (x[0] / denominator, -x[1] / denominator)


one, two, three = (F(1), F(0)), (F(2), F(0)), (F(3), F(0))
c = (F(3, 2), F(-1, 2))
assert mul(c, c) == add(mul(three, c), neg(one))
one_minus_2c = add(one, neg(mul(two, c)))
assert inv(one_minus_2c) == (F(2), F(1))
stability = add(inv(one_minus_2c), neg(mul(two, c)))
assert stability == (F(-1), F(2))
Lc = add(one, neg(mul(c, one_minus_2c)))
assert Lc == (F(13, 2), F(-5, 2))


def scalar_averaging_bound(u, lam):
    return (1 - lam) * u + lam * (1 - u) ** 2


lam = F(2, 5)
caps = [F(1)]
for _ in range(3):
    caps.append(max(scalar_averaging_bound(F(0), lam),
                    scalar_averaging_bound(caps[-1], lam)))
assert caps == [F(1), F(3, 5), F(53, 125), F(2, 5)]
assert scalar_averaging_bound(F(53, 125), lam) == F(30243, 78125)
assert 1 - lam * (1 - 2 * F(2, 5)) == F(23, 25)
assert 1 / (1 - 2 * F(2, 5)) == 5

q = F(49, 128)
d = 1 - 2 * q
epsilon = d ** 2 / 2
rate = 1 - epsilon
theta_endpoint = epsilon / (d - 2 * epsilon) ** 2
overlap_endpoint = (d - epsilon) * (1 - theta_endpoint)
assert d == F(15, 64)
assert epsilon == F(225, 8192)
assert rate == F(7967, 8192)
assert d - 2 * epsilon == F(735, 4096) > 0
assert theta_endpoint == F(2048, 2401) < 1
assert overlap_endpoint == F(598335, 19668992)
assert overlap_endpoint - epsilon == F(29055, 9834496) > 0
assert rate - (F(1, 2) + q) == F(735, 8192) > 0


def validate(P):
    n = len(P)
    for i in range(n):
        for j in range(n):
            assert P[i][j] == P[j][i]
            assert sum(P[i][j]) == 1
            assert min(P[i][j]) >= 0
            assert all(P[i][j][k] == 0 for k in {i, j})


def apply(P, x):
    n = len(P)
    return [sum(P[i][j][k] * x[i] * x[j]
                for i in range(n) for j in range(n)) for k in range(n)]


def averaged(P, x):
    return [(a + b) / 2 for a, b in zip(x, apply(P, x))]


# The smallest permissible offspring gives both a raw 2-cycle and a sharp cap.
P4 = [[[F(0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        k = min(set(range(4)) - {i, j})
        P4[i][j][k] = F(1)
validate(P4)
e1, e2 = [F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)]
assert apply(P4, e1) == e2 and apply(P4, e2) == e1
x = [F(1, 2), F(1, 2), F(0), F(0)]
half_second = averaged(P4, averaged(P4, x))
assert half_second[0] == q

# Archived five-type coefficient table, including both parent orders.
P5 = [[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]
for i in range(3):
    for j in range(3):
        if i == j:
            for k in set(range(3)) - {i}:
                P5[i][j][k] = F(1, 2)
        else:
            P5[i][j][next(iter(set(range(3)) - {i, j}))] = F(1)
for i in range(3):
    P5[i][3][4] = P5[3][i][4] = F(1)
    P5[i][4][3] = P5[4][i][3] = F(1)
P5[3][3][4] = P5[4][4][3] = F(1)
for k in range(3):
    P5[3][4][k] = P5[4][3][k] = F(1, 3)
validate(P5)
first = [F(1, 3)] * 3 + [F(0)] * 2
second = [F(1, 9)] * 3 + [F(1, 3)] * 2
assert sum(first) == sum(second) == 1 and first != second
assert apply(P5, first) == first
assert apply(P5, second) == second

# A rational point on s^2=1+4a^2 checks all leakage normalization constants.
# This specialization is an arithmetic check, not a proof for all leakage.
a, s, leakage = F(15, 16), F(17, 8), F(1, 16)
assert s ** 2 == 1 + 4 * a ** 2 and s > 2
cap = 1 - (s - 1) / (2 * a)
lam = cap
beta = leakage + a * cap
L = 1 - lam * (s - 2)
rho = 1 - lam * (s + 1) / 2
exponent = 2 * (s - 1) / (L * (s + 1))
assert cap == F(2, 5)
assert leakage + a * (1 - cap) ** 2 == cap
assert beta == (3 - s) / 2
assert 1 - cap * s == 2 * a * (s - 2 * a) / (s + 1) > 0
assert L == F(19, 20) and rho == F(3, 8)
assert exponent == F(72, 95)
assert exponent == 2 * lam * a * (1 - cap) / (L * (1 - rho))

result = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "status": "all exact assertions passed",
    "scope": "Displayed constants and explicit coefficient witnesses only; universal proofs are in agents/031.md.",
    "rational_iteration_caps": [str(t) for t in caps],
    "strict_stability_constant_Q_sqrt5": [str(t) for t in stability],
    "optimized_L_Q_sqrt5": [str(t) for t in Lc],
    "half_step_rate": str(rate),
    "half_step_theta_endpoint": str(theta_endpoint),
    "half_step_overlap_margin": str(overlap_endpoint - epsilon),
    "half_step_cap_witness_second_iterate": [str(t) for t in half_second],
    "raw_two_cycle_checked": True,
    "five_type_fixed_points_checked": [[str(t) for t in first], [str(t) for t in second]],
    "leakage_rational_specialization": {
        "delta": str(leakage), "q": str(cap), "L": str(L),
        "rho": str(rho), "exponential_prefactor_exponent": str(exponent)
    }
}
output = Path(__file__).with_name("031_exact_results.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
