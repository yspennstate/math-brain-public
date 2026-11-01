from itertools import combinations, permutations, product
import sympy as sp

# NM13-08 / T07 exact checker for
# F_{p,r} = K_{3,5p+r} plus p disjoint P5's on the right side and r isolated right vertices.
# The three left terminals are independent. All edge weights are 1.

STATES = [
    ((0,), (1,), (2,)),
    ((0,), (1,2)),
    ((0,1),(2,)),
    ((0,2),(1,)),
    ((0,1,2),),
]

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

def state_index(dsu):
    blocks={}
    for t in (0,1,2): blocks.setdefault(dsu.find(t),[]).append(t)
    bset={frozenset(v) for v in blocks.values()}
    for i,p in enumerate(STATES):
        if {frozenset(z) for z in p}==bset: return i
    raise AssertionError(bset)

def transfer_all(n_right, internal_edges=()):
    edges=[]
    for rv in range(n_right):
        for t in range(3): edges.append(("s",rv,t))
    for u,v in internal_edges: edges.append(("i",u,v))
    E=len(edges)
    M0=[[0]*5 for _ in range(5)]
    M1={e:[[0]*5 for _ in range(5)] for e in edges}
    M2={frozenset((e,f)):[[0]*5 for _ in range(5)] for e,f in combinations(edges,2)}
    for si,part in enumerate(STATES):
        for mask in range(1<<E):
            d=DSU(3+n_right)
            for block in part:
                for z in block[1:]: assert d.union(block[0],z)
            chosen=[]; bad=False
            for j,e in enumerate(edges):
                if not ((mask>>j)&1): continue
                if e[0]=="s": _,rv,t=e; aa=t; bb=3+rv
                else: _,u,v=e; aa=3+u; bb=3+v
                if not d.union(aa,bb): bad=True; break
                chosen.append(e)
            if bad: continue
            sj=state_index(d); M0[si][sj]+=1
            for e in chosen: M1[e][si][sj]+=1
            for e,f in combinations(chosen,2): M2[frozenset((e,f))][si][sj]+=1
    marks={frozenset([e]):sp.Matrix(M) for e,M in M1.items()}
    marks.update({k:sp.Matrix(M) for k,M in M2.items()})
    return sp.Matrix(M0),edges,marks

S,Sedges,Smark=transfer_all(1)
N=S-4*sp.eye(5)
P5,P5edges,P5mark=transfer_all(5,[(0,1),(1,2),(2,3),(3,4)])
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert P5==4144*sp.eye(5)+5524*N+sp.Rational(9050,3)*N**2
print("S(singleton)="); print(S)
print("P5 layer="); print(P5)
print("N^3=0: PASS")
print("P5 = 4144 I + 5524 N + (9050/3) N^2: PASS")

x,z=sp.symbols('x z', integer=True, nonnegative=True)
a=sp.Rational(1381,1036); b=sp.Rational(4525,6216); s=sp.Rational(1,4)
u=a*x+s*z
v=b*x+sp.Rational(1,2)*x*(x-1)*a*a+sp.Rational(1,2)*z*(z-1)*s*s+x*z*a*s
U=sp.eye(5)+u*N+v*N**2
d0=sp.Matrix([[1,0,0,0,0]]); one=sp.ones(5,1)

p,r=sp.symbols('p r', integer=True, nonnegative=True)
up=a*p+s*r
vp=b*p+sp.Rational(1,2)*p*(p-1)*a*a+sp.Rational(1,2)*r*(r-1)*s*s+p*r*a*s
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((d0*Up*one)[0])
Ztarget=(5721483*p**2+2146074*p*r+4689281*p+201243*r**2+872053*r+1073296)/sp.Integer(1073296)
assert sp.simplify(Znorm-Ztarget)==0
print("Z/(4144^p 4^r) =",Znorm)
print("closed forest-count formula: PASS")

def edgekey(a,b): return tuple(sorted((a,b),key=repr))
Gedges=[]
for q in range(2):
    for i in range(5):
        for t in range(3): Gedges.append(edgekey(('A',q,i),('T',t)))
    for u0,v0 in [(0,1),(1,2),(2,3),(3,4)]: Gedges.append(edgekey(('A',q,u0),('A',q,v0)))
for q in range(2):
    for t in range(3): Gedges.append(edgekey(('O',q,0),('T',t)))
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
                    for i in range(5): mp[('A',q,i)]=('A',nq,4-i if Afl[q] else i)
                for q in range(2): mp[('O',q,0)]=('O',Op[q],0)
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
assert len(orbits)==61
print("edge-pair orbit count = 61: PASS")

def localize(e):
    a0,b0=e
    if a0[0]=='T': t=a0[1]; q=b0
    elif b0[0]=='T': t=b0[1]; q=a0
    else:
        assert a0[0]==b0[0] and a0[1]==b0[1]
        return (a0[0],a0[1],('i',min(a0[2],b0[2]),max(a0[2],b0[2])))
    return (q[0],q[1],('s',q[2],t))

def layer_matrix(kind,req):
    req=frozenset(req)
    if kind=='A': return P5 if not req else P5mark[req]
    if kind=='O': return S if not req else Smark[req]
    raise AssertionError(kind)

def quantity(pair,required):
    layers={}
    for e in pair:
        kind,idx,loc=localize(e); layers.setdefault((kind,idx),[]).append((e,loc))
    M=sp.eye(5)
    for lid,els in sorted(layers.items(),key=repr):
        req=[loc for e,loc in els if e in required]
        M=M*layer_matrix(lid[0],req)
    return sp.expand((d0*M*U*one)[0])

