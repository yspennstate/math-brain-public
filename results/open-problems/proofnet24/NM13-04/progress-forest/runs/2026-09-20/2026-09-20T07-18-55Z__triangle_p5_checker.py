#!/usr/bin/env python3
from itertools import combinations, permutations, product
import sympy as sp

# NM13-04 / T07 exact checker.
# Restricted theorem:
#   G_{p,r} = K_3 join (p P5 disjoint_union r K1), p,r >= 0.
# Unit edge weights; the measure is uniform over all forests.

STATES = [
    ((0,), (1,), (2,)),
    ((0,), (1,2)),
    ((0,1),(2,)),
    ((0,2),(1,)),
    ((0,1,2),),
]

class DSU:
    __slots__=("p","r")
    def __init__(self,n):
        self.p=list(range(n)); self.r=[0]*n
    def find(self,a):
        p=self.p
        while p[a]!=a:
            p[a]=p[p[a]]; a=p[a]
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

def transfer_all(n_right, internal_edges=()):
    edges=[]
    for rv in range(n_right):
        for t in range(3): edges.append(("s",rv,t))
    for u,v in internal_edges: edges.append(("i",u,v))
    E=len(edges)
    M0=[[0]*5 for _ in range(5)]
    M1={e:[[0]*5 for _ in range(5)] for e in edges}
    M2={frozenset((e,f)):[[0]*5 for _ in range(5)] for e,f in combinations(edges,2)}
    init=[[],[(1,2)],[(0,1)],[(0,2)],[(0,1),(0,2)]]
    ends=[]
    for e in edges:
        if e[0]=="s":
            _,rv,t=e; ends.append((t,3+rv))
        else:
            _,u,v=e; ends.append((3+u,3+v))
    for si,joins in enumerate(init):
        for mask in range(1<<E):
            d=DSU(3+n_right)
            for aa,bb in joins: assert d.union(aa,bb)
            chosen=[]; mm=mask; bad=False
            while mm:
                lb=mm & -mm; j=lb.bit_length()-1
                aa,bb=ends[j]
                if not d.union(aa,bb):
                    bad=True; break
                chosen.append(j); mm-=lb
            if bad: continue
            sj=state_index(d); M0[si][sj]+=1
            for j in chosen: M1[edges[j]][si][sj]+=1
            for ii in range(len(chosen)):
                e=edges[chosen[ii]]
                for jj in range(ii+1,len(chosen)):
                    f=edges[chosen[jj]]
                    M2[frozenset((e,f))][si][sj]+=1
    marks={frozenset([e]):sp.Matrix(M) for e,M in M1.items()}
    marks.update({k:sp.Matrix(M) for k,M in M2.items()})
    return sp.Matrix(M0),edges,marks

def triangle_vector(required=frozenset()):
    E=[(0,1),(0,2),(1,2)]
    out=[0]*5
    for mask in range(8):
        if any(not ((mask>>i)&1) for i in required): continue
        d=DSU(3); ok=True
        for i,(a,b) in enumerate(E):
            if (mask>>i)&1 and not d.union(a,b):
                ok=False; break
        if ok: out[state_index(d)]+=1
    return sp.Matrix([out])

S,Sedges,Smark=transfer_all(1)
N=S-4*sp.eye(5)
P5,P5edges,P5mark=transfer_all(5,[(0,1),(1,2),(2,3),(3,4)])
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert P5==4144*sp.eye(5)+5524*N+sp.Rational(9050,3)*N**2

