#!/usr/bin/env python3
"""
HARD10-01 exact adversarial verifier for the 2026-09-15T18:31:40Z report.

Standard library only.

For representative adjacent and disjoint distinguished pairs on all labelled
simple graphs with n=6 and n=7, enumerate every graph with |R|=5 and verify:

  1. root-fiber partition is (4,1);
  2. the size-four fiber is root + three one-edge extensions;
  3. the three extension edges have one common endpoint w outside the root
     cycle and w has full graph degree exactly 3;
  4. the singleton root uses exactly two spokes;
  5. after deleting those spokes, its remaining edges are principal-root edges;
  6. the two common cycles differ by one path exchange;
  7. the unused spoke attaches to the retained common arc;
  8. e and f lie on opposite sides of that third attachment vertex along the
     retained arc, giving the topological-K4 placement proved in the report.

Expected exact populations:
  n=6 adjacent: 99
  n=6 disjoint: 288
  n=7 adjacent: 1108
  n=7 disjoint: 5040
  total: 6535

This is finite self-checking evidence only; the universal proofs are in the
Markdown report.
"""

from collections import defaultdict
from itertools import combinations


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
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
    all_edges = list(combinations(range(n), 2))
    H = [g for g in all_edges if g not in (e, f)]
    m = len(H)
    N = 1 << m
    r = [0] * N
    root = [0] * N

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        if (
            is_forest(n, A + [e])
            and is_forest(n, A + [f])
            and not is_forest(n, A + [e, f])
        ):
            r[mask] = 1

    for mask in range(N):
        if not r[mask]:
            continue
        x = mask
        minimal = True
        while x:
            bit = x & -x
            if r[mask ^ bit]:
                minimal = False
                break
            x -= bit
        if minimal:
            root[mask] = 1

    return H, r, root, zeta(r, m)


def norm(edge):
    return tuple(sorted(edge))


def edge_set(H, mask):
    return {norm(H[i]) for i in range(len(H)) if (mask >> i) & 1}


def cycle_order(edges):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    vertices = [v for v in adj if adj[v]]
    assert vertices
    assert all(len(adj[v]) == 2 for v in vertices)

    start = min(vertices)
    order = [start]
    prev = None
    cur = start
    while True:
        a, b = adj[cur]
        nxt = a if a != prev else b
        if nxt == start:
            break
        order.append(nxt)
        prev, cur = cur, nxt
    assert len(order) == len(vertices)
    return order


def arc(order, u, v, step):
    n = len(order)
    i = order.index(u)
    j = order.index(v)
    vertices = [u]
    while i != j:
        i = (i + step) % n
        vertices.append(order[i])
    edges = {
        norm((vertices[k], vertices[k + 1]))
        for k in range(len(vertices) - 1)
    }
    return vertices, edges


def verify_family(n, e, f, expected):
    H, r, root, Rcnt = fixed_arrays(n, e, f)
    r_masks = [m for m, val in enumerate(r) if val]
    root_masks = [m for m, val in enumerate(root) if val]

    count = 0
    for M in range(1 << len(H)):
        if Rcnt[M] != 5:
            continue
        count += 1

        Rs = [A for A in r_masks if (A & ~M) == 0]
        roots = [P for P in root_masks if (P & ~M) == 0]
        assert len(Rs) == 5

        fibers = {P: [A for A in Rs if (P & ~A) == 0] for P in roots}
        partition = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
        assert partition == (4, 1)

        P = max(roots, key=lambda x: len(fibers[x]))
        Q = min(roots, key=lambda x: len(fibers[x]))

        extensions = [A ^ P for A in fibers[P] if A != P]
        assert sorted(x.bit_count() for x in extensions) == [1, 1, 1]
        spoke_indices = [(x & -x).bit_length() - 1 for x in extensions]
        spokes = [norm(H[i]) for i in spoke_indices]

        common = set(spokes[0]) & set(spokes[1]) & set(spokes[2])
        assert len(common) == 1
        w = next(iter(common))

        P_edges = edge_set(H, P)
        Q_edges = edge_set(H, Q)
        P_support = {v for g in P_edges for v in g}
        assert w not in P_support

        attachments = [b if a == w else a for a, b in spokes]
        assert len(set(attachments)) == 3

        all_edges = {norm(e), norm(f)} | edge_set(H, M)
        assert sum(w in g for g in all_edges) == 3

        used_spokes = [g for g in spokes if g in Q_edges]
        assert len(used_spokes) == 2
        used_attachments = [b if a == w else a for a, b in used_spokes]
        z = next(x for x in attachments if x not in used_attachments)

        # Finite check of the one-bubble conclusion: after deleting the two
        # Q-spokes, every remaining Q edge belongs to P.
        assert Q_edges - set(used_spokes) <= P_edges

        C = P_edges | {norm(e), norm(f)}
        Cq = Q_edges | {norm(e), norm(f)}
        order = cycle_order(C)
        u, v = used_attachments
        arcs = [arc(order, u, v, 1), arc(order, u, v, -1)]

        retained = [
            item
            for item in arcs
            if norm(e) in item[1] and norm(f) in item[1]
        ]
        assert len(retained) == 1
        retained_vertices, retained_edges = retained[0]
        removed_vertices, removed_edges = next(item for item in arcs if item != retained[0])

        assert norm(e) not in removed_edges
        assert norm(f) not in removed_edges
        assert z in retained_vertices
        assert z not in removed_vertices[1:-1]

        # Exact path-exchange edge identity.
        expected_Cq = (C - removed_edges) | set(used_spokes)
        assert Cq == expected_Cq

        # e and f occupy opposite sides of z on the retained path.
        zi = retained_vertices.index(z)
        side = []
        for distinguished in (norm(e), norm(f)):
            k = next(
                k
                for k in range(len(retained_vertices) - 1)
                if norm((retained_vertices[k], retained_vertices[k + 1])) == distinguished
            )
            side.append(k < zi)
        assert side[0] != side[1]

    assert count == expected, (n, e, f, count, expected)
    print(f"n={n}, e={e}, f={f}: verified {count} exact |R|=5 instances")
    return count


def main():
    checks = [
        (6, (0, 1), (0, 2), 99),
        (6, (0, 1), (2, 3), 288),
        (7, (0, 1), (0, 2), 1108),
        (7, (0, 1), (2, 3), 5040),
    ]
    total = 0
    for args in checks:
        total += verify_family(*args)
    assert total == 6535
    print("TOTAL VERIFIED |R|=5 INSTANCES:", total)
    print("ALL EXACT HARD10-01 R5 STAR/K4 CHECKS PASSED")


if __name__ == "__main__":
    main()
