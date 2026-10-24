#!/usr/bin/env python3
"""PROB20-11 targeted exact K=5 coarse reproducer for sorted slack pair (0,3).

Enumerates all 26 unlabeled five-edge close-graph shapes, all active parity
assignments, all parity-compatible close distances, and all total parity counts;
canonicalizes by graph automorphisms plus global parity exchange. Exact integer
arithmetic. Requires networkx. This targeted run is complete; timeout is not used.
"""
from itertools import combinations, product, permutations
from collections import defaultdict
from math import comb
import networkx as nx, time
N=2048

def fd(a,b):
    w=(a^b).bit_count(); return min(w,12-w)
def par(x): return x.bit_count()&1
B0=[x for x in range(N) if fd(0,x)<=3]
balls=[]
for c in range(N):
    m=0
    for b in B0:m|=1<<(c^b)
    balls.append(m)
EVEN=sum(1<<x for x in range(N) if par(x)==0); ALL=(1<<N)-1; ODD=ALL^EVEN

def halves(m):return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def pairh(a,b):return halves(balls[a]&balls[b])
def trih(a,b,c):return halves(balls[a]&balls[b]&balls[c])
trimax={}
for b in range(1,N):
    bb=balls[0]&balls[b]
    for c in range(b+1,N):
        key=(0,par(b),par(c),fd(0,b),fd(0,c),fd(b,c));h=halves(bb&balls[c]);old=trimax.get(key,(-1,-1));trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key;trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])
def tmax(p0,p1,p2,d01,d02,d12):
    ps=(p0,p1,p2); D=((0,d01,d02),(d01,0,d12),(d02,d12,0))
    for q in permutations(range(3)):
        k=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if k in trimax:return trimax[k]
    return None
pairB={(0,0):(0,40),(0,1):(10,10),(1,0):(10,10),(1,1):(40,0)}
pairD={}
for p in (0,1):
    a=0 if p==0 else 1
    for q in (0,1):
        for d in ((2,4) if p==q else (1,3)):
            vals={pairh(a,b) for b in range(N) if b!=a and par(b)==q and fd(a,b)==d};assert len(vals)==1;pairD[(p,q,d)]=next(iter(vals))
baseTri={}
for ps in product((0,1),repeat=3):
    p0,p1,p2=ps;ds=(6 if p0==p1 else 5,6 if p0==p2 else 5,6 if p1==p2 else 5);baseTri[ps]=tmax(p0,p1,p2,*ds)

def coarse_U(nv,es,ap,ds,neven):
    nodd=12-neven
    S1=(67*neven+232*nodd,232*neven+67*nodd)
    S2=(comb(nodd,2)*40+neven*nodd*10,comb(neven,2)*40+neven*nodd*10)
    S3=(neven*comb(nodd,2)+4*comb(nodd,3),4*comb(neven,3)+comb(neven,2)*nodd)
    edge_d={tuple(sorted(e)):d for e,d in zip(es,ds)}
    dp=[0,0]
    for (i,j),d in zip(es,ds):
        b=pairB[(ap[i],ap[j])]; a=pairD[(ap[i],ap[j],d)];dp[0]+=a[0]-b[0];dp[1]+=a[1]-b[1]
    dt=[0,0]; E=set(edge_d)
    for i,j,k in combinations(range(nv),3):
        eij=tuple(sorted((i,j)));eik=tuple(sorted((i,k)));ejk=tuple(sorted((j,k)))
        if not ({eij,eik,ejk}&E):continue
        dij=edge_d.get(eij,6 if ap[i]==ap[j] else 5);dik=edge_d.get(eik,6 if ap[i]==ap[k] else 5);djk=edge_d.get(ejk,6 if ap[j]==ap[k] else 5)
        a=tmax(ap[i],ap[j],ap[k],dij,dik,djk)
        if a is None:return None
        b=baseTri[(ap[i],ap[j],ap[k])];dt[0]+=a[0]-b[0];dt[1]+=a[1]-b[1]
    isoE=neven-sum(p==0 for p in ap);isoO=(12-nv)-isoE
    if isoE<0 or isoO<0:return None
    for (i,j),d in zip(es,ds):
        for q,n in ((0,isoE),(1,isoO)):
            if not n:continue
            a=tmax(ap[i],ap[j],q,d,6 if ap[i]==q else 5,6 if ap[j]==q else 5)
            if a is None:return None
            b=baseTri[(ap[i],ap[j],q)];dt[0]+=n*(a[0]-b[0]);dt[1]+=n*(a[1]-b[1])
    return (S1[0]-(S2[0]+dp[0])+(S3[0]+dt[0]),S1[1]-(S2[1]+dp[1])+(S3[1]+dt[1]))

def autos(G):return [tuple(m[i] for i in range(G.number_of_nodes())) for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
def canon(st,nv,es,aa):
    ap,ds,ne,U=st;old={tuple(sorted(e)):d for e,d in zip(es,ds)};best=None
    for q in aa:
        ap2=tuple(ap[q[i]] for i in range(nv));ds2=tuple(old[tuple(sorted((q[i],q[j])))] for i,j in es)
        for f in (0,1):
            z=(tuple(1-p for p in ap2) if f else ap2,ds2,12-ne if f else ne)
            if best is None or z<best:best=z
    return best

atlas=nx.graph_atlas_g();comps=[]
for e in range(1,6):
    for idx,G in enumerate([H for H in atlas if H.number_of_edges()==e and H.number_of_nodes()>=2 and nx.is_connected(H)]):
        comps.append((e,f'e{e}_{idx}',nx.convert_node_labels_to_integers(G)))
shapes=[]
def rec(start,rem,chosen):
    if rem==0:
        G=nx.Graph();off=0;names=[]
        for ci in chosen:
            e,n,C=comps[ci];C2=nx.relabel_nodes(C,{v:v+off for v in C.nodes()});G=nx.compose(G,C2);off+=C.number_of_nodes();names.append(n)
        shapes.append(('+'.join(names),G));return
    for ci in range(start,len(comps)):
        e,n,C=comps[ci]
        if e<=rem:rec(ci,rem-e,chosen+[ci])
rec(0,5,[]);assert len(shapes)==26
alllow=[]
t0=time.time()
for si,(name,G) in enumerate(shapes):
    nv=G.number_of_nodes();es=sorted(tuple(sorted(e)) for e in G.edges()); raw=[]
    for ap in product((0,1),repeat=nv):
        opts=[((2,4) if ap[i]==ap[j] else (1,3)) for i,j in es]
        ae=sum(p==0 for p in ap);niso=12-nv
        for ds in product(*opts):
            for ne in range(ae,ae+niso+1):
                U=coarse_U(nv,es,ap,ds,ne)
                if U is not None and min(U)>=1024 and min(U)-1024==0:
                    raw.append((tuple(ap),tuple(ds),ne,U))
    aa=autos(G); cc={canon(s,nv,es,aa):s for s in raw}
    low=[]
    for key,st in cc.items():
        sl=tuple(sorted((st[3][0]-1024,st[3][1]-1024)))
        if sl==(0,3): low.append((sl,key,st))
    low.sort()
    if low:
        print("SHAPE",name,"nv",nv,"edges",es,"count",len(low),flush=True)
        for x in low:
            print(x,flush=True)
            alllow.append((name,es,x[0],x[1],x[2]))
print('TOTAL TARGET',len(alllow))
