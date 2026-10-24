#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter, deque


def edges_of(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def incident(n):
    inc = [[] for _ in range(n)]
    for e in edges_of(n):
        i, j = e
        inc[i].append(e)
        inc[j].append(e)
    return inc


def realizable(n, profile):
    """Exact: chosen edges are the two largest at each vertex iff the strict comparison DAG is acyclic."""
    E = edges_of(n)
    idx = {e: t for t, e in enumerate(E)}
    inc = incident(n)
    out = [set() for _ in E]
    indeg = [0] * len(E)
    for v, Rt in enumerate(profile):
        R = set(Rt)
        for hi in R:
            for lo in inc[v]:
                if lo not in R:
                    a, b = idx[lo], idx[hi]
                    if b not in out[a]:
                        out[a].add(b)
                        indeg[b] += 1
    q = deque(i for i, d in enumerate(indeg) if d == 0)
    seen = 0
    while q:
        a = q.popleft()
        seen += 1
        for b in out[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                q.append(b)
    return seen == len(E)


def graphs_from_profile(n, profile):
    H = [set() for _ in range(n)]
    for R in profile:
        for i, j in R:
            H[i].add(j)
            H[j].add(i)
    G = [set(range(n)) - {i} for i in range(n)]
    for i in range(n):
        G[i] -= H[i]
    return G, H


def components(G):
    seen = set()
    comps = []
    for s in range(len(G)):
        if s in seen:
            continue
        q = [s]
        seen.add(s)
        c = []
        for u in q:
            c.append(u)
            for v in G[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        comps.append(c)
    return comps


def diameter(G):
    if len(components(G)) != 1:
        return None
    ans = 0
    for s in range(len(G)):
        dist = [-1] * len(G)
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in G[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        ans = max(ans, max(dist))
    return ans


def degeneracy(H):
    rem = set(range(len(H)))
    deg = [len(H[v]) for v in range(len(H))]
    ans = 0
    while rem:
        v = min(rem, key=lambda x: (deg[x], x))
        ans = max(ans, deg[v])
        rem.remove(v)
        for u in H[v]:
            if u in rem:
                deg[u] -= 1
    return ans


def theorem_class(G, H):
    comps = components(G)
    if len(comps) > 1:
        return ("disc", tuple(sorted((len(c) for c in comps), reverse=True)))
    bad = False
    for u in range(len(G)):
        for v in H[u]:
            if u >= v:
                continue
            A = G[u]
            B = G[v]
            if A & B:
                continue
            bad = True
            if all((b not in G[a]) for a in A for b in B):
                return 4
    return 3 if bad else 2


def enumerate_profiles(n):
    inc = incident(n)
    choices = [list(combinations(inc[v], 2)) for v in range(n)]
    total = 1
    for c in choices:
        total *= len(c)
    real = 0
    counts = Counter()
    mismatch = 0
    max_degen = 0
    for profile in product(*choices):
        if not realizable(n, profile):
            continue
        real += 1
        G, H = graphs_from_profile(n, profile)
        max_degen = max(max_degen, degeneracy(H))
        d = diameter(G)
        truth = d if d is not None else ("disc", tuple(sorted((len(c) for c in components(G)), reverse=True)))
        got = theorem_class(G, H)
        counts[truth] += 1
        if got != truth:
            mismatch += 1
    print(f"n={n} total_profiles={total} realizable_profiles={real}")
    print(f"n={n} outcome_counts={dict(sorted(counts.items(), key=lambda kv: str(kv[0])))}")
    print(f"n={n} max_H_degeneracy={max_degen} theorem_mismatches={mismatch}")
    assert max_degen <= 2
    assert mismatch == 0
    for key in counts:
        if isinstance(key, tuple) and key[0] == "disc":
            assert sum(key[1][1:]) <= 2


def graph_from_order(n, order_text):
    toks = order_text.split()
    order = []
    for t in toks:
        a, b = int(t[0]) - 1, int(t[1]) - 1
        order.append((min(a, b), max(a, b)))
    assert set(order) == set(edges_of(n)) and len(order) == len(edges_of(n))
    rank = {e: r for r, e in enumerate(order)}
    inc = incident(n)
    profile = []
    for v in range(n):
        profile.append(tuple(sorted(inc[v], key=lambda e: rank[e], reverse=True)[:2]))
    G, H = graphs_from_profile(n, profile)
    return G, H


WITNESSES = {
    "diam2": "13 34 45 26 12 36 25 56 35 16 24 15 14 23 46",
    "diam3": "13 15 46 56 14 34 16 25 36 35 23 24 12 26 45",
    "diam4": "25 15 12 35 14 46 45 34 56 16 23 24 13 36 26",
    "disc_5_1": "34 14 24 12 25 45 35 26 13 36 23 56 15 16 46",
    "disc_4_2": "23 35 12 15 13 36 46 34 16 56 26 24 14 45 25",
    "disc_4_1_1": "24 26 56 46 16 45 25 23 35 14 36 34 12 15 13",
}

for n in (5, 6):
    enumerate_profiles(n)

for name, ordtxt in WITNESSES.items():
    G, H = graph_from_order(6, ordtxt)
    d = diameter(G)
    comps = tuple(sorted((len(c) for c in components(G)), reverse=True))
    got = theorem_class(G, H)
    print(f"witness={name} diameter={d} components={comps} theorem={got}")
    if name.startswith("diam"):
        assert d == int(name[-1])
    elif name == "disc_5_1":
        assert d is None and comps == (5, 1)
    elif name == "disc_4_2":
        assert d is None and comps == (4, 2)
    elif name == "disc_4_1_1":
        assert d is None and comps == (4, 1, 1)

print("ALL_EXACT_CHECKS_PASS")
