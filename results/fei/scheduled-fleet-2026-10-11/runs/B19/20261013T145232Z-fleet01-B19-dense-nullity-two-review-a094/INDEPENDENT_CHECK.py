#!/usr/bin/env python3
"""Independent reconstruction of B05 dense-nullity-two A023 claims."""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import log2
import random

SEED = 0xB19A0942
rng = random.Random(SEED)


def parity(z):
    return z.bit_count() & 1


def rank_masks(rows, m):
    a = list(rows)
    out = 0
    for j in range(m):
        p = next((i for i in range(out, len(a)) if (a[i] >> j) & 1), None)
        if p is None:
            continue
        a[out], a[p] = a[p], a[out]
        for i in range(len(a)):
            if i != out and ((a[i] >> j) & 1):
                a[i] ^= a[out]
        out += 1
    return out


def walsh(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for z in range(0, len(a), 2 * h):
            for j in range(z, z + h):
                a[j], a[j + h] = a[j] + a[j + h], a[j] - a[j + h]
        h *= 2
    return a


def law(vals):
    den = len(vals) ** 2
    return [Fraction(c * c, den) for c in walsh(vals)]


def H(vals):
    return sum(float(-q) * log2(float(q)) for q in law(vals) if q)


def U(vals):
    p = law(vals)
    n = len(vals).bit_length() - 1
    cap = p[:]
    for j in range(n):
        for s in range(1 << n):
            if not ((s >> j) & 1):
                cap[s] += cap[s | (1 << j)]
    return sum(float(q) * log2(float(cap[s] / q)) for s, q in enumerate(p) if q)


def directional_inf(vals, j):
    n = len(vals).bit_length() - 1
    return Fraction(sum(vals[z] != vals[z ^ (1 << j)] for z in range(1 << n)), 1 << n)


def I(vals):
    n = len(vals).bit_length() - 1
    return sum((directional_inf(vals, j) for j in range(n)), Fraction(0))


def restrict(vals, j, bit):
    n = len(vals).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << j) - 1)
        hi = z >> j
        out.append(vals[lo | (bit << j) | (hi << (j + 1))])
    return out


def shield(rows, m, dvals, a=0, b=0, c=0):
    s = len(rows)
    out = []
    for z in range(1 << (s + m)):
        x = z & ((1 << s) - 1)
        y = z >> s
        q = parity(a & x) ^ parity(b & y) ^ c
        for i, row in enumerate(rows):
            if (x >> i) & 1:
                q ^= parity(row & y)
        out.append((-1 if q else 1) * dvals[y])
    return out


def random_pruned_tree(vals, labels, stop=0.30):
    if not labels or rng.random() < stop:
        return [(Fraction(1), vals)], Fraction(0), 0.0
    pos = rng.randrange(len(labels))
    j = pos
    root_inf = directional_inf(vals, j)
    root_du = U(vals) - (U(restrict(vals, j, 0)) + U(restrict(vals, j, 1))) / 2
    leaves = []
    paid = root_inf
    charge = root_du
    next_labels = labels[:pos] + labels[pos + 1:]
    for bit in (0, 1):
        ls, sub_paid, sub_charge = random_pruned_tree(restrict(vals, j, bit), next_labels, stop)
        leaves.extend((w / 2, f) for w, f in ls)
        paid += sub_paid / 2
        charge += sub_charge / 2
    return leaves, paid, charge


def tensor(f, g):
    return [f[x] * g[y] for y in range(len(g)) for x in range(len(f))]


# 1. Exhaust the exact two-bit directional fiber inequality for every Boolean E
# and every subset of the two physical directions.
fiber_checks = 0
for mask in range(16):
    e = [1 if (mask >> z) & 1 else -1 for z in range(4)]
    for k in range(3):
        for Z in combinations(range(2), k):
            rhs = 2 - k + 2 * sum(float(directional_inf(e, j)) for j in Z)
            assert H(e) <= rhs + 1e-13
            fiber_checks += 1


