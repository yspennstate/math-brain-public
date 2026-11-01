#!/usr/bin/env python3
"""Exact finite audit for FOREST three-terminal response polarizations.
Finite regression evidence only; not a proof for all graphs.
"""
import numpy as np
from itertools import combinations

def forest_zeta(n):
    edges=list(combinations(range(n),2)); m=len(edges); N=1<<m
    arr=np.zeros((5,N),dtype=np.int32)
    parent=list(range(n)); size=[1]*n
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    def dfs(i,mask):
        if i==m:
            r=[find(k) for k in range(3)]
            idx=4 if r[0]==r[1]==r[2] else 1 if r[0]==r[1] else 2 if r[0]==r[2] else 3 if r[1]==r[2] else 0
            arr[idx,mask]=1; return
        dfs(i+1,mask)
        u,v=edges[i]; ru,rv=find(u),find(v)
        if ru!=rv:
            if size[ru]<size[rv]: ru,rv=rv,ru
            old=size[ru]; parent[rv]=ru; size[ru]+=size[rv]
            dfs(i+1,mask|(1<<i)); parent[rv]=rv; size[ru]=old
    dfs(0,0)
    for bit in range(m):
        step=1<<bit; view=arr.reshape(5,-1,2*step); view[:,:,step:]+=view[:,:,:step]
    return edges,arr.astype(np.int64,copy=False)

def edges_from_mask(edges,mask): return [edges[i] for i in range(len(edges)) if (mask>>i)&1]

total_graphs=total_splits=negative_s2=0
smallest=None; worst=(0.0,None)
for n in range(3,8):
    edges,A=forest_zeta(n); m=len(edges); N=1<<m; total_graphs+=N
    d,a,b,c,t=A; Tau=d*t-(a*b+a*c+b*c); Sig=a*b*c-Tau*t
    assert np.all(Tau>=0); assert np.all(Sig>=0)
    idx=np.arange(N,dtype=np.int64)
    for bit in range(m):
        bm=1<<bit; sel=idx[(idx&bm)!=0]; total_splits+=len(sel)
        v=A[:,sel]; v0=A[:,sel-bm]; v1=v-v0
        d0,a0,b0,c0,t0=v0; d1,a1,b1,c1,t1=v1
        P=(d0*t1+d1*t0-(a0*b1+a1*b0+a0*c1+a1*c0+b0*c1+b1*c0))
        assert np.all(P>=0)
        S1=(a0*b0*c1+a0*b0*t1+a0*b1*c0+a0*b1*t0+a0*c0*t1+a0*c1*t0+a1*b0*c0+a1*b0*t0+a1*c0*t0+b0*c0*t1+b0*c1*t0+b1*c0*t0-2*d0*t0*t1-d1*t0*t0)
        S2=(a0*b1*c1+a0*b1*t1+a0*c1*t1+a1*b0*c1+a1*b0*t1+a1*b1*c0+a1*b1*t0+a1*c0*t1+a1*c1*t0+b0*c1*t1+b1*c0*t1+b1*c1*t0-d0*t1*t1-2*d1*t0*t1)
        S3=a1*b1*c1-(d1*t1-(a1*b1+a1*c1+b1*c1))*t1
        assert np.all(S1>=0)
        neg=S2<0; negative_s2+=int(neg.sum()); bad=neg & ((S3<=0)|(S2*S2>3*S1*S3)); assert not np.any(bad)
        if np.any(neg):
            for j in np.where(neg)[0]:
                mask=int(sel[j]); rec=(n,mask.bit_count(),mask,bit,int(S2[j]),int(S1[j]),int(S3[j]),tuple(map(int,v0[:,j])),tuple(map(int,v1[:,j])))
                if smallest is None or rec[:4]<smallest[:4]: smallest=rec
            good=neg&(S1>0)&(S3>0)
            if np.any(good):
                ratios=(S2[good].astype(float)**2)/(3*S1[good].astype(float)*S3[good].astype(float)); k=int(np.argmax(ratios)); gv=np.where(good)[0][k]
                if float(ratios[k])>worst[0]: worst=(float(ratios[k]),(n,int(sel[gv]),bit,int(S1[gv]),int(S2[gv]),int(S3[gv])))
    print(f"n={n}: graphs={N}, edge_splits={m*(1<<(m-1))}, tau>=0 PASS, sigma>=0 PASS")
print(f"TOTAL_GRAPHS={total_graphs}"); print(f"TOTAL_EDGE_SPLITS={total_splits}"); print(f"NEGATIVE_S2_INSTANCES={negative_s2}")
print("P_TAU_NONNEGATIVE=PASS"); print("SIGMA_DERIVATIVE_NONNEGATIVE_FOR_W_GE_0=PASS")
n,ecount,mask,bit,s2,s1,s3,v0,v1=smallest; edges=list(combinations(range(n),2))
print("SMALLEST_NEGATIVE_S2_WITNESS:"); print(f"  n={n}, edge_count={ecount}, graph_edges={edges_from_mask(edges,mask)}, g={edges[bit]}"); print(f"  v0={v0}, v1={v1}, s1={s1}, s2={s2}, s3={s3}")
d0,a0,b0,c0,t0=v0; d1,a1,b1,c1,t1=v1
T0=d0*t0-(a0*b0+a0*c0+b0*c0); T1=d1*t1-(a1*b1+a1*c1+b1*c1); P=d0*t1+d1*t0-(a0*b1+a1*b0+a0*c1+a1*c0+b0*c1+b1*c0); Sig0=a0*b0*c0-T0*t0
print(f"  tau(w)={T0}+{P}*w+{T1}*w^2"); print(f"  sigma(w)={Sig0}+{s1}*w+({s2})*w^2+{s3}*w^3")
print(f"WORST_NEGATIVE_S2_DERIVATIVE_RATIO={worst[0]:.12f}"); print("STATUS=PASS")
