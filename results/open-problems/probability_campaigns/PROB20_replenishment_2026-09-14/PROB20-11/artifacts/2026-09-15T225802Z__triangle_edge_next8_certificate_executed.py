#!/usr/bin/env python3
"""PROB20-11 exact certificate: eliminate eight next low-slack
K=4 triangle+disjoint-edge canonical classes.

Standard-library only. Exact integer/bitset arithmetic on the 2048-point
folded Hamming quotient. No timeout, floating point, heuristic, or solver
status is used as infeasibility.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from functools import lru_cache

N=2048

def fd(a,b):
    w=(a^b).bit_count(); return min(w,12-w)
def par(x): return x.bit_count()&1

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
ALL=(1<<N)-1; ODD=ALL^EVEN

def halves(m): return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def tri_actual(a,b,c): return halves(balls[a]&balls[b]&balls[c])

trimax={}
for b in range(1,N):
    bb=balls[0]&balls[b]; pb=par(b); d0b=fd(0,b)
    for c in range(b+1,N):
        key=(0,pb,par(c),d0b,fd(0,c),fd(b,c))
        h=halves(bb&balls[c]); old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])

def tri_max(p0,p1,p2,d01,d02,d12):
    ps=[p0,p1,p2]; D=((0,d01,d02),(d01,0,d12),(d02,d12,0))
    for q in permutations(range(3)):
        key=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if key in trimax: return trimax[key]
    raise AssertionError((p0,p1,p2,d01,d02,d12))
def triple_max_centers(a,b,c):
    return tri_max(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c))

def deficit_half(cs,half):
    ans=0
    for a,b,c in combinations(cs,3):
        mx=triple_max_centers(a,b,c)[half]; act=tri_actual(a,b,c)[half]
        assert act<=mx; ans += mx-act
    return ans

def excess_half(cs,half):
    mask=EVEN if half==0 else ODD; ans=0
    for r in range(4,len(cs)+1):
        coeff=1 if (r-4)%2==0 else -1
        for inds in combinations(cs,r):
            m=mask
            for c in inds: m &= balls[c]
            ans += coeff*m.bit_count()
    assert ans>=0; return ans

@lru_cache(maxsize=None)
def cost_key(t,half): return deficit_half(t,half)+excess_half(t,half)
def cost(cs,half): return cost_key(tuple(sorted(cs)),half)

def zero_increment(existing,z,half):
    # Exact criterion for cost(existing+[z],half)==cost(existing,half).
    for a,b in combinations(existing,2):
        if tri_actual(a,b,z)[half] != triple_max_centers(a,b,z)[half]: return False
    mask=EVEN if half==0 else ODD
    for a,b,c in combinations(existing,3):
        if balls[a]&balls[b]&balls[c]&balls[z]&mask: return False
    return True

# Complete coordinate-permutation orbit invariants for four nonzero antipodal
# rows, modulo independent row complementation.  Coordinate permutations merely
# reorder the 12 column patterns, so the column-pattern histogram is complete.
def base_hist4(rows):
    h=[0]*16
    for col in range(12):
        p=0
        for i,r in enumerate(rows): p|=((r>>col)&1)<<i
        h[p]+=1
    return tuple(h)

def canon_xy(rows):
    # Preserve first two row roles; swap only the two disjoint-edge endpoints.
    h=base_hist4(rows); best=None
    for flip in range(16):
        for sw in (0,1):
            q=[0]*16
            for p,n in enumerate(h):
                v=p^flip; bits=[(v>>i)&1 for i in range(4)]
                if sw: bits[2],bits[3]=bits[3],bits[2]
                w=sum(b<<i for i,b in enumerate(bits)); q[w]+=n
            t=tuple(q)
            if best is None or t<best: best=t
    return best

def canon4(rows):
    # Also permit swapping the two nonzero vertices of the normalized
    # equilateral d=4 triangle.
    h=base_hist4(rows); best=None
    for flip in range(16):
        for sw01 in (0,1):
            for sw23 in (0,1):
                q=[0]*16
                for p,n in enumerate(h):
                    v=p^flip; bits=[(v>>i)&1 for i in range(4)]
                    if sw01: bits[0],bits[1]=bits[1],bits[0]
                    if sw23: bits[2],bits[3]=bits[3],bits[2]
                    w=sum(b<<i for i,b in enumerate(bits)); q[w]+=n
                t=tuple(q)
                if best is None or t<best: best=t
    return best

def clique_number_d6(vertices):
    n=len(vertices); adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if fd(vertices[i],vertices[j])==6:
                adj[i].add(j); adj[j].add(i)
    best=0
    def rec(P,sz):
        nonlocal best
        if sz>best: best=sz
        if sz+len(P)<=best: return
        while P:
            if sz+len(P)<=best: return
            v=P.pop(); rec([u for u in P if u in adj[v]],sz+1)
    rec(list(range(n)),0); return best

def max_extension_cost(active,cand,half,budget,need):
    n=len(cand); adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if fd(cand[i],cand[j])==6:
                adj[i].add(j); adj[j].add(i)
    best=0
    def rec(ex,P,depth):
        nonlocal best
        if depth>best: best=depth
        if depth>=need or depth+len(P)<=best: return
        while P:
            if depth+len(P)<=best: return
            v=P.pop(); z=cand[v]
            if cost(ex+[z],half)<=budget:
                rec(ex+[z],[u for u in P if u in adj[v]],depth+1)
    rec(active,list(range(n)),0); return best

# Normalized triangles used below. In full 12-coordinate supports:
# T224: 0,{1,2},{3,4}; T244: 0,{1,2},{1,3,4,5};
# T233: 0,{1,2},{1,3,4}; T444: 0,{1,2,3,4},{1,2,5,6}.
# The relevant stabilizers S2xS10 or S4xS8 are transitive on the prescribed
# support intersections, so each is a complete normalization of its triangle type.
T224=[0,3,12]; T244=[0,3,29]; T233=[0,3,13]; T444=[0,15,51]
assert (fd(0,3),fd(0,12),fd(3,12))==(2,2,4)
assert (fd(0,3),fd(0,29),fd(3,29))==(2,4,4)
assert (fd(0,3),fd(0,13),fd(3,13))==(2,3,3)
assert (fd(0,15),fd(0,51),fd(15,51))==(4,4,4)

# A. 00011 (2,2,4,4), neven=6, U=(1025,1068): even slack 1.
oddA=[x for x in range(N) if par(x)==1 and all(fd(x,c)==5 for c in T224)]
assert len(oddA)==560
cntA=Counter(); pairsA=0
for i,x in enumerate(oddA):
    for y in oddA[i+1:]:
        if fd(x,y)==4:
            pairsA+=1; cntA[cost(T224+[x,y],0)]+=1
assert pairsA==76692 and min(cntA)==2

# B. 00011 (2,4,4,4), neven=5, U=(1039,1025): odd slack 1.
oddB=[x for x in range(N) if par(x)==1 and all(fd(x,c)==5 for c in T244)]
assert len(oddB)==518
cntB=Counter(); pairsB=0
for i,x in enumerate(oddB):
    for y in oddB[i+1:]:
        if fd(x,y)==4:
            pairsB+=1; cntB[cost(T244+[x,y],1)]+=1
assert pairsB==65730 and min(cntB)==3

# C. 00000 (2,4,4,4), neven=5, U=(1026,1036): even slack 2.
evenC=[x for x in range(N) if par(x)==0 and x not in T244 and all(fd(x,c)==6 for c in T244)]
activeC=[]
for i,x in enumerate(evenC):
    for y in evenC[i+1:]:
        if fd(x,y)==4:
            assert cost(T244+[x,y],0)==0; activeC.append((x,y))
assert len(activeC)==2625
orbsC=defaultdict(list)
for x,y in activeC: orbsC[canon_xy([3,29,x,y])].append((x,y))
assert sorted(map(len,orbsC.values()))==[420,945,1260]
statsC=[]
for vals in orbsC.values():
    x,y=vals[0]; active=T244+[x,y]
    pool=[z for z in range(N) if par(z)==1 and all(fd(z,c)==5 for c in active) and cost(active+[z],0)<=2]
    statsC.append((len(vals),len(pool),clique_number_d6(pool)))
assert sorted(statsC)==[(420,90,4),(945,125,5),(1260,116,5)]
# Seven odd isolates are required; even the relaxed d6 clique number is <=5.

# D. 00111 (2,3,3,2), neven=6, U=(1026,1027): slacks (2,3).
oddD=[x for x in range(N) if par(x)==1 and x!=13 and fd(x,13)==6 and fd(x,0)==5 and fd(x,3)==5]
cntD=Counter(); pairsD=0
for i,x in enumerate(oddD):
    for y in oddD[i+1:]:
        if fd(x,y)==2:
            pairsD+=1; cs=T233+[x,y]; cntD[(cost(cs,0),cost(cs,1))]+=1
assert pairsD==4676 and min(k[0] for k in cntD)==5

# E. 00011 (2,2,4,2), neven=5, U=(1065,1027): odd slack 3.
cntE=Counter(); pairsE=0
for i,x in enumerate(oddA):
    for y in oddA[i+1:]:
        if fd(x,y)==2:
            pairsE+=1; cntE[cost(T224+[x,y],1)]+=1
assert pairsE==12348 and min(cntE)==9

# F. 00011 (4,4,4,2), neven=6, U=(1027,1046): even slack 3.
oddF=[x for x in range(N) if par(x)==1 and all(fd(x,c)==5 for c in T444)]
cntF=Counter(); survF=[]; pairsF=0
for i,x in enumerate(oddF):
    for y in oddF[i+1:]:
        if fd(x,y)==2:
            pairsF+=1; cc=cost(T444+[x,y],0); cntF[cc]+=1
            if cc<=3: survF.append((x,y,cc))
assert pairsF==9630 and len(survF)==675 and Counter(c for _,_,c in survF)==Counter({3:495,1:180})
orbsF=defaultdict(list)
for x,y,cc in survF: orbsF[canon4([15,51,x,y])].append((x,y,cc))
assert sorted((len(v),v[0][2]) for v in orbsF.values())==[(15,3),(60,1),(120,1),(480,3)]
statsF=[]
for vals in orbsF.values():
    x,y,cc=vals[0]; active=T444+[x,y]
    evcand=[z for z in range(N) if par(z)==0 and z not in active and all(fd(z,c)==6 for c in T444) and all(fd(z,c)==5 for c in (x,y)) and cost(active+[z],0)<=3]
    # enumerate exact triples of additional even isolates
    triples=[]
    for ia,a in enumerate(evcand):
        if cost(active+[a],0)>3: continue
        for ib in range(ia+1,len(evcand)):
            b=evcand[ib]
            if fd(a,b)!=6 or cost(active+[a,b],0)>3: continue
            for ic in range(ib+1,len(evcand)):
                c=evcand[ic]
                if fd(a,c)==6 and fd(b,c)==6 and cost(active+[a,b,c],0)<=3:
                    triples.append((a,b,c))
    if not triples:
        best=max_extension_cost(active,evcand,0,3,3)
        statsF.append((len(vals),cc,len(evcand),best,0,0))
    else:
        zeroodd=0
        for a,b,c in triples:
            ex=active+[a,b,c]
            assert cost(ex,0)==3
            ev=[q for q in ex if par(q)==0]; od=[q for q in ex if par(q)==1]
            for z in range(N):
                if par(z)==1 and all(fd(z,e)==5 for e in ev) and all(fd(z,o)==6 for o in od) and zero_increment(ex,z,0):
                    zeroodd+=1
        statsF.append((len(vals),cc,len(evcand),3,len(triples),zeroodd))
assert sorted(statsF)==[(15,3,32,3,192,0),(60,1,14,1,0,0),(120,1,14,1,0,0),(480,3,29,3,138,0)]
# The only orbits admitting all three required even isolates have no admissible
# next odd isolate at all once the even-half budget is saturated.

# G. 00011 (2,2,4,4), neven=5, U=(1046,1028): odd slack 4.
cntG=Counter(); pairsG=0
for i,x in enumerate(oddA):
    for y in oddA[i+1:]:
        if fd(x,y)==4:
            pairsG+=1; cntG[cost(T224+[x,y],1)]+=1
assert pairsG==76692 and min(cntG)==6

# H. 00000 (2,4,4,2), neven=5, U=(1031,1037): even slack 7.
evenH=evenC
activeH=[]
for i,x in enumerate(evenH):
    for y in evenH[i+1:]:
        if fd(x,y)==2:
            assert cost(T244+[x,y],0)==0; activeH.append((x,y))
assert len(activeH)==735
orbsH=defaultdict(list)
for x,y in activeH: orbsH[canon_xy([3,29,x,y])].append((x,y))
assert sorted(map(len,orbsH.values()))==[105,630]
statsH=[]
for vals in orbsH.values():
    x,y=vals[0]; active=T244+[x,y]
    pool=[z for z in range(N) if par(z)==1 and all(fd(z,c)==5 for c in active) and cost(active+[z],0)<=7]
    best=max_extension_cost(active,pool,0,7,7)
    statsH.append((len(vals),len(pool),best))
assert sorted(statsH)==[(105,224,3),(630,244,4)]
# Seven odd isolates are required, but the exact cost-constrained maxima are 3,4.

print('CERTIFICATE PASSED')
print('A one-slack 00011 (2,2,4,4) neven=6: placements',pairsA,'min even cost',min(cntA))
print('B one-slack 00011 (2,4,4,4) neven=5: placements',pairsB,'min odd cost',min(cntB))
print('C 00000 (2,4,4,4) neven=5: active',len(activeC),'orbit stats',sorted(statsC))
print('D 00111 (2,3,3,2) neven=6: placements',pairsD,'min even cost',min(k[0] for k in cntD))
print('E 00011 (2,2,4,2) neven=5: placements',pairsE,'min odd cost',min(cntE))
print('F 00011 (4,4,4,2) neven=6: active placements',pairsF,'budget survivors',len(survF),'orbit stats',sorted(statsF))
print('G 00011 (2,2,4,4) neven=5: placements',pairsG,'min odd cost',min(cntG))
print('H 00000 (2,4,4,2) neven=5: active',len(activeH),'orbit stats',sorted(statsH))
print('CONCLUSION: eight additional canonical K=4 triangle+edge classes are impossible; 11 of the prior 19 remain.')
