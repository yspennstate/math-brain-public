"""Exact finite certificate for PROB20-12, 2026-09-15T183128Z.

Checks:
  * K6 colored-perfect-matching polytope affine dimension 37;
  * 2-2-2 bridge inequality is a facet, has 0/1 slack, orbit size 270;
  * exact coefficient identity bounding the Cauchy auxiliary factor B by a
    previously proved single-fibre inequality + nonnegativity + affine degrees;
  * residue facet is a facet with orbit size 360 and 0/1 slack;
  * sparse-cover facet is a facet with orbit size 1080 and 0/1 slack;
  * complement duplication counts for blossom and s1 families.

All rank/orbit checks use exact integer arithmetic / SymPy. No floating-point
LP conclusion is used as a certificate.
"""

import itertools
import math
import sympy as sp

V=tuple(range(6))
EDGES=list(itertools.combinations(V,2))
EID={e:i for i,e in enumerate(EDGES)}
def edge(e): return tuple(sorted(e))
def ix(c,e): return 15*c+EID[edge(e)]

# 90 balanced three-colorings / labeled perfect matchings.
STATES=[]
for coloring in itertools.product(range(3), repeat=6):
    if all(coloring.count(c)==2 for c in range(3)):
        row=[0]*45
        for c in range(3):
            pts=tuple(v for v in V if coloring[v]==c)
            row[ix(c,pts)]=1
        STATES.append(row)
assert len(STATES)==90

def affdim(rows):
    return sp.Matrix([[1]+list(r) for r in rows]).rank()-1
assert affdim(STATES)==37

def slack(a,b,row):
    return sp.Rational(b)-sum(sp.Rational(ai)*xi for ai,xi in zip(a,row))

def facet_check(a,b):
    vals=[slack(a,b,r) for r in STATES]
    assert min(vals)>=0
    active=[r for r,s in zip(STATES,vals) if s==0]
    assert affdim(active)==36
    assert set(vals)=={sp.Rational(0),sp.Rational(1)}
    return len(active)

def transform_coeff(a, vp, cp):
    out=[0]*45
    for c in range(3):
        for e in EDGES:
            ee=edge((vp[e[0]],vp[e[1]]))
            out[ix(cp[c],ee)]=a[ix(c,e)]
    return out

def orbit_active_sets(a,b):
    out=set()
    for vp_tuple in itertools.permutations(V):
        vp={i:vp_tuple[i] for i in V}
        for cp_tuple in itertools.permutations(range(3)):
            cp={i:cp_tuple[i] for i in range(3)}
            aa=transform_coeff(a,vp,cp)
            act=tuple(j for j,r in enumerate(STATES) if slack(aa,b,r)==0)
            out.add(act)
    return out

# -------------------------------------------------------------------------
# 1. Bridge facet: L={0,3}, D={1,2}, R={4,5}, singled color 0.
#    mu0(E(LuD)\{D}) <= mu1(E(DuR)\{D})+mu2(...).
# -------------------------------------------------------------------------
L={0,3}; D={1,2}; R={4,5}
def inside(S): return [e for e in EDGES if set(e)<=set(S)]
SA=[e for e in inside(L|D) if set(e)!=D]
SB=[e for e in inside(D|R) if set(e)!=D]
assert set(SA)=={(0,1),(0,2),(0,3),(1,3),(2,3)}
assert set(SB)=={(1,4),(1,5),(2,4),(2,5),(4,5)}
bridge=[0]*45
for e in SA: bridge[ix(0,e)]+=1
for c in (1,2):
    for e in SB: bridge[ix(c,e)]-=1
assert facet_check(bridge,0)==60
bridge_orbit=orbit_active_sets(bridge,0)
assert len(bridge_orbit)==270
assert 4320//len(bridge_orbit)==16
print('bridge facet: active=60 orbit=270 stabilizer=16')

# -------------------------------------------------------------------------
# 2. Exact linear identity proving the Cauchy auxiliary factor B <= 1.
#
# B = sum_{e subset {1,2,4,5}} mu0(e)
#     +mu1(12)+mu2(12)-mu1(03)-mu2(03).
#
# It equals fibre(mask36,target color0,edge03)
#      -mu1(14)-mu1(24)-mu1(25)-mu2(24)
#      + 1/2(-D0+D1+D2-D3+D4+D5).
# -------------------------------------------------------------------------

def unit(c,e,coef=1):
    r=[sp.Rational(0)]*45; r[ix(c,e)]=sp.Rational(coef); return r

def add(*rows): return [sum(vs) for vs in zip(*rows)]
def scale(q,row): return [sp.Rational(q)*v for v in row]

def degree(v):
    r=[sp.Rational(0)]*45
    for c in range(3):
        for e in EDGES:
            if v in e: r[ix(c,e)]+=1
    return r

B=[sp.Rational(0)]*45
for e in inside({1,2,4,5}): B[ix(0,e)]+=1
B[ix(1,(1,2))]+=1; B[ix(2,(1,2))]+=1
B[ix(1,(0,3))]-=1; B[ix(2,(0,3))]-=1

