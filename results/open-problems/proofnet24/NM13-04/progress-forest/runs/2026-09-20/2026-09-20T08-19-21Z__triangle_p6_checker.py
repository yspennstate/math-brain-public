#!/usr/bin/env python3
# NM13-04 / T07 exact checker, 2026-09-20.
# Restricted theorem:
#   G_{p,r} = K_3 join (p P6 disjoint_union r K1), p,r >= 0.
# Unit edge weights; uniform measure on all forests.
# Exact arithmetic only for every sign decision.

from itertools import combinations, permutations, product
from functools import lru_cache
import collections
import sympy as sp

def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp:
            mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)

TERMINAL_STATES=[
    canon((0,1,2)), canon((0,1,1)), canon((0,0,1)),
    canon((0,1,0)), canon((0,0,0))
]

def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]:
        return None
    la,lb=labels[a],labels[b]
    labels=[la if q==lb else q for q in labels]
    return canon(labels)

def introduce(labels):
    return canon(tuple(labels)+(max(labels,default=-1)+1,))

def forget(labels,idx):
    return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

@lru_cache(None)
def transfer_path(L, required_tuple=()):
    required=set(required_tuple)
    M=[[0]*5 for _ in range(5)]
    for si,tstate in enumerate(TERMINAL_STATES):
        dp={introduce(tstate):1}
        stage=[(('s',0,t),t,3) for t in range(3)]
        nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            for bits in product([0,1],repeat=3):
                if any((eid in required) and not bit for bit,(eid,_,__) in zip(bits,stage)):
                    continue
                cur=lab; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur2=union_part(cur,a,b)
                        if cur2 is None:
                            ok=False; break
                        cur=cur2
                if ok: nd[cur]+=cnt
        dp=nd
        for i in range(1,L):
            nd=collections.defaultdict(int)
            stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product([0,1],repeat=4):
                    if any((eid in required) and not bit for bit,(eid,_,__) in zip(bits,stage)):
                        continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur2=union_part(cur,a,b)
                            if cur2 is None:
                                ok=False; break
                            cur=cur2
                    if ok: nd[forget(cur,3)]+=cnt
            dp=nd
        for lab,cnt in dp.items():
            sj=TERMINAL_STATES.index(forget(lab,3))
            M[si][sj]+=cnt
    return sp.Matrix(M)

S=transfer_path(1)
N=S-4*sp.eye(5)
P6=transfer_path(6)
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert P6==23396*sp.eye(5)+37512*N+25562*N**2

class DSU:
    def __init__(self,n):
        self.p=list(range(n)); self.r=[0]*n
    def find(self,a):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]; a=self.p[a]
        return a
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        if self.r[a]<self.r[b]: a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]: self.r[a]+=1
        return True

def state_index(d):
    r=[d.find(i) for i in range(3)]
    if r[0]==r[1]==r[2]: return 4
    if r[1]==r[2]: return 1
    if r[0]==r[1]: return 2
    if r[0]==r[2]: return 3
    return 0

def triangle_vector(required=frozenset()):
    E=[(0,1),(0,2),(1,2)]
    out=[0]*5
    for mask in range(8):
        if any(not ((mask>>i)&1) for i in required): continue
        d=DSU(3); ok=True
        for i,(aa,bb) in enumerate(E):
            if (mask>>i)&1 and not d.union(aa,bb):
                ok=False; break
        if ok: out[state_index(d)]+=1
    return sp.Matrix([out])

