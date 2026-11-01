#!/usr/bin/env python3
"""PROB20-11 exact certificate eliminating the four K=5 canonical states
with third-Bonferroni half bounds U=(1024,1024).

Standard library only; exact integer/bitset arithmetic on the 2048-point
folded quotient. No timeout/heuristic is interpreted as infeasibility.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import comb

N=2048
def fd(a,b):
    w=(a^b).bit_count(); return min(w,12-w)
def par(x): return x.bit_count()&1
B0=[x for x in range(N) if fd(0,x)<=3]
assert len(B0)==299
balls=[]
for c in range(N):
    m=0
    for b in B0: m |= 1<<(c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if par(x)==0: EVEN |= 1<<x
ALL=(1<<N)-1; ODD=ALL^EVEN
def halves(m): return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def pairh(a,b): return halves(balls[a]&balls[b])
def trih(a,b,c): return halves(balls[a]&balls[b]&balls[c])

trimax={}
for b in range(1,N):
    bb=balls[0]&balls[b]
    for c in range(b+1,N):
        key=(0,par(b),par(c),fd(0,b),fd(0,c),fd(b,c))
        h=halves(bb&balls[c]); old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])
def tmax(p0,p1,p2,d01,d02,d12):
    ps=(p0,p1,p2); D=((0,d01,d02),(d01,0,d12),(d02,d12,0))
    for q in permutations(range(3)):
        k=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if k in trimax: return trimax[k]
    raise AssertionError((p0,p1,p2,d01,d02,d12))
def tm(a,b,c): return tmax(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c))

def zero_inc(ex,z):
    # If current cost d_H+E_H is zero on both halves, adding z keeps it zero
    # iff all new triples attain their exact maxima and every new 4-fold
    # intersection is empty. Any multiplicity >=4 contributes positive excess.
    for a,b in combinations(ex,2):
        if trih(a,b,z)!=tm(a,b,z): return False
    for a,b,c in combinations(ex,3):
        if balls[a]&balls[b]&balls[c]&balls[z]: return False
    return True

def seed_zero(cs):
    for a,b,c in combinations(cs,3):
        if trih(a,b,c)!=tm(a,b,c): return False
    for a,b,c,d in combinations(cs,4):
        if balls[a]&balls[b]&balls[c]&balls[d]: return False
    return True

# Verify the four coarse states really have U=(1024,1024).
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

def coarse_U(nv,es,ap,ds,neven):
    nodd=12-neven
    S1=[67*neven+232*nodd,232*neven+67*nodd]
    S2=[comb(nodd,2)*40+neven*nodd*10,comb(neven,2)*40+neven*nodd*10]
    S3=[neven*comb(nodd,2)+4*comb(nodd,3),4*comb(neven,3)+comb(neven,2)*nodd]
    ed={tuple(sorted(e)):d for e,d in zip(es,ds)}
    for (i,j),d in zip(es,ds):
        a=pairD[(ap[i],ap[j],d)]; b=pairB[(ap[i],ap[j])]
        for h in (0,1): S2[h]+=a[h]-b[h]
    E=set(ed)
    for i,j,k in combinations(range(nv),3):
        ij=tuple(sorted((i,j))); ik=tuple(sorted((i,k))); jk=tuple(sorted((j,k)))
        if not ({ij,ik,jk}&E): continue
        dij=ed.get(ij,6 if ap[i]==ap[j] else 5)
        dik=ed.get(ik,6 if ap[i]==ap[k] else 5)
        djk=ed.get(jk,6 if ap[j]==ap[k] else 5)
        a=tmax(ap[i],ap[j],ap[k],dij,dik,djk); b=baseTri[(ap[i],ap[j],ap[k])]
        for h in (0,1): S3[h]+=a[h]-b[h]
    isoE=neven-sum(p==0 for p in ap); isoO=12-nv-isoE
    for (i,j),d in zip(es,ds):
        for q,n in ((0,isoE),(1,isoO)):
            if not n: continue
            a=tmax(ap[i],ap[j],q,d,6 if ap[i]==q else 5,6 if ap[j]==q else 5)
            b=baseTri[(ap[i],ap[j],q)]
            for h in (0,1): S3[h]+=n*(a[h]-b[h])
    return (S1[0]-S2[0]+S3[0],S1[1]-S2[1]+S3[1])

states=[
    (9,[(0,1),(2,3),(4,5),(6,7),(6,8)],(0,0,0,0,0,1,1,1,1),(4,4,3,2,4),6),
    (8,[(0,1),(2,3),(4,7),(5,7),(6,7)],(0,0,1,1,0,0,1,0),(4,2,4,4,1),6),
    (6,[(0,1),(1,2),(1,3),(2,4),(3,5)],(0,0,0,1,1,1),(4,2,3,3,2),6),
    (6,[(0,4),(0,5),(1,3),(2,3),(3,4)],(0,0,1,1,1,0),(3,2,3,4,2),6),
]
for st in states:
    assert coarse_U(*st)==(1024,1024)

# A. Connected tree e5_9. Complete normalization:
# c0=0; c1 has folded weight 4 -> {1,2,3,4}; c2 has folded distance
# 6 from c0 and 2 from c1. Complementing c2 identifies intersection 0 with
# intersection 4, so choose c2={1,...,6}.
seedA=[0,15,63]
assert seed_zero(seedA)
candA=[z for z in range(N) if par(z)==1 and fd(z,0)==5 and fd(z,15)==3 and fd(z,63)==5]
assert len(candA)==80
failA=Counter(); goodA=0
for z in candA:
    bad=[]
    for a,b in combinations(seedA,2):
        ac=trih(a,b,z); mx=tm(a,b,z)
        if ac!=mx: bad.append((mx[0]-ac[0],mx[1]-ac[1]))
    q=(balls[0]&balls[15]&balls[63]&balls[z]).bit_count()
    failA[(tuple(bad),q)]+=1
    goodA += zero_inc(seedA,z)
assert goodA==0
assert failA==Counter({((),1):60,(((3,7),),0):20})

# B. Connected tree e5_10. Normalize even edge c0-c5 of distance 2 to
# 0,{1,2}; odd vertex c4 is distance 3 from c0 and far (5) from c5, forcing
# a 3-subset disjoint from {1,2}, unique under the stabilizer.
seedB=[0,3,28]
assert seed_zero(seedB)
candB=[z for z in range(N) if par(z)==1 and fd(z,0)==5 and fd(z,3)==5 and fd(z,28)==2]
assert len(candB)==35
failB=Counter(); goodB=0
for z in candB:
    bad=[]
    for a,b in combinations(seedB,2):
        ac=trih(a,b,z); mx=tm(a,b,z)
        if ac!=mx: bad.append((mx[0]-ac[0],mx[1]-ac[1]))
    q=(balls[0]&balls[3]&balls[28]&balls[z]).bit_count()
    failB[(tuple(bad),q)]+=1
    goodB += zero_inc(seedB,z)
assert goodB==0
assert failB==Counter({(((4,6),(6,4)),0):21,((),6):14})

# C. two disjoint edges + K1,3. Normalize the star component: center=0,
# odd distance-1 leaf={1}; each even distance-4 leaf avoids coordinate 1,
# and the two leaves are far distance 6, hence intersect in exactly one
# coordinate. The stabilizer is transitive, giving leaves 30 and 226.
seedC=[0,1,30,226]
for a,b,c in combinations(seedC,3): assert trih(a,b,c)==tm(a,b,c)
qC=balls[0]&balls[1]&balls[30]&balls[226]
assert halves(qC)==(0,1)
# Positive fourfold overlap gives positive odd-half Bonferroni excess, impossible
# because the state's odd-half slack is zero.

# D. three disjoint edges + P3. Translate by the odd P3 center; global parity
# flips but neven=6 is unchanged. Normalize the resulting even P3 to
# 0 --d2-- 3 and 0 --d4-- 60, with leaf distance 6. The stabilizer is transitive.
seedD=[0,3,60]
assert seed_zero(seedD)
candD=[z for z in range(N) if par(z)==1 and all(fd(z,c)==5 for c in seedD)]
assert len(candD)==520
failD=Counter(); goodD=0
for z in candD:
    bad=[]
    for a,b in combinations(seedD,2):
        ac=trih(a,b,z); mx=tm(a,b,z)
        if ac!=mx: bad.append((mx[0]-ac[0],mx[1]-ac[1]))
    q=(balls[0]&balls[3]&balls[60]&balls[z]).bit_count()
    failD[(tuple(bad),q)]+=1
    goodD += zero_inc(seedD,z)
assert goodD==0
assert failD==Counter({((),1):180,(((1,3),),0):160,(((4,6),),0):120,(((4,6),(1,3)),0):60})

print('K5 ZERO-SLACK-4 CERTIFICATE PASSED')
print('A e5_9:',len(candA),'distance candidates; failure profile',failA)
print('B e5_10:',len(candB),'distance candidates; failure profile',failB)
print('C two edges + K1,3: normalized star fourfold intersection halves',halves(qC))
print('D three edges + P3:',len(candD),'distance candidates; failure profile',failD)
print('All four canonical K=5 states with U=(1024,1024) are impossible.')
