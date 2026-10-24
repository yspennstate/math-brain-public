from itertools import combinations, product
from collections import deque, defaultdict


def is_acyclic(adj):
    n = len(adj)
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    q = deque(i for i, d in enumerate(indeg) if d == 0)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == n


def asymmetry_dag(K):
    n = len(K)
    D = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            uv = v in K[u]
            vu = u in K[v]
            if uv and not vu:
                D[u].add(v)
            elif vu and not uv:
                D[v].add(u)
    return D


def comparison_dag(K):
    n = len(K)
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    D = [set() for _ in edges]
    for v in range(n):
        selected = []
        rejected = []
        for u in range(n):
            if u == v:
                continue
            e = tuple(sorted((u, v)))
            (selected if u in K[v] else rejected).append(idx[e])
        for a in selected:
            D[a].update(rejected)
    return D


def mutual_graph(K):
    n = len(K)
    G = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if v in K[u] and u in K[v]:
                G[u].add(v)
                G[v].add(u)
    return G


def diameter(G):
    n = len(G)
    ans = 0
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in G[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    q.append(v)
        if -1 in d:
            return None
        ans = max(ans, max(d))
    return ans


def lk_from_integer_weights(n, k, w):
    K = [set() for _ in range(n)]
    for v in range(n):
        inc = []
        for u in range(n):
            if u == v:
                continue
            e = tuple(sorted((u, v)))
            inc.append((w[e], u))
        inc.sort()
        K[v] = {u for _, u in inc[:k]}
    return K, mutual_graph(K)


def s3_classifier(G):
    n = len(G)
    if diameter(G) is None:
        return None
    D = 2
    for u in range(n):
        for v in range(u + 1, n):
            if v in G[u]:
                continue
            A = G[u]
            B = G[v]
            if A & B:
                d = 2
            elif any((b in G[a]) for a in A for b in B):
                d = 3
            else:
                NA = set()
                NB = set()
                for a in A:
                    NA.update(G[a])
                for b in B:
                    NB.update(G[b])
                d = 4 if (NA & NB) else 5
            D = max(D, d)
    return D


def build_extremal_profile(s, q):
    m = s + 3
    n = m + q
    k = q + 2
    Q = set(range(m, n))
    K = [set() for _ in range(n)]
    for y in Q:
        K[y] = (Q - {y}) | {0, 1, 2}
    K[0] = Q | {1, 2}
    for i in range(1, m - 1):
        K[i] = Q | {i - 1, i + 1}
    K[m - 1] = Q | {m - 3, m - 2}
    assert all(len(S) == k for S in K)
    return K


# 1. Exhaustive finite check of the realizability criterion:
# a k-selection profile is realizable iff its vertex-asymmetry digraph is acyclic.
profile_count = 0
for n, k in [(4, 1), (4, 2), (5, 2), (5, 3)]:
    opts = []
    for v in range(n):
        others = [u for u in range(n) if u != v]
        opts.append([set(c) for c in combinations(others, k)])
    local = 0
    for tup in product(*opts):
        K = list(tup)
        a = is_acyclic(asymmetry_dag(K))
        b = is_acyclic(comparison_dag(K))
        assert a == b
        local += 1
    profile_count += local
    print(f"REALIZABILITY_EQUIVALENCE n={n} k={k} profiles={local} PASS")

# 2. Exact integer-weight s=3 sharpness witness: LK(6,2)=P6.
n = 6
k = 2
edges = list(combinations(range(n), 2))
w = {
    (0, 1): 4,
    (1, 2): 3,
    (2, 3): 1,
    (3, 4): 2,
    (4, 5): 5,
    (0, 2): 55,
    (3, 5): 65,
}
for value, e in enumerate([e for e in edges if e not in w], start=101):
    w[e] = value
K, G = lk_from_integer_weights(n, k, w)
expected = [{1}, {0, 2}, {1, 3}, {2, 4}, {3, 5}, {4}]
assert G == expected
assert diameter(G) == 5
assert s3_classifier(G) == 5
print("EXPLICIT_S3_WITNESS LK(6,2)=P6 diameter=5 PASS")

# 3. Exhaustive n=6,k=2 local-profile census, using the exact
# realizability criterion; compare the s=3 shell classifier with BFS.
opts = []
for v in range(6):
    others = [u for u in range(6) if u != v]
    opts.append([set(c) for c in combinations(others, 2)])
realizable = 0
connected = 0
diam_counts = defaultdict(int)
mismatch = 0
for tup in product(*opts):
    K = list(tup)
    if not is_acyclic(asymmetry_dag(K)):
        continue
    realizable += 1
    G = mutual_graph(K)
    d = diameter(G)
    if d is not None:
        connected += 1
        diam_counts[d] += 1
        if s3_classifier(G) != d:
            mismatch += 1
assert mismatch == 0
assert realizable == 272860
assert connected == 5460
assert diam_counts == {3: 60, 5: 5400}
print("S3_N6_EXHAUSTIVE realizable=272860 connected=5460 diam3=60 diam5=5400 mismatches=0 PASS")

# 4. Check the all-s/all-n sharpness profile over a broad exact finite grid.
cases = 0
for s in range(1, 13):
    for q in range(0, 7):
        K = build_extremal_profile(s, q)
        assert is_acyclic(asymmetry_dag(K))
        G = mutual_graph(K)
        assert diameter(G) == s + 2
        cases += 1
print(f"EXTREMAL_PROFILE_GRID cases={cases} s=1..12 q=0..6 PASS")

print(f"TOTAL_REALIZABILITY_PROFILES_CHECKED={profile_count}")
print("ALL_EXACT_CHECKS_PASS")
