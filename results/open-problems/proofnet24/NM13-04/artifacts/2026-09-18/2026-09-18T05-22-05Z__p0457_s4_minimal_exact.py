from itertools import product, combinations
from collections import deque


def selections_from_weights(n, k, weights):
    K = []
    for v in range(n):
        inc = sorted((weights[tuple(sorted((v, u)))], u)
                     for u in range(n) if u != v)
        K.append(frozenset(u for _, u in inc[:k]))
    return K


def mutual_graph(n, K):
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in K[u]:
            if u in K[v]:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def connected(adj):
    seen = {0}
    q = deque([0])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return len(seen) == len(adj)


def all_pairs_dist(adj):
    n = len(adj)
    D = [[None] * n for _ in range(n)]
    for s in range(n):
        D[s][s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if D[s][w] is None:
                    D[s][w] = D[s][v] + 1
                    q.append(w)
    return D


def asymmetry_arcs(K):
    arcs = set()
    for u in range(len(K)):
        for v in K[u]:
            if u not in K[v]:
                arcs.add((u, v))
    return arcs


def acyclic(n, arcs):
    out = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in arcs:
        out[u].append(v)
        indeg[v] += 1
    q = deque(i for i, d in enumerate(indeg) if d == 0)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in out[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == n


def path_weights_n7():
    w = {(i, i + 1): i + 1 for i in range(6)}
    w[(0, 2)] = 150
    w[(4, 6)] = 140
    z = 301
    for e in combinations(range(7), 2):
        if e not in w:
            w[e] = z
            z += 1
    return w


def cycle_weights_n7():
    cyc = {tuple(sorted((i, (i + 1) % 7))) for i in range(7)}
    w = {e: j for j, e in enumerate(sorted(cyc), 1)}
    z = 301
    for e in combinations(range(7), 2):
        if e not in w:
            w[e] = z
            z += 1
    return w


def set_distance(adj, A, B):
    if A & B:
        return 0
    dist = [None] * len(adj)
    q = deque()
    for a in A:
        dist[a] = 0
        q.append(a)
    while q:
        u = q.popleft()
        if u in B:
            return dist[u]
        for v in adj[u]:
            if dist[v] is None:
                dist[v] = dist[u] + 1
                q.append(v)
    return None


# Exact P7 source witness for s=4: n=7, k=2.
wp = path_weights_n7()
Kp = selections_from_weights(7, 2, wp)
target = [
    frozenset([1, 2]),
    frozenset([0, 2]),
    frozenset([1, 3]),
    frozenset([2, 4]),
    frozenset([3, 5]),
    frozenset([4, 6]),
    frozenset([4, 5]),
]
assert Kp == target
adjp = mutual_graph(7, Kp)
assert all(adjp[i] == ({i - 1} if i == 6 else {i + 1} if i == 0
                        else {i - 1, i + 1}) for i in range(7))
Dp = all_pairs_dist(adjp)
assert Dp[0][6] == 6 and max(max(row) for row in Dp) == 6
arcs = asymmetry_arcs(Kp)
assert arcs == {(0, 2), (6, 4)} and acyclic(7, arcs)

# Exact C7 source witness at the same minimal order.
wc = cycle_weights_n7()
Kc = selections_from_weights(7, 2, wc)
adjc = mutual_graph(7, Kc)
assert connected(adjc)
assert all(len(x) == 2 for x in adjc)
Dc = all_pairs_dist(adjc)
assert max(max(row) for row in Dc) == 3
assert asymmetry_arcs(Kc) == set()

# Exhaust every local k=1 profile at n=6.  There are 5^6 profiles, and none
# can have a connected mutual graph.  This independently certifies that n=7
# is the first order at which a connected s=4 source realization is possible.
n = 6
neighbors = [[u for u in range(n) if u != v] for v in range(n)]
profiles = 0
conn = 0
for choices in product(range(5), repeat=6):
    K = [frozenset([neighbors[v][choices[v]]]) for v in range(n)]
    profiles += 1
    if connected(mutual_graph(n, K)):
        conn += 1
assert profiles == 15625 and conn == 0

# Check the neighbor-shell identity d(u,v)=2+d(N(u),N(v)) on every missing
# pair of both explicit minimal-order witnesses.
shell_checks = 0
for adj, D in [(adjp, Dp), (adjc, Dc)]:
    for u, v in combinations(range(len(adj)), 2):
        if v not in adj[u]:
            sd = set_distance(adj, adj[u], adj[v])
            assert D[u][v] == 2 + sd
            shell_checks += 1
assert set_distance(adjp, adjp[0], adjp[6]) == 4

print('P7 selections =', [sorted(s) for s in Kp])
print('P7 asymmetry arcs =', sorted(arcs))
print('P7 mutual graph edges =',
      [(u, v) for u in range(7) for v in adjp[u] if u < v])
print('P7 diameter =', max(max(row) for row in Dp))
print('C7 diameter =', max(max(row) for row in Dc))
print('n=6,k=1 local profiles checked =', profiles)
print('n=6,k=1 connected mutual profiles =', conn)
print('neighbor-shell identity missing-pair checks =', shell_checks)
print('endpoint set-distance for P7 (0,6) =',
      set_distance(adjp, adjp[0], adjp[6]))
print('ALL_EXACT_CHECKS_PASS')
