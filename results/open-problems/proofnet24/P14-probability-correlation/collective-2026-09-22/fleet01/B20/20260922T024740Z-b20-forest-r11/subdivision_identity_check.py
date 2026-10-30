from fractions import Fraction


def is_forest(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    return all(union(u, v) for u, v in edges)


def unit_counts(vertices, edges, e, f):
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        A = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(vertices, A):
            continue
        Z += 1
        xe = e in A
        xf = f in A
        Ze += int(xe)
        Zf += int(xf)
        Zef += int(xe and xf)
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


def weighted_counts(vertices, edges, weights, e, f):
    Z = Ze = Zf = Zef = Fraction(0)
    for mask in range(1 << len(edges)):
        A = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(vertices, A):
            continue
        w = Fraction(1)
        for h in A:
            w *= weights[h]
        Z += w
        if e in A:
            Ze += w
        if f in A:
            Zf += w
        if e in A and f in A:
            Zef += w
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


def subdivide_nonedges(n, graph_edges, a):
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    graph_edges = set(graph_edges)
    vertices = set(range(n))
    edges = []
    nxt = n
    for u, v in all_edges:
        if (u, v) in graph_edges:
            edges.append((u, v))
            continue
        path = [u] + list(range(nxt, nxt + a - 1)) + [v]
        nxt += a - 1
        vertices.update(path[1:-1])
        edges.extend(zip(path, path[1:]))
    return sorted(vertices), list(edges)


n = 4
G = {(0, 1), (0, 2), (1, 2), (2, 3)}
e, f = (0, 1), (0, 2)
K = [(i, j) for i in range(n) for j in range(i + 1, n)]
m = len(K) - len(G)

for a in (2, 3):
    D = 2 ** a - 1
    q = Fraction(1, D)
    weights = {h: (Fraction(1) if h in G else q) for h in K}
    weighted = weighted_counts(range(n), K, weights, e, f)
    vertices, expanded_edges = subdivide_nonedges(n, G, a)
    expanded = unit_counts(vertices, expanded_edges, e, f)
    count_factor = D ** m
    gap_factor = D ** (2 * m)
    assert expanded[:4] == tuple(count_factor * x for x in weighted[:4])
    assert expanded[4] == gap_factor * weighted[4]
    print(f"a={a} D={D} q={q} m={m}")
    print("weighted", weighted)
    print("expanded", expanded)
    print("count_factor", count_factor, "gap_factor", gap_factor, "PASS")
