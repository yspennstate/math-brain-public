#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
import heapq, math
import numpy as np

THRESHOLD = 0.6005646

def band_graph(L,W):
    verts=[]
    for s in range(2*L+1):
        for d in range(-W,W+1):
            if (s-d)%2==0:
                verts.append((s,d))
    idx={v:i for i,v in enumerate(verts)}
    adj=[[] for _ in verts]
    edges=[]
    for i,(s,d) in enumerate(verts):
        if s<2*L:
            for dd in (d-1,d+1):
                v=(s+1,dd)
                if v in idx:
                    j=idx[v]
                    e=len(edges)
                    edges.append((i,j))
                    adj[i].append((j,e))
                    adj[j].append((i,e))
    left=[idx[v] for v in verts if v[0]==0]
    right=[idx[v] for v in verts if v[0]==2*L]
    ds=[verts[i][1] for i in left]
    return verts,adj,edges,left,right,ds

def exact_q_l1(W):
    L=1
    verts,adj,edges,left,right,ds=band_graph(L,W)
    targets=set(right)
    nonterms=[i for i in range(len(verts)) if i not in targets]
    pos={v:j for j,v in enumerate(nonterms)}
    @lru_cache(None)
    def u(mask):
        rate=0
        trans={}
        for a,b in edges:
            ia=(a in pos) and ((mask>>pos[a])&1)
            ib=(b in pos) and ((mask>>pos[b])&1)
            if ia and b in targets:
                rate += 1
            elif ib and a in targets:
                rate += 1
            elif ia and b in pos and not ib:
                rate += 1
                nm=mask | (1<<pos[b])
                trans[nm]=trans.get(nm,0)+1
            elif ib and a in pos and not ia:
                rate += 1
                nm=mask | (1<<pos[a])
                trans[nm]=trans.get(nm,0)+1
        assert rate>0
        ans=Fraction(1,rate)
        for nm,mult in trans.items():
            ans += Fraction(mult,rate)*u(nm)
        return ans
    source=left[ds.index(0)]
    q=u(1<<pos[source])
    return q,u.cache_info().currsize,len(verts),len(edges)

EXPECTED = {
    1: Fraction(5,4),
    2: Fraction(11,12),
    3: Fraction(37643,41472),
    4: Fraction(95513,105840),
    5: Fraction(39916137923,44236800000),
    6: Fraction(213930628381,237105792000),
}

print("EXACT_RICHARDSON_BLOCK_CHECK")
for W in range(1,7):
    q,states,nv,ne=exact_q_l1(W)
    assert q == EXPECTED[W]
    assert states == (W+1)**2
    print(f"W={W} q={q} float={float(q):.15f} reachable_states={states} V={nv} E={ne}")
print("EXACT_SMALL_BLOCKS_PASS = True")

def apply_band(y,L,W,rng,directed=False):
    verts,adj,edges,left,right,ds=band_graph(L,W)
    weights=rng.exponential(size=len(edges))
    dist=np.full(len(verts),np.inf)
    hp=[]
    for val,i in zip(y,left):
        if np.isfinite(val):
            dist[i]=val
            heapq.heappush(hp,(float(val),i))
    while hp:
        du,u=heapq.heappop(hp)
        if du != dist[u]:
            continue
        su=verts[u][0]
        for v,e in adj[u]:
            if directed and verts[v][0] < su:
                continue
            nv=du+weights[e]
            if nv<dist[v]:
                dist[v]=nv
                heapq.heappush(hp,(float(nv),v))
    out=dist[right]
    g=float(out.min())
    return out-g,g

def replicate_screen(directed):
    L,W=1,40
    reps,burn,keep=40,100,400
    vals=[]
    for r in range(reps):
        rng=np.random.default_rng(90000+r)
        verts,adj,edges,left,right,ds=band_graph(L,W)
        y=np.full(len(left),np.inf)
        y[ds.index(0)]=0.0
        total=0.0
        for j in range(burn+keep):
            y,g=apply_band(y,L,W,rng,directed)
            if j>=burn:
                total += g
        vals.append(total/(keep*L))
    a=np.array(vals)
    mean=float(a.mean())
    se=float(a.std(ddof=1)/math.sqrt(reps))
    q05,q50,q95=map(float,np.quantile(a,[.05,.5,.95]))
    return mean,se,q05,q50,q95

print("NEGATION_FIRST_NUMERICAL_SCREEN_ONLY")
for directed in (False,True):
    mean,se,q05,q50,q95=replicate_screen(directed)
    print(f"directed={directed} mean={mean:.15f} independent_rep_SE={se:.15f} q05={q05:.15f} median={q50:.15f} q95={q95:.15f} threshold={THRESHOLD:.7f}")
print("NUMERICAL_SCREEN_IS_NOT_A_PROOF = True")
