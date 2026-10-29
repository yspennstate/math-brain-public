"""D3 on every graph on 6 vertices up to isomorphism (networkx atlas), every edge pair."""
import itertools
import networkx as nx
import brute, d3
gs=[g for g in nx.graph_atlas_g() if g.number_of_nodes()==6]
cnt=bad=0
for gi,g in enumerate(gs):
    E=sorted(tuple(sorted(e)) for e in g.edges())
    for e,f in itertools.combinations(E,2):
        N=brute.N_of(6,E,e,f)
        if not N: continue
        cnt+=1
        if d3.series_ok_dict(N)[0]: bad+=1; print('FAIL',E,e,f,flush=True)
    if gi%20==0: print('graph',gi,'of',len(gs),'pairs so far',cnt,'failures',bad,flush=True)
print('all',len(gs),'graphs on 6 vertices (iso classes): pairs with N != 0:',cnt,'failures',bad,flush=True)
