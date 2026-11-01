#!/usr/bin/env python3
"""
Exact finite self-check for P11-I0062-PARETO-CLUSTER-SURFACE-06.

This is NOT a proof of the asymptotic probability theorem. It exhaustively
checks the deterministic finite cut identity used in the proof on the
3-vertex base path at slab height h=3, with integer capacities:
  vertical capacities in {1,3};
  each middle horizontal capacity in {1,4};
  threshold M=2.
For every one of 8192 capacity assignments it checks:
  (1) labels are constant on every heavy-bond component;
  (2) no crossed middle horizontal edge has capacity > M;
  (3) selected vertical cost on each component is exactly the minimum over
      the h common-height choices;
  (4) the height-label energy equals the explicit edge-boundary cut capacity;
  (5) total cut capacity <= component-minimum vertical cost
      + M*(h-1)*(number of base bonds).
All arithmetic is integer/exact; no floating point is used.
"""

from itertools import product

N = 3
BASE_EDGES = [(0, 1), (1, 2)]
H = 3
M = 2


def components(heavy):
    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i, (a, b) in enumerate(BASE_EDGES):
        if heavy[i]:
            union(a, b)

    out = {}
    for x in range(N):
        out.setdefault(find(x), []).append(x)
    return list(out.values())


def height_energy(labels, vert, horiz):
    ans = sum(vert[x][labels[x]] for x in range(N))
    for ei, (x, y) in enumerate(BASE_EDGES):
        lo, hi = sorted((labels[x], labels[y]))
        for z in range(lo + 1, hi + 1):
            ans += horiz[ei][z - 1]
    return ans


def explicit_edge_boundary(labels, vert, horiz):
    # Source side in column x consists of levels z <= labels[x].
    ans = 0
    for x in range(N):
        for z in range(H):
            if (z <= labels[x]) != (z + 1 <= labels[x]):
                ans += vert[x][z]
    for ei, (x, y) in enumerate(BASE_EDGES):
        for z in range(1, H):
            if (z <= labels[x]) != (z <= labels[y]):
                ans += horiz[ei][z - 1]
    return ans


assignments = 0
for vraw in product((1, 3), repeat=N * H):
    vert = [list(vraw[x * H:(x + 1) * H]) for x in range(N)]
    for hraw in product((1, 4), repeat=len(BASE_EDGES) * (H - 1)):
        horiz = [
            list(hraw[e * (H - 1):(e + 1) * (H - 1)])
            for e in range(len(BASE_EDGES))
        ]
        heavy = [any(c > M for c in horiz[e]) for e in range(len(BASE_EDGES))]
        comps = components(heavy)

        labels = [None] * N
        component_minimum = 0
        for comp in comps:
            sums = [sum(vert[x][j] for x in comp) for j in range(H)]
            j = min(range(H), key=lambda k: (sums[k], k))
            component_minimum += sums[j]
            for x in comp:
                labels[x] = j

        # (1) heavy bonds never connect different labels.
        for ei, (x, y) in enumerate(BASE_EDGES):
            if heavy[ei]:
                assert labels[x] == labels[y]

        # (2) every crossed horizontal capacity is <= M.
        for ei, (x, y) in enumerate(BASE_EDGES):
            lo, hi = sorted((labels[x], labels[y]))
            for z in range(lo + 1, hi + 1):
                assert horiz[ei][z - 1] <= M

        # (3) selected vertical cost is the sum of component minima.
        selected_vertical = sum(vert[x][labels[x]] for x in range(N))
        assert selected_vertical == component_minimum

        # (4) energy representation is exactly the explicit cut boundary.
        energy = height_energy(labels, vert, horiz)
        boundary = explicit_edge_boundary(labels, vert, horiz)
        assert energy == boundary

        # (5) deterministic crude horizontal bound used by the theorem.
        assert energy <= component_minimum + M * (H - 1) * len(BASE_EDGES)

        assignments += 1

assert assignments == 8192
print("P11-I0062-PARETO-CLUSTER-SURFACE-06 finite self-check: PASS")
print(f"assignments_checked = {assignments}")
print("base_vertices = 3")
print("base_edges = 2")
print("height = 3")
print("threshold_M = 2")
print("vertical_capacities = {1,3}")
print("middle_horizontal_capacities = {1,4}")
print("floating_point_used = false")
print("asymptotic_probability_theorem = proved_on_report_page_not_by_enumeration")
