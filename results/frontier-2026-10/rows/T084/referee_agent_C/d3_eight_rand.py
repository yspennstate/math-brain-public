"""D3 on random graphs on 8 vertices (12..20 edges, seed given), every edge pair, via fastN."""
import sys, random, itertools, time, fastN, d3
seed=int(sys.argv[1]); T=int(sys.argv[2]); rnd=random.Random(seed)
allE=list(itertools.combinations(range(8),2)); cnt=bad=0; t0=time.time()
for t in range(T):
    E=sorted(rnd.sample(allE,rnd.randint(12,20)))
    for (e,f),N in fastN.all_N(8,E).items():
        if not N: continue
        cnt+=1
        if d3.series_ok_dict(N)[0]: bad+=1; print('FAIL',E,e,f,flush=True)
    print('graph',t+1,'of',T,'edges',len(E),'pairs so far',cnt,'failures',bad,'t',round(time.time()-t0),flush=True)
print('all',T,'random graphs on 8 vertices (seed %d, 12..20 edges): pairs with N != 0:'%seed,cnt,'failures',bad,flush=True)
