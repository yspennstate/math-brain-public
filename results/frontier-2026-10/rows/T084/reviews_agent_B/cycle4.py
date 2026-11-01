# T084, agent B: the two moves (e to the empty copy, or f) make the +/- pair graph a union of 4-cycles
# {-(a, b+ef), +(a+e, b+f), -(b, a+ef), +(b+e, a+f)} over unordered base pairs {a, b}. Pointwise positivity would follow
# from each cycle: min(plus) <= min(minus) and max(plus) <= max(minus) (sums: plus <= minus by submodularity of rank).
import numpy as np, networkx as nx, itertools, json, sys
exec(open('qseries_atlas.py', encoding='utf-8').read().split('def check')[0].split('nmin, nmax')[0])
exec('def comps_all' + open('qseries_atlas.py', encoding='utf-8').read().split('def comps_all')[1].split('def check')[0])
tot = dict(graphs=0, cycles=0, minfail=0, maxfail=0, either=0); ex = []
for G in nx.graph_atlas_g():
    n, m = G.number_of_nodes(), G.number_of_edges()
    if n < 3 or m < 2 or m > 9 or not nx.is_connected(G): continue
    edges = list(G.edges()); k = comps_all(n, edges); tot['graphs'] += 1
    for e, f in itertools.combinations(range(m), 2):
        others = [i for i in range(m) if i not in (e, f)]
        subs = [sum(1 << others[i] for i in range(len(others)) if (x >> i) & 1) for x in range(1 << len(others))]
        E, Fb = 1 << e, 1 << f
        for i, a in enumerate(subs):
            for b in subs[i:]:
                mn = (k[a] + k[b | E | Fb], k[b] + k[a | E | Fb]); pl = (k[a | E] + k[b | Fb], k[b | E] + k[a | Fb])
                f1, f2 = min(pl) > min(mn), max(pl) > max(mn)
                tot['cycles'] += 1; tot['minfail'] += f1; tot['maxfail'] += f2; tot['either'] += f1 or f2
                if (f1 or f2) and len(ex) < 5: ex.append((edges, edges[e], edges[f], a, b, mn, pl))
print(json.dumps({x: int(y) for x, y in tot.items()})); [print(x) for x in ex]
