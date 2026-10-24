from itertools import combinations, permutations, product
import sympy as sp

# NM13-08 / T07 exact checker.
# Family F_{p,r}: three independent terminals; on the right,
# p disjoint P4 blocks and r isolated vertices; every right vertex is
# adjacent to all three terminals. Unit forest weights throughout.

STATES = [
    ((0,), (1,), (2,)),
    ((0,), (1,2)),
    ((0,1),(2,)),
    ((0,2),(1,)),
    ((0,1,2),)
]

class DSU:
    def __init__(self,n):
        self.p=list(range(n)); self.r=[0]*n
    def find(self,a):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]
            a=self.p[a]
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
    for t in (0,1,2):
        blocks.setdefault(dsu.find(t),[]).append(t)
    bset={frozenset(v) for v in blocks.values()}
    for i,p in enumerate(STATES):
        if {frozenset(z) for z in p}==bset:
            return i
    raise AssertionError(bset)

def transfer_all(n_right, internal_edges=()):
    edges=[]
    for rv in range(n_right):
        for t in range(3):
            edges.append(("s",rv,t))
    for u,v in internal_edges:
        edges.append(("i",u,v))
    E=len(edges)
    M0=[[0]*5 for _ in range(5)]
    M1={e:[[0]*5 for _ in range(5)] for e in edges}
    M2={frozenset((e,f)):[[0]*5 for _ in range(5)] for e,f in combinations(edges,2)}
    for si,part in enumerate(STATES):
        for mask in range(1<<E):
            d=DSU(3+n_right)
            for block in part:
                for z in block[1:]:
                    assert d.union(block[0],z)
            chosen=[]; bad=False
            for j,e in enumerate(edges):
                if not ((mask>>j)&1): continue
                if e[0]=="s": _,rv,t=e; a=t; b=3+rv
                else: _,u,v=e; a=3+u; b=3+v
                if not d.union(a,b): bad=True; break
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
P4,P4edges,P4mark=transfer_all(4,[(0,1),(1,2),(2,3)])
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert P4==734*sp.eye(5)+780*N+sp.Rational(961,3)*N**2
print("S(singleton)="); print(S)
print("P(P4 right block)="); print(P4)
print("N^3=0: PASS")
print("P4 = 734 I + 780 N + (961/3) N^2: PASS")

x,z=sp.symbols('x z', integer=True, nonnegative=True)
a=sp.Rational(390,367); b=sp.Rational(961,2202); s=sp.Rational(1,4)
u=a*x+s*z
v=(b*x+sp.Rational(1,2)*x*(x-1)*a*a+sp.Rational(1,2)*z*(z-1)*s*s+x*z*a*s)
U=sp.eye(5)+u*N+v*N**2
d0=sp.Matrix([[1,0,0,0,0]]); one=sp.ones(5,1)
p,r=sp.symbols('p r', integer=True, nonnegative=True)
up=a*p+s*r
vp=(b*p+sp.Rational(1,2)*p*(p-1)*a*a+sp.Rational(1,2)*r*(r-1)*s*s+p*r*a*s)
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((d0*Up*one)[0])
Ztarget=(7300800*p**2+3435120*p*r+7502512*p+404067*r**2+1750957*r+2155024)/sp.Integer(2155024)
assert sp.simplify(Znorm-Ztarget)==0
print("Z/(734^p 4^r) =",Znorm)
print("closed forest-count formula: PASS")

def edgekey(a,b): return tuple(sorted((a,b),key=repr))
Gedges=[]
for q in range(2):
    for i in range(4):
        for t in range(3): Gedges.append(edgekey(('A',q,i),('T',t)))
    for u0,v0 in [(0,1),(1,2),(2,3)]: Gedges.append(edgekey(('A',q,u0),('A',q,v0)))
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
                    for i in range(4): mp[('A',q,i)]=('A',nq,3-i if Afl[q] else i)
                for q in range(2): mp[('O',q,0)]=('O',Op[q],0)
                auts.append(mp)
pairs=[tuple(sorted((e,f),key=repr)) for e,f in combinations(Gedges,2)]
seen=set(); orbits=[]
for pair in pairs:
    if pair in seen: continue
    orb=set()
    for mp in auts:
        e,f=pair; e2=edgekey(mp[e[0]],mp[e[1]]); f2=edgekey(mp[f[0]],mp[f[1]])
        orb.add(tuple(sorted((e2,f2),key=repr)))
    seen |= orb; orbits.append(orb)
assert len(orbits)==40
print("edge-pair orbit count = 40: PASS")

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
    if kind=='A': return P4 if not req else P4mark[req]
    if kind=='O': return S if not req else Smark[req]
    raise AssertionError(kind)

def quantity(pair,required):
    layers={}
    for e in pair:
        kind,idx,loc=localize(e); layers.setdefault((kind,idx),[]).append((e,loc))
    M=sp.eye(5)
    for lid,els in sorted(layers.items(),key=repr):
        req=[loc for e,loc in els if e in required]; M=M*layer_matrix(lid[0],req)
    return sp.expand((d0*M*U*one)[0])

