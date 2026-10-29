"""Statement S (colouring form), exhaustively: every labelled multigraph on 4 vertices with m edges, every ordered
triple (u, v, w); and every graph on 5 and 6 vertices (networkx atlas), every ordered triple. python colour_triple_all.py"""
import itertools, time
from collections import defaultdict
import networkx as nx
from e1_swap import comps


def s_fails(V, H):
    m = len(H)
    cfg = []
    for mask in range(1 << m):
        kr, fr = comps(V, [H[j] for j in range(m) if mask >> j & 1])
        kb, fb = comps(V, [H[j] for j in range(m) if not mask >> j & 1])
        cfg.append((kr + kb, [fr(x) for x in range(V)], [fb(x) for x in range(V)]))
    cases = fails = 0
    for u, v, w in itertools.permutations(range(V), 3):
        T = defaultdict(int)
        for k, r, b in cfg:
            if r[u] == r[v] or r[u] == r[w] or b[u] != b[v]:
                continue
            bvw, rvw = b[v] == b[w], r[v] == r[w]
            if bvw != rvw:
                T[k] += 1 if bvw else -1
        cases += 1
        fails += any(c < 0 for c in T.values())
    return cases, fails


t0 = time.time()
pairs = list(itertools.combinations(range(4), 2))
for m in range(2, 8):
    c = f = 0
    for mult in itertools.product(range(m + 1), repeat=6):
        if sum(mult) == m:
            a, b = s_fails(4, [p for p, n in zip(pairs, mult) for _ in range(n)])
            c += a; f += b
    print('4 vertices, every multigraph with %d edges: triples %d, S fails %d (%ds)' % (m, c, f, time.time() - t0), flush=True)
for V in (5, 6):
    c = f = 0
    for g in nx.graph_atlas_g():
        if g.number_of_nodes() == V and g.number_of_edges() >= 1:
            a, b = s_fails(V, sorted(tuple(sorted(e)) for e in g.edges()))
            c += a; f += b
    print('%d vertices, every graph (atlas): triples %d, S fails %d (%ds)' % (V, c, f, time.time() - t0), flush=True)
