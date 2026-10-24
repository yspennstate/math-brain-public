"""Edge-set coordinates of fixed graphs H and generators of Aut(H) acting on edges."""
import itertools


def bip_edges(a, b):
    return [(i, j) for i in range(a) for j in range(b)]


def kab(a, b):
    """K_{a,b}: edge (i,j) -> index i*b + j. Generators: row cycles/transpositions, column
    cycles/transpositions, transpose if a == b."""
    E = bip_edges(a, b)
    idx = {e: k for k, e in enumerate(E)}
    gens = []
    def rowperm(p):
        return tuple(idx[(p[i], j)] for (i, j) in E)
    def colperm(q):
        return tuple(idx[(i, q[j])] for (i, j) in E)
    if a > 1:
        gens.append(rowperm([1, 0] + list(range(2, a))))
        gens.append(rowperm(list(range(1, a)) + [0]))
    if b > 1:
        gens.append(colperm([1, 0] + list(range(2, b))))
        gens.append(colperm(list(range(1, b)) + [0]))
    if a == b:
        gens.append(tuple(idx[(j, i)] for (i, j) in E))
    return len(E), gens, E


def kn(n):
    E = list(itertools.combinations(range(n), 2))
    idx = {e: k for k, e in enumerate(E)}
    def vperm(p):
        return tuple(idx[tuple(sorted((p[i], p[j])))] for (i, j) in E)
    gens = [vperm([1, 0] + list(range(2, n))), vperm(list(range(1, n)) + [0])]
    return len(E), gens, E


def graph_from_edges(edges):
    """Arbitrary graph H given by an edge list on vertices 0..n-1; Aut(H) computed by brute force
    (n <= 9)."""
    n = 1 + max(max(e) for e in edges)
    E = [tuple(sorted(e)) for e in edges]
    Es = set(E)
    idx = {e: k for k, e in enumerate(E)}
    auts = []
    for p in itertools.permutations(range(n)):
        if all(tuple(sorted((p[i], p[j]))) in Es for (i, j) in E):
            auts.append(tuple(idx[tuple(sorted((p[i], p[j])))] for (i, j) in E))
    return len(E), auts, E


def cube3():
    # Q3: vertices 0..7, edges between words differing in one bit
    edges = [(x, x ^ (1 << i)) for x in range(8) for i in range(3) if x < x ^ (1 << i)]
    return graph_from_edges(edges)


def petersen():
    outer = [(i, (i + 1) % 5) for i in range(5)]
    spokes = [(i, i + 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return graph_from_edges(outer + spokes + inner)


def has_pm_bip(X, E, a, b):
    """Does the bipartite edge subset (bitmask X over E) saturate the smaller side a <= b?"""
    adj = [[] for _ in range(a)]
    for k, (i, j) in enumerate(E):
        if (X >> k) & 1:
            adj[i].append(j)
    match = [-1] * b
    def try_(i, seen):
        for j in adj[i]:
            if not seen[j]:
                seen[j] = True
                if match[j] < 0 or try_(match[j], seen):
                    match[j] = i
                    return True
        return False
    for i in range(a):
        if not try_(i, [False] * b):
            return False
    return True
