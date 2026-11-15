#!/usr/bin/env python3
"""Exact, small finite checks for the bounded resolvent audit."""
import itertools
import os
import resource
import signal
from fractions import Fraction as Q

signal.alarm(60)
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
ZERO = Q(0)
ONE = Q(1)

def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]

def transpose(a):
    return [list(row) for row in zip(*a)]

def mul(a, b):
    return [[sum((x * y for x, y in zip(row, col)), ZERO)
             for col in zip(*b)] for row in a]

def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]

def inverse(a):
    n = len(a)
    b = [row[:] + e for row, e in zip(a, eye(n))]
    for k in range(n):
        p = next(i for i in range(k, n) if b[i][k])
        b[k], b[p] = b[p], b[k]
        pivot = b[k][k]
        b[k] = [x / pivot for x in b[k]]
        for i in range(n):
            if i != k:
                t = b[i][k]
                b[i] = [x - t * y for x, y in zip(b[i], b[k])]
    return [row[n:] for row in b]

def determinant(a):
    if not a:
        return ONE
    b = [row[:] for row in a]
    out = ONE
    n = len(b)
    for k in range(n):
        candidates = [i for i in range(k, n) if b[i][k]]
        if not candidates:
            return ZERO
        p = candidates[0]
        if p != k:
            b[k], b[p] = b[p], b[k]
            out = -out
        pivot = b[k][k]
        out *= pivot
        for i in range(k + 1, n):
            t = b[i][k] / pivot
            for j in range(k + 1, n):
                b[i][j] -= t * b[k][j]
    return out

def inertia(a):
    """Exact symmetric congruence, including zero and 2x2 pivots."""
    if not a:
        return (0, 0, 0)
    n = len(a)
    p = next((i for i in range(n) if a[i][i]), None)
    if p is not None:
        idx = [p] + [i for i in range(n) if i != p]
        b = [[a[i][j] for j in idx] for i in idx]
        d = b[0][0]
        schur = [[b[i][j] - b[i][0] * b[0][j] / d
                  for j in range(1, n)] for i in range(1, n)]
        pos, neg, zero = inertia(schur)
        return (pos + (d > 0), neg + (d < 0), zero)
    pair = next(((i, j) for i in range(n) for j in range(i + 1, n)
                 if a[i][j]), None)
    if pair is None:
        return (0, 0, n)
    i, j = pair
    idx = [i, j] + [k for k in range(n) if k not in pair]
    b = [[a[r][s] for s in idx] for r in idx]
    t = b[0][1]
    schur = [[b[r][s] - (b[r][0] * b[1][s] + b[r][1] * b[0][s]) / t
              for s in range(2, n)] for r in range(2, n)]
    pos, neg, zero = inertia(schur)
    return (pos + 1, neg + 1, zero)

def reciprocal(a):
    return [[ONE / x for x in row] for row in a]

def qmatrix(m, weights, nodes):
    # I - W M, similar to I - sqrt(W) M sqrt(W).
    return [[Q(i == j) - weights[z] * m[z][t]
             for j, t in enumerate(nodes)] for i, z in enumerate(nodes)]

def direct(m, weights, nodes):
    if not nodes:
        return [row[:] for row in m]
    # M + M_:Z (I-W M_ZZ)^(-1) W M_Z:
    q = qmatrix(m, weights, nodes)
    left = [[row[z] for z in nodes] for row in m]
    right = [[weights[z] * x for x in m[z]] for z in nodes]
    return add(m, mul(mul(left, inverse(q)), right))

