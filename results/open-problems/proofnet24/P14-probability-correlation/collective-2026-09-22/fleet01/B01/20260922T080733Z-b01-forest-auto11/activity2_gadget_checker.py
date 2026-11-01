from itertools import combinations


def forest_terminal_counts(n, edges, s=0, t=1):
    A = B = 0
    m = len(edges)
    for mask in range(1 << m):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ok = True
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                a, b = find(u), find(v)
                if a == b:
                    ok = False
                    break
                parent[a] = b
        if not ok:
            continue
        if find(s) == find(t):
            B += 1
        else:
            A += 1
    return A, B


def connected(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
    return all(find(i) == find(0) for i in range(n))


checked = 0
witness = None
for n in range(2, 8):
    all_edges = list(combinations(range(n), 2))
    for m in range(max(1, n - 1), min(6, len(all_edges)) + 1):
        for edges in combinations(all_edges, m):
            if not connected(n, edges):
                continue
            checked += 1
            A, B = forest_terminal_counts(n, edges)
            if B == 2 * A:
                witness = (n, m, edges, A, B)
                break
        if witness:
            break
    if witness:
        break

print(f"CONNECTED_SIMPLE_GADGETS_AT_MOST_6_EDGES_CHECKED={checked}")
print(f"RATIO2_WITNESS_AT_MOST_6_EDGES={witness}")

candidate = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4))
A, B = forest_terminal_counts(5, candidate)
print(f"SEVEN_EDGE_CANDIDATE_A={A}")
print(f"SEVEN_EDGE_CANDIDATE_B={B}")
print(f"SEVEN_EDGE_CANDIDATE_RATIO2={B == 2*A}")
