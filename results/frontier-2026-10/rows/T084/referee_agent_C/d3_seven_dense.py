"""D3 on every graph on 7 vertices with 14..21 edges up to isomorphism (networkx atlas), every edge pair, via fastN."""
import sys, time, networkx as nx, fastN, d3
lo=int(sys.argv[1]) if len(sys.argv)>1 else 14
gs=[g for g in nx.graph_atlas_g() if g.number_of_nodes()==7 and g.number_of_edges()>=lo]
cnt=bad=0; t0=time.time()
for gi,g in enumerate(gs):
    E=sorted(tuple(sorted(e)) for e in g.edges())
    for (e,f),N in fastN.all_N(7,E).items():
        if not N: continue
        cnt+=1
        if d3.series_ok_dict(N)[0]: bad+=1; print('FAIL',E,e,f,flush=True)
    print('graph',gi+1,'of',len(gs),'edges',len(E),'pairs so far',cnt,'failures',bad,'t',round(time.time()-t0),flush=True)
print('all',len(gs),'graphs on 7 vertices with >=%d edges (iso classes): pairs with N != 0:'%lo,cnt,'failures',bad,flush=True)
