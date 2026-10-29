"""E1 on every graph on 7 vertices up to isomorphism (networkx atlas), every edge pair, via fastN. python e1_seven.py"""
import time, networkx as nx, fastN
from e1_check import e1_neg
gs = [g for g in nx.graph_atlas_g() if g.number_of_nodes() == 7 and g.number_of_edges() >= 2]
cnt = bad = 0; t0 = time.time()
for gi, g in enumerate(gs):
    E = sorted(tuple(sorted(e)) for e in g.edges())
    for (e, f), N in fastN.all_N(7, E).items():
        if not N:
            continue
        cnt += 1
        b = e1_neg(N)
        if b:
            bad += 1
            if bad <= 5:
                print('FAIL', E, e, f, b[:3], flush=True)
    if gi % 100 == 0:
        print('graph', gi, 'of', len(gs), 'pairs', cnt, 'failures', bad, 't', round(time.time() - t0), flush=True)
print('all %d graphs on 7 vertices with >= 2 edges: pairs with N != 0: %d, E1 failures %d, %ds'
      % (len(gs), cnt, bad, time.time() - t0), flush=True)
