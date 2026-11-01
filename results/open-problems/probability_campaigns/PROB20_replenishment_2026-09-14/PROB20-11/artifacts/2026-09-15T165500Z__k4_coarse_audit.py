#!/usr/bin/env python3
"""PROB20-11 exact K=4 coarse audit, 2026-09-15.

Standard-library-only exact finite verification in the folded Hamming quotient.
Reconstructs the K=3 regression counts and full K=4 coarse
third-Bonferroni counts, obtaining 486 raw / 74 canonical K=4 classes.

No floating point, solver, timeout inference, or heuristic witness is used.
"""
from itertools import combinations, product, permutations
from collections import defaultdict

N=2048

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)

def parity(x): return x.bit_count()&1

B0=[x for x in range(N) if fd(0,x)<=3]
assert len(B0)==299
balls=[]
for c in range(N):
    m=0
    for b in B0:m|=1<<(c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if parity(x)==0:EVEN|=1<<x
ALL=(1<<N)-1
ODD=ALL^EVEN

def halves(m): return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def pair_halves(a,b): return halves(balls[a]&balls[b])
def tri_halves(a,b,c): return halves(balls[a]&balls[b]&balls[c])

pairtbl={}
for p0 in (0,1):
    a=0 if p0==0 else 1
    for p1 in (0,1):
        seen=defaultdict(set)
        for b in range(N):
            if b==a or parity(b)!=p1:continue
            seen[fd(a,b)].add(pair_halves(a,b))
        for d,s in seen.items():
            assert len(s)==1
            pairtbl[(p0,p1,d)]=next(iter(s))

trimax={}
for b in range(1,N):
    for c in range(b+1,N):
        key=(0,parity(b),parity(c),fd(0,b),fd(0,c),fd(b,c))
        h=tri_halves(0,b,c)
        old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])

def tri_max_for(p0,p1,p2,d01,d02,d12):
    ps=[p0,p1,p2]
    D=((0,d01,d02),(d01,0,d12),(d02,d12,0))
    for q in permutations(range(3)):
        key=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if key in trimax:return trimax[key]
    return None

def enumerate_shape(nactive, edge_list):
    eidx={}
    for k,(i,j) in enumerate(edge_list):eidx[(i,j)]=eidx[(j,i)]=k
    out=[]
    for ap in product((0,1),repeat=nactive):
        opts=[((2,4) if ap[i]==ap[j] else (1,3)) for i,j in edge_list]
        for ds in product(*opts):
            for neven in range(13):
                niso=12-nactive
                ie=neven-sum(p==0 for p in ap)
                if ie<0 or ie>niso:continue
                ps=list(ap)+[0]*ie+[1]*(niso-ie)
                D=[[0]*12 for _ in range(12)]
                for i in range(12):
                    for j in range(i+1,12):
                        d=ds[eidx[(i,j)]] if i<nactive and j<nactive and (i,j) in eidx else (6 if ps[i]==ps[j] else 5)
                        D[i][j]=D[j][i]=d
                S1=[sum(67 if p==0 else 232 for p in ps),sum(232 if p==0 else 67 for p in ps)]
                S2=[0,0];valid=True
                for i,j in combinations(range(12),2):
                    h=pairtbl.get((ps[i],ps[j],D[i][j]))
                    if h is None:valid=False;break
                    S2[0]+=h[0];S2[1]+=h[1]
                if not valid:continue
                S3=[0,0]
                for i,j,k in combinations(range(12),3):
                    h=tri_max_for(ps[i],ps[j],ps[k],D[i][j],D[i][k],D[j][k])
                    if h is None:valid=False;break
                    S3[0]+=h[0];S3[1]+=h[1]
                if not valid:continue
                U=(S1[0]-S2[0]+S3[0],S1[1]-S2[1]+S3[1])
                if min(U)>=1024:out.append((tuple(ap),tuple(ds),neven,U))
    return out

def automorphisms(nv,es):
    E={tuple(sorted(e)) for e in es};ans=[]
    for q in permutations(range(nv)):
        if {tuple(sorted((q[i],q[j]))) for i,j in es}==E:ans.append(q)
    return ans

def canonical_state(st,nv,es,autos):
    ap,ds,neven,U=st
    old={tuple(sorted(e)):d for e,d in zip(es,ds)}
    best=None
    for q in autos:
        ap2=tuple(ap[q[i]] for i in range(nv))
        ds2=tuple(old[tuple(sorted((q[i],q[j])))] for i,j in es)
        for f in (0,1):
            key=(tuple(1-p for p in ap2) if f else ap2,ds2,12-neven if f else neven)
            if best is None or key<best:best=key
    return best

shapes3={
 'triangle':(3,[(0,1),(1,2),(0,2)]),
 'matching':(6,[(0,1),(2,3),(4,5)]),
 'path2edge':(5,[(0,1),(1,2),(3,4)]),
 'path3':(4,[(0,1),(1,2),(2,3)]),
 'star':(4,[(0,1),(0,2),(0,3)])}
expect3={'triangle':14,'matching':24,'path2edge':6,'path3':2,'star':0}
for name,(nv,es) in shapes3.items():assert len(enumerate_shape(nv,es))==expect3[name]

shapes4={
 'triangle_pendant':(4,[(0,1),(0,2),(1,2),(2,3)]),
 'tree32111':(5,[(0,1),(0,2),(0,3),(3,4)]),
 'star3_plus_edge':(6,[(0,1),(0,2),(0,3),(4,5)]),
 'triangle_plus_edge':(5,[(0,1),(0,2),(1,2),(3,4)]),
 'path5':(5,[(0,1),(1,2),(2,3),(3,4)]),
 'path4_plus_edge':(6,[(0,1),(1,2),(2,3),(4,5)]),
 'two_p3':(6,[(0,1),(1,2),(3,4),(4,5)]),
 'p3_plus_2edges':(7,[(0,1),(1,2),(3,4),(5,6)]),
 'matching4':(8,[(0,1),(2,3),(4,5),(6,7)]),
 'star4':(5,[(0,1),(0,2),(0,3),(0,4)]),
 'cycle4':(4,[(0,1),(1,2),(2,3),(3,0)])}
expected4={
 'triangle_pendant':(16,6),'tree32111':(6,2),'star3_plus_edge':(26,4),
 'triangle_plus_edge':(98,23),'path5':(8,2),'path4_plus_edge':(30,9),
 'two_p3':(18,3),'p3_plus_2edges':(76,14),'matching4':(208,11),
 'star4':(0,0),'cycle4':(0,0)}
totraw=totcan=0
for name,(nv,es) in shapes4.items():
    rr=enumerate_shape(nv,es);autos=automorphisms(nv,es)
    cc={canonical_state(s,nv,es,autos) for s in rr}
    assert (len(rr),len(cc))==expected4[name],(name,len(rr),len(cc))
    totraw+=len(rr);totcan+=len(cc)
assert (totraw,totcan)==(486,74)

print('COARSE AUDIT PASSED')
print('K=3 raw regression:',expect3)
print('K=4 shape counts:',expected4)
print('K=4 total: 486 raw / 74 canonical')
