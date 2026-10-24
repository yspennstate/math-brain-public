from itertools import combinations, permutations, product
import sympy as sp

# NM13-08 / T07 exact checker.
# Family L_{p,m,r}: three fixed independent terminals; on the right,
# p disjoint P3 blocks, m disjoint K2 blocks, and r isolated vertices;
# every right vertex is adjacent to all three terminals.

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

def transfer(n_right, internal_edges=(), required=frozenset()):
    edges=[]
    for rv in range(n_right):
        for t in range(3): edges.append(("s",rv,t))
    for u,v in internal_edges: edges.append(("i",u,v))
    M=[[0]*5 for _ in range(5)]
    for si,part in enumerate(STATES):
        for mask in range(1<<len(edges)):
            if any(((mask>>j)&1)==0 for j,e in enumerate(edges) if e in required):
                continue
            d=DSU(3+n_right)
            for block in part:
                for z in block[1:]: d.union(block[0],z)
            bad=False
            for j,e in enumerate(edges):
                if not ((mask>>j)&1): continue
                if e[0]=="s": _,rv,t=e; a=t; b=3+rv
                else: _,u,v=e; a=3+u; b=3+v
                if not d.union(a,b): bad=True; break
            if bad: continue
            M[si][state_index(d)]+=1
    return sp.Matrix(M),edges

S,Sedges=transfer(1)
N=S-4*sp.eye(5)
B,Bedges=transfer(2,[(0,1)])
A,Aedges=transfer(3,[(0,1),(1,2)])
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert B==23*sp.eye(5)+12*N+sp.Rational(5,3)*N**2
assert A==130*sp.eye(5)+103*N+sp.Rational(85,3)*N**2
print("S="); print(S)
print("B(K2 right block)="); print(B)
print("A(P3 right block)="); print(A)
print("N^3=0: PASS")
print("B = 23 I + 12 N + (5/3)N^2: PASS")
print("A = 130 I + 103 N + (85/3)N^2: PASS")

# Normalized remainder transfer for x P3 blocks, y K2 blocks, z singleton blocks.
x,y,z=sp.symbols('x y z', integer=True, nonnegative=True)
aA,bA=sp.Rational(103,130),sp.Rational(17,78)
aB,bB=sp.Rational(12,23),sp.Rational(5,69)
aS=sp.Rational(1,4)
u=aA*x+aB*y+aS*z
v=(bA*x+bB*y
   +sp.Rational(1,2)*x*(x-1)*aA*aA
   +sp.Rational(1,2)*y*(y-1)*aB*aB
   +sp.Rational(1,2)*z*(z-1)*aS*aS
   +x*y*aA*aB+x*z*aA*aS+y*z*aB*aS)
U=sp.eye(5)+u*N+v*N**2
d0=sp.Matrix([[1,0,0,0,0]]); one=sp.ones(5,1)

p,m,r=sp.symbols('p m r', integer=True, nonnegative=True)
up=aA*p+aB*m+aS*r
vp=(bA*p+bB*m
   +sp.Rational(1,2)*p*(p-1)*aA*aA
   +sp.Rational(1,2)*m*(m-1)*aB*aB
   +sp.Rational(1,2)*r*(r-1)*aS*aS
   +p*m*aA*aB+p*r*aA*aS+m*r*aB*aS)
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((d0*Up*one)[0])
Ztarget=(29203200*m**2+88695360*m*p+27986400*m*r+60975200*m
         +67345932*p**2+42499860*p*r+92750628*p
         +6705075*r**2+29055325*r+35760400)/sp.Integer(35760400)
assert sp.simplify(Znorm-Ztarget)==0
print("Z/(130^p 23^m 4^r) =",Znorm)
print("closed forest-count formula: PASS")

# Exact marked matrices for all edge requirements in one layer.
def marked_family(nr, internal):
    M0,edges=transfer(nr,internal)
    marks={}
    for e in edges: marks[frozenset([e])]=transfer(nr,internal,frozenset([e]))[0]
    for e,f in combinations(edges,2): marks[frozenset([e,f])]=transfer(nr,internal,frozenset([e,f]))[0]
    return M0,edges,marks
A,Aedges,Amark=marked_family(3,[(0,1),(1,2)])
B,Bedges,Bmark=marked_family(2,[(0,1)])
S,Sedges,Smark=marked_family(1,[])

def edgekey(a,b): return tuple(sorted((a,b),key=repr))
# Universal witness: 2 blocks of each kind, enough to realize every pair orbit.
Gedges=[]
for typ,nv in [('A',3),('B',2)]:
    for q in range(2):
        for i in range(nv):
            for t in range(3): Gedges.append(edgekey(('T',t),(typ,q,i)))
        if typ=='A':
            Gedges.append(edgekey((typ,q,0),(typ,q,1))); Gedges.append(edgekey((typ,q,1),(typ,q,2)))
        else:
            Gedges.append(edgekey((typ,q,0),(typ,q,1)))
for q in range(2):
    for t in range(3): Gedges.append(edgekey(('T',t),('O',q,0)))
Gedges=list(dict.fromkeys(Gedges))

