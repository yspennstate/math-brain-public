#!/usr/bin/env python3
"""HARD10-01 exact checks for the post-19:12 dependency audit and |R|=6 reconnaissance.

Standard library only.

Checks:
  1. an explicit counterexample to the archived universal L45 one-bubble claim;
  2. exact |R|=6 root-fiber partition counts for representative adjacent/disjoint
     distinguished pairs on n=6,7 (edge-transitivity makes these representative);
  3. every observed size-three root fiber is exactly a two-edge ear;
  4. every observed 3+3 case is either common-ear or cross-ear, with exact counts;
  5. every observed 4+1+1 case has a three-spoke size-four fiber with a common
     outside endpoint, and its two singleton roots use distinct spoke pairs.

The finite computations are checks only, not proof dependencies.
"""

from collections import Counter, defaultdict
from itertools import combinations


def norm(e):
    return tuple(sorted(e))


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    return True


def zeta(a, m):
    z = a[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                z[mask] += z[mask ^ bit]
    return z


def fixed_arrays(n, e, f):
    e, f = norm(e), norm(f)
    all_edges = list(combinations(range(n), 2))
    H = [g for g in all_edges if g not in (e, f)]
    m = len(H)
    N = 1 << m
    names = ("R", "B", "Ne", "Nf", "N0")
    arr = {name: [0] * N for name in names}

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        eo = is_forest(n, A + [e])
        fo = is_forest(n, A + [f])
        efo = is_forest(n, A + [e, f])
        if eo and fo and not efo:
            cat = "R"
        elif eo and fo:
            cat = "B"
        elif eo:
            cat = "Ne"
        elif fo:
            cat = "Nf"
        else:
            cat = "N0"
        arr[cat][mask] = 1

    root = [0] * N
    for mask in range(N):
        if not arr["R"][mask]:
            continue
        x = mask
        minimal = True
        while x:
            bit = x & -x
            if arr["R"][mask ^ bit]:
                minimal = False
                break
            x -= bit
        if minimal:
            root[mask] = 1

    counts = {name: zeta(arr[name], m) for name in names}
    return H, arr["R"], root, counts


def edge_set(H, mask):
    return {H[i] for i in range(len(H)) if (mask >> i) & 1}


def cycle_edge_sets(n, edges, required):
    edges = sorted(norm(g) for g in edges)
    req = set(map(norm, required))
    out = []
    for mask in range(1 << len(edges)):
        S = {edges[i] for i in range(len(edges)) if (mask >> i) & 1}
        if not req <= S or len(S) < 3:
            continue
        deg = Counter()
        for a, b in S:
            deg[a] += 1
            deg[b] += 1
        verts = {v for v, d in deg.items() if d}
        if not verts or any(deg[v] != 2 for v in verts):
            continue
        adj = defaultdict(list)
        for a, b in S:
            adj[a].append(b)
            adj[b].append(a)
        seen = set()
        stack = [next(iter(verts))]
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            stack.extend(adj[v])
        if seen == verts:
            out.append(frozenset(S))
    return sorted(set(out), key=lambda s: (len(s), sorted(s)))


def verify_l45_counterexample():
    n = 6
    e, f = (0, 1), (2, 3)
    E = {
        (0, 1), (2, 3), (2, 4), (2, 5),
        (0, 5), (0, 3), (1, 3), (1, 4),
    }
    cycles = cycle_edge_sets(n, E, (e, f))
    C1 = frozenset({(0, 1), (1, 4), (2, 4), (2, 3), (0, 3)})
    C2 = frozenset({(0, 1), (1, 3), (2, 3), (2, 5), (0, 5)})
    assert set(cycles) == {C1, C2}
    assert C1 & C2 == frozenset({e, f})
    assert set(e).isdisjoint(f)

    H = sorted(E - {e, f})
    classes = Counter()
    Rs = []
    for mask in range(1 << len(H)):
        A = [H[i] for i in range(len(H)) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        eo = is_forest(n, A + [e])
        fo = is_forest(n, A + [f])
        efo = is_forest(n, A + [e, f])
        if eo and fo and not efo:
            cat = "R"
            Rs.append(frozenset(A))
        elif eo and fo:
            cat = "B"
        elif eo:
            cat = "Ne"
        elif fo:
            cat = "Nf"
        else:
            cat = "N0"
        classes[cat] += 1
    roots = [A for A in Rs if not any(B < A for B in Rs)]
    fibers = sorted((sum(1 for A in Rs if P <= A) for P in roots), reverse=True)
    assert classes == Counter({"B": 33, "Nf": 10, "N0": 8, "R": 6, "Ne": 6})
    assert fibers == [3, 3]

    EE = sorted(E)
    ie, jf = EE.index(e), EE.index(f)
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(EE)):
        A = [EE[i] for i in range(len(EE)) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        Z += 1
        he, hf = (mask >> ie) & 1, (mask >> jf) & 1
        Ze += he
        Zf += hf
        Zef += he & hf
    assert (Z, Ze, Zf, Zef) == (190, 78, 82, 33)
    assert Ze * Zf - Z * Zef == 126
    print("L45 COUNTEREXAMPLE VERIFIED: two common cycles, R partition (3,3), Delta=126")


def root_fibers(Rs, roots):
    return {P: [A for A in Rs if (P & ~A) == 0] for P in roots}


def cycle_vertices_from_root(n, H, P, e, f):
    edges = edge_set(H, P) | {norm(e), norm(f)}
    deg = Counter()
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    verts = {v for v, d in deg.items() if d}
    assert verts and all(deg[v] == 2 for v in verts)
    return verts


def extension_single_edges(H, P, fiber):
    diffs = [A ^ P for A in fiber if A != P]
    assert all(x.bit_count() == 1 for x in diffs)
    return [H[(x & -x).bit_length() - 1] for x in diffs]


def verify_size3_ear(n, H, P, fiber, e, f, graph_edges):
    ext = extension_single_edges(H, P, fiber)
    assert len(ext) == 2
    Cverts = cycle_vertices_from_root(n, H, P, e, f)
    common = set(ext[0]) & set(ext[1])
    assert len(common) == 1
    w = next(iter(common))
    assert w not in Cverts
    endpoints = []
    for a, b in ext:
        z = b if a == w else a
        assert z in Cverts
        endpoints.append(z)
    assert endpoints[0] != endpoints[1]
    outside_edges = [
        g for g in graph_edges
        if g not in (norm(e), norm(f))
        and (g[0] not in Cverts or g[1] not in Cverts)
    ]
    assert set(outside_edges) == set(ext)
    return frozenset(ext), w, tuple(endpoints)


def classify_family(n, e, f, expected_partitions, expected_33=None, expected_411=0):
    e, f = norm(e), norm(f)
    H, r, root, counts = fixed_arrays(n, e, f)
    r_masks = [m for m, val in enumerate(r) if val]
    root_masks = [m for m, val in enumerate(root) if val]
    part_counts = Counter()
    case33 = Counter()
    count411 = 0
    pairuse = Counter()

    for M in range(1 << len(H)):
        if counts["R"][M] != 6:
            continue
        Rs = [A for A in r_masks if (A & ~M) == 0]
        roots = [P for P in root_masks if (P & ~M) == 0]
        fibers = root_fibers(Rs, roots)
        part = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
        part_counts[part] += 1
        graph_edges = edge_set(H, M) | {e, f}

        if part == (3, 3):
            assert len(roots) == 2
            infos = {}
            for P in roots:
                infos[P] = verify_size3_ear(n, H, P, fibers[P], e, f, graph_edges)
            P, Q = roots
            EP, EQ = infos[P][0], infos[Q][0]
            Pset, Qset = edge_set(H, P), edge_set(H, Q)
            p_in_q = sum(g in Qset for g in EP)
            q_in_p = sum(g in Pset for g in EQ)
            assert p_in_q in (0, 2) and q_in_p in (0, 2)
            if p_in_q == 0:
                assert q_in_p == 0
                assert EP == EQ
                case33["same"] += 1
            else:
                assert q_in_p == 2
                assert EP != EQ
                for _, _, (u, v) in (infos[P], infos[Q]):
                    assert norm((u, v)) not in graph_edges
                case33["cross"] += 1

        elif part == (4, 1, 1):
            count411 += 1
            big = next(P for P in roots if len(fibers[P]) == 4)
            singles = [P for P in roots if len(fibers[P]) == 1]
            ext = extension_single_edges(H, big, fibers[big])
            assert len(ext) == 3
            common = set(ext[0]) & set(ext[1]) & set(ext[2])
            assert len(common) == 1
            w = next(iter(common))
            Cverts = cycle_vertices_from_root(n, H, big, e, f)
            assert w not in Cverts
            for g in ext:
                assert (g[0] == w) ^ (g[1] == w)
                z = g[1] if g[0] == w else g[0]
                assert z in Cverts
            used = []
            for Q in singles:
                Qset = edge_set(H, Q)
                pair = frozenset(g for g in ext if g in Qset)
                assert len(pair) == 2
                used.append(pair)
            assert used[0] != used[1]
            idx = {g: i for i, g in enumerate(sorted(ext))}
            key = tuple(sorted(tuple(sorted(idx[g] for g in pair)) for pair in used))
            pairuse[key] += 1

    assert part_counts == Counter(expected_partitions), (n, e, f, part_counts, expected_partitions)
    if expected_33 is not None:
        assert case33 == Counter(expected_33), (n, e, f, case33, expected_33)
    assert count411 == expected_411
    print(
        f"n={n}, e={e}, f={f}: partitions={dict(part_counts)}, "
        f"3+3={dict(case33)}, 4+1+1={count411}"
    )
    if pairuse:
        print("  4+1+1 singleton spoke-pair patterns:", dict(pairuse))
    return sum(part_counts.values())


if __name__ == "__main__":
    verify_l45_counterexample()
    totals = []
    totals.append(classify_family(
        6, (0, 1), (0, 2),
        {(6,): 234, (3, 3): 15},
        {"cross": 15}, 0))
    totals.append(classify_family(
        6, (0, 1), (2, 3),
        {(6,): 200, (4, 1, 1): 144, (3, 3): 72},
        {"same": 52, "cross": 20}, 144))
    totals.append(classify_family(
        7, (0, 1), (0, 2),
        {(6,): 3216, (3, 3): 198},
        {"cross": 198}, 0))
    totals.append(classify_family(
        7, (0, 1), (2, 3),
        {(6,): 5844, (4, 1, 1): 2520, (3, 3): 1770},
        {"same": 1230, "cross": 540}, 2520))
    assert totals == [249, 416, 3414, 10134]
    assert sum(totals) == 14213
    print("TOTAL VERIFIED |R|=6 INSTANCES:", sum(totals))
    print("ALL EXACT HARD10-01 L45/R6 CHECKS PASSED")