TV={frozenset(req):triangle_vector(frozenset(req))
    for req in [(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]}
q=TV[frozenset()]
assert list(q)==[1,1,1,1,3]
one=sp.ones(5,1)

x,z=sp.symbols('x z', integer=True, nonnegative=True)
a=sp.Rational(37512,23396)
c=sp.Rational(25562,23396)
s=sp.Rational(1,4)
u=a*x+s*z
v=c*x+sp.Rational(1,2)*x*(x-1)*a*a+sp.Rational(1,2)*z*(z-1)*s*s+x*z*a*s
U=sp.eye(5)+u*N+v*N**2

p,r=sp.symbols('p r', integer=True, nonnegative=True)
up=a*p+s*r
vp=c*p+sp.Rational(1,2)*p*(p-1)*a*a+sp.Rational(1,2)*r*(r-1)*s*s+p*r*a*s
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((q*Up*one)[0])

def edgekey(a,b): return tuple(sorted((a,b),key=repr))
Gedges=[]
for i,j in [(0,1),(0,2),(1,2)]:
    Gedges.append(edgekey(('T',i),('T',j)))
for qid in range(2):
    for i in range(6):
        for t in range(3): Gedges.append(edgekey(('A',qid,i),('T',t)))
    for i in range(5):
        Gedges.append(edgekey(('A',qid,i),('A',qid,i+1)))
for qid in range(2):
    for t in range(3): Gedges.append(edgekey(('O',qid,0),('T',t)))
Gedges=list(dict.fromkeys(Gedges))
print("edges",len(Gedges))

auts=[]
for tp in permutations(range(3)):
    for Ap in permutations(range(2)):
        for Afl in product([0,1],repeat=2):
            for Op in permutations(range(2)):
                mp={('T',t):('T',tp[t]) for t in range(3)}
                for qid in range(2):
                    nq=Ap[qid]
                    for i in range(6): mp[('A',qid,i)]=('A',nq,5-i if Afl[qid] else i)
                for qid in range(2): mp[('O',qid,0)]=('O',Op[qid],0)
                auts.append(mp)

pairs=[tuple(sorted((e,f),key=repr)) for e,f in combinations(Gedges,2)]
seen=set(); orbits=[]
for pair in pairs:
    if pair in seen: continue
    orb=set()
    for mp in auts:
        e,f=pair
        e2=edgekey(mp[e[0]],mp[e[1]]); f2=edgekey(mp[f[0]],mp[f[1]])
        orb.add(tuple(sorted((e2,f2),key=repr)))
    seen |= orb; orbits.append(orb)
print("pairs",len(pairs),"orbits",len(orbits))

def core_idx(e):
    a0,b0=e
    if a0[0]=='T' and b0[0]=='T':
        return {(0,1):0,(0,2):1,(1,2):2}[tuple(sorted((a0[1],b0[1])))]
    return None

def localize(e):
    ci=core_idx(e)
    if ci is not None: return ('T',0,ci)
    a0,b0=e
    if a0[0]=='T': t=a0[1]; qv=b0
    elif b0[0]=='T': t=b0[1]; qv=a0
    else:
        assert a0[0]==b0[0] and a0[1]==b0[1]
        return (a0[0],a0[1],('i',min(a0[2],b0[2]),max(a0[2],b0[2])))
    return (qv[0],qv[1],('s',qv[2],t))

def layer_matrix(kind,req):
    req=tuple(sorted(req,key=repr))
    if kind=='A': return P6 if not req else transfer_path(6,req)
    if kind=='O': return S if not req else transfer_path(1,req)
    raise AssertionError(kind)

def quantity(pair,required):
    treq=[]; layers={}
    for e in pair:
        kind,idx,loc=localize(e)
        if kind=='T':
            if e in required: treq.append(loc)
        else:
            layers.setdefault((kind,idx),[]).append((e,loc))
    row=TV[frozenset(treq)]
    for lid,els in sorted(layers.items(),key=repr):
        req=[loc for e,loc in els if e in required]
        row=row*layer_matrix(lid[0],req)
    return sp.expand((row*U*one)[0])

def rayleigh_poly(pair):
    e,f=pair
    I=quantity(pair,set())
    Ie=quantity(pair,{e})
    If=quantity(pair,{f})
    Ief=quantity(pair,{e,f})
    return sp.Poly(sp.expand(Ie*If-I*Ief),x,z,domain=sp.QQ)

def newton_coeffs(poly):
    expr=poly.as_expr(); D=poly.total_degree(); ans={}
    for i in range(D+1):
        for j in range(D+1-i):
            cc=sp.Rational(0)
            for aa0 in range(i+1):
                for bb0 in range(j+1):
                    cc += (-1)**((i-aa0)+(j-bb0))*sp.binomial(i,aa0)*sp.binomial(j,bb0)*expr.subs({x:aa0,z:bb0})
            cc=sp.factor(cc)
            if cc: ans[(i,j)]=cc
    return ans

def desc(e):
    ci=core_idx(e)
    if ci is not None: return ['T01','T02','T12'][ci]
    a0,b0=e
    if a0[0]=='T': t=a0[1]; qv=b0
    elif b0[0]=='T': t=b0[1]; qv=a0
    else: return f"{a0[0]}{a0[1]}:h{min(a0[2],b0[2])}{max(a0[2],b0[2])}"
    return f"{qv[0]}{qv[1]}:v{qv[2]}-T{t}"

# Exact orbit classification.
bad=[]; zero_constant=[]; min_constant=None; min_positive_newton=None
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]
    poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    constant=sp.factor(poly.as_expr().subs({x:0,z:0}))
    if constant==0:
        zero_constant.append((idx,desc(rep[0]),desc(rep[1])))
    neg=[(k,cc) for k,cc in nc.items() if cc<0]
    if neg:
        bad.append((idx,rep,poly,nc))
    else:
        assert constant>0
        min_constant=constant if min_constant is None else min(min_constant,constant)
        pos=[cc for cc in nc.values() if cc>0]
        if pos:
            mm=min(pos)
            min_positive_newton=mm if min_positive_newton is None else min(min_positive_newton,mm)

