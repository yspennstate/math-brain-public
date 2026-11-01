#!/usr/bin/env python3
"""Exact FOREST degree-4 boundary checker; standard library only.

Law: uniform over all unrooted forests, including disconnected forests,
the empty forest, and every size. Marked edges are v-0 and v-1, where
v is a degree-four vertex adjacent to terminals 0,1,2,3.
"""
from itertools import combinations
from fractions import Fraction


def partitions(xs):
    if not xs:
        yield []
        return
    x = xs[0]
    for p in partitions(xs[1:]):
        yield [{x}] + [set(b) for b in p]
        for i in range(len(p)):
            yield [set(b) if j != i else set(b) | {x} for j, b in enumerate(p)]


def canon(p):
    blocks = sorted((tuple(sorted(b)) for b in p), key=lambda b: b[0])
    return "|".join("".join(map(str, b)) for b in blocks)


PARTS = {canon(p): p for p in partitions(list(range(4)))}
NAMES = sorted(PARTS)


def block_of(p, i):
    return next(b for b in p if i in b)


def local_values(p):
    w = 1
    for b in p:
        w *= 1 + len(b)
    b0 = block_of(p, 0)
    b1 = block_of(p, 1)
    a = Fraction(w, 1 + len(b0))
    b = Fraction(w, 1 + len(b1))
    c = Fraction(0) if b0 is b1 else Fraction(w, (1 + len(b0)) * (1 + len(b1)))
    return Fraction(w), a, b, c


VAL = {n: local_values(PARTS[n]) for n in NAMES}


def coeff(n, m):
    w, a, b, c = VAL[n]
    W, A, B, C = VAL[m]
    if n == m:
        return a * b - w * c
    return a * B + A * b - w * C - W * c


neg, zero, pos = [], [], []
for i, n in enumerate(NAMES):
    for m in NAMES[i:]:
        q = coeff(n, m)
        (neg if q < 0 else zero if q == 0 else pos).append((n, m, q))

expected_neg = {
    ("0123", "0|1|23"): -3,
    ("0123", "0|1|2|3"): -4,
    ("02|13", "0|1|23"): -3,
    ("02|13", "0|1|2|3"): -4,
    ("03|12", "0|1|23"): -3,
    ("03|12", "0|1|2|3"): -4,
}
assert {(a, b): int(q) for a, b, q in neg} == expected_neg


def delta_from_vector(d):
    Z = E0 = E1 = E01 = 0
    for n in NAMES:
        q = d.get(n, 0)
        w, a, b, c = VAL[n]
        Z += q * int(w)
        E0 += q * int(a)
        E1 += q * int(b)
        E01 += q * int(c)
    return E0 * E1 - Z * E01, (Z, E0, E1, E01)


# Nonnegative abstract boundary data need not be Rayleigh.
toy = {n: 0 for n in NAMES}
toy["0|1|2|3"] = 1
toy["0123"] = 1
toy_delta, toy_tuple = delta_from_vector(toy)
assert toy_delta == -3 and toy_tuple == (21, 9, 9, 4)

# Exhaust all simple H on six labelled vertices. 0,1,2,3 are terminals.
NV = 6
EDGES = list(combinations(range(NV), 2))
M = len(EDGES)
assert M == 15
INDEX = {n: i for i, n in enumerate(NAMES)}
base = [[0] * (1 << M) for _ in NAMES]


def forest_terminal_partition(mask):
    parent = list(range(NV))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True

    for j, (a, b) in enumerate(EDGES):
        if (mask >> j) & 1 and not union(a, b):
            return None
    blocks = {}
    for t in range(4):
        blocks.setdefault(find(t), []).append(t)
    return "|".join(
        "".join(map(str, b))
        for b in sorted((tuple(x) for x in blocks.values()), key=lambda x: x[0])
    )


forest_masks = 0
for mask in range(1 << M):
    n = forest_terminal_partition(mask)
    if n is not None:
        base[INDEX[n]][mask] = 1
        forest_masks += 1

# Subset-zeta transform: counts[class][Hmask] counts forest subsets of H.
counts = [row[:] for row in base]
for bit in range(M):
    bm = 1 << bit
    for mask in range(1 << M):
        if mask & bm:
            prev = mask ^ bm
            for i in range(len(NAMES)):
                counts[i][mask] += counts[i][prev]


def vector_for(mask):
    return {n: counts[INDEX[n]][mask] for n in NAMES}


def edges_of(mask):
    return [EDGES[j] for j in range(M) if (mask >> j) & 1]


def connected(n, eds, removed=frozenset()):
    verts = [x for x in range(n) if x not in removed]
    if len(verts) <= 1:
        return True
    adj = {x: [] for x in verts}
    for a, b in eds:
        if a in removed or b in removed:
            continue
        adj[a].append(b)
        adj[b].append(a)
    seen = {verts[0]}
    stack = [verts[0]]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == len(verts)


def g_is_3_connected(mask):
    # Add new vertex v=6 and star v-{0,1,2,3}.
    eds = edges_of(mask) + [(6, i) for i in range(4)]
    if not connected(7, eds):
        return False
    for r in (1, 2):
        for rem in combinations(range(7), r):
            if not connected(7, eds, frozenset(rem)):
                return False
    return True


all_neg = all_zero = 0
all_min = all_minmask = None
three_count = three_neg = three_zero = 0
three_min = three_minmask = None
for mask in range(1 << M):
    d, _ = delta_from_vector(vector_for(mask))
    if d < 0:
        all_neg += 1
    if d == 0:
        all_zero += 1
    if all_min is None or d < all_min:
        all_min, all_minmask = d, mask
    if g_is_3_connected(mask):
        three_count += 1
        if d < 0:
            three_neg += 1
        if d == 0:
            three_zero += 1
        if three_min is None or d < three_min:
            three_min, three_minmask = d, mask

assert all_neg == 0
assert three_count == 5744 and three_neg == 0 and three_zero == 0 and three_min == 5384

print("FOREST-DEG4-REALIZABILITY-DEFICIT-v1")
print("partitions", len(NAMES))
for n in NAMES:
    print("local", n, *map(int, VAL[n]))
print("quadratic_coefficients", "negative", len(neg), "zero", len(zero), "positive", len(pos))
for a, b, q in neg:
    print("negative", a, b, int(q))
print("negative_factor = -(4*N[0|1|2|3] + 3*N[0|1|23])*(N[0123] + N[02|13] + N[03|12])")
print("toy_nonrealized_vector", toy, "tuple", toy_tuple, "delta", toy_delta)
print("K6_edge_masks", 1 << M, "forest_edge_masks", forest_masks)
print("all_H", "negative", all_neg, "zero", all_zero, "minimum_delta", all_min)
print("three_connected_G", "count", three_count, "negative", three_neg, "zero", three_zero, "minimum_delta", three_min)
print("three_connected_min_H_edges", edges_of(three_minmask))
vec = vector_for(three_minmask)
print("three_connected_min_partition_vector", vec)
print("three_connected_min_Z_tuple", delta_from_vector(vec)[1])
