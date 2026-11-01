#!/usr/bin/env python3
"""PROB20-11 exact certificate: eliminate the four lowest-slack
K=4 triangle+disjoint-edge coarse classes.

Standard-library only. Exact integer/bitset arithmetic in the 2048-point
folded Hamming quotient. No floating point, solver, heuristic, or timeout
is used as a negative certificate.
"""
from itertools import combinations, permutations
from collections import defaultdict, Counter
from math import comb

N=2048
MASK12=(1<<12)-1

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)
def par(x): return x.bit_count()&1

# Folded radius-3 balls as 2048-bit integers.
B0=[x for x in range(N) if fd(0,x)<=3]
assert len(B0)==299
balls=[]
for c in range(N):
    m=0
    for b in B0: m |= 1 << (c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if par(x)==0: EVEN |= 1<<x
ALL=(1<<N)-1
ODD=ALL^EVEN

def halves(m):
    return ((m&EVEN).bit_count(),(m&ODD).bit_count())

def tri_actual(a,b,c):
    return halves(balls[a]&balls[b]&balls[c])

# Exact triple-intersection maxima by parity/distance orbit.
trimax={}
for b in range(1,N):
    bb=balls[0]&balls[b]
    pb=par(b); d0b=fd(0,b)
    for c in range(b+1,N):
        key=(0,pb,par(c),d0b,fd(0,c),fd(b,c))
        h=halves(bb&balls[c])
        old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])

def tri_max(p0,p1,p2,d01,d02,d12):
    ps=[p0,p1,p2]
    D=((0,d01,d02),(d01,0,d12),(d02,d12,0))
    for q in permutations(range(3)):
        key=(ps[q[0]],ps[q[1]],ps[q[2]],
             D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if key in trimax: return trimax[key]
    raise AssertionError((p0,p1,p2,d01,d02,d12))

def triple_max_centers(a,b,c):
    return tri_max(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c))

def deficit_half(cs,half):
    ans=0
    for a,b,c in combinations(cs,3):
        mx=triple_max_centers(a,b,c)[half]
        act=tri_actual(a,b,c)[half]
        assert act<=mx
        ans += mx-act
    return ans

def excess_half(cs,half):
    # E=sum_x C(m(x)-1,3) for m>0.
    # Exact inclusion identity: E=S4-S5+S6-... .
    mask=EVEN if half==0 else ODD
    ans=0
    for r in range(4,len(cs)+1):
        coeff=1 if (r-4)%2==0 else -1
        for inds in combinations(cs,r):
            m=mask
            for c in inds: m &= balls[c]
            ans += coeff*m.bit_count()
    assert ans>=0
    return ans

def cost(cs,half): return deficit_half(cs,half)+excess_half(cs,half)

def zero_add_ok(existing,newc,half):
    # Valid when existing already has zero deficit and zero excess.
    for a,b in combinations(existing,2):
        if tri_actual(a,b,newc)[half] != triple_max_centers(a,b,newc)[half]:
            return False
    mask=EVEN if half==0 else ODD
    for a,b,c in combinations(existing,3):
        if (balls[a]&balls[b]&balls[c]&balls[newc]&mask):
            return False
    return True

shell1=[x for x in range(N) if fd(0,x)==1]
shell2=[x for x in range(N) if fd(0,x)==2]
assert (len(shell1),len(shell2))==(12,66)

# Canonical column-histogram key for four quotient rows, modulo independent
# row complementation, coordinate permutations, and optional swaps of rows
# (0,1) and (2,3). Equality of these canonical histograms is a complete
# orbit test for the stated symmetry subgroup.
def base_hist(rows):
    h=[0]*16
    for col in range(12):
        p=0
        for i,r in enumerate(rows): p |= ((r>>col)&1)<<i
        h[p]+=1
    return tuple(h)

def perm_pattern(p,sw01,sw23):
    bits=[(p>>i)&1 for i in range(4)]
    if sw01: bits[0],bits[1]=bits[1],bits[0]
    if sw23: bits[2],bits[3]=bits[3],bits[2]
    q=0
    for i,b in enumerate(bits): q|=b<<i
    return q

