#!/usr/bin/env python3
"""Independent exact audit of B05's nullity-one shield theorem.

This program was written from the theorem statement, not adapted from the
author's checker.  All Walsh and influence calculations are integer exact.
Floating point is used only to evaluate U from exact dyadic masses in the
small adaptive-tree stress test; those inequalities have a large exact
analytic margin and are not the proof.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import log2
from random import Random


SEED = 0xB19A094
rng = Random(SEED)


def dot(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(x & y for x, y in zip(a, b)) & 1


def rank2(rows: tuple[tuple[int, ...], ...], m: int) -> int:
    a = [sum(bit << j for j, bit in enumerate(row)) for row in rows]
    rank = 0
    for j in range(m):
        pivot = next((k for k in range(rank, len(a)) if (a[k] >> j) & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for k in range(len(a)):
            if k != rank and ((a[k] >> j) & 1):
                a[k] ^= a[rank]
        rank += 1
    return rank


def mat_vec(M: tuple[tuple[int, ...], ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(dot(row, y) for row in M)


def truth_table(M, D, a, b, c=0):
    s, m = len(M), len(M[0])
    out = {}
    for x in product((0, 1), repeat=s):
        for y in product((0, 1), repeat=m):
            phase = dot(x, mat_vec(M, y)) ^ dot(a, x) ^ dot(b, y) ^ c
            out[x + y] = D[y] * (-1 if phase else 1)
    return out


def walsh_numerators(table: dict[tuple[int, ...], int]):
    keys = tuple(table)
    n = len(keys[0]) if keys else 0
    return {
        alpha: sum(val * (-1 if dot(alpha, z) else 1) for z, val in table.items())
        for alpha in product((0, 1), repeat=n)
    }


def influences_numerators(table):
    keys = tuple(table)
    n = len(keys[0]) if keys else 0
    N = len(keys)
    ans = []
    for i in range(n):
        changes = 0
        for z in keys:
            zz = z[:i] + (z[i] ^ 1,) + z[i + 1 :]
            changes += table[z] != table[zz]
        ans.append(Fraction(changes, N))
    return ans


def spectral_masses(table):
    N = len(table)
    nums = walsh_numerators(table)
    return {S: Fraction(v * v, N * N) for S, v in nums.items() if v}


def upper_set_U(masses):
    total = 0.0
    for S, p in masses.items():
        pi = sum(q for T, q in masses.items() if all(not bit or T[i] for i, bit in enumerate(S)))
        total += float(p) * log2(float(pi / p))
    return total


def entropy(masses):
    return sum(float(p) * log2(float(1 / p)) for p in masses.values())


def restrict_table(table, assignment):
    """Return truth table after fixing original coordinate indices."""
    n = len(next(iter(table)))
    keep = tuple(i for i in range(n) if i not in assignment)
    return {
        tuple(z[i] for i in keep): val
        for z, val in table.items()
        if all(z[i] == bit for i, bit in assignment.items())
    }


def random_tree_leaves(table, max_depth):
    """Build a genuinely branch-dependent pruned physical restriction tree."""
    n = len(next(iter(table)))
    leaves = []

    def rec(assignment, depth):
        remaining = [i for i in range(n) if i not in assignment]
        if depth >= max_depth or not remaining or rng.random() < 0.28:
            leaves.append((Fraction(1, 2 ** len(assignment)), restrict_table(table, assignment)))
            return
        i = rng.choice(remaining)
        for bit in (0, 1):
            nxt = dict(assignment)
            nxt[i] = bit
            rec(nxt, depth + 1)

    rec({}, 0)
    return leaves


def tensor_table(f, g):
    return {x + y: fx * gy for x, fx in f.items() for y, gy in g.items()}


counts = {
    "matrices": 0,
    "cores": 0,
    "formula_spectra": 0,
    "direct_walsh": 0,
    "direct_atoms": 0,
    "physical_influence": 0,
    "adaptive_trees": 0,
    "tensor_checks": 0,
}
max_u_over_ix = 0.0
max_u_over_itotal = 0.0


# Exhaust every rank-(m-1) matrix and Boolean core through m,s <= 3.  The
# closed form is evaluated from the two-point fibers, independently of a
# truth-table Walsh transform.
for m in range(1, 4):
    r = m - 1
    for s in range(max(1, r), 4):
        for raw in product((0, 1), repeat=s * m):
            M = tuple(tuple(raw[i * m + j] for j in range(m)) for i in range(s))
            if rank2(M, m) != r:
                continue
            counts["matrices"] += 1
            ys = tuple(product((0, 1), repeat=m))
            # Exhaust all cores for m <= 3.
            for signs in product((-1, 1), repeat=1 << m):
                D = dict(zip(ys, signs))
                counts["cores"] += 1
                # Two affine phases suffice for the exhaustive fiber-shape
                # check; direct reconstruction below samples all phase bits.
                for a, b in (
                    ((0,) * s, (0,) * m),
                    ((1,) * s, tuple(j & 1 for j in range(m))),
                ):
                    masses = []
                    for alpha in product((0, 1), repeat=s):
                        fiber = [y for y in ys if mat_vec(M, y) == tuple(a[i] ^ alpha[i] for i in range(s))]
                        if not fiber:
                            continue
                        assert len(fiber) == 2
                        for beta in product((0, 1), repeat=m):
                            num = sum(D[y] * (-1 if dot(tuple(b[j] ^ beta[j] for j in range(m)), y) else 1) for y in fiber)
                            if num:
                                assert abs(num) == 2
                                masses.append(Fraction(num * num, 1 << (2 * m)))
                    assert len(masses) == 1 << (2 * r)
                    assert set(masses) == {Fraction(1, 1 << (2 * r))}
                    assert sum(masses) == 1
                    counts["formula_spectra"] += 1


# Independent direct Walsh and physical-influence reconstruction on a fixed,
# reproducible sample spanning kernel orientations, affine phases and cores.
candidate_instances = []
for m in range(1, 4):
    r = m - 1
    for s in range(max(1, r), 4):
        matrices = []
        for raw in product((0, 1), repeat=s * m):
            M = tuple(tuple(raw[i * m + j] for j in range(m)) for i in range(s))
            if rank2(M, m) == r:
                matrices.append(M)
        rng.shuffle(matrices)
        for M in matrices[: min(24, len(matrices))]:
            ys = tuple(product((0, 1), repeat=m))
            for _ in range(12):
                D = {y: rng.choice((-1, 1)) for y in ys}
                a = tuple(rng.randrange(2) for _ in range(s))
                b = tuple(rng.randrange(2) for _ in range(m))
                candidate_instances.append((M, D, a, b, rng.randrange(2)))

for M, D, a, b, c in candidate_instances:
    s, m = len(M), len(M[0])
    r = m - 1
    table = truth_table(M, D, a, b, c)
    masses = spectral_masses(table)
    assert len(masses) == 1 << (2 * r)
    assert set(masses.values()) == {Fraction(1, 1 << (2 * r))}
    assert abs(entropy(masses) - 2 * r) < 1e-12
    u = upper_set_U(masses)
    assert u <= 2 * r + 1e-12
    infl = influences_numerators(table)
    Ix = sum(infl[:s], Fraction())
    Iy = sum(infl[s:], Fraction())
    nonzero_rows = sum(any(row) for row in M)
    nonzero_cols = sum(any(M[i][j] for i in range(s)) for j in range(m))
    assert nonzero_rows >= r and nonzero_cols >= r
    for i, row in enumerate(M):
        if any(row):
            assert infl[i] == Fraction(1, 2)
    for j in range(m):
        if any(M[i][j] for i in range(s)):
            assert infl[s + j] == Fraction(1, 2)
    assert Ix >= Fraction(r, 2) and Iy >= Fraction(r, 2)
    assert u <= 4 * float(Ix) + 1e-12
    assert u <= 2 * float(Ix + Iy) + 1e-12
    if Ix:
        max_u_over_ix = max(max_u_over_ix, u / float(Ix))
    if Ix + Iy:
        max_u_over_itotal = max(max_u_over_itotal, u / float(Ix + Iy))
    counts["direct_walsh"] += 1
    counts["direct_atoms"] += len(masses)
    counts["physical_influence"] += 1


# Endpoint telescoping / pruning stress test.  This deliberately does not
# assert nodewise sign or ownership: the theorem needs only root U minus the
# weighted nonnegative leaf U.
for M, D, a, b, c in candidate_instances[:400]:
    table = truth_table(M, D, a, b, c)
    root_u = upper_set_U(spectral_masses(table))
    leaves = random_tree_leaves(table, max_depth=min(4, len(next(iter(table)))))
    assert sum(w for w, _ in leaves) == 1
    leaf_u = sum(float(w) * upper_set_U(spectral_masses(t)) for w, t in leaves)
    lhs = root_u - leaf_u
    assert lhs <= root_u + 1e-12
    s = len(M)
    infl = influences_numerators(table)
    Ix = sum(infl[:s], Fraction())
    It = sum(infl, Fraction())
    assert lhs <= 4 * float(Ix) + 1e-12
    assert lhs <= 2 * float(It) + 1e-12
    counts["adaptive_trees"] += 1


# Directly verify the common disjoint terminal-core cancellation on random
# small Boolean factors, including restricted leaves.
for M, D, a, b, c in candidate_instances[:240]:
    table = truth_table(M, D, a, b, c)
    q = 1 + rng.randrange(3)
    h = {z: rng.choice((-1, 1)) for z in product((0, 1), repeat=q)}
    up = upper_set_U(spectral_masses(table))
    uh = upper_set_U(spectral_masses(h))
    assert abs(upper_set_U(spectral_masses(tensor_table(table, h))) - (up + uh)) < 2e-11
    assignment = {}
    n = len(next(iter(table)))
    for i in rng.sample(range(n), k=min(2, n)):
        assignment[i] = rng.randrange(2)
    leaf = restrict_table(table, assignment)
    ul = upper_set_U(spectral_masses(leaf))
    assert abs(upper_set_U(spectral_masses(tensor_table(leaf, h))) - (ul + uh)) < 2e-11
    counts["tensor_checks"] += 2


print("PASS")
print(f"seed={SEED}")
for key, value in counts.items():
    print(f"{key}={value}")
print(f"max_sampled_U_over_Ix={max_u_over_ix:.12f}")
print(f"max_sampled_U_over_Itotal={max_u_over_itotal:.12f}")
