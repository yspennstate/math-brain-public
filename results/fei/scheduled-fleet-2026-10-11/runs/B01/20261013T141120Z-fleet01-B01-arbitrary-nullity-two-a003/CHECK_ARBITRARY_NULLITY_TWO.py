#!/usr/bin/env python3
"""Direct Walsh checks for the arbitrary-orientation nullity-two theorem.

Bits are in F_2 and Boolean values are in {-1,+1}.  The finite search is
supporting evidence only; PROOF.md contains the all-parameter argument.
"""

from fractions import Fraction
from itertools import product
from math import log2
import random


SEED = 0xB01A0032
rng = random.Random(SEED)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) & 1


def rank(rows):
    if not rows:
        return 0
    a = [sum(bit << j for j, bit in enumerate(row)) for row in rows]
    out = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(out, len(a)) if (a[i] >> j) & 1), None)
        if pivot is None:
            continue
        a[out], a[pivot] = a[pivot], a[out]
        for i in range(len(a)):
            if i != out and ((a[i] >> j) & 1):
                a[i] ^= a[out]
        out += 1
    return out


def entropy(probs):
    return sum(-p * log2(p) for p in probs if p)


def walsh_entropy(vals):
    n = (len(vals)).bit_length() - 1
    coeffs = []
    for mask in range(1 << n):
        total = 0
        for x in range(1 << n):
            total += vals[x] * (-1 if ((mask & x).bit_count() & 1) else 1)
        coeffs.append(Fraction(total * total, (1 << n) ** 2))
    return entropy([float(q) for q in coeffs]), coeffs


def total_influence(vals):
    n = (len(vals)).bit_length() - 1
    ans = Fraction(0)
    for j in range(n):
        changes = sum(vals[x] != vals[x ^ (1 << j)] for x in range(1 << n))
        ans += Fraction(changes, 1 << n)
    return ans


def upper_u(vals):
    n = (len(vals)).bit_length() - 1
    _, coeffs = walsh_entropy(vals)
    p = [float(q) for q in coeffs]
    pi = p[:]
    for j in range(n):
        for s in range(1 << n):
            if not ((s >> j) & 1):
                pi[s] += pi[s | (1 << j)]
    return sum(x * log2(pi[s] / x) for s, x in enumerate(p) if x)


def global_u(vals):
    n = (len(vals)).bit_length() - 1
    u = upper_u(vals)
    g = 0.0
    for j in range(n):
        child_u = []
        for bit in (0, 1):
            child = [vals[x] for x in range(1 << n) if ((x >> j) & 1) == bit]
            child_u.append(upper_u(child))
        g += u - sum(child_u) / 2
    return u, g


def exact_dyadic_u(vals):
    """Exact U when every nonzero upper-mass/atom ratio is a power of two."""
    n = (len(vals)).bit_length() - 1
    _, p = walsh_entropy(vals)
    pi = p[:]
    for j in range(n):
        for s in range(1 << n):
            if not ((s >> j) & 1):
                pi[s] += pi[s | (1 << j)]
    ans = Fraction(0)
    for s, x in enumerate(p):
        if not x:
            continue
        q = pi[s] / x
        num, den = q.numerator, q.denominator
        assert num & (num - 1) == 0 and den & (den - 1) == 0
        ans += x * ((num.bit_length() - 1) - (den.bit_length() - 1))
    return ans


def build_phase(rows, dvals):
    s, m = len(rows), len(rows[0]) if rows else 2
    vals = []
    for w in range(1 << (s + m)):
        x = tuple((w >> j) & 1 for j in range(s))
        y = tuple((w >> (s + j)) & 1 for j in range(m))
        phase = 0
        for i in range(s):
            if x[i]:
                phase ^= dot(rows[i], y)
        vals.append((1 if phase == 0 else -1) * dvals[sum(y[j] << j for j in range(m))])
    return vals


def all_rank_rows(s, m, target):
    for flat in product((0, 1), repeat=s * m):
        rows = [flat[i * m:(i + 1) * m] for i in range(s)]
        if rank(rows) == target:
            yield rows


def check_two_bit_lemma():
    checked = 0
    for mask in range(1 << 4):
        vals = [1 if (mask >> x) & 1 else -1 for x in range(4)]
        h, _ = walsh_entropy(vals)
        infs = []
        for j in range(2):
            changes = sum(vals[x] != vals[x ^ (1 << j)] for x in range(4))
            infs.append(Fraction(changes, 4))
        for k in range(3):
            rhs = 2 - k + 2 * sum(infs[:k])
            assert h <= float(rhs) + 1e-12
            checked += 1
    return checked


def check_case(rows, dvals):
    vals = build_phase(rows, dvals)
    h, _ = walsh_entropy(vals)
    inf = total_influence(vals)
    assert h <= 2 * float(inf) + 2e-11, (rows, dvals, h, inf)
    u, g = global_u(vals)
    return h / float(inf) if inf else 0.0, g / float(inf) if inf else 0.0, len(vals)