hist_maps=[]
for flip in range(16):
    for sw01 in (0,1):
        for sw23 in (0,1):
            mp=[]
            for p in range(16): mp.append(perm_pattern(p^flip,sw01,sw23))
            hist_maps.append(tuple(mp))

def canon4(rows):
    h=base_hist(rows); best=None
    for mp in hist_maps:
        q=[0]*16
        for p,n in enumerate(h): q[mp[p]]+=n
        t=tuple(q)
        if best is None or t<best: best=t
    return best

# -------------------------------------------------------------------------
# Class 1: active parities 00000, close distances (4,4,4,2), neven=5,
# coarse half bounds (1024,1034).  Even-half slack is exactly zero.
# -------------------------------------------------------------------------
# Normalize one triangle edge to 0--15. Enumerate all other active centers.
c0,c1=0,15
tri2=[x for x in range(1,N) if x!=c1 and par(x)==0 and fd(0,x)==4 and fd(c1,x)==4]
assert len(tri2)==238
tri2=[x for x in tri2 if tri_actual(0,c1,x)[0]==triple_max_centers(0,c1,x)[0]]
assert len(tri2)==168
active1=[]
for c2 in tri2:
    tri=[0,c1,c2]
    for c3 in range(N):
        if par(c3)!=0 or c3 in tri: continue
        if not all(fd(c3,c)==6 for c in tri): continue
        assert zero_add_ok(tri,c3,0)
        ex=tri+[c3]
        for s in shell2:
            c4=c3^s
            if c4<=c3 or par(c4)!=0 or c4 in ex: continue
            if not all(fd(c4,c)==6 for c in tri): continue
            if zero_add_ok(ex,c4,0): active1.append((c2,c3,c4))
assert len(active1)==90720
orb=defaultdict(list)
for c2,c3,c4 in active1:
    orb[canon4([15,c2,c3,c4])].append((c2,c3,c4))
assert len(orb)==4
assert sorted(map(len,orb.values()))==[6720,10080,13440,60480]

def odd_pool_zero(active):
    out=[]
    for x in range(N):
        if par(x)!=1: continue
        if all(fd(x,c)==5 for c in active) and zero_add_ok(active,x,0): out.append(x)
    return out

def max_zero_extension(active,cand):
    best=0
    def rec(ex,cands,depth):
        nonlocal best
        best=max(best,depth)
        if depth+len(cands)<=best: return
        for i,x in enumerate(cands):
            if not zero_add_ok(ex,x,0): continue
            rem=[y for y in cands[i+1:] if fd(x,y)==6]
            rec(ex+[x],rem,depth+1)
    rec(active,cand,0)
    return best
class1_info=[]
for vals in orb.values():
    rep=vals[0]
    active=[0,15,*rep]
    pool=odd_pool_zero(active)
    mx=max_zero_extension(active,pool)
    class1_info.append((rep,len(vals),len(pool),mx))
assert sorted(x[2] for x in class1_info)==[6,6,42,56]
assert max(x[3] for x in class1_info)==2
# Seven odd isolates would be required. Impossible.

# -------------------------------------------------------------------------
# Class 2: active parities 00011, distances (2,4,4,2), neven=5,
# coarse bounds (1058,1024). Odd-half slack zero.
# Normalize 0--3 as the unique triangle distance-2 edge.
# -------------------------------------------------------------------------
c2s=[x for x in range(N) if x not in (0,3) and par(x)==0 and fd(0,x)==4 and fd(3,x)==4]
assert len(c2s)==240
cost_counter2=Counter(); placements2=0
for c2 in c2s:
    tri=[0,3,c2]
    assert cost(tri,1)==0
    for x in range(N):
        if par(x)==1 and all(fd(x,c)==5 for c in tri):
            placements2+=1
            cc=cost(tri+[x],1)
            cost_counter2[cc]+=1
assert placements2==124320
assert min(cost_counter2)==1
assert cost_counter2==Counter({9:50400,6:33600,3:25200,1:15120})
# Slack is zero, so no first odd edge endpoint is admissible.

