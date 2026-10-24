#!/usr/bin/env python3
"""Independent deterministic checks for the B09 A091 review.

The analytic proof in COMPOSITION_REVIEW.md is primary.  This script checks
normalization, the block ledger, the Maassen--Uffink consequence on exhaustive
small Boolean truth tables, exact-product additivity, and the new AND endpoint
lower-bound family.  It does not reuse the original B09 numerical scripts.
"""

from itertools import product, combinations
from math import log2, sqrt


def entropy(probabilities):
    return sum(-x * log2(x) for x in probabilities if x > 0.0)


def assignments(n):
    return list(product((0, 1), repeat=n))


def point_prob(x, bias):
    out = 1.0
    for bit, p in zip(x, bias):
        out *= p if bit else 1.0 - p
    return out


def phi(bit, p):
    return sqrt((1.0 - p) / p) if bit else -sqrt(p / (1.0 - p))


def spectrum(values, bias):
    n = len(bias)
    xs = assignments(n)
    out = {}
    for mask in range(1 << n):
        c = 0.0
        for x, fx in zip(xs, values):
            basis = 1.0
            for i in range(n):
                if mask >> i & 1:
                    basis *= phi(x[i], bias[i])
            c += point_prob(x, bias) * fx * basis
        out[mask] = c * c
    return out


def restrict_values(values, n, A, z):
    A = tuple(A)
    B = tuple(i for i in range(n) if i not in A)
    table = {x: fx for x, fx in zip(assignments(n), values)}
    result = []
    for y in assignments(len(B)):
        x = [None] * n
        for i, bit in zip(A, z):
            x[i] = bit
        for i, bit in zip(B, y):
            x[i] = bit
        result.append(table[tuple(x)])
    return result, B


def ledger(values, bias, A):
    n = len(bias)
    A = tuple(sorted(A))
    B = tuple(i for i in range(n) if i not in A)
    spec = spectrum(values, bias)
    q = [0.0] * (1 << len(B))
    for mask, mass in spec.items():
        bmask = sum(((mask >> i) & 1) << j for j, i in enumerate(B))
        q[bmask] += mass
    child_average = 0.0
    for z in assignments(len(A)):
        child, _ = restrict_values(values, n, A, z)
        child_spec = spectrum(child, [bias[i] for i in B])
        branch = point_prob(z, [bias[i] for i in A])
        child_average += branch * entropy(child_spec.values())
    H_parent = entropy(spec.values())
    H_q = entropy(q)
    M = H_parent - H_q
    J = H_q - child_average
    L = H_parent - child_average
    Delta = sum(
        entropy((p, 1.0 - p)) + log2(max(p, 1.0 - p))
        for i, p in enumerate(bias) if i in A
    )
    return M, J, L, Delta, sum(spec.values()), sum(q)


def all_blocks(n):
    for r in range(1, n + 1):
        for A in combinations(range(n), r):
            yield A


checks = 0
max_identity_error = 0.0
max_bound_violation = -1e100

# Exhaust all Boolean truth tables through three variables at deterministic
# nonuniform bias vectors, including endpoints close enough to stress scaling.
bias_families = {
    1: [(0.125,), (0.37,), (0.81,)],
    2: [(0.125, 0.25), (0.2, 0.7), (0.49, 0.91)],
    3: [(0.125, 0.25, 0.75), (0.2, 0.7, 0.41), (0.49, 0.91, 0.03)],
}
for n in (1, 2, 3):
    N = 1 << n
    for truth_mask in range(1 << N):
        values = [1.0 if truth_mask >> j & 1 else -1.0 for j in range(N)]
        for bias in bias_families[n]:
            for A in all_blocks(n):
                M, J, L, Delta, mass, qmass = ledger(values, bias, A)
                err = max(abs(mass - 1.0), abs(qmass - 1.0), abs(L - M - J))
                max_identity_error = max(max_identity_error, err)
                max_bound_violation = max(max_bound_violation, J - M - Delta)
                assert err < 2e-12
                assert J >= -2e-12
                assert J <= M + Delta + 2e-12
                checks += 1


# Exact-product additivity for aligned blocks.  This is the accepted transfer
# scope; it is deliberately not generalized to arbitrary Boolean composition.
bias1, bias2 = (0.2, 0.65), (0.3,)
for mask1 in range(16):
    f1 = [1.0 if mask1 >> j & 1 else -1.0 for j in range(4)]
    for mask2 in range(4):
        f2 = [1.0 if mask2 >> j & 1 else -1.0 for j in range(2)]
        vals = []
        for x in assignments(3):
            j1 = x[0] * 2 + x[1]
            j2 = x[2]
            vals.append(f1[j1] * f2[j2])
        one = ledger(f1, bias1, (0,))
        two = ledger(f2, bias2, (0,))
        both = ledger(vals, bias1 + bias2, (0, 2))
        for j in range(4):
            assert abs(both[j] - one[j] - two[j]) < 3e-12
        checks += 1


# General biased-AND formulas and the endpoint lower bound.
def h2(t):
    return entropy((t, 1.0 - t))


q = 0.25
a = 4.0 * q * (1.0 - q)
b = 4.0 * q * q
ratios = []
for k in range(4, 51):
    p = 2.0 ** (-k)
    masses = (
        (1.0 - 2.0 * p * q) ** 2,
        4.0 * q * q * p * (1.0 - p),
        4.0 * p * p * q * (1.0 - q),
        4.0 * p * (1.0 - p) * q * (1.0 - q),
    )
    M = entropy(masses) - h2(a * p)
    J = h2(a * p) - p * h2(a)
    scale = p * log2(1.0 / p)
    ratios.append((k, (J - M) / scale))
    assert abs(sum(masses) - 1.0) < 2e-15
    checks += 1

assert a - b == 0.5
assert abs(ratios[-1][1] - 0.5) < 0.04

print(f"small_boolean_and_tensor_checks={checks}")
print(f"max_ledger_identity_error={max_identity_error:.3e}")
print(f"max_MU_bound_violation={max_bound_violation:.3e}")
print("and_endpoint_leading_coefficient=1/2")
for k, ratio in ratios[::8]:
    print(f"  p=2^-{k}: (J-M)/(p log2(1/p))={ratio:.12f}")
print(f"  p=2^-50: (J-M)/(p log2(1/p))={ratios[-1][1]:.12f}")
print("RESULT=PASS")
