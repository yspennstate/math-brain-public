from itertools import combinations, product, permutations
from functools import lru_cache
from fractions import Fraction
import collections

# NM13-04 / T07 exact checker.
# Extends the triangle-seeded response-strip theorem from right linear forests
# with components P_1,...,P_15 to arbitrary disjoint unions of those paths
# together with an arbitrary number of right-side triangles K_3.
# All graph edge weights are one.

def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp:
            mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)

ST=[canon((0,1,2)), canon((0,1,1)), canon((0,0,1)),
    canon((0,1,0)), canon((0,0,0))]

def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]:
        return None
    la,lb=labels[a],labels[b]
    return canon([la if q==lb else q for q in labels])

def introduce(labels):
    return canon(tuple(labels)+(max(labels,default=-1)+1,))

def forget(labels,idx):
    return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

@lru_cache(None)
def transfer_path(L, reqt=()):
    req=set(reqt); M=[[0]*5 for _ in range(5)]
    for si,ts in enumerate(ST):
        dp={introduce(ts):1}
        stage=[(('s',0,t),t,3) for t in range(3)]
        nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            for bits in product((0,1), repeat=3):
                if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)):
                    continue
                cur=lab; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur=union_part(cur,a,b)
                        if cur is None:
                            ok=False; break
                if ok:
                    nd[cur]+=cnt
        dp=nd
        for i in range(1,L):
            nd=collections.defaultdict(int)
            stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product((0,1),repeat=4):
                    if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)):
                        continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur=union_part(cur,a,b)
                            if cur is None:
                                ok=False; break
                    if ok:
                        nd[forget(cur,3)]+=cnt
            dp=nd
        for lab,cnt in dp.items():
            M[si][ST.index(forget(lab,3))]+=cnt
    return tuple(tuple(r) for r in M)

def transfer_component(m, internal_edges, reqt=()):
    req=set(reqt)
    edges=[('s',i,t) for i in range(m) for t in range(3)]
    edges += [('i',min(a,b),max(a,b)) for a,b in internal_edges]
    M=[[0]*5 for _ in range(5)]
    for si,ts in enumerate(ST):
        for bits in product((0,1), repeat=len(edges)):
            chosen=[e for e,b in zip(edges,bits) if b]
            if not req.issubset(chosen):
                continue
            par=list(range(3+m))
            def fd(x):
                while par[x]!=x:
                    par[x]=par[par[x]]; x=par[x]
                return x
            def un(a,b):
                a,b=fd(a),fd(b)
                if a==b:
                    return False
                par[b]=a
                return True
            for a in range(3):
                for b in range(a):
                    if ts[a]==ts[b]:
                        un(a,b)
            ok=True
            for e in chosen:
                if e[0]=='s':
                    _,i,t=e; a=t; b=3+i
                else:
                    _,i,j=e; a=3+i; b=3+j
                if not un(a,b):
                    ok=False; break
            if not ok:
                continue
            state=canon(tuple(fd(i) for i in range(3)))
            M[si][ST.index(state)]+=1
    return tuple(tuple(r) for r in M)

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(5))
                       for j in range(5)) for i in range(5))
def rm(r,M):
    return tuple(sum(r[k]*M[k][j] for k in range(5)) for j in range(5))
def rv(r,c):
    return sum(r[i]*c[i] for i in range(5))

I=tuple(tuple(1 if i==j else 0 for j in range(5)) for i in range(5))
S=transfer_path(1)
N=tuple(tuple(S[i][j]-4*I[i][j] for j in range(5)) for i in range(5))
N2=mm(N,N)
assert mm(N2,N)==tuple(tuple(0 for _ in range(5)) for _ in range(5))
one=(1,1,1,1,1)
None1=tuple(rv(N[i],one) for i in range(5))
None2=tuple(rv(N2[i],one) for i in range(5))

def decompose(M):
    A=M[0][0]
    B=M[0][1]
    C=Fraction(M[0][4]-B,6)
    for i in range(5):
        for j in range(5):
            assert Fraction(M[i][j]) == A*I[i][j]+B*N[i][j]+C*N2[i][j]
    return Fraction(A),Fraction(B),C

def rho_of(M):
    A,B,C=decompose(M)
    a=B/A; c=C/A
    return (a*a/2-c)/a