TV={frozenset(req):triangle_vector(frozenset(req))
    for req in [(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]}
q=TV[frozenset()]
assert list(q)==[1,1,1,1,3]
one=sp.ones(5,1)

x,z=sp.symbols('x z', integer=True, nonnegative=True)
a=sp.Rational(1381,1036)
b=sp.Rational(4525,6216)
s=sp.Rational(1,4)
u=a*x+s*z
v=b*x+sp.Rational(1,2)*x*(x-1)*a*a+sp.Rational(1,2)*z*(z-1)*s*s+x*z*a*s
U=sp.eye(5)+u*N+v*N**2

p,r=sp.symbols('p r', integer=True, nonnegative=True)
up=a*p+s*r
vp=b*p+sp.Rational(1,2)*p*(p-1)*a*a+sp.Rational(1,2)*r*(r-1)*s*s+p*r*a*s
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((q*Up*one)[0])
Ztarget=(5721483*p**2+2146074*p*r+13273577*p+201243*r**2+2481997*r+7513072)/sp.Integer(1073296)
assert sp.simplify(Znorm-Ztarget)==0

def edgekey(a,b): return tuple(sorted((a,b),key=repr))
Gedges=[]
for i,j in [(0,1),(0,2),(1,2)]: Gedges.append(edgekey(('T',i),('T',j)))
for qid in range(2):
    for i in range(5):
        for t in range(3): Gedges.append(edgekey(('A',qid,i),('T',t)))
    for u0,v0 in [(0,1),(1,2),(2,3),(3,4)]:
        Gedges.append(edgekey(('A',qid,u0),('A',qid,v0)))
for qid in range(2):
    for t in range(3): Gedges.append(edgekey(('O',qid,0),('T',t)))
Gedges=list(dict.fromkeys(Gedges))
assert len(Gedges)==47

auts=[]
for tp in permutations(range(3)):
    for Ap in permutations(range(2)):
        for Afl in product([0,1],repeat=2):
            for Op in permutations(range(2)):
                mp={('T',t):('T',tp[t]) for t in range(3)}
                for qid in range(2):
                    nq=Ap[qid]
                    for i in range(5):
                        mp[('A',qid,i)]=('A',nq,4-i if Afl[qid] else i)
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
assert len(pairs)==1081 and len(orbits)==72 and len(seen)==1081

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
    req=frozenset(req)
    if kind=='A': return P5 if not req else P5mark[req]
    if kind=='O': return S if not req else Smark[req]
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
            c=sp.Rational(0)
            for aa in range(i+1):
                for bb in range(j+1):
                    c += (-1)**((i-aa)+(j-bb))*sp.binomial(i,aa)*sp.binomial(j,bb)*expr.subs({x:aa,z:bb})
            c=sp.factor(c)
            if c: ans[(i,j)]=c
    return ans

def desc(e):
    ci=core_idx(e)
    if ci is not None: return ['T01','T02','T12'][ci]
    a0,b0=e
    if a0[0]=='T': t=a0[1]; qv=b0
    elif b0[0]=='T': t=b0[1]; qv=a0
    else: return f"{a0[0]}{a0[1]}:h{min(a0[2],b0[2])}{max(a0[2],b0[2])}"
    return f"{qv[0]}{qv[1]}:v{qv[2]}-T{t}"

bad=[]; zero_constant=[]; min_constant=None; min_positive_newton=None
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]
    poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    constant=sp.factor(poly.as_expr().subs({x:0,z:0}))
    if constant==0: zero_constant.append((idx,desc(rep[0]),desc(rep[1])))
    neg=[(k,c) for k,c in nc.items() if c<0]
    if neg:
        bad.append((idx,rep,poly,nc))
    else:
        assert constant>0
        min_constant=constant if min_constant is None else min(min_constant,constant)
        pos=[c for c in nc.values() if c>0]
        if pos:
            mm=min(pos)
            min_positive_newton=mm if min_positive_newton is None else min(min_positive_newton,mm)

assert len(bad)==2
assert zero_constant==[]
assert min_constant==2
assert min_positive_newton==sp.Rational(1,8)
bad_desc=[(q0[0],desc(q0[1][0]),desc(q0[1][1])) for q0 in bad]
assert bad_desc==[(18,'A0:v0-T0','A0:v3-T1'),(20,'A0:v0-T0','A0:v4-T1')]

