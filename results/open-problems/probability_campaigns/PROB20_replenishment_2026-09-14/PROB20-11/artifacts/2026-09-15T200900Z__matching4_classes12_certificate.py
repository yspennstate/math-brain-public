#!/usr/bin/env python3
"""PROB20-11 exact certificate for matching4 classes
  A: 00000011 ; (2,2,4,2), half bounds (1030,1062)
  B: 00000011 ; (2,2,2,2), half bounds (1032,1072).

Exact finite folded-cube computation. Standard library only.
"""
from itertools import combinations, product
from collections import defaultdict, Counter
from math import comb

N=2048
def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)
def parity(x): return x.bit_count()&1
def bit12(x,q): return ((x>>q)&1) if q<11 else 0

B0=[x for x in range(N) if fd(0,x)<=3]
assert len(B0)==299
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
    return tri_halves(edge[0],edge[1],o)==(0,0)
def low_odd(edge,e):
    return tri_halves(edge[0],edge[1],e)==(0,0)

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
E2pairs=[(a,b) for a,b in combinations(C,2) if fd(a,b)==2]
assert len(E2pairs)==3276

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
for p in E2pairs: G[sig_pair(p)].append(p)
reps=sorted((v[0],len(v)) for v in G.values())
assert reps==[((125,126),126),((125,189),3150)],reps

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

def run_class(edge3_distance,U):
    stats={}
    all_survivors=0
    for rep,_orb in reps:
        base=[0,3,rep[0],rep[1]]
        C3=[x for x in range(N) if parity(x)==0 and all(fd(x,e)==6 for e in base)]
        E3=[(a,b) for a,b in combinations(C3,2) if fd(a,b)==edge3_distance]
        active_count=0; hsurv=0; hist=Counter()
        for a,b in E3:
            E6=base+[a,b]
            mo=ODD
            for e in E6: mo &= D5[e]
            O=list(bits_iter(mo))
            for i,u in enumerate(O):
                for v in O[i+1:]:
                    if fd(u,v)!=2: continue
                    oe=(u,v)
                    y=sum(low_odd(oe,e) for e in E6)
                    if edge3_distance==4:
                        x2=sum(low_even(ed,o) for ed in (E1,rep) for o in oe)
                        x4=sum(low_even((a,b),o) for o in oe)
                        dE=4*x2+x4+6*y
                        dO=6*x2+3*x4+4*y
                        key=(x2,x4,y)
                    else:
                        x=sum(low_even(ed,o) for ed in (E1,rep,(a,b)) for o in oe)
                        dE=4*x+6*y
                        dO=6*x+4*y
                        key=(x,y)
                    if dE>U[0]-1024 or dO>U[1]-1024: continue
                    active_count+=1; hist[key]+=1
                    active=E6+[u,v]
                    if (excess3(active,EVEN)<=U[0]-1024-dE and
                        excess3(active,ODD)<=U[1]-1024-dO):
                        hsurv+=1
        stats[rep]=(len(E3),active_count,hsurv,hist)
        all_survivors+=hsurv
    return stats,all_survivors

statsA,survA=run_class(4,(1030,1062))
assert statsA[(125,126)][:3]==(0,0,0)
assert statsA[(125,189)][:3]==(600,18864,0)
assert statsA[(125,189)][3]==Counter({(0,2,0):10080,(0,0,0):8784})
assert survA==0

statsB,survB=run_class(2,(1032,1072))
assert statsB[(125,126)][:3]==(0,0,0)
assert statsB[(125,189)][:3]==(168,22176,0)
assert statsB[(125,189)][3]==Counter({(2,0):15552,(0,0):6624})
assert survB==0

print("MATCHING4 CLASSES 2 AND 1 CERTIFICATE PASSED")
print("second d2-edge reps/orbits =",reps)
print("class (2,2,4,2) stats =",statsA)
print("class (2,2,2,2) stats =",statsB)
print("CONCLUSION: both canonical matching4 classes are impossible")
