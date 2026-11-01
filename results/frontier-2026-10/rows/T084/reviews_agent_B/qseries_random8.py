# pointwise and second-partial-sum q-series test on random connected graphs with 8 vertices and 10-15 edges (all edge pairs)
import sys, json, random, networkx as nx
sys.argv = ['x', '99', '99']
exec(open('qseries_atlas.py', encoding='utf-8').read().split('tot = {')[0])
random.seed(20261018); tot = {'graphs': 0, 'pairs': 0, 'nonzero': 0, 'bad': 0, 'first_partial_fail': 0}
while tot['graphs'] < 60:
    m = random.randint(10, 15); G = nx.gnm_random_graph(8, m, seed=random.randrange(10**9))
    if not nx.is_connected(G): continue
    tot['graphs'] += 1
    for e, f, adj, nz, bad, rn, q2, qh, p1f, nc in check(8, list(G.edges())):
        tot['pairs'] += 1; tot['nonzero'] += nz; tot['bad'] += bool(bad); tot['first_partial_fail'] += p1f
        if bad or p1f: print('FAIL', list(G.edges()), e, f, flush=True)
    print(json.dumps(tot), flush=True)
