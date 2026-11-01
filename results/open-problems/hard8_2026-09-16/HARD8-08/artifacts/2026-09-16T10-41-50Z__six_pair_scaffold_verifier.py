#!/usr/bin/env python3
"""Exact checks for HARD8-08 checkpoint 6.

Standard-library only.  No floating point, randomization, SAT solver, or timeout
is used.

Checks:
  1. exact Eisenstein-coordinate squared distances for the six-point scaffold;
  2. exhaustive completion of that scaffold by non-unit pair constraints;
  3. exhaustive 7-vertex complement-star combinatorial criterion;
  4. exact black-box pair counts for R_6^+ under its three distance scalings
     and for R_7;
  5. a finite graph certificate underlying u(6)<=9: every 10-edge graph on six
     vertices avoiding K4 and K_{2,3} is the wheel W_6 (5-cycle plus hub).
     Such a wheel cannot be a planar unit-distance graph because its rim would
     be a 5-cycle of unit chords on a unit circle.  (The latter geometric step
     is proved in the report/addendum by the +/- pi/3 central-angle argument.)
"""

from itertools import combinations
from collections import Counter


def eisenstein_norm2(p, q):
    """Squared Euclidean distance in basis e1=(1,0), e2=(1/2,sqrt(3)/2)."""
    a = p[0] - q[0]
    b = p[1] - q[1]
    return a * a + a * b + b * b


def chromatic_number(n, edge_set):
    """Exact backtracking chromatic number for n<=7."""
    adj = [0] * n
    for a, b in edge_set:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    order = sorted(range(n), key=lambda v: adj[v].bit_count(), reverse=True)

    def can_color(k):
        color = [-1] * n

        def dfs(i):
            if i == n:
                return True
            v = order[i]
            forbidden = 0
            nb = adj[v]
            u = 0
            while nb:
                lsb = nb & -nb
                u = lsb.bit_length() - 1
                if color[u] >= 0:
                    forbidden |= 1 << color[u]
                nb ^= lsb
            for c in range(k):
                if not ((forbidden >> c) & 1):
                    color[v] = c
                    if dfs(i + 1):
                        return True
                    color[v] = -1
            return False

        return dfs(0)

    for k in range(1, n + 1):
        if can_color(k):
            return k
    raise AssertionError("unreachable")


def check_six_point_scaffold():
    # Six vertices of a unit regular hexagon in Eisenstein coordinates.
    # Delete outer vertex v0=(1,0), retain center and the next five outer points.
    outer = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    pts = [(0, 0)] + outer[1:]

    classes = {}
    for i, j in combinations(range(6), 2):
        d2 = eisenstein_norm2(pts[i], pts[j])
        classes.setdefault(d2, set()).add((i, j))

    counts = {d2: len(es) for d2, es in classes.items()}
    assert counts == {1: 9, 3: 4, 4: 2}, counts

    unit = classes[1]
    nonunit = sorted(classes[3] | classes[4])

    # Exhaust all 2^6 choices of black-box non-unit pair inequalities.
    best = 99
    best_masks = []
    distribution = Counter()
    for mask in range(1 << len(nonunit)):
        edges = set(unit)
        added = 0
        for i, e in enumerate(nonunit):
            if (mask >> i) & 1:
                edges.add(e)
                added += 1
        chi = chromatic_number(6, edges)
        distribution[(added, chi)] += 1
        if chi >= 6:
            if added < best:
                best = added
                best_masks = []
            if added == best:
                best_masks.append(mask)

    assert best == 6
    assert len(best_masks) == 1
    assert best_masks[0] == (1 << 6) - 1

    assert len(classes[3]) == 4
    assert len(classes[4]) == 2
    return counts, distribution


def is_star_subgraph(n, mask, edges):
    if mask == 0:
        return True
    common = (1 << n) - 1
    for i, (a, b) in enumerate(edges):
        if (mask >> i) & 1:
            common &= (1 << a) | (1 << b)
    return common != 0


def has_triangle(mask, triangle_masks):
    return any((mask & tm) == tm for tm in triangle_masks)


def has_matching_two(mask, disjoint_masks):
    x = mask
    while x:
        lsb = x & -x
        i = lsb.bit_length() - 1
        if mask & disjoint_masks[i]:
            return True
        x ^= lsb
    return False


def check_seven_vertex_criterion():
    n = 7
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}

    disjoint_masks = [0] * len(edges)
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges):
            if i != j and len({a, b, c, d}) == 4:
                disjoint_masks[i] |= 1 << j

    triangle_masks = []
    for tri in combinations(range(n), 3):
        tm = 0
        for e in combinations(tri, 2):
            tm |= 1 << idx[tuple(sorted(e))]
        triangle_masks.append(tm)

    checked = 0
    for mask in range(1 << len(edges)):
        bad_for_5color = not has_matching_two(mask, disjoint_masks) and not has_triangle(mask, triangle_masks)
        star = is_star_subgraph(n, mask, edges)
        assert bad_for_5color == star, (mask, bad_for_5color, star)
        checked += 1
    assert checked == 2 ** 21
    return checked