def rayleigh_poly(pair):
    e,f=pair
    I=quantity(pair,set()); Ie=quantity(pair,{e}); If=quantity(pair,{f}); Ief=quantity(pair,{e,f})
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
    a0,b0=e
    if a0[0]=='T': t=a0[1]; q=b0
    elif b0[0]=='T': t=b0[1]; q=a0
    else: return f"{a0[0]}{a0[1]}:h{min(a0[2],b0[2])}{max(a0[2],b0[2])}"
    return f"{q[0]}{q[1]}:v{q[2]}-T{t}"

bad=[]; zero_constant=[]; min_regular_constant=None; min_positive_newton=None
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]; poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    constant=sp.factor(poly.as_expr().subs({x:0,z:0}))
    if constant==0: zero_constant.append((idx,desc(rep[0]),desc(rep[1])))
    if (not nc) or any(c<0 for c in nc.values()):
        bad.append((idx,rep,poly,nc))
    else:
        if constant>0:
            min_regular_constant=constant if min_regular_constant is None else min(min_regular_constant,constant)
        pos=[c for c in nc.values() if c>0]
        if pos:
            mm=min(pos); min_positive_newton=mm if min_positive_newton is None else min(min_positive_newton,mm)
assert len(bad)==2
bad_desc=[(q[0],desc(q[1][0]),desc(q[1][1])) for q in bad]
assert bad_desc==[(7,'A0:v0-T0','A0:v3-T1'),(9,'A0:v0-T0','A0:v4-T1')]
print("59/61 orbit polynomials lie in the nonnegative two-variable Newton cone: PASS")
print("minimum positive Newton coefficient among regular orbits =",min_positive_newton)
print("minimum positive regular-orbit constant =",min_regular_constant)

# Reusable exact sign lemma used here: if Q(A+X,Z) and Q(X,B+Z) are coefficientwise
# positive and Q(i,j)>0 on 0<=i<A, 0<=j<B, then Q>0 on all integer x,z>=0.
# The two exceptional P5 spoke-pair orbits admit such two-corner certificates.
certspec=[(3,15),(10,50)]
for (idx,rep,poly,nc),(A,B) in zip(bad,certspec):
    neg=sorted((k,c) for k,c in nc.items() if c<0)
    den=sp.lcm([sp.denom(c) for c in poly.coeffs()])
    Q=sp.Poly(sp.expand(den*poly.as_expr()),x,z,domain=sp.ZZ).as_expr()
    X,Z=sp.symbols('X Z', integer=True, nonnegative=True)
    Qx=sp.Poly(sp.expand(Q.subs({x:X+A,z:Z})),X,Z,domain=sp.ZZ)
    Qz=sp.Poly(sp.expand(Q.subs({x:X,z:Z+B})),X,Z,domain=sp.ZZ)
    assert all(c>0 for c in Qx.coeffs()) and all(c>0 for c in Qz.coeffs())
    box=[(int(Q.subs({x:i,z:j})),i,j) for i in range(A) for j in range(B)]
    assert min(v for v,_,_ in box)>0
    print("EXCEPTION",idx,desc(rep[0]),desc(rep[1]))
    print("  negative Newton coefficients =",neg)
    print("  denominator cleared by",den)
    print("  Q =",Q)
    print(f"  shift ({A},0): all {len(Qx.terms())} monomial coefficients positive; min={min(Qx.coeffs())}")
    print(f"  shift (0,{B}): all {len(Qz.terms())} monomial coefficients positive; min={min(Qz.coeffs())}")
    bmin=min(box)
    print(f"  finite box 0<=x<{A}, 0<=z<{B}: {len(box)} exact values; min={bmin[0]} at ({bmin[1]},{bmin[2]})")
    print("  two-corner lattice sign certificate: PASS")

assert len(zero_constant)==1
assert {zero_constant[0][1],zero_constant[0][2]}=={'O0:v0-T0','O0:v0-T1'}
zidx=zero_constant[0][0]
zpoly=rayleigh_poly(sorted(orbits[zidx-1],key=repr)[0]); znc=newton_coeffs(zpoly)
assert all(c>0 for c in znc.values()) and zpoly.as_expr().subs({x:0,z:0})==0
print("unique zero-constant orbit =",zero_constant,"; equality only for F_{0,1}=K_{3,1}: PASS")

def physical_graph(P,R):
    ed=[]; nxt=3
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
    nv,ed=physical_graph(P,R); E=len(ed); Z0=0; onec=[0]*E; twoc=[[0]*E for _ in range(E)]
    for mask in range(1<<E):
        d=DSU(nv); chosen=[]; bad0=False
        for j,(aa,bb) in enumerate(ed):
            if (mask>>j)&1:
                if not d.union(aa,bb): bad0=True; break
                chosen.append(j)
        if bad0: continue
        Z0+=1
        for j in chosen: onec[j]+=1
        for i,j in combinations(chosen,2): twoc[i][j]+=1; twoc[j][i]+=1
    gaps=[onec[i]*onec[j]-Z0*twoc[i][j] for i,j in combinations(range(E),2)]
    return nv,E,Z0,min(gaps),max(gaps)

checks={(1,0):(8,19,44340,340560,49717320),(1,1):(9,22,227080,7363344,1829342544),(0,2):(5,6,54,36,90)}
for pars,want in checks.items():
    got=brute(*pars); assert got==want
    print(f"BRUTE F_{pars}: n={got[0]} m={got[1]} Z={got[2]} min_gap={got[3]} max_gap={got[4]}")
print("ALL_EXACT_CHECKS_PASS")
