#!/usr/bin/env python3
r"""
Independent exact audit for P14 equation (5.1), used by
P14-FOREST-N8-UNIT-PAIR-CERT-01.

For every labeled simple graph on n<=5 vertices and every nonempty vertex subset S,
verify exactly:
    F_G(S) = sum_{T subseteq S, min(S) in T} tau_G(T) F_G(S\T),
where F_G(S) is the number of forests of G[S] and tau_G(T) is the number of
spanning trees of G[T], with tau(singleton)=1.

All computations are integer exhaustive enumeration.
"""
from itertools import combinations


def all_edges(n):
    return list(combinations(range(n), 2))


def acyclic(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
    return True


def forest_count(n, E, S):
    allowed = [e for e in E if (S >> e[0]) & 1 and (S >> e[1]) & 1]
    total = 0
    for mask in range(1 << len(allowed)):
        chosen = [allowed[k] for k in range(len(allowed)) if (mask >> k) & 1]
        if acyclic(n, chosen):
            total += 1
    return total


def tree_count(n, E, T):
    verts = [v for v in range(n) if (T >> v) & 1]
    if len(verts) == 1:
        return 1
    allowed = [e for e in E if (T >> e[0]) & 1 and (T >> e[1]) & 1]
    need = len(verts) - 1
    total = 0
    for chosen in combinations(allowed, need):
        if not acyclic(n, chosen):
            continue
        parent = {v: v for v in verts}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in chosen:
            ra, rb = find(a), find(b)
            parent[rb] = ra
        if len({find(v) for v in verts}) == 1:
            total += 1
    return total


graphs = 0
subset_checks = 0

for n in range(1, 6):
    universe = all_edges(n)
    for gmask in range(1 << len(universe)):
        E = [universe[k] for k in range(len(universe)) if (gmask >> k) & 1]
        graphs += 1
        F = {S: forest_count(n, E, S) for S in range(1 << n)}
        tau = {T: tree_count(n, E, T) for T in range(1, 1 << n)}
        for S in range(1, 1 << n):
            a = (S & -S).bit_length() - 1
            rhs = 0
            T = S
            while T:
                if (T >> a) & 1:
                    rhs += tau[T] * F[S ^ T]
                T = (T - 1) & S
            assert F[S] == rhs, (n, tuple(E), S, F[S], rhs)
            subset_checks += 1

print("P13 independent peer audit of P14 equation (5.1)")
print("scope: every labeled simple graph on n=1,2,3,4,5 and every nonempty vertex subset")
print(f"graphs_checked={graphs}")
print(f"subset_recurrences_checked={subset_checks}")
print("result=PASS")