# Triangle core seed K_3.
CORE=[('c',0,1),('c',0,2),('c',1,2)]
def qcore(req=()):
    req={tuple(sorted(e)) for e in req}
    tri=[(0,1),(0,2),(1,2)]
    counts=[0]*5
    for bits in product((0,1), repeat=3):
        chosen=[tri[i] for i,b in enumerate(bits) if b]
        if not req.issubset(chosen):
            continue
        if len(chosen)==3:
            continue
        par=list(range(3))
        def fd(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        def un(a,b):
            a,b=fd(a),fd(b)
            if a!=b:
                par[b]=a
        for a,b in chosen:
            un(a,b)
        counts[ST.index(canon(tuple(fd(i) for i in range(3))))]+=1
    return tuple(counts)

Q0=qcore()
assert Q0==(1,1,1,1,3)

# New right component: triangle C_3=K_3, all three vertices joined to all terminals.
RINT=((0,1),(0,2),(1,2))
REDGES=[('s',i,t) for i in range(3) for t in range(3)] + [('i',i,j) for i,j in RINT]

@lru_cache(None)
def triM(reqt=()):
    return transfer_component(3,RINT,reqt)

Ttri=triM(())
Atri,Btri,Ctri=decompose(Ttri)
assert (Atri,Btri,Ctri)==(178,144,41)
rho_tri=rho_of(Ttri)

# Recompute the predecessor strip endpoint rho_15 exactly.
P15=transfer_path(15)
A15,B15,C15=decompose(P15)
assert (A15,B15,C15)==(136344403840,550341138496,Fraction(3134382731200,3))
rho15=rho_of(P15)
assert rho15==Fraction(13162845795778912063,109915919585249991540)
assert rho15 < rho_tri < Fraction(1,8)

# Exact margins showing that arbitrary unmarked right triangles do not widen
# the predecessor response strip.
print("T_C3 = 178 I + 144 N + 41 N^2: PASS")
print("rho_C3 =",rho_tri)
print("rho_15 =",rho15)
print("rho_C3-rho_15 =",rho_tri-rho15)
print("1/8-rho_C3 =",Fraction(1,8)-rho_tri)
print("triangle response lies strictly inside predecessor strip: PASS")

PERMS=list(permutations(range(3)))

def edges_path(L):
    return [('s',i,t) for i in range(L) for t in range(3)] + [('i',i,i+1) for i in range(L-1)]

def tcore(e,p):
    _,a,b=e; a,b=p[a],p[b]
    return ('c',min(a,b),max(a,b))

def ttri(e,tp,rp):
    k,a,b=e
    if k=='s':
        return ('s',rp[a],tp[b])
    a,b=rp[a],rp[b]
    return ('i',min(a,b),max(a,b))

def tpath(e,L,tp,rev):
    k,a,b=e
    if k=='s':
        return ('s',L-1-a if rev else a,tp[b])
    i,j=a,b
    if rev:
        i,j=L-1-j,L-1-i
    return ('i',i,j)

def key_ct(c,e):
    return min(((tcore(c,tp),ttri(e,tp,rp))
                for tp in PERMS for rp in PERMS),key=repr)

def key_same_tri(pair):
    return min((tuple(sorted((ttri(pair[0],tp,rp),ttri(pair[1],tp,rp)),key=repr))
                for tp in PERMS for rp in PERMS),key=repr)

def key_cross_tri(e,f):
    return min((tuple(sorted((ttri(e,tp,r1),ttri(f,tp,r2)),key=repr))
                for tp in PERMS for r1 in PERMS for r2 in PERMS),key=repr)

def key_tri_path(e,L,f):
    return min(((ttri(e,tp,rp),tpath(f,L,tp,rev))
                for tp in PERMS for rp in PERMS for rev in (0,1)),key=repr)

def new_reps(maxL=15):
    out=[]
    seen={}
    for c in CORE:
        for e in REDGES:
            seen.setdefault(key_ct(c,e),('ct',0,3,c,e))
    out += list(seen.values())

    seen={}
    for pair in combinations(REDGES,2):
        seen.setdefault(key_same_tri(pair),('ttsame',3,3,pair[0],pair[1]))
    out += list(seen.values())

    seen={}
    for e in REDGES:
        for f in REDGES:
            seen.setdefault(key_cross_tri(e,f),('ttcross',3,3,e,f))
    out += list(seen.values())

    for L in range(1,maxL+1):
        seen={}
        for e in REDGES:
            for f in edges_path(L):
                seen.setdefault(key_tri_path(e,L,f),('tp',3,L,e,f))
        out += list(seen.values())
    return out

@lru_cache(None)
def pathM(L,reqt=()):
    return transfer_path(L,reqt)

def triple(row):
    return (rv(row,one),rv(row,None1),rv(row,None2))

def quantity(rep,mask):
    typ,L,M,e,f=rep
    if typ=='ct':
        req=[]
        if mask&1:
            req.append((e[1],e[2]))
        row=qcore(req)
        row=rm(row,triM((f,)) if mask&2 else Ttri)
    elif typ=='ttsame':
        row=Q0
        if mask==0:
            mat=Ttri
        elif mask==1:
            mat=triM((e,))
        elif mask==2:
            mat=triM((f,))
        else:
            mat=triM(tuple(sorted((e,f),key=repr)))
        row=rm(row,mat)
    elif typ=='ttcross':
        row=Q0
        row=rm(row,triM((e,)) if mask&1 else Ttri)
        row=rm(row,triM((f,)) if mask&2 else Ttri)
    elif typ=='tp':
        row=Q0
        row=rm(row,triM((e,)) if mask&1 else Ttri)
        row=rm(row,pathM(M,(f,)) if mask&2 else pathM(M))
    else:
        raise AssertionError
    return triple(row)

def qcoeff(rep):
    A,Ie,If,Ief=[quantity(rep,m) for m in range(4)]
    mons=((0,0),(1,0),(0,1))
    def mul(a,b):
        d=collections.defaultdict(int)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=x*y
        return d
    p=mul(Ie,If); m=mul(A,Ief)
    for k,z in m.items():
        p[k]-=z
    return {k:z for k,z in p.items() if z}

# Substitute v=u^2/2-hu. Each c_j(h) is quadratic at worst.
def strip_coeffs(q):
    c=[[Fraction(0),Fraction(0),Fraction(0)] for _ in range(5)]
    for (iu,iv),coef in q.items():
        coef=Fraction(coef)
        if iv==0:
            c[iu][0]+=coef
        elif iv==1:
            c[iu+2][0]+=coef/2
            c[iu+1][1]-=coef
        elif iv==2:
            c[iu+4][0]+=coef/4
            c[iu+3][1]-=coef
            c[iu+2][2]+=coef
        else:
            raise AssertionError
    return [tuple(z) for z in c]

def peval(p,x):
    return p[0]+p[1]*x+p[2]*x*x

def bernstein2(p,lo,hi):
    d=hi-lo
    b0=peval(p,lo)
    b2=peval(p,hi)
    b1=b0+(p[1]+2*p[2]*lo)*d/2
    return b0,b1,b2

reps=new_reps(15)
counts=collections.Counter(rep[0] for rep in reps)
assert counts==collections.Counter({'tp':304,'ttsame':6,'ttcross':4,'ct':3})
assert len(reps)==317

lo,hi=rho15,Fraction(1,8)
min_const=None
min_pos=None
bad=[]
for rep in reps:
    sc=strip_coeffs(qcoeff(rep))
    bs=[]
    for p in sc:
        if p!=(0,0,0):
            bs.extend(bernstein2(p,lo,hi))
    const=sc[0][0]
    if not (const>0 and all(b>=0 for b in bs)):
        bad.append((rep,sc,bs))
        continue
    min_const=const if min_const is None else min(min_const,const)
    pos=[b for b in bs if b>0]
    if pos:
        mmn=min(pos)
        min_pos=mmn if min_pos is None else min(min_pos,mmn)

print("new local orbit counts =",dict(sorted(counts.items())))
print("new local orbits total =",len(reps))
print("Bernstein-positive new orbits =",len(reps)-len(bad))
print("new-orbit failures =",len(bad))
print("minimum new constant =",min_const)
print("minimum positive new Bernstein coefficient =",min_pos)
assert not bad
assert min_const==13052
assert min_pos==270
print("all 317 triangle-involving local response polynomials are positive on predecessor strip: PASS")

# Independent brute-force sanity check on the smallest noncomplete mixed example
# K3 join (K3 disjoint union K1), which has 7 vertices and 18 edges.
gedges=[(0,1),(0,2),(1,2)]
for v in (3,4,5,6):
    for t in (0,1,2):
        gedges.append((t,v))
gedges += [(3,4),(3,5),(4,5)]
assert len(gedges)==18

Z=0
onecnt=[0]*18
twocnt=[[0]*18 for _ in range(18)]
for mask in range(1<<18):
    par=list(range(7)); rank=[0]*7; chosen=[]; ok=True
    def fd(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    for ei,(a,b) in enumerate(gedges):
        if not ((mask>>ei)&1):
            continue
        ra,rb=fd(a),fd(b)
        if ra==rb:
            ok=False; break
        if rank[ra]<rank[rb]:
            ra,rb=rb,ra
        par[rb]=ra
        if rank[ra]==rank[rb]:
            rank[ra]+=1
        chosen.append(ei)
    if not ok:
        continue
    Z+=1
    for i in chosen:
        onecnt[i]+=1
    for aa in range(len(chosen)):
        for bb in range(aa+1,len(chosen)):
            i,j=chosen[aa],chosen[bb]
            twocnt[i][j]+=1
            twocnt[j][i]+=1

row=rm(Q0,Ttri)
row=rm(row,S)
Ztransfer=rv(row,one)
assert Z==Ztransfer==14372
gaps=[]
for i in range(18):
    for j in range(i+1,18):
        gaps.append((onecnt[i]*onecnt[j]-Z*twocnt[i][j],i,j))
mn=min(gaps); mx=max(gaps)
assert mn[0]==82772 and mx[0]==8228516
print("bruteforce K3 join (K3 disjoint K1): forests =",Z)
print("bruteforce minimum Rayleigh gap =",mn[0],"edge_pair =",mn[1:])
print("bruteforce maximum Rayleigh gap =",mx[0],"edge_pair =",mx[1:])
print("independent brute-force sanity check: PASS")
print("ALL_EXACT_CHECKS_PASS")
