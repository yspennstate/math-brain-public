from fractions import Fraction
import itertools
import networkx as nx


def inv_matrix(A):
    n = len(A)
    M = [list(map(Fraction, row)) + [Fraction(int(i == j)) for j in range(n)]
         for i, row in enumerate(A)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col] != 0), None)
        assert pivot is not None
        M[col], M[pivot] = M[pivot], M[col]
        p = M[col][col]
        M[col] = [x / p for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            f = M[r][col]
            if f:
                M[r] = [M[r][j] - f * M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]


def kemeny_fraction(G):
    nodes = list(G.nodes())
    n = len(nodes)
    deg = [G.degree(v) for v in nodes]
    m = G.number_of_edges()
    pi = [Fraction(d, 2*m) for d in deg]
    A = []
    for i, u in enumerate(nodes):
        row = []
        for j, v in enumerate(nodes):
            p = Fraction(1, deg[i]) if G.has_edge(u, v) else Fraction(0)
            row.append(Fraction(int(i == j)) - p + pi[j])
        A.append(row)
    Z = inv_matrix(A)
    return sum(Z[i][i] for i in range(n)) - 1


def c4_check(G, H):
    n = G.number_of_nodes()
    mG, mH = G.number_of_edges(), H.number_of_edges()
    q = mG - mH
    KG, KH = kemeny_fraction(G), kemeny_fraction(H)
    rhs = Fraction(mH, mG) * KH + Fraction(n - 1) * Fraction(2*q*mH + q*q, mG)
    rhs2 = KH + 2*q*(n - 1) + Fraction(q*q*(n - 1), mG)
    assert KG <= rhs
    assert KG <= rhs2


def direct_bridge_contribution(G):
    m = G.number_of_edges()
    deg = dict(G.degree())
    total = Fraction(0)
    for u, v in nx.bridges(G):
        H = G.copy()
        H.remove_edge(u, v)
        side = nx.node_connected_component(H, u)
        vol = sum(deg[x] for x in side)
        total += Fraction(vol * (2*m - vol), 2*m)
    return total


def bridge_block_formula(G):
    m = G.number_of_edges()
    bridges = list(nx.bridges(G))
    H = G.copy()
    H.remove_edges_from(bridges)
    comps = list(nx.connected_components(H))
    comp_idx = {}
    for i, C in enumerate(comps):
        for v in C:
            comp_idx[v] = i
    mi = [G.subgraph(C).number_of_edges() for C in comps]
    w = [x + 1 for x in mi]
    W = m + 1
    Q = nx.Graph()
    Q.add_nodes_from(range(len(comps)))
    for u, v in bridges:
        Q.add_edge(comp_idx[u], comp_idx[v])
    dists = dict(nx.all_pairs_shortest_path_length(Q))
    Ed = Fraction(0)
    for i in range(len(comps)):
        for j in range(len(comps)):
            Ed += Fraction(w[i], W) * Fraction(w[j], W) * dists[i][j]
    return Fraction((m + 1)**2, m) * Ed - Fraction((2*m + 1) * Q.number_of_edges(), 2*m)


def resistance_diameter_component(G, nodes):
    H = G.subgraph(nodes).copy()
    vs = list(H.nodes())
    if len(vs) <= 1:
        return Fraction(0)
    root = vs[-1]
    others = vs[:-1]
    idx = {v: i for i, v in enumerate(others)}
    L = []
    for u in others:
        row = []
        for v in others:
            if u == v:
                row.append(Fraction(H.degree(u)))
            else:
                row.append(Fraction(-1 if H.has_edge(u, v) else 0))
        L.append(row)
    Q = inv_matrix(L)

    def R(a, b):
        if a == b:
            return Fraction(0)
        if a == root:
            return Q[idx[b]][idx[b]]
        if b == root:
            return Q[idx[a]][idx[a]]
        ia, ib = idx[a], idx[b]
        return Q[ia][ia] + Q[ib][ib] - 2*Q[ia][ib]

    return max((R(a, b) for a, b in itertools.combinations(vs, 2)), default=Fraction(0))


atlas = nx.graph_atlas_g()
connected6 = [G for G in atlas if 2 <= G.number_of_nodes() <= 6 and nx.is_connected(G)]
connected7 = [G for G in atlas if 2 <= G.number_of_nodes() <= 7 and nx.is_connected(G)]

# C4: all connected one-edge deletions for atlas graphs through 6 vertices.
c4_single = 0
for G in connected6:
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H):
            c4_check(G, H)
            c4_single += 1