certspec=[(3,11),(9,46)]
for (idx,rep,poly,nc),(A,B) in zip(bad,certspec):
    neg=sorted((k,c) for k,c in nc.items() if c<0)
    den=sp.ilcm(*[int(sp.denom(c)) for c in poly.coeffs()])
    Q=sp.Poly(sp.expand(den*poly.as_expr()),x,z,domain=sp.ZZ).as_expr()
    X,Z=sp.symbols('X Z', integer=True, nonnegative=True)
    Qx=sp.Poly(sp.expand(Q.subs({x:X+A,z:Z})),X,Z,domain=sp.ZZ)
    Qz=sp.Poly(sp.expand(Q.subs({x:X,z:Z+B})),X,Z,domain=sp.ZZ)
    assert len(Qx.terms())==15 and len(Qz.terms())==15
    assert all(c>0 for c in Qx.coeffs()) and all(c>0 for c in Qz.coeffs())
    box=[(int(Q.subs({x:i,z:j})),i,j) for i in range(A) for j in range(B)]
    assert min(v for v,_,_ in box)>0
    print("EXCEPTION",idx,desc(rep[0]),desc(rep[1]))
    print(" negative Newton =",neg)
    print(" denominator =",den)
    print(" Q =",Q)
    print(f" shift ({A},0): min_coeff={min(Qx.coeffs())}; terms={len(Qx.terms())}")
    print(f" shift (0,{B}): min_coeff={min(Qz.coeffs())}; terms={len(Qz.terms())}")
    bmin=min(box)
    print(f" finite box {A}x{B}: min={bmin[0]} at ({bmin[1]},{bmin[2]})")

def physical_graph(P,R):
    ed=[(0,1),(0,2),(1,2)]; nxt=3
    for _ in range(P):
        vs=list(range(nxt,nxt+5)); nxt+=5
        for vv in vs:
            for t in range(3): ed.append((t,vv))
        ed += [(vs[0],vs[1]),(vs[1],vs[2]),(vs[2],vs[3]),(vs[3],vs[4])]
    for _ in range(R):
        vv=nxt; nxt+=1
        for t in range(3): ed.append((t,vv))
    return nxt,ed

def brute(P,R):
    nv,ed=physical_graph(P,R); E=len(ed)
    Z0=0; onec=[0]*E; twoc=[[0]*E for _ in range(E)]
    for mask in range(1<<E):
        d=DSU(nv); chosen=[]; mm=mask; bad0=False
        while mm:
            lb=mm & -mm; j=lb.bit_length()-1
            aa,bb=ed[j]
            if not d.union(aa,bb):
                bad0=True; break
            chosen.append(j); mm-=lb
        if bad0: continue
        Z0+=1
        for j in chosen: onec[j]+=1
        for ii in range(len(chosen)):
            i=chosen[ii]
            for jj in range(ii+1,len(chosen)):
                j=chosen[jj]; twoc[i][j]+=1; twoc[j][i]+=1
    gaps=[onec[i]*onec[j]-Z0*twoc[i][j] for i,j in combinations(range(E),2)]
    return nv,E,Z0,min(gaps),max(gaps)

got=brute(1,0)
assert got==(8,22,102348,1003968,299891200)

print("P5 transfer =",P5)
print("N^3=0 and P5 decomposition: PASS")
print("triangle seed =",list(TV[frozenset()]))
print("normalized total forest count =",Znorm)
print("witness edges/pairs/orbits = 47 / 1081 / 72")
print("regular Newton-positive orbits = 70/72")
print("minimum regular constant =",min_constant)
print("minimum positive Newton coefficient =",min_positive_newton)
print("BRUTE G_(1,0): n=%d m=%d Z=%d min_gap=%d max_gap=%d" % got)
print("ALL_EXACT_CHECKS_PASS")
