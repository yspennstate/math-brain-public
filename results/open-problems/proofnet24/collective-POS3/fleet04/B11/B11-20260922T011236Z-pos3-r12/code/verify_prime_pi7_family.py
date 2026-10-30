#!/usr/bin/env python3
from itertools import combinations


def intervals(N):
    # Path vertices 0,...,N-1 use [i,i+5/4], scaled by 4.
    data = {i: (4*i, 4*i+5) for i in range(N)}
    # Hub z=N uses [5/4,27/4].
    data[N] = (5, 27)
    return data


def overlap(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


def graph_from_intervals(N):
    ints = intervals(N)
    V = list(range(N+1))
    adj = {v: set() for v in V}
    for u, v in combinations(V, 2):
        if overlap(ints[u], ints[v]):
            adj[u].add(v)
            adj[v].add(u)
    return adj


def expected_graph(N):
    z = N
    adj = {v: set() for v in range(N+1)}
    for i in range(N-1):
        adj[i].add(i+1)
        adj[i+1].add(i)
    for i in range(7):
        adj[z].add(i)
        adj[i].add(z)
    return adj


def clique_number(adj):
    V = list(adj)
    best = 0
    for r in range(1, len(V)+1):
        found = False
        for S in combinations(V, r):
            if all(v in adj[u] for u, v in combinations(S, 2)):
                best = r
                found = True
                break
        if not found:
            break
    return best


def nontrivial_modules(adj):
    V = list(adj)
    out = []
    for r in range(2, len(V)):
        for T in combinations(V, r):
            S = set(T)
            ok = True
            for z in V:
                if z in S:
                    continue
                pattern = {s in adj[z] for s in S}
                if len(pattern) > 1:
                    ok = False
                    break
            if ok:
                out.append(T)
    return out


def main():
    rows = []
    for N in range(8, 13):
        adj = graph_from_intervals(N)
        assert adj == expected_graph(N)
        assert max(len(adj[v]) for v in adj) == 7
        assert len(adj[N]) == 7
        assert clique_number(adj) == 3
        mods = nontrivial_modules(adj)
        assert mods == []
        rows.append((N, N+1, 7, 3, len(mods)))
    print("POS3_PRIME_PI7_FAMILY_CHECK_PASS")
    print("N path_vertices total_vertices max_incomparability width nontrivial_modules")
    for row in rows:
        print(*row)


if __name__ == "__main__":
    main()