assert c4_single == 976
print("C4_single_deletion_exact_cases", c4_single, "PASS")

# C4: multi-edge deletion stress test, replacing every connected atlas graph by a spanning tree.
c4_tree = 0
for G in connected6:
    H = nx.minimum_spanning_tree(G)
    c4_check(G, H)
    c4_tree += 1
assert c4_tree == 142
print("C4_spanning_tree_exact_cases", c4_tree, "PASS")

# C6: exact bridge-block identity for every connected atlas graph through 7 vertices.
bridge_cases = 0
for G in connected7:
    assert direct_bridge_contribution(G) == bridge_block_formula(G)
    bridge_cases += 1
assert bridge_cases == 995
print("C6_bridge_identity_all_atlas_connected_n_le_7", bridge_cases, "PASS")

# C7: natural bridge-block instance of the series/resistance-diameter inequality through 6 vertices.
c7_cases = 0
for G in connected6:
    bridges = list(nx.bridges(G))
    H0 = G.copy()
    H0.remove_edges_from(bridges)
    comps = list(nx.connected_components(H0))
    eps = max((resistance_diameter_component(G, C) for C in comps), default=Fraction(0))
    lhs = kemeny_fraction(G)
    rhs = direct_bridge_contribution(G) + G.number_of_edges() * G.number_of_nodes() * eps
    assert lhs <= rhs
    c7_cases += 1
assert c7_cases == 142
print("C7_bridge_block_series_bound_connected_n_le_6", c7_cases, "PASS")

# C6 variational core: p_i proportional to integer squares, so Q2*S^2 and (1-Q2)/S^2 are exact rationals.
holder_cases = 0
min_q2s2 = None
max_ratio = Fraction(0)
for k in range(1, 6):
    for a in itertools.product(range(1, 6), repeat=k):
        den = sum(x*x for x in a)
        Q2 = Fraction(sum(x**4 for x in a), den*den)
        S2 = Fraction(sum(a)**2, den)
        product = Q2 * S2
        ratio = (1 - Q2) / S2
        assert product >= 1
        assert ratio <= Fraction(1, 4)
        min_q2s2 = product if min_q2s2 is None else min(min_q2s2, product)
        max_ratio = max(max_ratio, ratio)
        holder_cases += 1
assert holder_cases == 3905
assert min_q2s2 == 1
assert max_ratio == Fraction(1, 4)
print("C6_holder_square_rational_vectors", holder_cases, "PASS",
      "min_Q2S2", min_q2s2, "max_ratio", max_ratio)

# Exact scalar optimization identity:
# 1/54 - s^2(1-s)/8 = (3s-2)^2(3s+1)/216 >= 0 on [0,1].
scalar_cases = 0
for j in range(1001):
    s = Fraction(j, 1000)
    lhs = Fraction(1, 54) - s*s*(1-s)/8
    rhs = (3*s-2)**2 * (3*s+1) / 216
    assert lhs == rhs
    assert lhs >= 0
    scalar_cases += 1
assert scalar_cases == 1001
assert Fraction(1, 54) - Fraction(4, 9)*Fraction(1, 3)/8 == 0
print("C6_scalar_optimization_exact_grid", scalar_cases, "PASS",
      "factorization_exact", "YES", "equality_s", Fraction(2, 3))

print("P26-I0027-AUDIT-EXACT-CHECK: PASS")
