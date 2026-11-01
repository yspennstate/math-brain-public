"""Maximise Cov(w_e,w_f) over all edge weights, with q = exp(u).
u<0 is the conjecture's regime (q<1); u>0 is the positive control (FKG => Cov>0)."""
import math, random, sys
from fk_lib import comps

def make_eval(n, edges, i, j):
    m=len(edges); N=1<<m
    kk=[comps(n,edges,x) for x in range(N)]
    def f(t, u):
        p=[1/(1+math.exp(-z)) for z in t]; q=math.exp(u)
        Z=Ni=Nj=Nij=0.0
        for x in range(N):
            w=q**kk[x]
            for b in range(m): w *= p[b] if (x>>b&1) else (1-p[b])
            Z+=w
            if x>>i&1:
                Ni+=w
                if x>>j&1: Nij+=w
            if x>>j&1: Nj+=w
        return Nij/Z - (Ni/Z)*(Nj/Z)
    return f, m

def hill(f, m, restarts=8, iters=300, seed=0, sign=-1, ulo=-12.0, uhi=-1e-6):
    rng=random.Random(seed); best=(-1e18,None)
    for _ in range(restarts):
        t=[rng.uniform(-3,3) for _ in range(m)]
        u=rng.uniform(max(ulo,-6), uhi if uhi<0 else 3.0)
        cur=f(t,u); step=1.0
        for it in range(iters):
            imp=False
            for idx in range(m+1):
                for d in (step,-step):
                    if idx<m:
                        t[idx]+=d; v=f(t,u)
                        if v>cur: cur=v; imp=True
                        else: t[idx]-=d
                    else:
                        nu=u+d
                        if nu<ulo or nu>uhi: continue
                        u=nu; v=f(t,u)
                        if v>cur: cur=v; imp=True
                        else: u-=d
            if not imp:
                step*=0.5
                if step<1e-5: break
        if cur>best[0]: best=(cur,(list(t),u))
    return best
