#!/usr/bin/env python3
"""PROB20-11 exact K=5 coarse third-Bonferroni frontier.
Requires networkx. Exact integer arithmetic and exhaustive finite graph/state search.
Regresses all archived K=4 raw/canonical counts before reporting K=5.

STATUS NOTE: the combined monolithic run of this reproducer hit the local 120s
execution cap in the originating run. The archived K=5 counts were obtained by
completed exact chunked runs of the same formulas/state enumeration. Timeout is
not used as an infeasibility claim.
"""
from itertools import combinations, product, permutations
from collections import defaultdict
from math import comb
import networkx as nx

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
EVEN=0
for x in range(N):
    if par(x)==0:EVEN|=1<<x
ALL=(1<<N)-1; ODD=ALL^EVEN
def halves(m):return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def pairh(a,b):return halves(balls[a]&balls[b])
def trih(a,b,c):return halves(balls[a]&balls[b]&balls[c])

trimax={}
for b in range(1,N):
    for c in range(b+1,N):
        key=(0,par(b),par(c),fd(0,b),fd(0,c),fd(b,c))
        h=trih(0,b,c); old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])
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
            vals={pairh(a,b) for b in range(N) if b!=a and par(b)==q and fd(a,b)==d}
            assert len(vals)==1
            pairD[(p,q,d)]=next(iter(vals))
baseTri={}
for ps in product((0,1),repeat=3):
    p0,p1,p2=ps
    ds=(6 if p0==p1 else 5,6 if p0==p2 else 5,6 if p1==p2 else 5)
    baseTri[ps]=tmax(p0,p1,p2,*ds)
    assert baseTri[ps] is not None

def coarse_U(nv,es,ap,ds,neven):
    nodd=12-neven
    S1=(67*neven+232*nodd,232*neven+67*nodd)
    S2=(comb(nodd,2)*40+neven*nodd*10,comb(neven,2)*40+neven*nodd*10)
    S3=(neven*comb(nodd,2)+4*comb(nodd,3),4*comb(neven,3)+comb(neven,2)*nodd)
    edge_d={tuple(sorted(e)):d for e,d in zip(es,ds)}
    dp=[0,0]
    for (i,j),d in zip(es,ds):
        b=pairB[(ap[i],ap[j])]; a=pairD[(ap[i],ap[j],d)]
        dp[0]+=a[0]-b[0]; dp[1]+=a[1]-b[1]
    dt=[0,0]; E=set(edge_d)
    for i,j,k in combinations(range(nv),3):
        eij=tuple(sorted((i,j))); eik=tuple(sorted((i,k))); ejk=tuple(sorted((j,k)))
        if not ({eij,eik,ejk}&E):continue
        dij=edge_d.get(eij,6 if ap[i]==ap[j] else 5)
        dik=edge_d.get(eik,6 if ap[i]==ap[k] else 5)
        djk=edge_d.get(ejk,6 if ap[j]==ap[k] else 5)
        a=tmax(ap[i],ap[j],ap[k],dij,dik,djk)
        if a is None:return None
        b=baseTri[(ap[i],ap[j],ap[k])]
        dt[0]+=a[0]-b[0];dt[1]+=a[1]-b[1]
    isoE=neven-sum(p==0 for p in ap); isoO=(12-nv)-isoE
    if isoE<0 or isoO<0:return None
    for (i,j),d in zip(es,ds):
        for q,n in ((0,isoE),(1,isoO)):
            if not n:continue
            a=tmax(ap[i],ap[j],q,d,6 if ap[i]==q else 5,6 if ap[j]==q else 5)
            if a is None:return None
            b=baseTri[(ap[i],ap[j],q)]
            dt[0]+=n*(a[0]-b[0]);dt[1]+=n*(a[1]-b[1])
    return (S1[0]-(S2[0]+dp[0])+(S3[0]+dt[0]),S1[1]-(S2[1]+dp[1])+(S3[1]+dt[1]))

def enumerate_shape(nv,es):
    out=[]
    for ap in product((0,1),repeat=nv):
        opts=[((2,4) if ap[i]==ap[j] else (1,3)) for i,j in es]
        ae=sum(p==0 for p in ap); niso=12-nv
        for ds in product(*opts):
            for ne in range(ae,ae+niso+1):
                U=coarse_U(nv,es,ap,ds,ne)
                if U is not None and min(U)>=1024:out.append((tuple(ap),tuple(ds),ne,U))
    return out

