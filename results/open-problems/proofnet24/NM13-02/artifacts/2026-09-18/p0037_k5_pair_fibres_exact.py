#!/usr/bin/env python3
"""
Exact finite self-check for NM13-02 / P0037.

Scope:
- uniform spanning trees of K5;
- ordered-pair fibres indexed by (intersection, union);
- explicit obstruction to a naive Mészáros/Reimer fibrewise inequality
  even for two distinct single-edge principal increasing events.

All arithmetic is integer counting.
"""

from collections import defaultdict, Counter

N = 5
EDGES = [(i,j) for i in range(N) for j in range(i+1,N)]
M = len(EDGES)
assert M == 10

def popcount(x):
    return x.bit_count()

def is_tree(mask):
    if popcount(mask) != N-1:
        return False
    parent = list(range(N))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a,b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    for k,(u,v) in enumerate(EDGES):
        if mask >> k & 1:
            if not union(u,v):
                return False
    r = find(0)
    return all(find(i) == r for i in range(N))

TREES = [m for m in range(1<<M) if is_tree(m)]
assert len(TREES) == 125

fibres = defaultdict(list)
for a in TREES:
    for b in TREES:
        fibres[(a & b, a | b)].append((a,b))

size_dist = Counter(len(v) for v in fibres.values())
expected_dist = {1:125, 2:930, 4:1605, 8:640, 12:80, 24:30, 28:15}
assert dict(sorted(size_dist.items())) == expected_dist
assert len(fibres) == 3425
assert sum(size * count for size,count in size_dist.items()) == 125**2

# In each fibre the edge-multiplicity vector is fixed, hence the product
# of arbitrary edge weights of the two trees is fixed.
for (inter, union), pairs in fibres.items():
    target_mult = tuple(((inter >> e) & 1) + ((union >> e) & 1) for e in range(M))
    for a,b in pairs:
        mult = tuple(((a >> e) & 1) + ((b >> e) & 1) for e in range(M))
        assert mult == target_mult

# Explicit bad fibre.
# edge indices:
# 0=(0,1), 1=(0,2), 2=(0,3), 3=(0,4),
# 4=(1,2), 5=(1,3), 6=(1,4), 7=(2,3), 8=(2,4), 9=(3,4).
I = 1 << 3           # common edge (0,4)
U = sum(1 << e for e in [0,1,2,3,4,5,7])
F = 1 << 0           # witness edge (0,1)
H = 1 << 7           # witness edge (2,3)
cell = fibres[(I,U)]
assert len(cell) == 12

# Contract the common edge (0,4), and check U\I becomes K4 on components
# A={0,4}, B={1}, C={2}, D={3}.
comp = {0:0, 4:0, 1:1, 2:2, 3:3}
quot_edges = set()
for e,(u,v) in enumerate(EDGES):
    if ((U & ~I) >> e) & 1:
        a,b = comp[u], comp[v]
        assert a != b
        if a > b: a,b = b,a
        quot_edges.add((a,b))
assert quot_edges == {(i,j) for i in range(4) for j in range(i+1,4)}

# Fibrewise inequality one would want in the most naive pair-cell port:
# # { (C,D) in cell : F union H subset C }
# <=
# # { (C,D) in cell : F subset C and H subset D }.
lhs = sum(1 for a,b in cell if (a & (F|H)) == (F|H))
rhs = sum(1 for a,b in cell if (a & F) == F and (b & H) == H)
assert (lhs, rhs) == (4,2)
assert lhs > rhs

# Exhaust all fibres and all ordered pairs of distinct single edges.
# A fibre is called "bad" if at least one pair violates the same cellwise inequality.
bad_by_size = Counter()
bad_examples = {}
for key,pairs in fibres.items():
    bad = False
    witness = None
    for e in range(M):
        for f in range(M):
            if e == f:
                continue
            fe, hf = 1<<e, 1<<f
            l = sum(1 for a,b in pairs if (a & (fe|hf)) == (fe|hf))
            r = sum(1 for a,b in pairs if (a & fe) == fe and (b & hf) == hf)
            if l > r:
                bad = True
                witness = (e,f,l,r)
                break
        if bad:
            break
    if bad:
        sz = len(pairs)
        bad_by_size[sz] += 1
        bad_examples.setdefault(sz, (key,witness))

expected_bad = {12:80, 24:30, 28:15}
assert dict(sorted(bad_by_size.items())) == expected_bad
assert sum(bad_by_size.values()) == 125
assert all(sz > 8 for sz in bad_by_size)

# Check every fibre of size 12,24,28 is bad, and no smaller fibre is bad.
for sz in expected_dist:
    total = expected_dist[sz]
    bad = bad_by_size[sz]
    if sz in (12,24,28):
        assert bad == total
    else:
        assert bad == 0

# Global principal edge events are still fine; for the explicit disjoint pair
# e=(0,1), f=(2,3), the uniform K5 UST has exact equality.
count_F = sum(1 for t in TREES if (t & F) == F)
count_H = sum(1 for t in TREES if (t & H) == H)
count_FH = sum(1 for t in TREES if (t & (F|H)) == (F|H))
assert (count_F, count_H, count_FH) == (50,50,20)
assert count_FH * len(TREES) == count_F * count_H

print("K5_edges =", EDGES)
print("spanning_trees =", len(TREES))
print("pair_fibres =", len(fibres))
print("fibre_size_distribution =", dict(sorted(size_dist.items())))
print("explicit_fibre_intersection_mask =", I)
print("explicit_fibre_union_mask =", U)
print("explicit_fibre_size =", len(cell))
print("explicit_quotient_after_contraction = K4")
print("explicit_witness_edges =", EDGES[0], EDGES[7])
print("explicit_cell_lhs_rhs =", lhs, rhs)
print("bad_fibres_by_size =", dict(sorted(bad_by_size.items())))
print("total_bad_fibres =", sum(bad_by_size.values()))
print("global_counts_F_H_FH =", count_F, count_H, count_FH)
print("global_principal_edge_ratio = 1 exactly")
print("ALL_EXACT_CHECKS_PASS")