def run_fixture(name, m, all_weights):
    n = len(m)
    nodes = [z for z, w in enumerate(all_weights) if w]
    weights = dict(enumerate(all_weights))
    # Nonnegative M W is similar to symmetric sqrt(W) M sqrt(W).
    # This rational row-sum bound certifies its spectral radius < 1.
    row_bound = max((sum((m[i][z] * weights[z] for z in nodes), ZERO)
                     for i in nodes), default=ZERO)
    assert row_bound < 1
    assert inertia(reciprocal(m))[0] <= 1
    expected = direct(m, weights, nodes)
    assert inertia(reciprocal(expected))[0] == 1
    orders = 0
    min_pivot = ONE
    for order in itertools.permutations(nodes):
        h = [row[:] for row in m]
        allowed = []
        for z in order:
            pivot = ONE - weights[z] * h[z][z]
            det_ratio = (determinant(qmatrix(m, weights, allowed + [z]))
                         / determinant(qmatrix(m, weights, allowed)))
            assert pivot == det_ratio and pivot > 0
            min_pivot = min(min_pivot, pivot)
            c = weights[z] / pivot
            h = [[h[i][j] + c * h[i][z] * h[z][j]
                  for j in range(n)] for i in range(n)]
            allowed.append(z)
            assert h == direct(m, weights, allowed)
            assert inertia(reciprocal(h))[0] == 1
        assert h == expected
        orders += 1
    print(f"{name}: orders={orders}, row_bound={row_bound}, "
          f"minimum_pivot={min_pivot}, final_inertia={inertia(reciprocal(expected))}")
    return orders

points = [
    (Q(0), Q(0)), (Q(1, 2), Q(0)), (Q(-1, 3), Q(1, 4)),
    (Q(1, 5), Q(-2, 5)), (Q(-1, 3), Q(1, 4)), (Q(0), Q(0))
]
m = [[ONE / (ONE - sum((x * y for x, y in zip(u, v)), ZERO))
      for v in points] for u in points]
fixtures = [
    ("four_nodes_with_duplicate_evaluation_points", [Q(1, 25)] * 4 + [ZERO] * 2),
    ("zero_weights", [ZERO, Q(1, 25), ZERO, Q(1, 30), ZERO, ZERO]),
    ("one_node", [ZERO, ZERO, Q(1, 10), ZERO, ZERO, ZERO]),
    ("coincident_integration_nodes", [Q(1, 30), ZERO, Q(1, 40), ZERO, Q(1, 60), ZERO]),
    ("empty", [ZERO] * 6)
]
orders = sum(run_fixture(name, m, weights) for name, weights in fixtures)
assert orders == 34
# Combining coincident physical nodes must give the same complete matrix.
split = [Q(1, 30), ZERO, Q(1, 40), ZERO, Q(1, 60), ZERO]
merged = [Q(1, 30), ZERO, Q(1, 24), ZERO, ZERO, ZERO]
assert direct(m, dict(enumerate(split)), [0, 2, 4]) == direct(
    m, dict(enumerate(merged)), [0, 2])
print("coincident-node merging: exact equality")
# Negative update is a counterexample, even though all entries stay positive.
bad_m = [[ONE, ONE, ONE],
         [ONE, Q(4, 3), Q(4, 5)],
         [ONE, Q(4, 5), Q(4, 3)]]
bad = [[x - Q(1, 2) for x in row] for row in bad_m]
assert inertia(reciprocal(bad_m)) == (1, 1, 1)
assert all(x > 0 for row in bad for x in row)
assert inertia(reciprocal(bad)) == (2, 1, 0)
assert Q(-4, 5) + Q(4, 3) == Q(8, 15)
assert Q(-4, 5) - Q(4, 3) == Q(-32, 15)
print("negative update: initial inertia=(1,1,1), final inertia=(2,1,0)")
assert determinant([[ONE - ONE]]) == 0
print("critical one-node weight w=1: singular, as required")
# Scalar exact checks of all constants in the perturbation estimate (10).
checks = 0
for d in [Q(1, 5), Q(1, 2), Q(3, 4)]:
    for delta in [Q(0), Q(1, 100), (ONE - d) / 2]:
        alpha = ONE - d
        beta = alpha - delta
        for x, y, dx, dy in [(Q(2), Q(3), Q(1, 10), Q(1, 20)),
                             (ONE, ONE, ZERO, ZERO)]:
            actual = abs((x + dx) * (y + dy) / (ONE - d - delta)
                         - x * y / (ONE - d))
            bound = (dx * (y + dy) + x * dy) / beta + x * y * delta / (alpha * beta)
            assert actual == bound  # In these positive scalar cases the bound is sharp.
            checks += 1
print(f"quadrature perturbation formula: {checks} exact scalar equality checks")
print(f"PASS: {orders} elimination orders; exact rational arithmetic throughout")
print(f"priority={os.getpriority(os.PRIO_PROCESS, 0)}, "
      f"peak_rss_bytes={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")

