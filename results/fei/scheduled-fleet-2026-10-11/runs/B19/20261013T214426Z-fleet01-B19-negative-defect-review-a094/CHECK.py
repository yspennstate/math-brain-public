#!/usr/bin/env python3
"""Independent checks for the B05 negative point-defect tower review."""
from fractions import Fraction
from math import log2
import random

C = Fraction(5, 3)


def fwht(values):
    a = [Fraction(x) for x in values]
    width = 1
    while width < len(a):
        for left in range(0, len(a), 2 * width):
            for j in range(width):
                u, v = a[left + j], a[left + width + j]
                a[left + j], a[left + width + j] = u + v, u - v
        width *= 2
    return [x / len(a) for x in a]


def upper_potential(values):
    a = fwht(values)
    masses = [x * x for x in a]
    caps = masses[:]
    n = len(values).bit_length() - 1
    for j in range(n):
        bit = 1 << j
        for s in range(len(caps)):
            if s & bit == 0:
                caps[s] += caps[s | bit]
    u = 0.0
    influence = Fraction(0)
    for s, mass in enumerate(masses):
        if mass:
            u += float(mass) * log2(float(caps[s] / mass))
            influence += s.bit_count() * mass
    return u, influence


def product(f, g):
    return [a * b for a in f for b in g]


def half_activate(q):
    return [1 for _ in q] + q


def negative_defect(r):
    return [1] + [-1] * (2**r - 1)


def tower(base, ranks):
    current = half_activate(product([1, -1], base))
    for r in ranks:
        current = half_activate(product(negative_defect(r), current))
    return current


def scalar_R(t):
    def h(x):
        return 0.0 if x == 0 else x * log2(1 / x)
    a = (1 + t) ** 2 / 4
    b = (1 - t) ** 2 / 4
    return h(a) + b * log2(2 / (1 - t)) - h(t * t) / 2 + (1 - t * t) / 4


def restrict(values, coordinate, sign):
    n = len(values).bit_length() - 1
    mask = 1 << (n - 1 - coordinate)
    selected = 0 if sign == 1 else mask
    return [v for i, v in enumerate(values) if i & mask == selected]


def walk(values, remaining, depth, weight, seed):
    # Deterministic adaptive pruning distinct from the author's policy.
    if not remaining or depth >= 5 or ((seed + depth + values[-1]) % 5 == 0):
        return [], [(weight, values)]
    pick = (seed + 3 * depth + (1 if values[0] > 0 else 0)) % len(remaining)
    coordinate = remaining[pick]
    charges = []
    leaves = []
    parent_u = upper_potential(values)[0]
    children = []
    for sign in (1, -1):
        child = restrict(values, coordinate, sign)
        children.append(child)
    charges.append(weight * (parent_u - (upper_potential(children[0])[0]
                                          + upper_potential(children[1])[0]) / 2))
    # Coordinate indices shift after restriction.
    next_remaining = [x - (x > coordinate) for x in remaining if x != coordinate]
    for branch, child in enumerate(children):
        c, l = walk(child, next_remaining, depth + 1, weight / 2,
                    seed * 7 + branch + 1)
        charges.extend(c)
        leaves.extend(l)
    return charges, leaves


# Exact certificates used in the analytic strengthening.
assert 7**5 > 2**14                 # log_2 7 > 14/5
assert 3**12 > 2**19                # log_2 3 > 19/12
assert 7**49 > 2**137               # rank-four block bound
r_eighth_upper = Fraction(2361, 2560)
assert r_eighth_upper < Fraction(15, 16)

# Block ratios over a range far beyond the direct truth-table tests.
max_block = (0.0, None)
for r in range(2, 501):
    p = 2.0 ** (-r)
    beta = 1 - 2 * p
    influence = 2 * r * p
    u = beta * beta * log2(1 / (beta * beta)) + influence * beta
    ratio = u / influence
    if ratio > max_block[0]:
        max_block = (ratio, r)
    assert ratio < 5 / 3

