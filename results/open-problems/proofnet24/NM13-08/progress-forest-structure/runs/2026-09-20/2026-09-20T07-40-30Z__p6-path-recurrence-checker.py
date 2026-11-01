from itertools import combinations, permutations, product
from functools import lru_cache
import collections
import sympy as sp

# NM13-08 / T07 exact checker.
# Family F6_{p,r}=K_{3,6p+r} with p disjoint P6 paths and r isolated
# vertices inside the right side; the three left terminals are independent.
# All real edge weights are one.

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
                    if ok:
                        nd[forget(cur,3)]+=cnt
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
print("S(singleton)="); print(S)
print("P6 layer="); print(P6)
print("N^3=0: PASS")
print("P6 = 23396 I + 37512 N + 25562 N^2: PASS")

def all_partitions4():
    out=[]
    def rec(prefix,maxlab):
        if len(prefix)==4:
            out.append(tuple(prefix)); return
        for q in range(maxlab+2):
            rec(prefix+[q],max(maxlab,q))
    rec([0],0)
    return out
PART4=all_partitions4(); PI={p:i for i,p in enumerate(PART4)}
E=sp.zeros(15)
for p0 in PART4:
    i0=PI[p0]
    lab2=introduce(p0)
    stage=[(3,4),(0,4),(1,4),(2,4)]
    for bits in product([0,1],repeat=4):
        cur=lab2; ok=True
        for bit,(a,b) in zip(bits,stage):
            if bit:
                cur2=union_part(cur,a,b)
                if cur2 is None:
                    ok=False; break
                cur=cur2
        if ok:
            E[i0,PI[forget(cur,3)]]+=1

lam=sp.symbols('lam')
char=sp.factor(E.charpoly(lam).as_expr())
assert char==(lam-1)**5*(lam**2-6*lam+2)**5
Q=E**2-6*E+2*sp.eye(15)
assert (E-sp.eye(15))**2 * Q**3 == sp.zeros(15)
assert (E-sp.eye(15)) * Q**3 != sp.zeros(15)
assert (E-sp.eye(15))**2 * Q**2 != sp.zeros(15)
print("frontier characteristic polynomial =",char)
print("minimal polynomial = (lambda-1)^2 (lambda^2-6 lambda+2)^3: PASS")
print("every unmarked path-layer transfer entry obeys the induced order-8 recurrence: PASS")

x,z=sp.symbols('x z', integer=True, nonnegative=True)
a=sp.Rational(37512,23396)
c=sp.Rational(25562,23396)
s=sp.Rational(1,4)
u=a*x+s*z
v=c*x+sp.Rational(1,2)*x*(x-1)*a*a+sp.Rational(1,2)*z*(z-1)*s*s+x*z*a*s
U=sp.eye(5)+u*N+v*N**2
d0=sp.Matrix([[1,0,0,0,0]]); one=sp.ones(5,1)

p,r=sp.symbols('p r', integer=True, nonnegative=True)
up=a*p+s*r
vp=c*p+sp.Rational(1,2)*p*(p-1)*a*a+sp.Rational(1,2)*r*(r-1)*s*s+p*r*a*s
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((d0*Up*one)[0])
Ztarget=(4221450432*p**2+1316446128*p*r+2877363888*p+
         102632403*r**2+444740413*r+547372816)/sp.Integer(547372816)
assert sp.simplify(Znorm-Ztarget)==0
print("Z/(23396^p 4^r) =",Znorm)
print("closed forest-count formula: PASS")

def edgekey(a,b): return tuple(sorted((a,b),key=repr))
Gedges=[]
for q in range(2):
    for i in range(6):
        for t in range(3):
            Gedges.append(edgekey(('A',q,i),('T',t)))
    for i in range(5):
        Gedges.append(edgekey(('A',q,i),('A',q,i+1)))
for q in range(2):
    for t in range(3):
        Gedges.append(edgekey(('O',q,0),('T',t)))
Gedges=list(dict.fromkeys(Gedges))

auts=[]
for tp in permutations(range(3)):
    for Ap in permutations(range(2)):
        for Afl in product([0,1],repeat=2):
            for Op in permutations(range(2)):
                mp={}
                for t in range(3): mp[('T',t)]=('T',tp[t])
                for q in range(2):
                    nq=Ap[q]
                    for i in range(6):
                        mp[('A',q,i)]=('A',nq,5-i if Afl[q] else i)
                for q in range(2): mp[('O',q,0)]=('O',Op[q],0)
                auts.append(mp)

pairs=[tuple(sorted((e,f),key=repr)) for e,f in combinations(Gedges,2)]
seen=set(); orbits=[]
for pair in pairs:
    if pair in seen: continue
    orb=set()
    for mp in auts:
        e,f=pair
        e2=edgekey(mp[e[0]],mp[e[1]])
        f2=edgekey(mp[f[0]],mp[f[1]])
        orb.add(tuple(sorted((e2,f2),key=repr)))
    seen |= orb
    orbits.append(orb)
assert len(Gedges)==52 and len(pairs)==1326 and len(orbits)==81
print("universal witness: 52 edges, 1326 pairs, 81 automorphism orbits: PASS")

def localize(e):
    a0,b0=e
    if a0[0]=='T':
        t=a0[1]; q=b0
    elif b0[0]=='T':
        t=b0[1]; q=a0
    else:
        assert a0[0]==b0[0] and a0[1]==b0[1]
        return (a0[0],a0[1],('i',min(a0[2],b0[2]),max(a0[2],b0[2])))
    return (q[0],q[1],('s',q[2],t))

