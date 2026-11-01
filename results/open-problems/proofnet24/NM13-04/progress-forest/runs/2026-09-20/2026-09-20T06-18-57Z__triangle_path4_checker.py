#!/usr/bin/env python3
from itertools import combinations, permutations, product
from math import comb
import sympy as sp

# NM13-04 / T07 exact checker.
# Theorem family:
#   G_{a,b,c,d} = K_3 join (a P4 disjoint_union b P3 disjoint_union c K2 disjoint_union d K1).
# Unit edge weights; every forest component count is mixed.

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

def triangle_vector(required=frozenset()):
    E=[(0,1),(0,2),(1,2)]
    out=[0]*5
    for mask in range(8):
        if any(not ((mask>>i)&1) for i in required): continue
        d=DSU(3); ok=True
        for i,(a,b) in enumerate(E):
            if (mask>>i)&1 and not d.union(a,b): ok=False; break
        if not ok: continue
        out[state_index(d)] += 1
    return sp.Matrix([out])

S,Sedges,Smark=transfer_all(1)
N=S-4*sp.eye(5)
P4,P4edges,P4mark=transfer_all(4,[(0,1),(1,2),(2,3)])
P3,P3edges,P3mark=transfer_all(3,[(0,1),(1,2)])
K2,K2edges,K2mark=transfer_all(2,[(0,1)])
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert P4==734*sp.eye(5)+780*N+sp.Rational(961,3)*N**2
assert P3==130*sp.eye(5)+103*N+sp.Rational(85,3)*N**2
assert K2==23*sp.eye(5)+12*N+sp.Rational(5,3)*N**2

