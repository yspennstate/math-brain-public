"""Independent exact check of the two corollaries proved in the C0091 memo.

Cor 1 (parallel pair).  If e,f join the same pair of vertices then Cov(w_e,w_f)<0
for every 0<q<1, every host graph and every edge weights.
Cor 2 (series pair).  If e={a,v}, f={v,b} and v is incident to no other edge of G
then Cov(w_e,w_f)<0 under the same hypotheses.
Cor 0 (bridge).  If e is a bridge of G then w_e is independent of everything.

Checked here by exact rational brute force on randomly generated multigraphs.
"""
import random, sys
from fractions import Fraction as Fr

def comps_multi(n, edges, mask):
    par=list(range(n))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    c=n
    for i,(u,v) in enumerate(edges):
        if mask>>i&1:
            a,b=find(u),find(v)
            if a!=b: par[a]=b; c-=1
    return c

def cov_exact(n, edges, w, q, i, j):
    m=len(edges); Z=Fr(0); Ni=Fr(0); Nj=Fr(0); Nij=Fr(0)
    for mask in range(1<<m):
        k=comps_multi(n,edges,mask)
        t=q**k
        for b in range(m):
            t *= w[b] if (mask>>b&1) else (1-w[b])
        Z+=t
        if mask>>i&1:
            Ni+=t
            if mask>>j&1: Nij+=t
        if mask>>j&1: Nj+=t
    return Nij*Z-Ni*Nj      # sign of the covariance

def rand_case(rng, kind):
    n=rng.randint(3,6)
    base=[]
    for u in range(n):
        for v in range(u+1,n):
            if rng.random()<0.55: base.append((u,v))
    if kind=="parallel":
        if not base: return None
        (u,v)=rng.choice(base)
        edges=[(u,v),(u,v)]+base
        i,j=0,1
    elif kind=="series":
        # add a fresh degree-2 vertex v joined to a and b
        a,b = rng.sample(range(n),2)
        vnew=n; n=n+1
        edges=[(a,vnew),(vnew,b)]+base
        i,j=0,1
    else:  # bridge
        a=rng.randrange(n); vnew=n; n=n+1
        edges=[(a,vnew)]+base
        i,j=0,1 if len(base) else None
        if j is None: return None
    if len(edges)>13: return None
    return n,edges,i,j

def main(trials=60, seed=5):
    rng=random.Random(seed)
    qs=[Fr(1,10),Fr(1,3),Fr(3,4),Fr(9,10)]
    for kind in ("parallel","series","bridge"):
        bad=0; done=0; mx=None
        for _ in range(trials):
            c=rand_case(rng,kind)
            if c is None: continue
            n,edges,i,j=c; m=len(edges)
            w=[Fr(rng.randint(1,9),10) for _ in range(m)]
            for q in qs:
                s=cov_exact(n,edges,w,q,i,j)
                done+=1
                if kind=="bridge":
                    if s!=0: bad+=1; print("  BRIDGE NOT INDEPENDENT", n,edges,w,q,s)
                else:
                    same_block = None
                    if s>0:
                        bad+=1; print("  SIGN FAILURE",kind,n,edges,w,q,s)
                    if mx is None or s>mx: mx=s
        print("%-9s cases %4d  failures %d  (largest covariance numerator seen: %s)"
              %(kind,done,bad, "n/a" if mx is None else float(mx)))

if __name__=="__main__":
    main(int(sys.argv[1]) if len(sys.argv)>1 else 60)
