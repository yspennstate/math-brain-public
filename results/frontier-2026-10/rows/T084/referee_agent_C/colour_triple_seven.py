"""Statement S on every graph on 7 vertices with at most 11 edges (networkx atlas), every ordered triple.
python colour_triple_seven.py"""
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
c = f = n = 0
for g in nx.graph_atlas_g():
    if g.number_of_nodes() == 7 and 1 <= g.number_of_edges() <= 11:
        a, b = s_fails(7, sorted(tuple(sorted(e)) for e in g.edges()))
        c += a; f += b; n += 1
        if n % 200 == 0:
            print('graphs %d triples %d fails %d (%ds)' % (n, c, f, time.time() - t0), flush=True)
print('7 vertices, every graph with 1 to 11 edges (%d graphs): triples %d, S fails %d (%ds)' % (n, c, f, time.time() - t0), flush=True)
