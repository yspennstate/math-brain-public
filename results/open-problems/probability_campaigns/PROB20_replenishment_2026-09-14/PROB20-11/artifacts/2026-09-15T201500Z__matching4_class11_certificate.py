#!/usr/bin/env python3
"""PROB20-11 exact certificate for the all-d4 balanced four-edge-matching class.

Eliminates canonical K=4 matching class
    active parities 00001111
    close-edge distances (4,4,4,4)
    total parity split 6+6
    parity-half third-Bonferroni bounds (1028,1028).

Exact finite computation in the 2048-point folded Hamming quotient.
No floating point, MILP, heuristic, or timeout inference.
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
    for b in B0:
        m |= 1 << (c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if parity(x)==0:
        EVEN |= 1<<x
ALL=(1<<N)-1
ODD=ALL^EVEN

def tri_halves(a,b,c):
    z=balls[a]&balls[b]&balls[c]
    return ((z&EVEN).bit_count(),(z&ODD).bit_count())

E1=(0,15)
odd_cross=[x for x in range(N)
           if parity(x)==1 and fd(x,E1[0])==5 and fd(x,E1[1])==5]
vals=Counter(tri_halves(E1[0],E1[1],x) for x in odd_cross)
assert vals==Counter({(1,3):336,(0,0):280}), vals

def type_values(p1,p2,d01,d02,d12):
    s=set()
    for b in range(1,N):
        if parity(b)!=p1 or fd(0,b)!=d01: continue
        for c in range(b+1,N):
            if parity(c)!=p2 or fd(0,c)!=d02 or fd(b,c)!=d12: continue
            s.add(tri_halves(0,b,c))
    return s
assert type_values(0,0,4,6,6)=={(0,8)}
assert type_values(0,0,6,6,6)=={(0,4)}
assert type_values(0,1,6,5,5)=={(0,1)}
assert type_values(0,1,4,5,5)=={(1,3),(0,0)}
assert type_values(1,1,5,5,6)=={(1,0)}
assert type_values(1,1,5,5,4)=={(3,1),(0,0)}

def low(edge,x):
    a,b=edge
    assert parity(a)==parity(b) and parity(x)!=parity(a)
    assert fd(a,b)==4 and fd(a,x)==5 and fd(b,x)==5
    return 1 if tri_halves(a,b,x)==(0,0) else 0

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

C=[x for x in range(N)
   if parity(x)==0 and fd(x,E1[0])==6 and fd(x,E1[1])==6]
E2pairs=[(a,b) for a,b in combinations(C,2) if fd(a,b)==4]
assert len(E2pairs)==10605

def sig_pair(ws,blocks=(tuple(range(4)),tuple(range(4,12)))):
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
                        if bit12(ws[r],q)^flips[t]:
                            pat|=1<<t
                    cnt[pat]+=1
                out.extend(cnt)
            out=tuple(out)
            if best is None or out<best:
                best=out
    return best

G=defaultdict(list)
for p in E2pairs:
    G[sig_pair(p)].append(p)
assert sorted(map(len,G.values()))==[105,3780,6720]
reps=sorted((v[0],len(v)) for v in G.values())
assert reps==[((243,252),105),((243,373),6720),((243,819),3780)], reps

D5=[];D6=[]
for c in range(N):
    m5=m6=0
    for x in range(N):
        d=fd(c,x)
        if d==5: m5|=1<<x
        elif d==6: m6|=1<<x
    D5.append(m5);D6.append(m6)

def bits_iter(m):
    while m:
        z=m&-m
        yield z.bit_length()-1
        m-=z

def active_odd_data(evens,eedge2):
    m=ODD
    for e in evens:
        m &= D5[e]
    O=list(bits_iter(m))
    vw=[low(E1,o)+low(eedge2,o) for o in O]
    keep=[i for i,w in enumerate(vw) if w<=1]
    O=[O[i] for i in keep]; vw=[vw[i] for i in keep]
    n=len(O)
    far=[0]*n
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            d=fd(O[i],O[j])
            if d==6:
                far[i]|=1<<j; far[j]|=1<<i
            elif d==4:
                oe=(O[i],O[j])
                y=sum(low(oe,e) for e in evens)
                x=vw[i]+vw[j]
                if x<=1 and y<=1:
                    edges.append((i,j,y,x))
    return O,vw,far,edges

def active_configs(evens,eedge2):
    O,vw,far,edges=active_odd_data(evens,eedge2)
    for t,(i,j,y1,x1) in enumerate(edges):
        common=far[i]&far[j]
        for k,l,y2,x2 in edges[t+1:]:
            x=x1+x2; y=y1+y2
            if x>1 or y>1: continue
            if ((common>>k)&1) and ((common>>l)&1):
                yield O,vw,(i,j,k,l),x,y

raw_expected={(243,252):80304,(243,373):74676,(243,819):94800}
pass_expected={(243,252):14640,(243,373):5268,(243,819):0}

passing=[]
for rep,_orb in reps:
    evens=[0,15,rep[0],rep[1]]
    raw=kept=0
    for O,vw,ids,x,y in active_configs(evens,rep):
        raw+=1
        active=evens+[O[q] for q in ids]
        dE=x+3*y; dO=3*x+y
        hE=excess3(active,EVEN); hO=excess3(active,ODD)
        if hE<=4-dE and hO<=4-dO:
            assert (x,y)==(0,0)
            kept+=1
            passing.append(active)
    assert raw==raw_expected[rep],(rep,raw)
    assert kept==pass_expected[rep],(rep,kept)

assert len(passing)==19908

pair_dist=Counter()
eligible_active=0
full_leaves=0
maxE=maxO=maxEp=maxOp=0

for active in passing:
    Eact=active[:4]; Oact=active[4:]
    Eedges=(tuple(Eact[:2]),tuple(Eact[2:4]))
    Oedges=(tuple(Oact[:2]),tuple(Oact[2:4]))

    me=EVEN
    for e in Eact: me &= D6[e]
    for o in Oact: me &= D5[o]
    mo=ODD
    for o in Oact: mo &= D6[o]
    for e in Eact: mo &= D5[e]

    E=[]; Ew={}
    for x in bits_iter(me):
        w=sum(low(ed,x) for ed in Oedges)
        if w<=1:
            E.append(x); Ew[x]=w
    O=[]; Ow={}
    for x in bits_iter(mo):
        w=sum(low(ed,x) for ed in Eedges)
        if w<=1:
            O.append(x); Ow[x]=w

    maxE=max(maxE,len(E)); maxO=max(maxO,len(O))
    if len(E)<2 or len(O)<2:
        continue
    eligible_active+=1

    Ep=[(a,b) for a,b in combinations(E,2)
        if fd(a,b)==6 and Ew[a]+Ew[b]<=1]
    Op=[(a,b) for a,b in combinations(O,2)
        if fd(a,b)==6 and Ow[a]+Ow[b]<=1]
    maxEp=max(maxEp,len(Ep)); maxOp=max(maxOp,len(Op))
    pair_dist[(len(Ep),len(Op))]+=1

    for ea,eb in Ep:
        cross=D5[ea]&D5[eb]
        for oa,ob in Op:
            if ((cross>>oa)&1) and ((cross>>ob)&1):
                full_leaves+=1

assert eligible_active==6720, eligible_active
assert pair_dist==Counter({
    (2,2):3456,
    (0,0):1584,
    (18,0):576,
    (0,18):576,
    (1,1):432,
    (24,24):96,
}), pair_dist
assert (maxE,maxO,maxEp,maxOp)==(12,12,24,24)
assert full_leaves==0

print("CLASS-11 MATCHING4 CERTIFICATE PASSED")
print("E2 pair count/orbit sizes =",len(E2pairs),sorted(map(len,G.values())))
print("E2 representatives/orbits =",reps)
print("active raw counts =",raw_expected)
print("active configs surviving Bonferroni-excess necessity =",pass_expected,
      "total",len(passing))
print("active survivors with >=2 isolate candidates of each parity =",eligible_active)
print("isolate-pair count distribution =",dict(sorted(pair_dist.items())))
print("max E/O isolate candidates =",maxE,maxO)
print("max E/O admissible isolate pairs =",maxEp,maxOp)
print("complete isolate quartets =",full_leaves)
print("CONCLUSION: canonical matching4 class (00001111; 4,4,4,4; neven=6) is impossible")
