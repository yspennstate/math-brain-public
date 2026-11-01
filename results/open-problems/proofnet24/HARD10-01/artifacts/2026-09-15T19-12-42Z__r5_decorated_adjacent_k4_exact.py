#!/usr/bin/env python3
"""
HARD10-01 exact adversarial checker for the 2026-09-15T19:12:42Z report.

Standard library only.

For the same exhaustive representative |R|=5 families used in the preceding
checkpoint, this verifier checks the new load-bearing claims:

  1. the omitted u-v rim arc is a single literal edge;
  2. every non-core edge is confined to one of the two distinguished adjacent
     rim branches u-z or z-v;
  3. if alpha_U and alpha_V are computed independently by exact forest
     enumeration in those two two-terminal branch networks, then the full
     unit-weight Rayleigh gap satisfies

             Delta_G = 44 * alpha_U * alpha_V,

     exactly, with integer arithmetic.

Expected populations:
  n=6 adjacent: 99
  n=6 disjoint: 288
  n=7 adjacent: 1108
  n=7 disjoint: 5040
  total: 6535

The finite computation is an adversarial check only; the universal proof is
in the Markdown report.
"""

from collections import defaultdict
from itertools import combinations


def norm(edge):
    return tuple(sorted(edge))


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
    e, f = norm(e), norm(f)
    all_edges = list(combinations(range(n), 2))
    H = [g for g in all_edges if g not in (e, f)]
    m = len(H)
    N = 1 << m

    names = ("R", "B", "Ne", "Nf", "N0")
    arr = {name: [0] * N for name in names}
    root = [0] * N

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue

        eok = is_forest(n, A + [e])
        fok = is_forest(n, A + [f])
        efok = is_forest(n, A + [e, f])

        if eok and fok and not efok:
            arr["R"][mask] = 1
        elif eok and fok:
            arr["B"][mask] = 1
        elif eok:
            arr["Ne"][mask] = 1
        elif fok:
            arr["Nf"][mask] = 1
        else:
            arr["N0"][mask] = 1

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


def connected(vertices, edges, s, t):
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    return find(s) == find(t)


def terminal_alpha_unit(vertices, edges, terminals, distinguished):
    """Return D*C_e - C*D_e by exact forest enumeration."""
    edges = sorted(norm(g) for g in edges)
    distinguished = norm(distinguished)
    idx = edges.index(distinguished)
    n = max(vertices) + 1

    D = C = De = Ce = 0
    for mask in range(1 << len(edges)):
        A = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        conn = connected(vertices, A, terminals[0], terminals[1])
        has_e = (mask >> idx) & 1
        if conn:
            C += 1
            Ce += has_e
        else:
            D += 1
            De += has_e

    return D * Ce - C * De


def verify_family(n, e, f, expected):
    e, f = norm(e), norm(f)
    H, r, root, counts = fixed_arrays(n, e, f)
    r_masks = [m for m, val in enumerate(r) if val]
    root_masks = [m for m, val in enumerate(root) if val]

    checked = 0
    for M in range(1 << len(H)):
        if counts["R"][M] != 5:
            continue
        checked += 1

        Rs = [A for A in r_masks if (A & ~M) == 0]
        roots = [P for P in root_masks if (P & ~M) == 0]
        assert len(Rs) == 5

        fibers = {P: [A for A in Rs if (P & ~A) == 0] for P in roots}
        assert tuple(sorted((len(x) for x in fibers.values()), reverse=True)) == (4, 1)

        P = max(roots, key=lambda x: len(fibers[x]))
        Q = min(roots, key=lambda x: len(fibers[x]))

        extensions = [A ^ P for A in fibers[P] if A != P]
        assert sorted(x.bit_count() for x in extensions) == [1, 1, 1]
        spokes = [norm(H[(x & -x).bit_length() - 1]) for x in extensions]

        common = set(spokes[0]) & set(spokes[1]) & set(spokes[2])
        assert len(common) == 1
        w = next(iter(common))

        P_edges = edge_set(H, P)
        Q_edges = edge_set(H, Q)
        attachments = [b if a == w else a for a, b in spokes]
        used_spokes = [g for g in spokes if g in Q_edges]
        assert len(used_spokes) == 2
        used_attachments = [b if a == w else a for a, b in used_spokes]
        u, v = used_attachments
        z = next(x for x in attachments if x not in used_attachments)

        principal_cycle = P_edges | {e, f}
        order = cycle_order(principal_cycle)
        arcs = [arc(order, u, v, 1), arc(order, u, v, -1)]
        retained = [item for item in arcs if e in item[1] and f in item[1]]
        assert len(retained) == 1
        retained_vertices, retained_edges = retained[0]
        removed_vertices, removed_edges = next(item for item in arcs if item != retained[0])

        # New Lemma L47: the omitted arc is literally uv.
        assert len(removed_edges) == 1
        assert removed_edges == {norm((u, v))}
        assert set(removed_vertices) == {u, v}

        # Split the retained u-v path at the third spoke attachment z.
        zi = retained_vertices.index(z)
        U_vertices = set(retained_vertices[: zi + 1])
        V_vertices = set(retained_vertices[zi:])
        U_path_edges = {
            norm((retained_vertices[k], retained_vertices[k + 1]))
            for k in range(zi)
        }
        V_path_edges = {
            norm((retained_vertices[k], retained_vertices[k + 1]))
            for k in range(zi, len(retained_vertices) - 1)
        }
        U_dist = [g for g in (e, f) if g in U_path_edges]
        V_dist = [g for g in (e, f) if g in V_path_edges]
        assert len(U_dist) == len(V_dist) == 1
        eU, eV = U_dist[0], V_dist[0]

        all_edges = {e, f} | edge_set(H, M)
        core_edges = principal_cycle | set(spokes)
        extra_edges = all_edges - core_edges

        # New Lemma L48: every extra edge stays within U or within V.
        for a, b in extra_edges:
            assert (
                (a in U_vertices and b in U_vertices)
                or (a in V_vertices and b in V_vertices)
            )

        K_U = {g for g in all_edges if g[0] in U_vertices and g[1] in U_vertices}
        K_V = {g for g in all_edges if g[0] in V_vertices and g[1] in V_vertices}

        alpha_U = terminal_alpha_unit(U_vertices, K_U, (u, z), eU)
        alpha_V = terminal_alpha_unit(V_vertices, K_V, (z, v), eV)
        assert alpha_U >= 0
        assert alpha_V >= 0

        N0 = counts["N0"][M]
        Ne = counts["Ne"][M]
        Nf = counts["Nf"][M]
        B = counts["B"][M]
        R = counts["R"][M]
        assert R == 5

        # Exact five-class Rayleigh gap.
        Delta = Ne * Nf + R * (Ne + Nf + B + R) - B * N0

        # Adjacent K4 at unit weights has exact Rayleigh gap 44.
        assert Delta == 44 * alpha_U * alpha_V
        assert Delta >= 0

    assert checked == expected, (n, e, f, checked, expected)
    print(f"n={n}, e={e}, f={f}: VERIFIED {checked} exact |R|=5 instances")
    return checked


def main():
    tests = [
        (6, (0, 1), (0, 2), 99),
        (6, (0, 1), (2, 3), 288),
        (7, (0, 1), (0, 2), 1108),
        (7, (0, 1), (2, 3), 5040),
    ]

    total = 0
    for args in tests:
        total += verify_family(*args)

    assert total == 6535
    print("TOTAL VERIFIED |R|=5 INSTANCES:", total)
    print("ALL EXACT HARD10-01 DECORATED-ADJACENT-K4 CHECKS PASSED")


if __name__ == "__main__":
    main()