assert len(Gedges)==55
assert len(pairs)==1485
assert len(orbits)==93
assert len(seen)==1485
assert len(bad)==4
assert zero_constant==[]
assert min_constant==2
assert min_positive_newton==sp.Rational(1,8)
bad_desc=[(q0[0],desc(q0[1][0]),desc(q0[1][1])) for q0 in bad]
assert bad_desc==[
    (19,'A0:v0-T0','A0:v3-T1'),
    (21,'A0:v0-T0','A0:v4-T1'),
    (23,'A0:v0-T0','A0:v5-T1'),
    (46,'A0:v1-T0','A0:v4-T1'),
]

# Exact two-corner certificates for the four exceptional quartics.
# If Q(A+X,Z) and Q(X,B+Z) have all coefficients positive, and Q is
# positive on 0<=x<A, 0<=z<B, then Q>0 on all Z_{\ge0}^2.
certspec=[(2,11),(9,52),(24,149),(2,13)]
X,Zs=sp.symbols('X Zs', integer=True, nonnegative=True)
cert_rows=[]
for (idx,rep,poly,nc),(A0,B0) in zip(bad,certspec):
    neg=sorted((k,cc) for k,cc in nc.items() if cc<0)
    den=sp.ilcm(*[int(sp.denom(cc)) for cc in poly.coeffs()])
    Qexpr=sp.Poly(sp.expand(den*poly.as_expr()),x,z,domain=sp.ZZ).as_expr()
    Qx=sp.Poly(sp.expand(Qexpr.subs({x:X+A0,z:Zs})),X,Zs,domain=sp.ZZ)
    Qz=sp.Poly(sp.expand(Qexpr.subs({x:X,z:Zs+B0})),X,Zs,domain=sp.ZZ)
    assert len(Qx.terms())==15 and len(Qz.terms())==15
    assert all(cc>0 for cc in Qx.coeffs())
    assert all(cc>0 for cc in Qz.coeffs())
    box=[(int(Qexpr.subs({x:i,z:j})),i,j) for i in range(A0) for j in range(B0)]
    assert box and min(v for v,_,_ in box)>0
    bmin=min(box)
    cert_rows.append((idx,desc(rep[0]),desc(rep[1]),neg,den,Qexpr,A0,B0,
                      min(Qx.coeffs()),min(Qz.coeffs()),len(box),bmin))

# Closed total forest-count formula for triangle-seeded P6/singleton family.
Ztarget=(4221450432*p**2+1316446128*p*r+8143148400*p+
         102632403*r**2+1265799637*r+3831609712)/sp.Integer(547372816)
assert sp.simplify(Znorm-Ztarget)==0

# Independent all-pairs physical sanity check for K3 join P6.
# This does NOT reuse the transfer matrices. It uses the identity
# F(H)=sum_{set partitions pi of V} prod_{B in pi} tau(H[B]),
# evaluating tau by the exact Matrix-Tree theorem. Required edges are
# handled by graph contraction (parallel edges retained).
def forest_count_multigraph(n, edgelist):
    mult=[[0]*n for _ in range(n)]
    for aa,bb in edgelist:
        mult[aa][bb]+=1; mult[bb][aa]+=1
    tau=[0]*(1<<n)
    for mask in range(1,1<<n):
        if mask & (mask-1)==0:
            tau[mask]=1
            continue
        verts=[i for i in range(n) if (mask>>i)&1]
        kk=len(verts)
        L=[[0]*kk for _ in range(kk)]
        for ii,uu in enumerate(verts):
            deg=0
            for jj,vv in enumerate(verts):
                if ii==jj: continue
                w=mult[uu][vv]
                if w:
                    L[ii][jj]-=w; deg+=w
            L[ii][ii]=deg
        minor=sp.Matrix([row[:-1] for row in L[:-1]])
        tau[mask]=int(minor.det())
    @lru_cache(None)
    def F(mask):
        if mask==0: return 1
        vv=(mask & -mask).bit_length()-1
        rest=mask^(1<<vv)
        total=0; sub=rest
        while True:
            B=sub | (1<<vv)
            tv=tau[B]
            if tv:
                total += tv*F(mask^B)
            if sub==0: break
            sub=(sub-1)&rest
        return total
    return F((1<<n)-1)