def check_distance_class_pair_counts():
    # R_6^+: center=0 and six outer vertices 1..6.
    center_spoke_and_side = set()
    sqrt3 = set()
    diameter = set()
    for i in range(1, 7):
        center_spoke_and_side.add(tuple(sorted((0, i))))
        center_spoke_and_side.add(tuple(sorted((i, 1 + (i % 6)))))
    for i, j in combinations(range(1, 7), 2):
        step = min((j - i) % 6, (i - j) % 6)
        e = tuple(sorted((i, j)))
        if step == 2:
            sqrt3.add(e)
        elif step == 3:
            diameter.add(e)

    assert len(center_spoke_and_side) == 12
    assert len(sqrt3) == 6
    assert len(diameter) == 3
    allpairs = set(combinations(range(7), 2))
    assert center_spoke_and_side | sqrt3 | diameter == allpairs

    results = []
    classes = [center_spoke_and_side, sqrt3, diameter]
    expected = [6, 9, 12]
    for unit, want in zip(classes, expected):
        non = allpairs - unit
        deg = [0] * 7
        for a, b in unit:
            deg[a] += 1
            deg[b] += 1
        formula = 15 - len(unit) + min(deg)
        # Equivalent complement form |N|-Delta(N).
        ndeg = [0] * 7
        for a, b in non:
            ndeg[a] += 1
            ndeg[b] += 1
        assert formula == len(non) - max(ndeg)
        assert formula == want
        results.append((len(unit), min(deg), formula))

    # R_7: each of its three chord-distance classes is a 7-cycle.
    # Scaling any class to unit gives |E(U)|=7 and delta(U)=2.
    r7_formula = 15 - 7 + 2
    assert r7_formula == 10
    return results, r7_formula


def contains_k4(edge_set):
    E = edge_set
    for S in combinations(range(6), 4):
        if all(tuple(sorted(e)) in E for e in combinations(S, 2)):
            return True
    return False


def contains_k23(edge_set):
    E = edge_set
    for A in combinations(range(6), 2):
        remaining = [v for v in range(6) if v not in A]
        for B in combinations(remaining, 3):
            if all(tuple(sorted((a, b))) in E for a in A for b in B):
                return True
    return False


def is_wheel_w6(edge_set):
    deg = [0] * 6
    for a, b in edge_set:
        deg[a] += 1
        deg[b] += 1
    hubs = [v for v, d in enumerate(deg) if d == 5]
    if len(hubs) != 1:
        return False
    h = hubs[0]
    rim = [v for v in range(6) if v != h]
    rim_degrees = {v: 0 for v in rim}
    rim_edges = 0
    for a, b in combinations(rim, 2):
        if (a, b) in edge_set or (b, a) in edge_set:
            rim_edges += 1
            rim_degrees[a] += 1
            rim_degrees[b] += 1
    return rim_edges == 5 and all(d == 2 for d in rim_degrees.values())


def check_u6_combinatorial_certificate():
    # Any planar unit-distance graph avoids K4 and K_{2,3}.
    # Exhaust all 10-edge abstract graphs on six labeled vertices satisfying
    # these two necessary conditions; every survivor is W_6.
    pairs = list(combinations(range(6), 2))
    survivors = 0
    degree_sequences = Counter()
    for comb in combinations(pairs, 10):
        E = set(comb)
        if contains_k4(E) or contains_k23(E):
            continue
        survivors += 1
        deg = [0] * 6
        for a, b in E:
            deg[a] += 1
            deg[b] += 1
        degree_sequences[tuple(sorted(deg, reverse=True))] += 1
        assert is_wheel_w6(E)

    assert survivors == 72
    assert degree_sequences == Counter({(5, 3, 3, 3, 3, 3): 72})

    # W_6 cannot be a Euclidean unit-distance graph: the hub puts the five rim
    # vertices on the unit circle, and each rim edge would subtend central angle
    # +/- pi/3.  Five such signed increments cannot sum to a multiple of 2*pi.
    # This last implication is exact mathematics, not numerically tested here.
    return survivors, degree_sequences


def main():
    counts, dist = check_six_point_scaffold()
    seven_checked = check_seven_vertex_criterion()
    r6p, r7 = check_distance_class_pair_counts()
    survivors, seqs = check_u6_combinatorial_certificate()

    print("SIX_POINT_DISTANCE_COUNTS", counts)
    print("SIX_POINT_COMPLETION_MINIMUM", 6)
    print("SEVEN_VERTEX_COMPLEMENTS_CHECKED", seven_checked)
    print("R6PLUS_PAIR_COUNTS", r6p)
    print("R7_PAIR_COUNT", r7)
    print("TEN_EDGE_K4_K23_FREE_SURVIVORS", survivors)
    print("SURVIVOR_DEGREE_SEQUENCES", dict(seqs))
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
