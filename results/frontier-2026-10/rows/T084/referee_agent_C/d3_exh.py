"""D3 on every graph on 5 vertices (every edge pair) and on dense random graphs on 6-7 vertices."""
import itertools, random
import brute, d3
allE=list(itertools.combinations(range(5),2)); cnt=0; bad=0
for mask in range(1<<10):
    E=[allE[i] for i in range(10) if mask>>i&1]
    for e,f in itertools.combinations(E,2):
        N=brute.N_of(5,E,e,f)
        if not N: continue
        cnt+=1
        if d3.series_ok_dict(N)[0]:
            bad+=1; print('FAIL',E,e,f)
print('all graphs on 5 vertices: pairs with N != 0:',cnt,'failures',bad,flush=True)
rnd=random.Random(3); cnt=bad=0
for t in range(120):
    n=rnd.choice((6,7)); aE=list(itertools.combinations(range(n),2)); E=rnd.sample(aE,rnd.randint(11,15)); e,f=rnd.sample(E,2)
    N=brute.N_of(n,E,e,f)
    if not N: continue
    cnt+=1
    if d3.series_ok_dict(N)[0]: bad+=1; print('FAIL',n,E,e,f)
print('dense random graphs on 6-7 vertices (11-15 edges):',cnt,'failures',bad)
