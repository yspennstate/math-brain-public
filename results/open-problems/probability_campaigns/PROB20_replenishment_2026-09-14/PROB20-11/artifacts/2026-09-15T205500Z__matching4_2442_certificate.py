#!/usr/bin/env python3
"""PROB20-11 exact certificate for matching4 class 00000011 ; 2,4,4,2.

Canonical K=4 class:
    active parities 00000011
    close-edge distances (2,4,4,2)
    total parity split 6+6
    half third-Bonferroni bounds (1028,1052).

Exact finite folded-cube computation.
"""
from itertools import combinations, product
from collections import defaultdict
from math import comb

N=2048
def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)
def parity(x): return x.bit_count()&1
def bit12(x,q): return ((x>>q)&1) if q<11 else 0

B0=[x for x in range(N) if fd(0,x)<=3]
balls=[]
for c in range(N):
    m=0
    for b in B0: m|=1<<(c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if parity(x)==0: EVEN|=1<<x
ALL=(1<<N)-1
ODD=ALL^EVEN

def tri_halves(a,b,c):
    z=balls[a]&balls[b]&balls[c]
    return ((z&EVEN).bit_count(),(z&ODD).bit_count())

def type_values(p1,p2,d01,d02,d12):
    s=set()
    for b in range(1,N):
        if parity(b)!=p1 or fd(0,b)!=d01: continue
        for c in range(b+1,N):
            if parity(c)!=p2 or fd(0,c)!=d02 or fd(b,c)!=d12: continue
            s.add(tri_halves(0,b,c))
    return s

assert type_values(0,1,2,5,5)=={(4,6),(0,0)}
assert type_values(0,1,4,5,5)=={(1,3),(0,0)}
assert type_values(1,1,5,5,2)=={(6,4),(0,0)}

def low_even(edge,o):
    return 1 if tri_halves(edge[0],edge[1],o)==(0,0) else 0

def high_odd_d2(edge,e):
    return tri_halves(edge[0],edge[1],e)==(6,4)

def excess3(cs,halfmask):
    c0=c1=c2=c3=0
    for c in cs:
        carry=balls[c]
        t=c0^carry; carry=c0&carry; c0=t
        t=c1^carry; carry=c1&carry; c1=t
        t=c2^carry; carry=c2&carry; c2=t
        t=c3^carry; carry=c3&carry; c3=t
        assert carry==0
    ex=0
    planes=(c0,c1,c2,c3)
    for k in range(4,len(cs)+1):
        m=halfmask
        for bit,p in enumerate(planes):
            m &= p if ((k>>bit)&1) else (ALL^p)
        ex += comb(k-1,3)*m.bit_count()
    return ex

E1=(0,3)
C=[x for x in range(N) if parity(x)==0 and fd(x,0)==6 and fd(x,3)==6]
P=[(a,b) for a,b in combinations(C,2) if fd(a,b)==4]
assert len(P)==15750

def sig_pair(ws,blocks=(tuple(range(2)),tuple(range(2,12)))):
    best=None
    for sw in (0,1):
        order=(1,0) if sw else (0,1)
        for flips in product((0,1),repeat=2):
            out=[]
            for B in blocks:
                cnt=[0]*4
                for q in B:
                    pat=0
                    for t,r in enumerate(order):
                        if bit12(ws[r],q)^flips[t]: pat|=1<<t
                    cnt[pat]+=1
                out.extend(cnt)
            out=tuple(out)
            if best is None or out<best: best=out
    return best

G=defaultdict(list)
for p in P: G[sig_pair(p)].append(p)
reps=sorted((v[0],len(v)) for v in G.values())
assert reps==[((125,190),3150),((125,413),12600)],reps

D5=[]
for c in range(N):
    m=0
    for x in range(N):
        if fd(c,x)==5: m|=1<<x
    D5.append(m)

def bits_iter(m):
    while m:
        z=m&-m
        yield z.bit_length()-1
        m-=z

expected_e3={(125,190):342,(125,413):459}
expected_active={(125,190):5616,(125,413):12060}

for rep,_ in reps:
    base=[0,3,rep[0],rep[1]]
    C3=[x for x in range(N) if parity(x)==0 and all(fd(x,e)==6 for e in base)]
    E3=[(a,b) for a,b in combinations(C3,2) if fd(a,b)==4]
    assert len(E3)==expected_e3[rep]
    active_count=0
    excess_survivors=0
    for a,b in E3:
        E6=base+[a,b]
        mo=ODD
        for e in E6: mo &= D5[e]
        O=list(bits_iter(mo))
        for i,u in enumerate(O):
            for v in O[i+1:]:
                if fd(u,v)!=2: continue
                Oedge=(u,v)
                if any(not high_odd_d2(Oedge,e) for e in E6):
                    continue
                x2=sum(low_even(E1,o) for o in Oedge)
                x4=sum(low_even(ed,o) for ed in (rep,(a,b)) for o in Oedge)
                dE=4*x2+x4
                dO=6*x2+3*x4
                if dE>4: continue
                active_count+=1
                active=E6+[u,v]
                if excess3(active,EVEN)<=4-dE and excess3(active,ODD)<=28-dO:
                    excess_survivors+=1
    assert active_count==expected_active[rep],(rep,active_count)
    assert excess_survivors==0,(rep,excess_survivors)

assert sum(expected_active.values())==17676
print("MATCHING4 2,4,4,2 CERTIFICATE PASSED")
print("first d4-edge representatives/orbits =",reps)
print("second d4-edge counts =",expected_e3)
print("active configurations after distance/deficit filters =",expected_active)
print("total active configurations =",sum(expected_active.values()))
print("active configurations satisfying monotone Bonferroni-excess necessity = 0")
print("CONCLUSION: canonical matching4 class (00000011; 2,4,4,2; neven=6) is impossible")
