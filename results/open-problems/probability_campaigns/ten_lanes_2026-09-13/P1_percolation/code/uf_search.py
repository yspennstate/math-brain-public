r"""Search for a counterexample to Grimmett's uniform-forest conjecture on graphs beyond
the Grimmett-Winkler (2004) verified range (8 vertices, or 9 vertices with <=18 edges).
Exact integer arithmetic: the test is  N(G) * N(G/e/f) <= N(G/e) * N(G/f)."""
import random, sys, time
from forests import forest_count, contract_id

def cov_num(verts, edges, i, j):
    ids=list(range(len(edges)))
    NG=forest_count(verts,edges)
    v1,e1,i1=contract_id(verts,edges,ids,i); NGe=forest_count(v1,e1)
    v2,e2,i2=contract_id(verts,edges,ids,j); NGf=forest_count(v2,e2)
    if j in i1:
        v3,e3,_=contract_id(v1,e1,i1,j); NGef=forest_count(v3,e3)
    else:
        NGef=0                      # f became a loop after contracting e
    return NG*NGef-NGe*NGf,(NG,NGe,NGf,NGef)

def rand_graph(rng, n, dens):
    E=[(u,v) for u in range(n) for v in range(u+1,n) if rng.random()<dens]
    return list(range(n)), E

def connected(verts, edges):
    idx={v:i for i,v in enumerate(verts)}; par=list(range(len(verts)))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for (a,b) in edges:
        ra,rb=find(idx[a]),find(idx[b])
        if ra!=rb: par[ra]=rb
    return len({find(i) for i in range(len(verts))})==1

def run(ngraphs, ns, denss, pairs, seed, tmax):
    rng=random.Random(seed); t0=time.time()
    worst=None; tested=0; hits=0; graphs=0; mseen=[]
    while graphs<ngraphs and time.time()-t0<tmax:
        n=rng.choice(ns); d=rng.choice(denss)
        verts,edges=rand_graph(rng,n,d)
        if len(edges)<n-1 or not connected(verts,edges): continue
        graphs+=1; m=len(edges); mseen.append(m)
        for _ in range(min(pairs, m*(m-1)//2)):
            i,j=sorted(rng.sample(range(m),2))
            val,info=cov_num(verts,edges,i,j); tested+=1
            if val>0:
                hits+=1
                print("COUNTEREXAMPLE n=%d m=%d edges=%s pair=(%d,%d) counts=%s"%(n,m,edges,i,j,info))
            if worst is None or val>worst[0]: worst=(val,n,m)
    print("graphs %d  edge pairs %d  time %.1fs  counterexamples %d"%(graphs,tested,time.time()-t0,hits))
    print("edge counts seen: min %d max %d"%(min(mseen),max(mseen)))
    print("largest value of N(G)N(G/ef) - N(G/e)N(G/f):", worst[0] if worst else None)

if __name__=="__main__":
    print("harness control, path P3 (two bridges):", cov_num([0,1,2],[(0,1),(1,2)],0,1), "(expect value 0)")
    print("harness control, 3 parallel edges     :", cov_num([0,1],[(0,1),(0,1),(0,1)],0,1), "(expect value < 0)")
    print("harness control, K4 pair              :", cov_num(list(range(4)),[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],0,5), "(expect value < 0)")
    run(ngraphs=int(sys.argv[1]) if len(sys.argv)>1 else 300,
        ns=(9,10), denss=(0.25,0.4,0.55,0.7,0.85), pairs=3, seed=1,
        tmax=float(sys.argv[2]) if len(sys.argv)>2 else 1e18)