# 2. Exhaust every rank-one orientation at m=3, every core modulo complement,
# and every affine spectral translation a,b. This is deliberately stronger
# than the author's finite test, which fixed a=b=0.
root_checks = 0
max_u_i = (0.0, None)
for row in range(1, 8):
    for mask in range(128):
        d = [1 if (mask >> y) & 1 else -1 for y in range(8)]
        for a in range(2):
            for b in range(8):
                f = shield([row], 3, d, a=a, b=b)
                h, u, ii = H(f), U(f), I(f)
                assert u <= h + 2e-12
                assert h <= 2 * float(ii) + 2e-12
                ratio = u / float(ii) if ii else 0.0
                if ratio > max_u_i[0]:
                    max_u_i = (ratio, (row, mask, a, b, h, u, ii))
                root_checks += 1


# 3. Cover every rank-two 2x4 physical orientation with independently sampled
# cores and affine phases; check root reservoir and random adaptive pruning.
tree_checks = 0
influence_telescopes = 0
rank2_matrices = 0
for r0 in range(16):
    for r1 in range(16):
        if rank_masks([r0, r1], 4) != 2:
            continue
        rank2_matrices += 1
        for _ in range(10):
            d = [rng.choice((-1, 1)) for _ in range(16)]
            a = rng.randrange(4)
            b = rng.randrange(16)
            f = shield([r0, r1], 4, d, a=a, b=b)
            h, u, ii = H(f), U(f), I(f)
            assert u <= h + 3e-12 <= 2 * float(ii) + 5e-12
            ratio = u / float(ii) if ii else 0.0
            if ratio > max_u_i[0]:
                max_u_i = (ratio, (r0, r1, d, a, b, h, u, ii))
            leaves, paid, charge = random_pruned_tree(f, list(range(6)))
            leaf_u = sum(float(w) * U(g) for w, g in leaves)
            leaf_i = sum(w * I(g) for w, g in leaves)
            assert abs(charge - (u - leaf_u)) < 3e-11
            assert paid + leaf_i == ii
            assert charge <= 2 * float(ii) + 3e-11
            tree_checks += 1
            influence_telescopes += 1


# 4. Common disjoint terminal cores cancel at a one-node restriction, including
# affine-shifted roots. Tensor ordering puts the first factor in low bits.
tensor_checks = 0
for _ in range(200):
    row = rng.randrange(1, 8)
    d = [rng.choice((-1, 1)) for _ in range(8)]
    f = shield([row], 3, d, a=rng.randrange(2), b=rng.randrange(8))
    g = [rng.choice((-1, 1)) for _ in range(8)]
    j = rng.randrange(4)
    fg = tensor(f, g)
    lhs = U(fg) - sum(U(restrict(fg, j, bit)) for bit in (0, 1)) / 2
    rhs = U(f) - sum(U(restrict(f, j, bit)) for bit in (0, 1)) / 2
    assert abs(lhs - rhs) < 3e-11
    tensor_checks += 1


# 5. Reconstruct the rank-release boundary and its coefficient-two failure.
rows = [0b0011, 0b0100]
d = []
for y in range(16):
    bad = ((y >> 0) & 1) == 0 and ((y >> 2) & 1) == 0 and ((y >> 3) & 1) == 0
    d.append(-1 if bad else 1)
f = shield(rows, 4, d)
child0 = restrict(f, 1, 0)
child1 = restrict(f, 1, 1)
boundary_gap = max(H(child0) - 2 * float(I(child0)), H(child1) - 2 * float(I(child1)))
formula_gap = -Fraction(1, 4) + Fraction(9, 16) * log2(Fraction(16, 9))
assert boundary_gap > 0.2169
assert abs(boundary_gap - float(formula_gap)) < 2e-12


print(f"seed={SEED}")
print(f"two_bit_fiber_checks={fiber_checks}")
print(f"affine_phase_exhaustive_root_checks={root_checks}")
print(f"rank_two_matrices={rank2_matrices}")
print(f"adaptive_pruned_tree_checks={tree_checks}")
print(f"influence_telescope_checks={influence_telescopes}")
print(f"common_disjoint_core_checks={tensor_checks}")
print(f"max_U_over_I={max_u_i[0]:.15f}")
print(f"max_U_over_I_witness={max_u_i[1]}")
print(f"nullity_three_child_H_minus_2I={boundary_gap:.15f}")
print("PASS")
