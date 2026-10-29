import numpy as np
from t2b1_adaptive import *
s, eps = 1.0, 0.5
for N in (401, 801):
    gs = np.linspace(-10, 12, N)
    dc = conj_delta(s, eps, gs)
    # conjectured strategy, mirrored sign: a=(-1,-1), v=(1,1)  and a=(1,1), v=(-1,-1)
    d1, _ = adaptive_delta(s, eps, gs, 1.0, -1.0, np.array([1.0, -1.0])[:1] if False else np.array([1.0]), False)
    # need a2=1, v2=-1 fixed: build custom
    g2 = np.array([1.0]); 
    def fixed(a1, v1, a2, v2, rev):
        dg = gs[1]-gs[0]; e=np.exp(eps); tot=0
        fv=phi(gs-v2,s); fa=phi(gs-a2,s); f0=phi(gs,s)
        for x1 in gs:
            wa=.5*phi(x1-a1,s); w0=.5*phi(x1,s); wc=.5*phi(x1-v1,s)
            p=wa*fv+wc*fa; q=w0*fv+wc*f0
            tot+=(np.maximum(q-e*p,0) if rev else np.maximum(p-e*q,0)).sum()*dg*dg
        return tot
    print(N, "conj2D", dc, "fixed(1,-1,1,-1)", fixed(1,-1,1,-1,False), fixed(1,-1,1,-1,True), "fixed(-1,1,-1,1)", fixed(-1,1,-1,1,False))
    grid2 = np.linspace(-1,1,9)
    d, best = adaptive_delta(s, eps, gs, -1.0, 1.0, grid2, False)
    A2, V2 = np.meshgrid(grid2, grid2, indexing="ij"); A2=A2.ravel(); V2=V2.ravel()
    print(N, "adaptive at a1=-1,v1=1:", d)
    prev=None
    for x1, k in zip(gs, best):
        c=(A2[k],V2[k])
        if c!=prev and -6<x1<6: print("   g1>=%.3f  a2=%.2f v2=%.2f"%(x1,c[0],c[1])); prev=c