auts=[]
for tp in permutations(range(3)):
  for Ap in permutations(range(2)):
   for Afl in product([0,1],repeat=2):
    for Bp in permutations(range(2)):
     for Bfl in product([0,1],repeat=2):
      for Op in permutations(range(2)):
        mp={}
        for t in range(3): mp[('T',t)]=('T',tp[t])
        for q in range(2):
            nq=Ap[q]
            for i in range(3): mp[('A',q,i)]=('A',nq,2-i if Afl[q] else i)
        for q in range(2):
            nq=Bp[q]
            for i in range(2): mp[('B',q,i)]=('B',nq,1-i if Bfl[q] else i)
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
assert len(orbits)==46
print("edge-pair orbit count = 46: PASS")

def localize(e):
    a,b=e
    if a[0]=='T': t=a[1]; q=b
    elif b[0]=='T': t=b[1]; q=a
    else:
        assert a[0]==b[0] and a[1]==b[1]
        return (a[0],a[1],('i',min(a[2],b[2]),max(a[2],b[2])))
    return (q[0],q[1],('s',q[2],t))

def layer_matrix(kind,req):
    req=frozenset(req)
    if kind=='A': return A if not req else Amark[req]
    if kind=='B': return B if not req else Bmark[req]
    if kind=='O': return S if not req else Smark[req]
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
    I=quantity(pair,set()); Ie=quantity(pair,{e}); If=quantity(pair,{f}); Ief=quantity(pair,{e,f})
    return sp.Poly(sp.expand(Ie*If-I*Ief),x,y,z,domain=sp.QQ)

def newton_coeffs(poly):
    # c_ijk = Delta_x^i Delta_y^j Delta_z^k R(0,0,0)
    expr=poly.as_expr(); D=poly.total_degree(); ans={}
    for i in range(D+1):
      for j in range(D+1-i):
       for k0 in range(D+1-i-j):
        c=sp.Rational(0)
        for a in range(i+1):
         for b in range(j+1):
          for c0 in range(k0+1):
           c += ((-1)**((i-a)+(j-b)+(k0-c0))*sp.binomial(i,a)*sp.binomial(j,b)*sp.binomial(k0,c0)
                 *expr.subs({x:a,y:b,z:c0}))
        c=sp.factor(c)
        if c: ans[(i,j,k0)]=c
    return ans

def desc(e):
    a,b=e
    if a[0]=='T': t=a[1]; q=b
    elif b[0]=='T': t=b[1]; q=a
    else: return f"{a[0]}{a[1]}:h{min(a[2],b[2])}{max(a[2],b[2])}"
    return f"{q[0]}{q[1]}:v{q[2]}-T{t}"

zero_constant=[]; mixed_monomial=[]
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]
    poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    assert nc and all(c>0 for c in nc.values())
    constant=sp.factor(poly.as_expr().subs({x:0,y:0,z:0}))
    if constant==0: zero_constant.append(idx)
    if any(c<0 for c in poly.coeffs()): mixed_monomial.append(idx)
    print("ORBIT %02d | %-12s | %-12s | deg=%d | Newton_terms=%d | constant=%s | min_Newton=%s" %
          (idx,desc(rep[0]),desc(rep[1]),poly.total_degree(),len(nc),constant,min(nc.values())))

assert zero_constant==[44]
print("all 46 orbit Rayleigh polynomials have strictly positive nonzero Newton/binomial coefficients: PASS")
print("zero-constant orbit(s) =",zero_constant,"(the two distinct spokes of the unique singleton star; equality only for K_{3,1})")
print("ordinary monomial coefficient mixed-sign orbit(s) =",mixed_monomial)
# print the two certificates that are easiest to inspect: the old P3 difficult orbit and the unique equality orbit.
for idx in (5,44):
    rep=sorted(orbits[idx-1],key=repr)[0]
    print("ORBIT %02d Newton certificate ="%idx,sorted(newton_coeffs(rayleigh_poly(rep)).items()))

# Independent brute-force checks of three physical graphs.
def physical_graph(P,M,R):
    ed=[]; nxt=3
    for q in range(P):
        vs=[nxt,nxt+1,nxt+2]; nxt+=3
        for vv in vs:
            for t in range(3): ed.append((t,vv))
        ed += [(vs[0],vs[1]),(vs[1],vs[2])]
    for q in range(M):
        vs=[nxt,nxt+1]; nxt+=2
        for vv in vs:
            for t in range(3): ed.append((t,vv))
        ed.append((vs[0],vs[1]))
    for q in range(R):
        vv=nxt; nxt+=1
        for t in range(3): ed.append((t,vv))
    return nxt,ed

def brute(P,M,R):
    nv,ed=physical_graph(P,M,R); E=len(ed)
    Z=0; onec=[0]*E; twoc=[[0]*E for _ in range(E)]
    for mask in range(1<<E):
        d=DSU(nv); chosen=[]; bad=False
        for j,(a,b) in enumerate(ed):
            if (mask>>j)&1:
                if not d.union(a,b): bad=True; break
                chosen.append(j)
        if bad: continue
        Z+=1
        for j in chosen: onec[j]+=1
        for i,j in combinations(chosen,2): twoc[i][j]+=1; twoc[j][i]+=1
    gaps=[onec[i]*onec[j]-Z*twoc[i][j] for i,j in combinations(range(E),2)]
    return nv,E,Z,min(gaps)

checks={(1,0,0):(6,11,712,1728), (0,1,1):(6,10,488,448), (1,1,0):(8,18,31332,137088)}
for pars,want in checks.items():
    got=brute(*pars); assert got==want
    print(f"BRUTE L_{pars}: n={got[0]} m={got[1]} Z={got[2]} min_gap={got[3]}")
print("ALL_EXACT_CHECKS_PASS")