# -------------------------------------------------------------------------
# Class 3: active parities 00000, distances (2,2,2,2), neven=6,
# coarse bounds (1025,1116). Even-half slack one.
# -------------------------------------------------------------------------
c2s=[x for x in range(N) if x not in (0,3) and par(x)==0 and fd(0,x)==2 and fd(3,x)==2]
assert len(c2s)==20
active3=[]; geom3=0
for c2 in c2s:
    tri=[0,3,c2]
    assert cost(tri,0)==0
    for c3 in range(N):
        if par(c3)!=0 or c3 in tri or not all(fd(c3,c)==6 for c in tri): continue
        assert zero_add_ok(tri,c3,0)
        ex=tri+[c3]
        for s in shell2:
            c4=c3^s
            if c4<=c3 or par(c4)!=0 or c4 in ex: continue
            if not all(fd(c4,c)==6 for c in tri): continue
            geom3+=1
            assert zero_add_ok(ex,c4,0)
            active3.append((c2,c3,c4))
assert geom3==len(active3)==25200
orb3=defaultdict(list)
for c2,c3,c4 in active3:
    orb3[canon4([3,c2,c3,c4])].append((c2,c3,c4))
assert len(orb3)==1 and len(next(iter(orb3.values())))==25200
rep3=next(iter(orb3.values()))[0]
active=[0,3,*rep3]
assert cost(active,0)==0
# One additional even isolate is required.
even_iso=[]
for x in range(N):
    if par(x)==0 and x not in active and all(fd(x,c)==6 for c in active):
        if cost(active+[x],0)<=1: even_iso.append(x)
assert len(even_iso)==18

def clique_number_d6(vertices):
    n=len(vertices); adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if fd(vertices[i],vertices[j])==6:
                adj[i].add(j); adj[j].add(i)
    best=0
    def expand(sz,P):
        nonlocal best
        best=max(best,sz)
        if sz+len(P)<=best: return
        while P:
            if sz+len(P)<=best: return
            v=P.pop()
            expand(sz+1,[u for u in P if u in adj[v]])
    expand(0,list(range(n)))
    return best
pool_sizes=[]; cliques=[]
for e in even_iso:
    ex=active+[e]
    assert cost(ex,0)==0
    pool=[]
    for x in range(N):
        if par(x)==1 and all(fd(x,c)==5 for c in ex) and cost(ex+[x],0)<=1:
            pool.append(x)
    pool_sizes.append(len(pool))
    cliques.append(clique_number_d6(pool))
assert Counter(pool_sizes)==Counter({10:12,17:6})
assert set(cliques)=={2}
# Six pairwise-distance-6 odd isolates would be required, impossible.

# -------------------------------------------------------------------------
# Class 4: active parities 00001, distances (2,2,2,1), neven=5,
# coarse bounds (1042,1025). Odd-half slack one.
# All equilateral folded-distance-2 triangles are one coordinate orbit, so
# normalize to 0,3,5.
# -------------------------------------------------------------------------
tri=[0,3,5]
assert fd(0,3)==fd(0,5)==fd(3,5)==2
c3s=[x for x in range(N) if par(x)==0 and x not in tri and all(fd(x,c)==6 for c in tri)]
assert len(c3s)==126
costs4=Counter(); placements4=0
for c3 in c3s:
    ex=tri+[c3]
    for s in shell1:
        c4=c3^s
        if par(c4)!=1 or c4 in ex: continue
        if not all(fd(c4,c)==5 for c in tri): continue
        placements4+=1
        costs4[cost(ex+[c4],1)]+=1
assert placements4==1512
assert costs4==Counter({32:1512})
# Slack is one, so every active placement is impossible already.

print('CERTIFICATE PASSED')
print('K=4 triangle+edge class 1 eliminated: active configs',len(active1),
      'orbit sizes',sorted(map(len,orb.values())),
      'odd pool sizes',sorted(x[2] for x in class1_info),
      'max zero-slack extension',max(x[3] for x in class1_info))
print('class 2 eliminated: first odd-endpoint placements',placements2,
      'minimum odd-half deficit+excess',min(cost_counter2))
print('class 3 eliminated: active configs',len(active3),
      'one active orbit; even isolates',len(even_iso),
      'odd candidate pool distribution',dict(Counter(pool_sizes)),
      'all d6 clique numbers',sorted(set(cliques)))
print('class 4 eliminated: active placements',placements4,
      'all odd-half deficit+excess =',next(iter(costs4)))
print('CONCLUSION: the four smallest-minimum-slack triangle+edge K=4 classes are impossible.')
