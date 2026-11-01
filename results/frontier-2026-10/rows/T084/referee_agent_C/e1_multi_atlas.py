"""Multivariate E1 for ADJACENT pairs on every graph of the networkx atlas with V vertices and at most M edges.
python e1_multi_atlas.py V M"""
import sys, itertools, time
import networkx as nx
from e1_multi import neg_rows

V, M = int(sys.argv[1]), int(sys.argv[2])
gs = [g for g in nx.graph_atlas_g() if g.number_of_nodes() == V and 2 <= g.number_of_edges() <= M]
pairs = bad = 0
t0 = time.time()
for g in gs:
    E = sorted(tuple(sorted(x)) for x in g.edges())
    for e, f in itertools.permutations(E, 2):
        if not set(e) & set(f):
            continue
        pairs += 1
        if neg_rows(V, E, e, f)[0]:
            bad += 1
            if bad <= 5:
                print('FAIL', E, e, f, flush=True)
print('every graph on %d vertices with 2..%d edges (%d graphs): ordered adjacent pairs %d, multivariate E1 failures %d, %ds'
      % (V, M, len(gs), pairs, bad, time.time() - t0), flush=True)
