#!/usr/bin/env python3
"""PROB20-11 exact certificate for the zero-deficit four-edge-matching K=4 class.

Eliminates the canonical class
    active parities 00000111
    close-edge distances (2,2,3,2)
    total parity split 6+6
    parity-half Bonferroni bounds (1024,1044).

Standard-library-only exact finite computation in the 2048-point folded
Hamming quotient. No MILP, floating point, heuristic, or timeout inference.
"""
from itertools import combinations, product, permutations
from collections import defaultdict

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
    return ((z&EVEN).bit_count(), (z&ODD).bit_count())

trimax={}
for b in range(1,N):
    pb=parity(b); db=fd(0,b)
    for c in range(b+1,N):
        key=(0,pb,parity(c),db,fd(0,c),fd(b,c))
        h=tri_halves(0,b,c)
        old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])
PERMS=tuple(permutations(range(3)))
def tri_max(a,b,c):
    ps=(parity(a),parity(b),parity(c))
    D=((0,fd(a,b),fd(a,c)),
       (fd(a,b),0,fd(b,c)),
       (fd(a,c),fd(b,c),0))
    for q in PERMS:
        key=(ps[q[0]],ps[q[1]],ps[q[2]],
             D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        v=trimax.get(key)
        if v is not None:
            return v
    raise AssertionError((a,b,c,ps,D))
def high_even(a,b,c):
    return tri_halves(a,b,c)[0] == tri_max(a,b,c)[0]

E1=(0,3)
C=[x for x in range(N)
   if parity(x)==0 and fd(x,E1[0])==6 and fd(x,E1[1])==6]
E2pairs=[(a,b) for a,b in combinations(C,2) if fd(a,b)==2]
assert len(E2pairs)==3276

def sig_pair(ws, blocks=((0,1),tuple(range(2,12)))):
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
                            pat |= 1<<t
                    cnt[pat]+=1
                out.extend(cnt)
            out=tuple(out)
            if best is None or out<best:
                best=out
    return best

E2groups=defaultdict(list)
for p in E2pairs:
    E2groups[sig_pair(p)].append(p)
assert sorted(map(len,E2groups.values())) == [126,3150]
small=next(v[0] for v in E2groups.values() if len(v)==126)
large=next(v[0] for v in E2groups.values() if len(v)==3150)
assert small==(125,126), small
assert large==(125,189), large

def far_from_all(x,centers,p):
    return all(fd(x,a)==(6 if p==parity(a) else 5) for a in centers)

ev4_small=list(E1)+list(small)
E4small=[x for x in range(N)
         if parity(x)==0 and x not in ev4_small and far_from_all(x,ev4_small,0)]
assert len(E4small)==0

ev4=list(E1)+list(large)
E4=[x for x in range(N)
    if parity(x)==0 and x not in ev4 and far_from_all(x,ev4,0)]
OBASE=[x for x in range(N)
       if parity(x)==1 and far_from_all(x,ev4,1)
       and high_even(E1[0],E1[1],x)
       and high_even(large[0],large[1],x)]
assert len(E4)==48
assert len(OBASE)==148
mixed=[(e,o) for e in E4 for o in OBASE if fd(e,o)==3]
assert len(mixed)==2160

patterns=defaultdict(list)
for q in range(12):
    patterns[tuple(bit12(x,q) for x in ev4)].append(q)
blocks=tuple(patterns.values())
assert sorted(map(len,blocks))==[1,1,1,1,4,4]

def sig_mixed(e,o):
    best=None
    for fe,fo in product((0,1),repeat=2):
        out=[]
        for B in blocks:
            cnt=[0]*4
            for q in B:
                pat=(bit12(e,q)^fe) | ((bit12(o,q)^fo)<<1)
                cnt[pat]+=1
            out.extend(cnt)
        out=tuple(out)
        if best is None or out<best:
            best=out
    return best

MG=defaultdict(list)
for e,o in mixed:
    MG[sig_mixed(e,o)].append((e,o))
assert len(MG)==22
assert sum(map(len,MG.values()))==2160

def far_dist(p,q):
    return 6 if p==q else 5

def cand_far_high(selected,p):
    aset=set(selected); out=[]
    for x in range(N):
        if x in aset or parity(x)!=p:
            continue
        if any(fd(x,a)!=far_dist(p,parity(a)) for a in selected):
            continue
        if all(high_even(a,b,x) for a,b in combinations(selected,2)):
            out.append(x)
    return out

def odd_edge_pairs(e,o):
    selected=ev4+[e,o]
    O=cand_far_high(selected,1)
    ans=[]
    for i,a in enumerate(O):
        for b in O[i+1:]:
            if fd(a,b)!=2:
                continue
            if all(high_even(x,a,b) for x in selected):
                ans.append((a,b))
    return ans

def isolate_stats(active):
    E=cand_far_high(active,0)
    O=cand_far_high(active,1)
    adj=[set() for _ in O]
    paircount=0
    for i,a in enumerate(O):
        for j in range(i+1,len(O)):
            b=O[j]
            if fd(a,b)!=6:
                continue
            if all(high_even(x,a,b) for x in active):
                adj[i].add(j); adj[j].add(i); paircount+=1
    tris=[]
    for i in range(len(O)):
        for j in sorted(x for x in adj[i] if x>i):
            for k in sorted(x for x in (adj[i]&adj[j]) if x>j):
                if high_even(O[i],O[j],O[k]):
                    tris.append((i,j,k))
    for e in E:
        for tri in tris:
            os=[O[i] for i in tri]
            if any(fd(e,u)!=5 for u in os):
                continue
            if any(not high_even(a,e,u) for a in active for u in os):
                continue
            if any(not high_even(e,os[i],os[j])
                   for i,j in combinations(range(3),2)):
                continue
            return True,(e,tuple(os)),(len(E),len(O),paircount,len(tris))
    return False,None,(len(E),len(O),paircount,len(tris))

active_count=0
maxE=maxO=maxPairs=maxTris=0
for arr in MG.values():
    e,o=arr[0]
    ps=odd_edge_pairs(e,o)
    for a,b in ps:
        active_count+=1
        active=ev4+[e,o,a,b]
        found,wit,st=isolate_stats(active)
        assert not found,(active,wit,st)
        maxE=max(maxE,st[0])
        maxO=max(maxO,st[1])
        maxPairs=max(maxPairs,st[2])
        maxTris=max(maxTris,st[3])

assert active_count==732, active_count
assert (maxE,maxO,maxPairs,maxTris)==(7,10,16,0), (maxE,maxO,maxPairs,maxTris)

print("CLASS-5 MATCHING4 CERTIFICATE PASSED")
print("E2 pair count/orbits =",len(E2pairs),sorted(map(len,E2groups.values())))
print("small E2 orbit representative/no fifth even =",small,len(E4small))
print("generic E2 representative =",large)
print("mixed endpoint counts E/O/pairs =",len(E4),len(OBASE),len(mixed))
print("mixed-pair subgroup orbits =",len(MG))
print("odd-edge active configurations =",active_count)
print("max eligible E isolates =",maxE)
print("max eligible O isolates =",maxO)
print("max compatible O isolate pairs =",maxPairs)
print("compatible O isolate triangles =",maxTris)
print("CONCLUSION: canonical matching4 class (00000111; 2,2,3,2; neven=6) is impossible")
