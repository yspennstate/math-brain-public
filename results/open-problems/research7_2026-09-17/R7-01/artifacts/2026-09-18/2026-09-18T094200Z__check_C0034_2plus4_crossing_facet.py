#!/usr/bin/env python3
"""Exact finite checks for the second genuinely colored C0034 facet orbit.

Uses only integer/Fraction arithmetic. It verifies the 90 ordered rainbow
perfect-matching vertices, ambient affine dimension, validity and facet rank of
the 2+4 cut crossing inequality, and its full S6 x S3 orbit size.
"""
from fractions import Fraction
from itertools import combinations, permutations

N = 6
COLORS = 3
EDGES = list(combinations(range(N), 2))
EI = {e: i for i, e in enumerate(EDGES)}


def rank_q(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z = A[i][c]
                A[i] = [A[i][j] - z * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def vec_for(A, B, C):
    x = [0] * (COLORS * len(EDGES))
    for color, e in enumerate((A, B, C)):
        x[color * 15 + EI[tuple(sorted(e))]] = 1
    return x


verts = []
for A in EDGES:
    rem = [v for v in range(N) if v not in A]
    for B in combinations(rem, 2):
        C = tuple(sorted(set(rem) - set(B)))
        B = tuple(sorted(B))
        verts.append(vec_for(A, B, C))
assert len(verts) == 90

base = verts[0]
aff_rank = rank_q([[a - b for a, b in zip(v, base)] for v in verts[1:]])
lin_rank = rank_q(verts)
print("vertex_count=", len(verts))
print("linear_rank=", lin_rank)
print("affine_dimension=", aff_rank)
assert lin_rank == 38
assert aff_rank == 37

# Canonical 2+4 cut X|Y and singled color 0.
X = frozenset({0, 1})
CROSS = {e for e in EDGES if ((e[0] in X) ^ (e[1] in X))}


def ccut(v, color):
    return sum(v[color * 15 + EI[e]] for e in CROSS)


gaps = []
tight = []
for v in verts:
    # c_0 <= c_1 + c_2
    g = ccut(v, 1) + ccut(v, 2) - ccut(v, 0)
    assert g in (0, 2)
    assert g >= 0
    gaps.append(g)
    if g == 0:
        tight.append(v)

print("canonical_gap_counts=", {g: gaps.count(g) for g in sorted(set(gaps))})
print("tight_vertex_count=", len(tight))
face0 = tight[0]
face_rank = rank_q([[a - b for a, b in zip(v, face0)] for v in tight[1:]])
print("tight_face_affine_dimension=", face_rank)
assert len(tight) == 66
assert face_rank == 36
assert face_rank == aff_rank - 1


def coeff_for(cut, singled):
    cut = frozenset(cut)
    cross = {e for e in EDGES if ((e[0] in cut) ^ (e[1] in cut))}
    c = [0] * 45
    for color in range(3):
        sign = 1 if color == singled else -1
        for e in cross:
            c[color * 15 + EI[e]] = sign
    return tuple(c)


def apply(c, vertex_perm, color_perm):
    out = [0] * 45
    for color in range(3):
        for e in EDGES:
            val = c[color * 15 + EI[e]]
            ee = tuple(sorted((vertex_perm[e[0]], vertex_perm[e[1]])))
            cc = color_perm[color]
            out[cc * 15 + EI[ee]] = val
    return tuple(out)


canon = coeff_for({0, 1}, 0)
orbit = set()
for vp in permutations(range(6)):
    for cp in permutations(range(3)):
        orbit.add(apply(canon, vp, cp))

print("S6xS3_orbit_size=", len(orbit))
expected = {
    coeff_for(cut, color)
    for cut in combinations(range(6), 2)
    for color in range(3)
}
print("2plus4_cut_x_singled_count=", len(expected))
assert len(expected) == 45
assert orbit == expected

print("ALL_EXACT_CHECKS_PASS")