def contract_graph(n, edgelist, req_indices):
    parent=list(range(n))
    def find(aa):
        while parent[aa]!=aa:
            parent[aa]=parent[parent[aa]]
            aa=parent[aa]
        return aa
    def union(aa,bb):
        aa,bb=find(aa),find(bb)
        if aa==bb: return False
        parent[bb]=aa
        return True
    # Required set is acyclic in every use below (one or two distinct edges).
    for idx in req_indices:
        aa,bb=edgelist[idx]
        assert union(aa,bb)
    roots={}
    for vv in range(n):
        rr=find(vv)
        if rr not in roots: roots[rr]=len(roots)
    newedges=[]
    req=set(req_indices)
    for i,(aa,bb) in enumerate(edgelist):
        if i in req: continue
        aa2,bb2=roots[find(aa)],roots[find(bb)]
        if aa2!=bb2:
            if aa2>bb2: aa2,bb2=bb2,aa2
            newedges.append((aa2,bb2))
    return len(roots),tuple(sorted(newedges))

def physical_triangle_p6():
    ed=[(0,1),(0,2),(1,2)]
    vs=list(range(3,9))
    for vv in vs:
        for t in range(3): ed.append((t,vv))
    ed += [(vs[i],vs[i+1]) for i in range(5)]
    return 9,ed

nphys,ep=physical_triangle_p6()
assert len(ep)==26
Zphys=forest_count_multigraph(nphys,tuple(ep))
assert Zphys==692264
assert Zphys==int((q*P6*one)[0])
onecnt=[]
for i in range(len(ep)):
    nn,ee=contract_graph(nphys,ep,(i,))
    onecnt.append(forest_count_multigraph(nn,ee))
gaps=[]
for i,j in combinations(range(len(ep)),2):
    nn,ee=contract_graph(nphys,ep,(i,j))
    two=forest_count_multigraph(nn,ee)
    gaps.append((onecnt[i]*onecnt[j]-Zphys*two,i,j,two))
mingap=min(gaps)
maxgap=max(gaps)
assert mingap==(23243040,21,25,62636)
assert maxgap[0]==14406637792
assert maxgap[1:3]==(19,20)

print("P6 transfer =",P6)
print("N^3=0 and P6 decomposition: PASS")
print("triangle seed =",list(q))
print("normalized total forest count =",Znorm)
print("witness edges/pairs/orbits = 55 / 1485 / 93")
print("regular Newton-positive orbits = 89/93")
print("minimum regular constant =",min_constant)
print("minimum positive Newton coefficient =",min_positive_newton)
for row in cert_rows:
    idx,d1,d2,neg,den,Qexpr,A0,B0,minx,minz,nbox,bmin=row
    print("EXCEPTION",idx,d1,d2)
    print("  negative Newton =",neg)
    print("  denominator =",den)
    print("  Q =",Qexpr)
    print(f"  shift ({A0},0): all 15 coefficients positive; min={minx}")
    print(f"  shift (0,{B0}): all 15 coefficients positive; min={minz}")
    print(f"  finite box {A0}x{B0}: {nbox} values; min={bmin[0]} at ({bmin[1]},{bmin[2]})")
print("INDEPENDENT_MATRIX_TREE K3_join_P6: n=9 m=26 Z=%d min_gap=%d edges=%s,%s max_gap=%d edges=%s,%s" %
      (Zphys,mingap[0],ep[mingap[1]],ep[mingap[2]],maxgap[0],ep[maxgap[1]],ep[maxgap[2]]))
print("ALL_EXACT_CHECKS_PASS")