# Fibre mask 36 for target color0 edge03. Complement bases ordered
# 12,14,15,24,25,45; mask36 selects 15,45 for color1.
te=(0,3); C=tuple(v for v in V if v not in te)
bases=list(itertools.combinations(C,2))
assert bases==[(1,2),(1,4),(1,5),(2,4),(2,5),(4,5)]
fib=[sp.Rational(0)]*45; fib[ix(0,te)]=1
mask=36
for j,e in enumerate(bases):
    comp=edge(set(C)-set(e))
    if (mask>>j)&1: fib[ix(1,e)]-=1
    else: fib[ix(2,comp)]-=1

Edeg=scale(sp.Rational(1,2), add(
    scale(-1,degree(0)), degree(1), degree(2),
    scale(-1,degree(3)), degree(4), degree(5)))
identity=add(fib,
             scale(-1,unit(1,(1,4))),
             scale(-1,unit(1,(2,4))),
             scale(-1,unit(1,(2,5))),
             scale(-1,unit(2,(2,4))),
             Edeg)
assert identity==B
# Degree expression has constant value 1 on every deterministic state.
assert all(sum(a*x for a,x in zip(Edeg,r))==1 for r in STATES)
print('auxiliary B<=1 coefficient identity verified exactly')

# -------------------------------------------------------------------------
# 3. Residue facet orbit 360.
# T={0,1,3}, d=2, R={4,5}.
# A=E(T) U dR, B=dT U E(R), C=T x R.
# mu0(A)+mu1(B)+mu2(C)-mu1(A)-mu2(B)-mu0(C)<=1.
# -------------------------------------------------------------------------
T={0,1,3}; d=2; RR={4,5}
A=set(inside(T)) | {edge((d,r)) for r in RR}
BB={edge((d,t)) for t in T} | set(inside(RR))
CC={edge((t,r)) for t in T for r in RR}
assert len(A)==5 and len(BB)==4 and len(CC)==6
assert A|BB|CC==set(EDGES) and not(A&BB or A&CC or BB&CC)
residue=[0]*45
for e in A: residue[ix(0,e)]+=1; residue[ix(1,e)]-=1
for e in BB: residue[ix(1,e)]+=1; residue[ix(2,e)]-=1
for e in CC: residue[ix(2,e)]+=1; residue[ix(0,e)]-=1
assert facet_check(residue,1)==60
res_orbit=orbit_active_sets(residue,1)
assert len(res_orbit)==360
assert 4320//len(res_orbit)==12
# Modular classification: vertex weights 1 on T, 0 on d, 2 on R.
w={v:(1 if v in T else 2 if v in RR else 0) for v in V}
assert all((w[u]+w[v])%3==2 for u,v in A)
assert all((w[u]+w[v])%3==1 for u,v in BB)
assert all((w[u]+w[v])%3==0 for u,v in CC)
print('residue facet: active=60 orbit=360 stabilizer=12')

# -------------------------------------------------------------------------
# 4. Sparse-cover facet orbit 1080.
# mu0(01)+mu0(02) <= mu1(15,25,34,35,45)+mu2(35,45).
# -------------------------------------------------------------------------
sparse=[0]*45
for e in [(0,1),(0,2)]: sparse[ix(0,e)]+=1
for e in [(1,5),(2,5),(3,4),(3,5),(4,5)]: sparse[ix(1,e)]-=1
for e in [(3,5),(4,5)]: sparse[ix(2,e)]-=1
assert facet_check(sparse,0)==60
sp_orbit=orbit_active_sets(sparse,0)
assert len(sp_orbit)==1080
assert 4320//len(sp_orbit)==4
print('sparse facet: active=60 orbit=1080 stabilizer=4')

# -------------------------------------------------------------------------
# 5. Complement duplicate corrections for old blossom and s1 rows.
# -------------------------------------------------------------------------
def active_set(a,b):
    return tuple(j for j,r in enumerate(STATES) if slack(a,b,r)==0)

bloss=[]
for SS in itertools.combinations(V,3):
    S=set(SS); a=[0]*45
    for c in range(3):
        for e in EDGES:
            if set(e)<=S: a[ix(c,e)]+=1
    bloss.append(active_set(a,1))
assert len(set(bloss))==10

s1=[]
for tc in range(3):
    others=[c for c in range(3) if c!=tc]
    for AA in itertools.combinations(V,3):
        A0=set(AA); B0=set(V)-A0; a=[0]*45
        for e in EDGES:
            if set(e)<=A0: a[ix(tc,e)]+=1
            if set(e)<=B0:
                for c in others: a[ix(c,e)]-=1
        s1.append(active_set(a,0))
assert len(set(s1))==30
print('old distinct-facet correction: blossom=10, s1=30')
print('old distinct total = 45+2610+10+30+45 =',45+2610+10+30+45)
print('with proved bridge orbit =',45+2610+10+30+45+270)

print('ALL EXACT CERTIFICATE CHECKS PASSED')
