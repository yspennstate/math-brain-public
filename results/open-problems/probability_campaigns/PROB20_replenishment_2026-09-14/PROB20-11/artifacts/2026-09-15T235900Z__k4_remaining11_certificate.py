#!/usr/bin/env python3
"""PROB20-11 exact finite certificate: eliminate all eleven remaining K=4
triangle+disjoint-edge canonical states in the folded length-12 cube.

Standard-library only. Exact integer/bitset arithmetic. No floating point,
heuristic acceptance, timeout, or solver status is used as infeasibility.
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
        mx=triple_max_centers(a,b,c)[half]; ac=tri_actual(a,b,c)[half]
        assert ac<=mx; ans += mx-ac
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

def hist_rows(rows):
    h=[0]*(1<<len(rows))
    for col in range(12):
        p=0
        for i,r in enumerate(rows): p|=((r>>col)&1)<<i
        h[p]+=1
    return tuple(h)

PERM4=list(permutations(range(4)))
def canon_active5(cs):
    best=None
    for oi,o in enumerate(cs):
        rem=[c^o for j,c in enumerate(cs) if j!=oi]
        for pm in PERM4:
            h=hist_rows([rem[i] for i in pm])
            for flip in range(16):
                q=tuple(h[p^flip] for p in range(16))
                if best is None or q<best: best=q
    return best

def canon_t222_edge(cs):
    best=None
    for oi in (0,1,2):
        o=cs[oi]; tr=[i for i in (0,1,2) if i!=oi]
        for trord in (tr,tr[::-1]):
            for eord in ((3,4),(4,3)):
                h=hist_rows([cs[i]^o for i in trord+list(eord)])
                for flip in range(16):
                    q=tuple(h[p^flip] for p in range(16))
                    if best is None or q<best: best=q
    return best

def even_candidates(active):
    ev=[c for c in active if par(c)==0]; od=[c for c in active if par(c)==1]
    return [z for z in range(N) if par(z)==0 and z not in active
            and all(fd(z,e)==6 for e in ev) and all(fd(z,o)==5 for o in od)]

def extend_examples(active,cand,need,b0,b1=None):
    out=[]; best=0
    def rec(cs,P,depth):
        nonlocal best
        best=max(best,depth)
        if depth==need:
            out.append(tuple(cs[len(active):])); return
        if depth+len(P)<need: return
        while P:
            i=P.pop(); z=cand[i]; ncs=cs+[z]
            if cost(ncs,0)<=b0 and (b1 is None or cost(ncs,1)<=b1):
                rec(ncs,[j for j in P if fd(cand[j],z)==6],depth+1)
    rec(list(active),list(range(len(cand))),0)
    return best,out

T244=[0,3,29]; T224=[0,3,12]; T222=[0,3,5]
assert tuple(fd(T244[i],T244[j]) for i in range(3) for j in range(i+1,3))==(2,4,4)
assert tuple(fd(T224[i],T224[j]) for i in range(3) for j in range(i+1,3))==(2,2,4)
assert tuple(fd(T222[i],T222[j]) for i in range(3) for j in range(i+1,3))==(2,2,2)

odd244=[x for x in range(N) if par(x)==1 and all(fd(x,c)==5 for c in T244)]
odd224=[x for x in range(N) if par(x)==1 and all(fd(x,c)==5 for c in T224)]
odd222=[x for x in range(N) if par(x)==1 and all(fd(x,c)==5 for c in T222)]
evfar224=[x for x in range(N) if par(x)==0 and x not in T224 and all(fd(x,c)==6 for c in T224)]
evfar222=[x for x in range(N) if par(x)==0 and x not in T222 and all(fd(x,c)==6 for c in T222)]
assert (len(odd244),len(odd224),len(odd222))==(518,560,588)
assert len(evfar224)==140 and len(evfar222)==126

# 1: 00011 (2,4,4,2), neven=6, U=(1031,1058)
s1=[]; pairs=0
for i,x in enumerate(odd244):
    for y in odd244[i+1:]:
        if fd(x,y)==2:
            pairs+=1; ce=cost(T244+[x,y],0)
            if ce<=7: s1.append((x,y,ce))
assert pairs==10878 and len(s1)==2058
orb1=defaultdict(list)
for x,y,ce in s1: orb1[canon_active5(T244+[x,y])].append((x,y,ce))
assert sorted((len(v),v[0][2]) for v in orb1.values())==[(63,3),(105,5),(105,7),(210,7),(315,5),(630,6),(630,7)]
st1=[]
for vals in orb1.values():
    x,y,ce=vals[0]; active=T244+[x,y]
    cand=[z for z in even_candidates(active) if cost(active+[z],0)<=7]
    best,exs=extend_examples(active,cand,3,7)
    oc=[cost(active+list(t),1) for t in exs]
    st1.append((len(vals),ce,len(cand),best,len(exs),min(oc) if oc else None,max(oc) if oc else None))
assert sorted(st1)==[(63,3,30,2,0,None,None),(105,5,30,2,0,None,None),(105,7,22,2,0,None,None),(210,7,30,3,108,48,50),(315,5,32,3,168,38,45),(630,6,33,3,144,40,47),(630,7,34,3,186,45,51)]
assert all(n==0 or lo>34 for _,_,_,_,n,lo,hi in st1)

# 2: 00000 (2,2,4,4), neven=5, U=(1033,1039)
c2=Counter(); p2=0
for i,x in enumerate(evfar224):
    for y in evfar224[i+1:]:
        if fd(x,y)==4:
            p2+=1; cs=T224+[x,y]; c2[(cost(cs,0),cost(cs,1))]+=1
assert p2==4830 and c2==Counter({(0,28):2520,(0,22):2240,(0,16):70})
assert min(k[1] for k in c2)>15

# 3: 00011 (2,2,2,4), neven=6, U=(1035,1094)
s3=[]; p3=0
for i,x in enumerate(odd222):
    for y in odd222[i+1:]:
        if fd(x,y)==4:
            p3+=1; ce=cost(T222+[x,y],0); co=cost(T222+[x,y],1)
            if ce<=11: s3.append((x,y,ce,co))
assert p3==84294 and len(s3)==2394
orb3=defaultdict(list)
for x,y,ce,co in s3: orb3[canon_t222_edge(T222+[x,y])].append((x,y,ce,co))
assert sorted((len(v),v[0][2],v[0][3]) for v in orb3.values())==[(504,5,9),(1890,7,8)]
st3=[]
for vals in orb3.values():
    x,y,ce,co=vals[0]; active=T222+[x,y]
    cand=[z for z in even_candidates(active) if cost(active+[z],0)<=11]
    best,exs=extend_examples(active,cand,3,11)
    oc=[cost(active+list(t),1) for t in exs]
    st3.append((len(vals),ce,co,len(cand),best,len(exs),min(oc) if oc else None,max(oc) if oc else None))
assert sorted(st3)==[(504,5,9,30,2,0,None,None),(1890,7,8,45,3,48,75,75)]

# 4: 00011 (2,2,4,2), neven=6, U=(1035,1070)
s4=[]; p4=0
for i,x in enumerate(odd224):
    for y in odd224[i+1:]:
        if fd(x,y)==2:
            p4+=1; ce=cost(T224+[x,y],0); co=cost(T224+[x,y],1)
            if ce<=11: s4.append((x,y,ce,co))
assert p4==12348 and len(s4)==2044
orb4=defaultdict(list)
for x,y,ce,co in s4: orb4[canon_active5(T224+[x,y])].append((x,y,ce,co))
assert sorted((len(v),v[0][2],v[0][3]) for v in orb4.values())==[(140,10,18),(224,5,9),(1680,8,12)]
st4=[]
for vals in orb4.values():
    x,y,ce,co=vals[0]; active=T224+[x,y]
    cand=[z for z in even_candidates(active) if cost(active+[z],0)<=11]
    best,exs=extend_examples(active,cand,3,11)
    oc=[cost(active+list(t),1) for t in exs]
    st4.append((len(vals),ce,co,len(cand),best,len(exs),min(oc) if oc else None,max(oc) if oc else None))
assert sorted(st4)==[(140,10,18,0,0,0,None,None),(224,5,9,60,1,0,None,None),(1680,8,12,43,3,456,57,64)]

# 5: 00001 (2,2,2,3), neven=5, U=(1042,1037)
c5=Counter(); p5=0
for x in evfar222:
    for y in odd222:
        if fd(x,y)==3:
            p5+=1; cs=T222+[x,y]; c5[(cost(cs,0),cost(cs,1))]+=1
assert p5==18396
assert c5==Counter({(8,29):7560,(4,26):5040,(1,24):3780,(8,26):1890,(4,20):126})
assert min(k[1] for k in c5)>13

# 6: 00000 (2,2,4,2), neven=5, U=(1038,1040)
c6=Counter(); p6=0
for i,x in enumerate(evfar224):
    for y in evfar224[i+1:]:
        if fd(x,y)==2:
            p6+=1; cs=T224+[x,y]; c6[(cost(cs,0),cost(cs,1))]+=1
assert p6==1260 and c6==Counter({(0,40):1120,(0,28):140})
assert min(k[1] for k in c6)>16

# 7: 00011 (2,2,2,2), neven=5, U=(1078,1044)
s7=[]; p7=0
for i,x in enumerate(odd222):
    for y in odd222[i+1:]:
        if fd(x,y)==2:
            p7+=1; ce=cost(T222+[x,y],0); co=cost(T222+[x,y],1)
            if ce<=54 and co<=20: s7.append((x,y,ce,co))
assert p7==13104 and len(s7)==2016
orb7=defaultdict(list)
for x,y,ce,co in s7: orb7[canon_t222_edge(T222+[x,y])].append((x,y,ce,co))
assert sorted((len(v),v[0][2],v[0][3]) for v in orb7.values())==[(756,10,13),(1260,14,18)]
for vals in orb7.values():
    x,y,ce,co=vals[0]; active=T222+[x,y]
    cand=[z for z in even_candidates(active) if cost(active+[z],0)<=54 and cost(active+[z],1)<=20]
    assert len(cand)==0

# 8: 00011 (2,2,2,2), neven=6, U=(1045,1096)
s8=[]
for i,x in enumerate(odd222):
    for y in odd222[i+1:]:
        if fd(x,y)==2:
            ce=cost(T222+[x,y],0); co=cost(T222+[x,y],1)
            if ce<=21: s8.append((x,y,ce,co))
assert len(s8)==7686
orb8=defaultdict(list)
for x,y,ce,co in s8: orb8[canon_t222_edge(T222+[x,y])].append((x,y,ce,co))
assert sorted((len(v),v[0][2],v[0][3]) for v in orb8.values())==[(378,18,22),(756,10,13),(1260,14,18),(1512,18,22),(3780,19,27)]
st8=[]
for vals in orb8.values():
    x,y,ce,co=vals[0]; active=T222+[x,y]
    cand=[z for z in even_candidates(active) if cost(active+[z],0)<=21]
    best,exs=extend_examples(active,cand,3,21)
    oc=[cost(active+list(t),1) for t in exs]
    st8.append((len(vals),ce,co,len(cand),best,len(exs),min(oc) if oc else None,max(oc) if oc else None))
assert sorted(st8)==[(378,18,22,0,0,0,None,None),(756,10,13,55,3,120,82,82),(1260,14,18,61,3,234,84,88),(1512,18,22,40,2,0,None,None),(3780,19,27,48,3,396,88,92)]
assert all(n==0 or lo>72 for *_,n,lo,hi in st8)

# 9: 00011 (2,2,2,4), neven=5, U=(1059,1045)
s9=[]
for i,x in enumerate(odd222):
    for y in odd222[i+1:]:
        if fd(x,y)==4:
            ce=cost(T222+[x,y],0); co=cost(T222+[x,y],1)
            if ce<=35 and co<=21: s9.append((x,y,ce,co))
assert len(s9)==49329
orb9=defaultdict(list)
for x,y,ce,co in s9: orb9[canon_t222_edge(T222+[x,y])].append((x,y,ce,co))
assert len(orb9)==9
assert sorted((len(v),v[0][2],v[0][3]) for v in orb9.values())==[(315,17,15),(504,5,9),(1890,7,8),(3780,12,14),(3780,15,17),(5040,14,12),(7560,15,19),(11340,14,17),(15120,18,20)]
for vals in orb9.values():
    x,y,ce,co=vals[0]; active=T222+[x,y]
    cand=[z for z in even_candidates(active) if cost(active+[z],0)<=35 and cost(active+[z],1)<=21]
    assert len(cand)==0

# 10: 00000 (2,2,2,4), neven=5, U=(1046,1056)
s10=[]; c10=Counter(); p10=0
for i,x in enumerate(evfar222):
    for y in evfar222[i+1:]:
        if fd(x,y)==4:
            p10+=1; cs=T222+[x,y]; cc=(cost(cs,0),cost(cs,1)); c10[cc]+=1
            if cc[0]<=22 and cc[1]<=32: s10.append((x,y,*cc))
assert p10==4095 and c10==Counter({(0,41):3780,(0,28):315}) and len(s10)==315
orb10=defaultdict(list)
for x,y,ce,co in s10: orb10[canon_t222_edge(T222+[x,y])].append((x,y,ce,co))
assert len(orb10)==1 and len(next(iter(orb10.values())))==315
x,y,ce,co=next(iter(orb10.values()))[0]; active=T222+[x,y]
pool10=[z for z in range(N) if par(z)==1 and all(fd(z,e)==5 for e in active)
        and cost(active+[z],0)<=22 and cost(active+[z],1)<=32]
assert len(pool10)==0

# 11: 00000 (2,2,2,2), neven=5, U=(1051,1057)
c11=Counter(); p11=0
for i,x in enumerate(evfar222):
    for y in evfar222[i+1:]:
        if fd(x,y)==2:
            p11+=1; cs=T222+[x,y]; c11[(cost(cs,0),cost(cs,1))]+=1
assert p11==1260 and c11==Counter({(0,55):1260})
assert min(k[1] for k in c11)>33

print('CERTIFICATE PASSED')
print('All 11 remaining K=4 triangle+edge classes eliminated exactly.')
print('Therefore every hypothetical 12-center folded radius-3 cover has at least 5 close pairs.')
print('State1 orbit stats:', sorted(st1))
print('State3 orbit stats:', sorted(st3))
print('State4 orbit stats:', sorted(st4))
print('State8 orbit stats:', sorted(st8))