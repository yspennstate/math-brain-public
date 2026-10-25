"""Maximise Cov(w_e,w_f) over ALL edge weights and q in (0,1) for a fixed graph.

Parameterisation: p_g = sigmoid(t_g), q = sigmoid(u).  Plain hill-climbing with
random restarts (no scipy dependency at import time).  Any positive value found
is re-checked with exact rational arithmetic before it is believed.
"""
import math, random, sys
from fk_lib import comps

def make_eval(n, edges, i, j):
    m=len(edges)
    N=1<<m
    pc=[bin(x).count("1") for x in range(N)]
    kk=[comps(n,edges,x) for x in range(N)]
    def f(t, u):
        p=[1/(1+math.exp(-z)) for z in t]
        q=1/(1+math.exp(-u))
        Z=0.0; Ni=0.0; Nj=0.0; Nij=0.0
        for x in range(N):
            w=q**kk[x]
            for b in range(m):
                w *= p[b] if (x>>b&1) else (1-p[b])
            Z+=w
            if x>>i&1:
                Ni+=w
                if x>>j&1: Nij+=w
            if x>>j&1: Nj+=w
        return Nij/Z - (Ni/Z)*(Nj/Z)
    return f, m

def hill(f, m, restarts=12, iters=400, seed=0):
    rng=random.Random(seed)
    best=(-1e18,None)
    for _ in range(restarts):
        t=[rng.uniform(-3,3) for _ in range(m)]; u=rng.uniform(-6,1.0)
        cur=f(t,u); step=1.0
        for it in range(iters):
            improved=False
            for idx in range(m+1):
                for d in (step,-step):
                    if idx<m:
                        t[idx]+=d; v=f(t,u)
                        if v>cur: cur=v; improved=True
                        else: t[idx]-=d
                    else:
                        if u+d>=0: continue   # keep q<1/2? no: keep q<1 -> u<0
                        u+=d; v=f(t,u)
                        if v>cur: cur=v; improved=True
                        else: u-=d
            if not improved:
                step*=0.5
                if step<1e-4: break
        if cur>best[0]: best=(cur,(list(t),u))
    return best

if __name__=="__main__":
    # theory-guided candidate: two marked pairs joined through a shared edge
    # H = a-u, u-v, v-b, c-u, v-d ;  e = (a,b), f = (c,d)
    a,b,c,d,u,v = 0,1,2,3,4,5
    edges=[(a,u),(u,v),(v,b),(c,u),(v,d),(a,b),(c,d)]
    ie, jf = 5, 6
    f,m=make_eval(6,edges,ie,jf)
    print("shared-edge gadget:", hill(f,m,restarts=20,seed=1)[0])
