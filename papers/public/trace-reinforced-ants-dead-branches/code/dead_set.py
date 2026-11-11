# The two edge sets of the paper, for a graph G (networkx) with nest N and food F.
#
# branch_edges(G, N, F): the edges covered by Theorem 2. For every neighbour u of F and every edge e = {u, y} of G - F,
#   y != N, such that the component H of y in G - F - e contains neither u nor N: the edge e, every edge inside H and
#   every edge between H and F.
#
# dead_set(G, N, F): the set D(G, N, F) of Conjecture 9. Let R be the component of N in G - F and I0 the component of
#   N in G - F - N(F) (empty if N is adjacent to F). The front A is the set of neighbours of F adjacent to I0
#   (A = {N} if N is adjacent to F); the shadow is R - I0.
#   (D1) {x, F} for every neighbour x of F in R outside A;
#   (D2) for every shadow vertex u and every bridge e = {u, y} of G - F whose far side H does not contain N:
#        e, every edge inside H and every edge between H and F.
import networkx as nx

def _branches(G, H, us, N, F):
    dead = set()
    for u in us:
        for y in list(H.neighbors(u)):
            if y == N: continue
            H.remove_edge(u, y)
            comp = nx.node_connected_component(H, y)
            H.add_edge(u, y)
            if u in comp or N in comp: continue
            dead.add(frozenset((u, y)))
            for a, b in G.edges():
                if (a in comp and b in comp) or (a in comp and b == F) or (b in comp and a == F): dead.add(frozenset((a, b)))
    return dead

def branch_edges(G, N, F):
    H = G.copy(); H.remove_node(F); R = nx.node_connected_component(H, N)
    return _branches(G, H, [u for u in G.neighbors(F) if u in R], N, F)

def front_and_interior(G, N, F):
    H = G.copy(); H.remove_node(F); R = nx.node_connected_component(H, N)
    NF = set(G.neighbors(F)) & R
    if N in NF: return H, R, NF, set(), {N}
    K = H.copy(); K.remove_nodes_from(NF); I0 = nx.node_connected_component(K, N)
    A = set(x for x in NF if any(z in I0 for z in H.neighbors(x)))
    return H, R, NF, I0, A

def dead_set(G, N, F):
    H, R, NF, I0, A = front_and_interior(G, N, F)
    dead = set(frozenset((x, F)) for x in NF - A)
    return dead | _branches(G, H, list(R - I0), N, F)

def has_shadowed_neighbour(G, N, F):
    # hypothesis of Theorem 5: N not adjacent to F and some neighbour of F has no neighbour in I0
    if G.has_edge(N, F): return False
    H, R, NF, I0, A = front_and_interior(G, N, F)
    return len(NF - A) > 0
