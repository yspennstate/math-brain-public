from itertools import combinations

V = (1, 2, 3, 4)
n = 4
s = 2
k = n - 1 - s

weights = {
    (1, 2): 1,
    (3, 4): 2,
    (1, 3): 10,
    (1, 4): 11,
    (2, 3): 12,
    (2, 4): 13,
}
weights = {tuple(sorted(e)): w for e, w in weights.items()}


def w(u, v):
    return weights[tuple(sorted((u, v)))]


# Exact LK(n,k): each vertex proposes its k lowest-weight incident edges;
# an edge is retained iff both endpoints propose it.
proposals = {}
for u in V:
    nbrs = [v for v in V if v != u]
    proposals[u] = set(sorted(nbrs, key=lambda v: w(u, v))[:k])

edges = set()
for u, v in combinations(V, 2):
    if v in proposals[u] and u in proposals[v]:
        edges.add((u, v))

adj = {u: set() for u in V}
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)


def shell(u, j):
    R = set(adj[u])
    for _ in range(j):
        expanded = set(R)
        for x in list(R):
            expanded.update(adj[x])
        R = expanded
    return R


# Connected components.
seen = set()
components = []
for start in V:
    if start in seen:
        continue
    comp = {start}
    stack = [start]
    seen.add(start)
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                comp.add(y)
                stack.append(y)
    components.append(comp)

u, v = 1, 3
shell_hits = []
for j in range(s + 1):
    R = shell(u, j)
    shell_hits.append(bool(R & adj[v]))

print(f"n={n} s={s} k={k}")
print("weights=" + repr(sorted(weights.items())))
print("proposals=" + repr({u: sorted(x) for u, x in proposals.items()}))
print("LK_edges=" + repr(sorted(edges)))
print("components=" + repr([sorted(c) for c in components]))
print(f"N({u})={sorted(adj[u])} N({v})={sorted(adj[v])}")
for j in range(s + 1):
    print(f"j={j} R_j={sorted(shell(u, j))} intersects_N({v})={shell_hits[j]}")
print("cross_component_shell_exists=" + repr(any(shell_hits)))

assert k == 1
assert edges == {(1, 2), (3, 4)}
assert [sorted(c) for c in components] == [[1, 2], [3, 4]]
assert not any(shell_hits)
print("ALL_EXACT_CHECKS_PASS")
