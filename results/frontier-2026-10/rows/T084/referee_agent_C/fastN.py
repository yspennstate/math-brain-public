"""All-pairs N = Z_e Z_f - Z Z_ef on one graph at once: component counts of every edge subset by a DP over edges
(numpy), then for each (|A|, k(A)) bin the Gram matrix X^T X of the subset-edge indicators gives Z_ef for every pair."""
import numpy as np
from collections import defaultdict
from math import comb
def bins(n,E):
    m=len(E); M=1<<m
    lab=np.zeros((M,n),np.int8); lab[0]=np.arange(n)
    k=np.zeros(M,np.int8); k[0]=n
    for i,(a,b) in enumerate(E):
        lo,hi=1<<i,1<<(i+1)
        L=lab[:lo].copy(); la=L[:,a].copy(); lb=L[:,b].copy()
        L=np.where(L==lb[:,None],la[:,None],L)
        lab[lo:hi]=L; k[lo:hi]=k[:lo]-(la!=lb)
    del lab
    masks=np.arange(M,dtype=np.int64)
    X=((masks[:,None]>>np.arange(m))&1).astype(np.float32)
    s=X.sum(1).astype(np.int64)
    key=s*(n+1)+k.astype(np.int64)
    order=np.argsort(key,kind='stable'); key=key[order]
    cuts=np.flatnonzero(np.diff(key))+1; starts=np.r_[0,cuts]; ends=np.r_[cuts,M]
    G={}
    for st,en in zip(starts,ends):
        Xb=X[order[st:en]]; kk=int(key[st]); sv,kv=divmod(kk,n+1)
        G[(sv,kv)]=(en-st, Xb.sum(0).astype(np.float64), (Xb.T@Xb).astype(np.float64))
    return G
def to_u(d):
    r=defaultdict(int)
    for (s,k),c in d.items():
        for j in range(k+1): r[(s,j)]+=c*comb(k,j)*(-1)**j
    return r
def mul(a,b):
    r=defaultdict(int)
    for (i,j),c in a.items():
        for (k,l),d in b.items(): r[(i+k,j+l)]+=c*d
    return r
def all_N(n,E):
    G=bins(n,E); m=len(E)
    Z=to_u({b:v[0] for b,v in G.items()})
    Ze=[to_u({b:int(round(v[1][i])) for b,v in G.items() if v[1][i]}) for i in range(m)]
    out={}
    for i in range(m):
        for j in range(i+1,m):
            Zef=to_u({b:int(round(v[2][i,j])) for b,v in G.items() if v[2][i,j]})
            a=mul(Ze[i],Ze[j]); bb=mul(Z,Zef)
            r={kk:a.get(kk,0)-bb.get(kk,0) for kk in set(a)|set(bb)}
            out[(E[i],E[j])]={kk:v for kk,v in r.items() if v}
    return out