def autos(G):
    return [tuple(m[i] for i in range(G.number_of_nodes())) for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
def canon(st,nv,es,aa):
    ap,ds,ne,U=st; old={tuple(sorted(e)):d for e,d in zip(es,ds)}; best=None
    for q in aa:
        ap2=tuple(ap[q[i]] for i in range(nv)); ds2=tuple(old[tuple(sorted((q[i],q[j])))] for i,j in es)
        for f in (0,1):
            z=(tuple(1-p for p in ap2) if f else ap2,ds2,12-ne if f else ne)
            if best is None or z<best:best=z
    return best

S4={
 'triangle_pendant':(4,[(0,1),(0,2),(1,2),(2,3)],(16,6)),
 'tree32111':(5,[(0,1),(0,2),(0,3),(3,4)],(6,2)),
 'star3_plus_edge':(6,[(0,1),(0,2),(0,3),(4,5)],(26,4)),
 'triangle_plus_edge':(5,[(0,1),(0,2),(1,2),(3,4)],(98,23)),
 'path5':(5,[(0,1),(1,2),(2,3),(3,4)],(8,2)),
 'path4_plus_edge':(6,[(0,1),(1,2),(2,3),(4,5)],(30,9)),
 'two_p3':(6,[(0,1),(1,2),(3,4),(4,5)],(18,3)),
 'p3_plus_2edges':(7,[(0,1),(1,2),(3,4),(5,6)],(76,14)),
 'matching4':(8,[(0,1),(2,3),(4,5),(6,7)],(208,11)),
 'star4':(5,[(0,1),(0,2),(0,3),(0,4)],(0,0)),
 'cycle4':(4,[(0,1),(1,2),(2,3),(3,0)],(0,0))}
for name,(nv,es,exp) in S4.items():
    rr=enumerate_shape(nv,es); G=nx.Graph();G.add_nodes_from(range(nv));G.add_edges_from(es); aa=autos(G)
    cc={canon(s,nv,es,aa) for s in rr}
    assert (len(rr),len(cc))==exp,(name,len(rr),len(cc),exp)

atlas=nx.graph_atlas_g(); comps=[]
for e in range(1,6):
    for idx,G in enumerate([H for H in atlas if H.number_of_edges()==e and H.number_of_nodes()>=2 and nx.is_connected(H)]):
        comps.append((e,f'e{e}_{idx}',nx.convert_node_labels_to_integers(G)))
shapes=[]
def rec(start,rem,chosen):
    if rem==0:
        G=nx.Graph();off=0;names=[]
        for ci in chosen:
            e,n,C=comps[ci]; C2=nx.relabel_nodes(C,{v:v+off for v in C.nodes()});G=nx.compose(G,C2);off+=C.number_of_nodes();names.append(n)
        shapes.append(('+'.join(names),G));return
    for ci in range(start,len(comps)):
        e,n,C=comps[ci]
        if e<=rem:rec(ci,rem-e,chosen+[ci])
rec(0,5,[])
assert len(shapes)==26

expected=[
('e1_0+e1_0+e1_0+e1_0+e1_0',2080,20),('e1_0+e1_0+e1_0+e2_0',648,43),
('e1_0+e1_0+e3_0',574,68),('e1_0+e1_0+e3_1',250,23),('e1_0+e1_0+e3_2',264,50),
('e1_0+e2_0+e2_0',274,25),('e1_0+e4_0',168,62),('e1_0+e4_1',22,4),('e1_0+e4_2',42,4),
('e1_0+e4_3',88,27),('e1_0+e4_4',102,27),('e2_0+e3_0',224,34),('e2_0+e3_1',72,7),
('e2_0+e3_2',86,17),('e5_0',54,12),('e5_1',38,12),('e5_2',32,10),('e5_3',84,32),('e5_4',4,1),
('e5_5',0,0),('e5_6',0,0),('e5_7',20,3),('e5_8',18,3),('e5_9',26,7),('e5_10',28,9),('e5_11',34,10)]
obs=[]; allcanon=[]
for name,G in shapes:
    nv=G.number_of_nodes();es=sorted(tuple(sorted(e)) for e in G.edges());rr=enumerate_shape(nv,es);aa=autos(G)
    cc={canon(s,nv,es,aa):s for s in rr};obs.append((name,len(rr),len(cc)))
    for key,s in cc.items():allcanon.append((name,key,s))
assert obs==expected,(obs,expected)
assert sum(x[1] for x in obs)==5232 and sum(x[2] for x in obs)==510
zero=[x for x in obs if x[1]==0]
assert [z[0] for z in zero]==['e5_5','e5_6']
slacks=sorted((min(s[3])-1024,max(s[3])-1024,name,key,s[3]) for name,key,s in allcanon)
assert sum(1 for x in slacks if x[0]==0)>=1

print('K5 COARSE FRONTIER CERTIFICATE PASSED')
print('K4 regression: 486 raw / 74 canonical, all shape counts matched')
print('K5 shapes:',len(shapes))
print('K5 total:',sum(x[1] for x in obs),'raw /',sum(x[2] for x in obs),'canonical')
print('K5 shape counts:',obs)
print('K5 zero-survivor connected shapes: e5_5=C5 and e5_6=K1,5')
print('Lowest 10 canonical slack pairs:',[(x[0],x[1],x[2]) for x in slacks[:10]])