lemma_checks = check_two_bit_lemma()
cases = 0
walsh_atoms = 0
max_ratio = 0.0
max_gu_ratio = 0.0

# Exhaust all two-bit functions (rank zero).
for mask in range(1 << 3):  # one representative modulo output complement
    d = [1 if (mask >> x) & 1 else -1 for x in range(4)]
    ratio, gu_ratio, atoms = check_case([], d)
    cases += 1
    walsh_atoms += atoms
    max_ratio = max(max_ratio, ratio)
    max_gu_ratio = max(max_gu_ratio, gu_ratio)

# Exhaust all rank-one orientations on three y bits and every Boolean core.
for rows in all_rank_rows(1, 3, 1):
    for mask in range(1 << 7):  # representatives modulo output complement
        d = [1 if (mask >> x) & 1 else -1 for x in range(8)]
        ratio, gu_ratio, atoms = check_case(rows, d)
        cases += 1
        walsh_atoms += atoms
        max_ratio = max(max_ratio, ratio)
        max_gu_ratio = max(max_gu_ratio, gu_ratio)

# Every 2x4 rank-two orientation, with deterministic random and structured cores.
for rows in all_rank_rows(2, 4, 2):
    cores = []
    cores.append([1] * 16)
    cores.append([-1 if x == 0 else 1 for x in range(16)])
    for _ in range(30):
        cores.append([rng.choice((-1, 1)) for _ in range(16)])
    for d in cores:
        ratio, gu_ratio, atoms = check_case(rows, d)
        cases += 1
        walsh_atoms += atoms
        max_ratio = max(max_ratio, ratio)
        max_gu_ratio = max(max_gu_ratio, gu_ratio)

# An exact six-bit GU witness within the theorem's class.  All relevant
# upper-mass/atom ratios are powers of two, so no floating logarithms enter.
gu_rows = [(0, 1, 1, 0), (1, 1, 0, 1)]
gu_mask = 18398
gu_d = [1 if (gu_mask >> x) & 1 else -1 for x in range(16)]
gu_vals = build_phase(gu_rows, gu_d)
gu_I = total_influence(gu_vals)
gu_H, _ = walsh_entropy(gu_vals)
gu_U = exact_dyadic_u(gu_vals)
gu_G = Fraction(0)
for j in range(6):
    child_u = []
    for bit in (0, 1):
        child = [gu_vals[x] for x in range(64) if ((x >> j) & 1) == bit]
        child_u.append(exact_dyadic_u(child))
    gu_G += gu_U - sum(child_u) / 2
assert gu_H == 6.0 and gu_U == 3 and gu_I == 3
assert gu_G == Fraction(277, 32)
assert gu_G > 2 * gu_I and gu_G < 3 * gu_I
max_gu_ratio = max(max_gu_ratio, float(gu_G / gu_I))

# Exact nullity-three boundary witness: M=[1,1,0,0], one point defect per coset.
rows = [(1, 1, 0, 0)]
d = []
for y in range(16):
    y1, y2, y3, y4 = ((y >> j) & 1 for j in range(4))
    d.append(-1 if (y1 == 0 and y3 == 0 and y4 == 0) else 1)
vals = build_phase(rows, d)
h3, masses3 = walsh_entropy(vals)
i3 = total_influence(vals)
expected_h3 = Fraction(15, 4) + Fraction(9, 16) * log2(Fraction(16, 9))
assert i3 == 2
assert abs(h3 - float(expected_h3)) < 2e-12
assert h3 > 2 * float(i3) + 0.21
mass_hist = {}
for q in masses3:
    mass_hist[str(q)] = mass_hist.get(str(q), 0) + 1

print(f"seed={SEED}")
print(f"two_bit_directional_lemma_checks={lemma_checks}")
print(f"nullity_two_direct_cases={cases}")
print(f"direct_truth_table_atoms={walsh_atoms}")
print(f"maximum_H_over_I={max_ratio:.15f}")
print(f"maximum_sampled_G_over_I={max_gu_ratio:.15f}")
print(f"exact_GU_witness_truth_mask={gu_mask}")
print(f"exact_GU_witness_H={gu_H:.0f}")
print(f"exact_GU_witness_U={gu_U}")
print(f"exact_GU_witness_I={gu_I}")
print(f"exact_GU_witness_G={gu_G}")
print(f"exact_GU_witness_G_over_I={gu_G / gu_I}")
print(f"nullity_three_witness_I={i3}")
print(f"nullity_three_witness_H={h3:.15f}")
print(f"nullity_three_witness_H_minus_2I={h3 - 2 * float(i3):.15f}")
print(f"nullity_three_witness_mass_histogram={mass_hist}")
print("PASS")
