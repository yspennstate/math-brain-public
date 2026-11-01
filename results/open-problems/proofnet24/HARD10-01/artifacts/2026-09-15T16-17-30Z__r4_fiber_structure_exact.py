#!/usr/bin/env python3
"""
HARD10-01 exact adversarial checker for the 2026-09-15T16:17:30Z report.

Standard library only.

For every labelled graph on six vertices containing a fixed representative
adjacent distinguished pair and a fixed representative vertex-disjoint pair,
this script:

  * computes the exact R family by subset zeta transforms;
  * classifies every |R|=4 graph by root-fiber partition;
  * verifies that 2+1+1 never occurs;
  * verifies every 2+2 case has one common extension edge, that edge is a
    bridge, and deleting it leaves exactly two R forests;
  * verifies every 3+1 case has two one-edge extensions forming the only
    outside two-edge ear, and suppressing the degree-two outside vertex gives
    a base graph with one R forest when the direct terminal edge is already
    present, and two R forests when it is absent;
  * verifies every all-minimal four-root case has disjoint distinguished edges
    and exactly two roots of each terminal pairing;
  * computes the exact unit-weight Rayleigh gap and the minimum gap in each
    fiber stratum.

These are finite checks, not proof dependencies for the universal lemmas.
"""

from collections import Counter
from itertools import combinations


def edge(u, v):
    return (u, v) if u < v else (v, u)


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    return all(union(a, b) for a, b in edges)


def zeta(a, m):
    z = a[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                z[mask] += z[mask ^ bit]
    return z


def fixed_pair_arrays(n, e, f):
    all_edges = list(combinations(range(n), 2))
    H = [g for g in all_edges if g not in (e, f)]
    m = len(H)
    N = 1 << m
    raw = {k: [0] * N for k in ("N0", "Ne", "Nf", "B", "R")}
    rmask = [0] * N

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        eok = is_forest(n, A + [e])
        fok = is_forest(n, A + [f])
        efok = is_forest(n, A + [e, f])
        if not eok and not fok:
            kind = "N0"
        elif eok and not fok:
            kind = "Ne"
        elif fok and not eok:
            kind = "Nf"
        elif efok:
            kind = "B"
        else:
            kind = "R"
            rmask[mask] = 1
        raw[kind][mask] = 1

    return H, rmask, {k: zeta(v, m) for k, v in raw.items()}


def submasks(M):
    s = M
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & M


def roots_and_fibers(M, rmask):
    Rs = [s for s in submasks(M) if rmask[s]]
    roots = [
        s for s in Rs
        if not any(t != s and (t & s) == t for t in Rs)
    ]
    fibers = {
        P: [A for A in Rs if (P & A) == P]
        for P in roots
    }
    return Rs, roots, fibers


def mask_edges(H, mask):
    return [H[i] for i in range(len(H)) if (mask >> i) & 1]


def cycle_support(H, P, e, f):
    W = set(e) | set(f)
    for i, g in enumerate(H):
        if (P >> i) & 1:
            W.update(g)
    return W


def is_bridge(n, edges, h):
    def components(E):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in E:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        return len({find(v) for v in range(n)})

    return components(edges) < components([g for g in edges if g != h])


def pairing_type(n, A, e, f):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in A:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    a, b = e
    c, d = f
    if find(a) == find(c) and find(b) == find(d):
        return 0
    if find(a) == find(d) and find(b) == find(c):
        return 1
    raise AssertionError(("not an R pairing", A, e, f))


def analyze(n, e, f):
    H, rmask, Z = fixed_pair_arrays(n, e, f)
    m = len(H)
    partition_count = Counter()
    minimum_gap = {}

    for M in range(1 << m):
        if Z["R"][M] != 4:
            continue

        Rs, roots, fibers = roots_and_fibers(M, rmask)
        partition = tuple(
            sorted((len(fibers[P]) for P in roots), reverse=True)
        )
        partition_count[partition] += 1

        N0, Ne, Nf, B, R = (
            Z[k][M] for k in ("N0", "Ne", "Nf", "B", "R")
        )
        delta = Ne * Nf + R * (Ne + Nf + B + R) - B * N0
        minimum_gap[partition] = min(
            minimum_gap.get(partition, 10**100), delta
        )
        assert delta > 0

        # Universal report claim: 2+1+1 does not occur.
        assert partition != (2, 1, 1)

        if partition == (2, 2):
            extension_indices = []
            for P in roots:
                A = next(A for A in fibers[P] if A != P)
                diff = A ^ P
                assert diff and (diff & (diff - 1)) == 0
                extension_indices.append(diff.bit_length() - 1)
            assert extension_indices[0] == extension_indices[1]
            i = extension_indices[0]
            h = H[i]
            graph_edges = [e, f] + mask_edges(H, M)
            assert is_bridge(n, graph_edges, h)
            assert Z["R"][M & ~(1 << i)] == 2

        if partition == (3, 1):
            P = max(roots, key=lambda x: len(fibers[x]))
            Q = min(roots, key=lambda x: len(fibers[x]))
            extra = []
            for A in fibers[P]:
                if A == P:
                    continue
                diff = A ^ P
                assert diff and (diff & (diff - 1)) == 0
                extra.append(diff.bit_length() - 1)
            assert len(extra) == 2

            W = cycle_support(H, P, e, f)
            outside_edges = [
                i for i, g in enumerate(H)
                if ((M >> i) & 1)
                and (g[0] not in W or g[1] not in W)
            ]
            assert set(outside_edges) == set(extra)

            h, k = H[extra[0]], H[extra[1]]
            outside_common = [
                w for w in (set(h) & set(k)) if w not in W
            ]
            assert len(outside_common) == 1
            w = outside_common[0]
            u = next(x for x in h if x != w)
            v = next(x for x in k if x != w)
            assert u in W and v in W

            g = edge(u, v)
            gi = H.index(g)
            base = M & ~(1 << extra[0]) & ~(1 << extra[1])
            if (base >> gi) & 1:
                # Direct uv edge already exists: deleting the ear leaves one R.
                assert Z["R"][base] == 1
            else:
                # Suppression adds the new simple edge uv: base has exactly two R.
                assert Z["R"][base | (1 << gi)] == 2

            # The singleton root must contain both ear edges.
            assert ((Q >> extra[0]) & 1) and ((Q >> extra[1]) & 1)

        if partition == (1, 1, 1, 1):
            assert not (set(e) & set(f))
            types = Counter(
                pairing_type(n, mask_edges(H, P), e, f)
                for P in roots
            )
            assert types == Counter({0: 2, 1: 2})

    return partition_count, minimum_gap


def main():
    adjacent = analyze(6, (0, 1), (0, 2))
    disjoint = analyze(6, (0, 1), (2, 3))

    assert adjacent[0] == Counter({(4,): 201, (3, 1): 99})
    assert adjacent[1] == {(4,): 32, (3, 1): 28}

    assert disjoint[0] == Counter({
        (3, 1): 288,
        (4,): 144,
        (2, 2): 89,
        (1, 1, 1, 1): 2,
    })
    assert disjoint[1] == {
        (4,): 64,
        (2, 2): 24,
        (3, 1): 38,
        (1, 1, 1, 1): 36,
    }

    print("adjacent |R|=4 partitions/min gaps:", adjacent)
    print("disjoint |R|=4 partitions/min gaps:", disjoint)
    print("ALL EXACT R4 FIBER-STRUCTURE CHECKS PASSED")


if __name__ == "__main__":
    main()