# Scalar payment on the full interval used by the theorem.
scalar_max = (-1.0, None)
for j in range(200001):
    s = 1 / 8 + (3 / 8) * j / 200000
    value = scalar_R(-s)
    if value > scalar_max[0]:
        scalar_max = (value, s)
    assert value <= (5 / 3) * (1 + s) / 2 + 1e-13

# Exhaust all 3-bit Boolean bases and several nonstationary towers.
direct_cases = 0
max_direct = 0.0
sequences = [(), (2,), (3,), (4,), (2, 2)]
for code in range(256):
    base = [1 if (code >> x) & 1 else -1 for x in range(8)]
    ub, ib = upper_potential(base)
    if ub > (5 / 3) * float(ib) + 1e-13:
        continue
    for seq in sequences:
        f = tower(base, seq)
        u, influence = upper_potential(f)
        ratio = 0.0 if influence == 0 else u / float(influence)
        max_direct = max(max_direct, ratio)
        assert u <= (5 / 3) * float(influence) + 2e-11
        direct_cases += 1

# Long arbitrary-rank recurrence stress test (not a proof).
rng = random.Random(20261013)
state_cases = 0
worst_deficit = -1e100
for _ in range(20000):
    influence = 0.25 + 8 * rng.random()
    u = (5 / 3) * influence * rng.random()
    # First balanced level.
    u = 1 + u / 2
    influence = 1 + influence / 2
    mean = 0.5
    for _ in range(rng.randint(1, 60)):
        r = rng.randint(2, 80)
        p = 2.0 ** (-r)
        beta = 1 - 2 * p
        block_i = 2 * r * p
        block_u = beta * beta * log2(1 / (beta * beta)) + block_i * beta
        s = beta * mean
        u = u / 2 + block_u / 2 + scalar_R(-s)
        influence = influence / 2 + block_i / 2 + (1 + s) / 2
        mean = (1 - s) / 2
        deficit = u - (5 / 3) * influence
        worst_deficit = max(worst_deficit, deficit)
        assert deficit <= 2e-12
        state_cases += 1

# Adaptive/pruned tree telescopes and disjoint terminal cancellation.
tree_cases = 0
max_tree_error = 0.0
terminal = [-1, 1, 1, 1]
for code in range(16):
    base = [1 if (code >> x) & 1 else -1 for x in range(4)]
    f = tower(base, (2,))
    root_u, root_i = upper_potential(f)
    n = len(f).bit_length() - 1
    for seed in range(8):
        charges, leaves = walk(f, list(range(n)), 0, Fraction(1), seed)
        leaf_u = sum(float(w) * upper_potential(g)[0] for w, g in leaves)
        telescope_error = abs(sum(charges) - (root_u - leaf_u))
        root_terminal = upper_potential(product(f, terminal))[0]
        leaf_terminal = sum(float(w) * upper_potential(product(g, terminal))[0]
                            for w, g in leaves)
        cancel_error = abs((root_terminal - leaf_terminal) - (root_u - leaf_u))
        max_tree_error = max(max_tree_error, telescope_error, cancel_error)
        assert telescope_error < 2e-10
        assert cancel_error < 2e-10
        assert root_u - leaf_u <= (5 / 3) * float(root_i) + 2e-11
        tree_cases += 1

print("exact_log_certificates=4 status=PASS")
print(f"block_ranks=2..500 max_ratio={max_block[0]:.12f} at_r={max_block[1]}")
print(f"scalar_grid_points=200001 max_R={scalar_max[0]:.12f} at_s={scalar_max[1]:.8f}")
print(f"exhaustive_three_bit_direct_towers={direct_cases} max_ratio={max_direct:.12f}")
print(f"arbitrary_rank_recurrence_states={state_cases} worst_deficit={worst_deficit:.3e}")
print(f"adaptive_pruned_trees={tree_cases} max_telescope_error={max_tree_error:.3e}")
print("original_constant_16/9=ACCEPTED")
print("strengthened_constant_5/3=PASS_PENDING_FRESH_REVIEW")
print("FEI_corollary_constant_16/3")