TV={frozenset(req):triangle_vector(frozenset(req)) for req in [(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]}
q=TV[frozenset()]
assert list(q)==[1,1,1,1,3]
one=sp.ones(5,1)

# Exact normalized unmarked product in the common nilpotent algebra.
x4,x3,x2,x1=sp.symbols('x4 x3 x2 x1', integer=True, nonnegative=True)
VARS=(x4,x3,x2,x1)
PARAMS=[
    (x4,sp.Rational(390,367),sp.Rational(961,2202)),
    (x3,sp.Rational(103,130),sp.Rational(17,78)),
    (x2,sp.Rational(12,23),sp.Rational(5,69)),
    (x1,sp.Rational(1,4),sp.Rational(0)),
]
u=sum(v*a for v,a,b in PARAMS)
v=sum(v*b for v,a,b in PARAMS)
for i,(var,a,b) in enumerate(PARAMS):
    v += sp.Rational(1,2)*var*(var-1)*a*a
    for var2,a2,b2 in PARAMS[i+1:]: v += var*var2*a*a2
U=sp.eye(5)+u*N+v*N**2

DATA={'P4':(P4,P4mark),'P3':(P3,P3mark),'K2':(K2,K2mark),'K1':(S,Smark)}
TAGK={'A':'P4','B':'P3','C':'K2','O':'K1'}

def edgekey(a,b): return tuple(sorted((a,b),key=repr))

# Universal local witness: triangle + two copies of every right component type.
G=[]
for i,j in [(0,1),(0,2),(1,2)]: G.append(edgekey(('T',i),('T',j)))
for kind,nv,int_edges in [
    ('P4',4,[(0,1),(1,2),(2,3)]),
    ('P3',3,[(0,1),(1,2)]),
    ('K2',2,[(0,1)]),
    ('K1',1,[]),
]:
    tag={'P4':'A','P3':'B','K2':'C','K1':'O'}[kind]
    for block in range(2):
        for i in range(nv):
            for t in range(3): G.append(edgekey((tag,block,i),('T',t)))
        for a,b in int_edges: G.append(edgekey((tag,block,a),(tag,block,b)))
G=list(dict.fromkeys(G))
assert len(G)==75
PAIRS=[tuple(sorted(p,key=repr)) for p in combinations(G,2)]
assert len(PAIRS)==2775

# Exact automorphism-orbit reduction under terminal S3 and independent block swaps/reversals.
seen=set(); ORBITS=[]
flips=list(product([0,1],repeat=2))
for seed in PAIRS:
    if seed in seen: continue
    orb=set()
    for tp in permutations(range(3)):
      for Aperm in permutations(range(2)):
       for Aflip in flips:
        for Bperm in permutations(range(2)):
         for Bflip in flips:
          for Cperm in permutations(range(2)):
           for Cflip in flips:
            for Operm in permutations(range(2)):
             mp={('T',t):('T',tp[t]) for t in range(3)}
             for block in range(2):
                nb=Aperm[block]
                for i in range(4): mp[('A',block,i)]=('A',nb,3-i if Aflip[block] else i)
                nb=Bperm[block]
                for i in range(3): mp[('B',block,i)]=('B',nb,2-i if Bflip[block] else i)
                nb=Cperm[block]
                for i in range(2): mp[('C',block,i)]=('C',nb,1-i if Cflip[block] else i)
                mp[('O',block,0)]=('O',Operm[block],0)
             e,f=seed
             e2=edgekey(mp[e[0]],mp[e[1]]); f2=edgekey(mp[f[0]],mp[f[1]])
             orb.add(tuple(sorted((e2,f2),key=repr)))
    seen |= orb; ORBITS.append(orb)
assert len(ORBITS)==126 and len(seen)==len(PAIRS)

def core_idx(e):
    a,b=e
    if a[0]=='T' and b[0]=='T': return {(0,1):0,(0,2):1,(1,2):2}[tuple(sorted((a[1],b[1])))]
    return None

def localize(e):
    ci=core_idx(e)
    if ci is not None: return ('T',0,ci)
    a,b=e
    if a[0]=='T': t=a[1]; qv=b
    elif b[0]=='T': t=b[1]; qv=a
    else: return (a[0],a[1],('i',min(a[2],b[2]),max(a[2],b[2])))
    return (qv[0],qv[1],('s',qv[2],t))

def desc(e):
    ci=core_idx(e)
    if ci is not None: return ['T01','T02','T12'][ci]
    a,b=e
    if a[0]=='T': t=a[1]; qv=b
    elif b[0]=='T': t=b[1]; qv=a
    else: return f'{a[0]}{a[1]}:h{min(a[2],b[2])}{max(a[2],b[2])}'
    return f'{qv[0]}{qv[1]}:v{qv[2]}-T{t}'

def quantity(pair,required):
    treq=[]; layers={}
    for e in pair:
        tag,idx,loc=localize(e)
        if tag=='T':
            if e in required: treq.append(loc)
        else: layers.setdefault((tag,idx),[]).append((e,loc))
    row=TV[frozenset(treq)]
    for lid,els in sorted(layers.items(),key=repr):
        base,marks=DATA[TAGK[lid[0]]]
        req=frozenset(loc for e,loc in els if e in required)
        row=row*(base if not req else marks[req])
    return sp.expand((row*U*one)[0])

def rayleigh_poly(pair):
    e,f=pair
    I=quantity(pair,set()); Ie=quantity(pair,{e}); If=quantity(pair,{f}); Ief=quantity(pair,{e,f})
    return sp.Poly(sp.expand(Ie*If-I*Ief),*VARS,domain=sp.QQ)

def newton_coeffs(poly):
    expr=poly.as_expr(); D=poly.total_degree(); out={}
    for idx in product(range(D+1),repeat=4):
        if sum(idx)>D: continue
        c=sp.Rational(0)
        for pt in product(*[range(i+1) for i in idx]):
            mul=1
            for i,a in zip(idx,pt): mul*=comb(i,a)
            c += (-1)**sum(i-a for i,a in zip(idx,pt))*mul*expr.subs(dict(zip(VARS,pt)))
        c=sp.factor(c)
        if c: out[idx]=c
    return out

bad=[]; min_constant=None; min_positive_newton=None; negative_newton_count=0
for idx,orb in enumerate(ORBITS,1):
    rep=sorted(orb,key=repr)[0]
    poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    c0=sp.factor(poly.as_expr().subs({v:0 for v in VARS}))
    assert c0>0
    min_constant=c0 if min_constant is None else min(min_constant,c0)
    neg=[(k,c) for k,c in nc.items() if c<0]
    if neg:
        bad.append((idx,rep,poly,nc)); negative_newton_count += len(neg)
    else:
        positives=[c for c in nc.values() if c>0]
        if positives:
            mp=min(positives)
            min_positive_newton=mp if min_positive_newton is None else min(min_positive_newton,mp)
assert len(bad)==1
bidx,brep,bpoly,bnc=bad[0]
assert {desc(brep[0]),desc(brep[1])}=={'A0:v0-T0','A0:v3-T1'}
assert negative_newton_count==20
assert min_constant==2

# Exceptional orbit: nested exact staircase certificate in all four remaining-layer variables.
expr=bpoly.as_expr()
X4,X3,X2,X1=sp.symbols('X4 X3 X2 X1', integer=True, nonnegative=True)
OUTER=[(3,0,0,0),(2,0,0,1),(1,0,0,6),(0,0,0,10)]
outer_mins=[]
for sh in OUTER:
    P=sp.Poly(sp.expand(expr.subs({x4:X4+sh[0],x3:X3+sh[1],x2:X2+sh[2],x1:X1+sh[3]})),X4,X3,X2,X1,domain=sp.QQ)
    assert len(P.terms())==70 and all(c>0 for c in P.coeffs())
    outer_mins.append(min(P.coeffs()))
assert outer_mins==[sp.Rational(9,32),sp.Rational(555,2936),sp.Rational(9,32),sp.Rational(9,32)]

# Outer staircase not covered by the four shifted orthants.
OUTER_BOUNDARY=[(0,z) for z in range(10)]+[(1,z) for z in range(6)]+[(2,0)]
assert len(OUTER_BOUNDARY)==17
Y,M=sp.symbols('Y M', integer=True, nonnegative=True)
INNER=[(3,0),(2,2),(1,3),(0,5)]
inner_worst=[]
for ys,ms in INNER:
    worst=None
    for xx,zz in OUTER_BOUNDARY:
        P=sp.Poly(sp.expand(expr.subs({x4:xx,x1:zz,x3:Y+ys,x2:M+ms})),Y,M,domain=sp.QQ)
        assert len(P.terms())==15 and all(c>0 for c in P.coeffs())
        cc=min(P.coeffs()); worst=cc if worst is None else min(worst,cc)
    inner_worst.append(worst)
assert inner_worst==[
    sp.Rational(34677504,18189665),
    sp.Rational(1492992,279841),
    sp.Rational(20245248,18189665),
    sp.Rational(1492992,279841),
]

INNER_BOUNDARY=[(0,j) for j in range(5)]+[(1,j) for j in range(3)]+[(2,j) for j in range(2)]
assert len(INNER_BOUNDARY)==10
finite_vals=[]
for xx,zz in OUTER_BOUNDARY:
    for yy,mm in INNER_BOUNDARY:
        finite_vals.append((sp.factor(expr.subs({x4:xx,x3:yy,x2:mm,x1:zz})),(xx,yy,mm,zz)))
assert len(finite_vals)==170 and all(val>0 for val,_ in finite_vals)
finite_min,finite_arg=min(finite_vals,key=lambda t:t[0])
assert finite_min==447184 and finite_arg==(0,0,0,0)

# Independent direct forest enumeration for triangle joined to one P4.
def physical_graph_one_p4():
    edges=[(0,1),(0,2),(1,2)]
    right=[3,4,5,6]
    for rv in right:
        for t in range(3): edges.append((t,rv))
    edges += [(3,4),(4,5),(5,6)]
    return 7,edges

def brute_one_p4():
    nv,edges=physical_graph_one_p4(); E=len(edges)
    Z=0; onec=[0]*E; twoc=[[0]*E for _ in range(E)]
    for mask in range(1<<E):
        d=DSU(nv); chosen=[]; bad=False
        for j,(a,b) in enumerate(edges):
            if (mask>>j)&1:
                if not d.union(a,b): bad=True; break
                chosen.append(j)
        if bad: continue
        Z+=1
        for j in chosen: onec[j]+=1
        for i,j in combinations(chosen,2): twoc[i][j]+=1; twoc[j][i]+=1
    gaps=[(onec[i]*onec[j]-Z*twoc[i][j],i,j) for i,j in combinations(range(E),2)]
    return nv,E,Z,min(gaps),max(gaps)
BRUTE=brute_one_p4()
assert BRUTE==(7,18,14860,(127864,3,17),(5945384,13,14))

print('NM13-04 T07 TRIANGLE + RIGHT LINEAR FOREST, COMPONENT ORDER <=4')
print('N^3=0 and transfers: P4=734I+780N+(961/3)N^2; P3=130I+103N+(85/3)N^2; K2=23I+12N+(5/3)N^2; K1=4I+N: PASS')
print('triangle initial response =',list(q))
print('universal witness edges =',len(G),'edge pairs =',len(PAIRS),'automorphism orbits =',len(ORBITS))
print('Newton-positive orbits =',len(ORBITS)-len(bad),'exceptional orbits =',len(bad),'exceptional negative Newton coefficients =',negative_newton_count)
print('minimum orbit constant =',min_constant,'minimum positive Newton coefficient among 125 regular orbits =',min_positive_newton)
print('exceptional orbit =',bidx,desc(brep[0]),desc(brep[1]))
print('outer shifted-orthant minima =',outer_mins)
print('outer staircase points =',len(OUTER_BOUNDARY),'inner shifted-quadrant worst minima =',inner_worst)
print('finite residual lattice points =',len(finite_vals),'minimum =',finite_min,'at (P4,P3,K2,K1 extras) =',finite_arg)
print('BRUTE one P4: n,m,Z,min_gap,max_gap =',BRUTE)
print('ALL_EXACT_CHECKS_PASS')