def layer_matrix(kind,req):
    req=tuple(sorted(req,key=repr))
    if kind=='A':
        return P6 if not req else transfer_path(6,req)
    if kind=='O':
        return S if not req else transfer_path(1,req)
    raise AssertionError(kind)

def quantity(pair,required):
    layers={}
    for e in pair:
        kind,idx,loc=localize(e)
        layers.setdefault((kind,idx),[]).append((e,loc))
    M=sp.eye(5)
    for lid,els in sorted(layers.items(),key=repr):
        req=[loc for e,loc in els if e in required]
        M=M*layer_matrix(lid[0],req)
    return sp.expand((d0*M*U*one)[0])

def rayleigh_poly(pair):
    e,f=pair
    I=quantity(pair,set())
    Ie=quantity(pair,{e}); If=quantity(pair,{f})
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
    a0,b0=e
    if a0[0]=='T':
        t=a0[1]; q=b0
    elif b0[0]=='T':
        t=b0[1]; q=a0
    else:
        return f"{a0[0]}{a0[1]}:h{min(a0[2],b0[2])}{max(a0[2],b0[2])}"
    return f"{q[0]}{q[1]}:v{q[2]}-T{t}"

bad=[]; zero_constant=[]; min_positive_newton=None; min_regular_constant=None
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]
    poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    constant=sp.factor(poly.as_expr().subs({x:0,z:0}))
    if constant==0:
        zero_constant.append((idx,desc(rep[0]),desc(rep[1])))
    if any(cc<0 for cc in nc.values()):
        bad.append((idx,rep,poly,nc))
    else:
        pos=[cc for cc in nc.values() if cc>0]
        if pos:
            mm=min(pos)
            min_positive_newton=mm if min_positive_newton is None else min(min_positive_newton,mm)
        if constant>0:
            min_regular_constant=constant if min_regular_constant is None else min(min_regular_constant,constant)

assert len(bad)==4
bad_desc=[(q[0],desc(q[1][0]),desc(q[1][1])) for q in bad]
assert bad_desc==[
    (7,'A0:v0-T0','A0:v3-T1'),
    (9,'A0:v0-T0','A0:v4-T1'),
    (11,'A0:v0-T0','A0:v5-T1'),
    (34,'A0:v1-T0','A0:v4-T1')
]
print("77/81 orbit polynomials lie in the nonnegative Newton cone: PASS")
print("minimum positive Newton coefficient among regular orbits =",min_positive_newton)
print("minimum positive regular-orbit constant =",min_regular_constant)

certspec=[(3,15),(9,56),(24,153),(3,17)]
X,Z=sp.symbols('X Z', integer=True, nonnegative=True)
for (idx,rep,poly,nc),(A0,B0) in zip(bad,certspec):
    neg=sorted((k,cc) for k,cc in nc.items() if cc<0)
    den=sp.ilcm(*[int(sp.denom(cc)) for cc in poly.coeffs()])
    Qexpr=sp.Poly(sp.expand(den*poly.as_expr()),x,z,domain=sp.ZZ).as_expr()
    Qx=sp.Poly(sp.expand(Qexpr.subs({x:X+A0,z:Z})),X,Z,domain=sp.ZZ)
    Qz=sp.Poly(sp.expand(Qexpr.subs({x:X,z:Z+B0})),X,Z,domain=sp.ZZ)
    assert all(cc>0 for cc in Qx.coeffs())
    assert all(cc>0 for cc in Qz.coeffs())
    box=[(int(Qexpr.subs({x:i,z:j})),i,j) for i in range(A0) for j in range(B0)]
    assert min(v for v,_,_ in box)>0
    print("EXCEPTION",idx,desc(rep[0]),desc(rep[1]))
    print("  negative Newton coefficients =",neg)
    print("  denominator cleared by",den)
    print("  Q =",Qexpr)
    print(f"  x-corner shift ({A0},0): all {len(Qx.terms())} monomial coefficients positive; min={min(Qx.coeffs())}")
    print(f"  z-corner shift (0,{B0}): all {len(Qz.terms())} monomial coefficients positive; min={min(Qz.coeffs())}")
    bmin=min(box)
    print(f"  residual box 0<=x<{A0},0<=z<{B0}: {len(box)} exact values; min={bmin[0]} at ({bmin[1]},{bmin[2]})")
    print("  two-corner lattice sign certificate: PASS")

assert len(zero_constant)==1
assert {zero_constant[0][1],zero_constant[0][2]}=={'O0:v0-T0','O0:v0-T1'}
zidx=zero_constant[0][0]
zrep=sorted(orbits[zidx-1],key=repr)[0]
znc=newton_coeffs(rayleigh_poly(zrep))
assert all(cc>0 for cc in znc.values())
print("unique zero-constant orbit =",zero_constant,"; equality only for F6_{0,1}=K_{3,1}: PASS")

local_edges=[('s',i,t) for i in range(6) for t in range(3)]+[('i',i,i+1) for i in range(5)]
def layer_count(req):
    M=transfer_path(6,tuple(sorted(req,key=repr)))
    return int((d0*M*one)[0])
Z10=layer_count(())
onecnt={e:layer_count((e,)) for e in local_edges}
gaps=[]
for e,f in combinations(local_edges,2):
    gap=onecnt[e]*onecnt[f]-Z10*layer_count((e,f))
    gaps.append((gap,e,f))
assert Z10==326816
assert min(gaps)[0]==10756032
print("DIRECT F6_{1,0}: n=9 m=23 Z=326816 min_gap=10756032 pair=",min(gaps)[1:])
print("ALL_EXACT_CHECKS_PASS")
