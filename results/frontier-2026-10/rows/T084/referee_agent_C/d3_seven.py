"""D3 on every graph on 7 vertices (<=13 edges) up to isomorphism (networkx atlas), every edge pair."""
import itertools
import networkx as nx
import brute, d3
gs=[g for g in nx.graph_atlas_g() if g.number_of_nodes()==7 and g.number_of_edges()<=13]
cnt=bad=0
for gi,g in enumerate(gs):
    E=sorted(tuple(sorted(e)) for e in g.edges())
    for e,f in itertools.combinations(E,2):
        N=brute.N_of(7,E,e,f)
        if not N: continue
        cnt+=1
        if d3.series_ok_dict(N)[0]: bad+=1; print('FAIL',E,e,f,flush=True)
    if gi%100==0: print('graph',gi,'of',len(gs),'pairs so far',cnt,'failures',bad,flush=True)
print('all',len(gs),'graphs on 7 vertices with <=13 edges (iso classes): pairs with N != 0:',cnt,'failures',bad,flush=True)