def rayleigh_poly(pair):
    e,f=pair; I=quantity(pair,set()); Ie=quantity(pair,{e}); If=quantity(pair,{f}); Ief=quantity(pair,{e,f})
    return sp.Poly(sp.expand(Ie*If-I*Ief),x,z,domain=sp.QQ)

def newton_coeffs(poly):
    expr=poly.as_expr(); D=poly.total_degree(); ans={}
    for i in range(D+1):
        for j in range(D+1-i):
            c=sp.Rational(0)
            for aa in range(i+1):
                for bb in range(j+1):
                    c += ((-1)**((i-aa)+(j-bb))*sp.binomial(i,aa)*sp.binomial(j,bb)*expr.subs({x:aa,z:bb}))
            c=sp.factor(c)
            if c: ans[(i,j)]=c
    return ans

def desc(e):
    a0,b0=e
    if a0[0]=='T': t=a0[1]; q=b0
    elif b0[0]=='T': t=b0[1]; q=a0
    else: return f"{a0[0]}{a0[1]}:h{min(a0[2],b0[2])}{max(a0[2],b0[2])}"
    return f"{q[0]}{q[1]}:v{q[2]}-T{t}"

bad=[]; zero_constant=[]; mixed_monomial=[]
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]; poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    constant=sp.factor(poly.as_expr().subs({x:0,z:0}))
    if constant==0: zero_constant.append((idx,desc(rep[0]),desc(rep[1])))
    if any(c<0 for c in poly.coeffs()): mixed_monomial.append(idx)
    if (not nc) or any(c<0 for c in nc.values()): bad.append((idx,rep,poly,nc))
    else: print("ORBIT %02d | %-12s | %-12s | deg=%d | positive_Newton_terms=%d | constant=%s | min_Newton=%s" %(idx,desc(rep[0]),desc(rep[1]),poly.total_degree(),len(nc),constant,min(nc.values())))
assert len(bad)==1
bidx,brep,bpoly,bnc=bad[0]
assert {desc(brep[0]),desc(brep[1])}=={'A0:v0-T0','A0:v3-T1'}
print("39/40 orbit polynomials lie in the positive two-variable Newton cone: PASS")
print("exceptional orbit =",bidx,desc(brep[0]),desc(brep[1]))
print("exceptional negative Newton coefficients =",sorted((k,c) for k,c in bnc.items() if c<0))
print("ordinary monomial mixed-sign orbit(s) =",mixed_monomial)
den=sp.lcm([sp.denom(c) for c in bpoly.coeffs()]); Q=sp.Poly(sp.expand(den*bpoly.as_expr()),x,z,domain=sp.ZZ).as_expr()
X,Z=sp.symbols('X Z', integer=True, nonnegative=True)
regions=[(4,0),(3,1),(2,5),(1,10),(0,14)]
for xa,za in regions:
    R=sp.Poly(sp.expand(Q.subs({x:X+xa,z:Z+za})),X,Z,domain=sp.ZZ)
    assert all(c>0 for c in R.coeffs())
    print(f"EXCEPTION SHIFT x={xa}+X, z={za}+Z: coefficientwise positive; terms={len(R.terms())}; min_coeff={min(R.coeffs())}; constant={R.eval({X:0,Z:0})}")
boundary=[]
for xa,za in [(0,14),(1,10),(2,5),(3,1)]:
    vals=[int(Q.subs({x:xa,z:j})) for j in range(za)]; assert vals and min(vals)>0
    boundary.extend((xa,j,v) for j,v in enumerate(vals))
    print(f"EXCEPTION BOUNDARY x={xa}, 0<=z<{za}: {len(vals)} exact values; min={min(vals)} at z={vals.index(min(vals))}")
assert len(boundary)==30
print("unique exceptional orbit positive on every integer (x,z)>=0 by five shifted quadrants + 30 boundary values: PASS")
assert len(zero_constant)==1
zi,ze,zf=zero_constant[0]; assert {ze,zf}=={'O0:v0-T0','O0:v0-T1'}
zpoly=rayleigh_poly(sorted(orbits[zi-1],key=repr)[0]); znc=newton_coeffs(zpoly)
assert all(c>0 for c in znc.values()); assert zpoly.as_expr().subs({x:0,z:0})==0
print("unique zero-constant orbit =",zero_constant,"; equality only for F_{0,1}=K_{3,1}: PASS")

def physical_graph(P,R):
    ed=[]; nxt=3
    for q in range(P):
        vs=list(range(nxt,nxt+4)); nxt+=4
        for vv in vs:
            for t in range(3): ed.append((t,vv))
        ed += [(vs[0],vs[1]),(vs[1],vs[2]),(vs[2],vs[3])]
    for q in range(R):
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
checks={(1,0):(7,15,5776,27300,951584),(1,1):(8,18,30720,715536,30145444),(0,2):(5,6,54,36,90)}
for pars,want in checks.items():
    got=brute(*pars); assert got==want
    print(f"BRUTE F_{pars}: n={got[0]} m={got[1]} Z={got[2]} min_gap={got[3]} max_gap={got[4]}")
print("ALL_EXACT_CHECKS_PASS")
