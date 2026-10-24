import itertools
import sympy as sp

V=tuple(range(6))
EDGES=list(itertools.combinations(V,2))
EID={e:i for i,e in enumerate(EDGES)}
def ix(c,e): return 15*c+EID[tuple(sorted(e))]

# 90 deterministic colored perfect matchings = balanced 3-colorings.
STATES=[]
for coloring in itertools.product(range(3), repeat=6):
    if all(coloring.count(c)==2 for c in range(3)):
        row=[0]*45
        for c in range(3):
            pts=[v for v in V if coloring[v]==c]
            row[ix(c,tuple(pts))]=1
        STATES.append(row)
assert len(STATES)==90

# Exact affine dimension.
def affdim(rows):
    M=sp.Matrix([[1]+list(r) for r in rows])
    return M.rank()-1
assert affdim(STATES)==37

# Representative target color 0, target edge (0,1), complement K4.
tc=0; te=(0,1); c0,c1=1,2
C=tuple(v for v in V if v not in te)
BASES=list(itertools.combinations(C,2))
assert BASES==[(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]

def fibre_row(mask):
    a=[0]*45
    a[ix(tc,te)]=1
    for j,B in enumerate(BASES):
        comp=tuple(sorted(set(C)-set(B)))
        if (mask>>j)&1:
            a[ix(c0,B)]-=1
        else:
            a[ix(c1,comp)]-=1
    return a,0

def eval_ineq(a,b,row): return b-sum(ai*xi for ai,xi in zip(a,row))

mask_dims={}
for mask in range(64):
    a,b=fibre_row(mask)
    active=[r for r in STATES if eval_ineq(a,b,r)==0]
    assert all(eval_ineq(a,b,r)>=0 for r in STATES)
    mask_dims[mask]=affdim(active)

expected34={11,21,38,56}
assert {m for m,d in mask_dims.items() if d==34}==expected34
assert {m for m,d in mask_dims.items() if d==35}=={0,63}
assert sum(d==36 for d in mask_dims.values())==58
print('representative fibre mask dimensions:', {d:sum(v==d for v in mask_dims.values()) for d in (34,35,36)})
print('dim34 masks:', sorted(expected34), 'dim35 masks: [0,63]')

# Helpers for exact coefficient-vector identities.
def unit_vec(c,e,coef=1):
    r=[sp.Rational(0)]*45; r[ix(c,e)]=sp.Rational(coef); return r

def add(*rows): return [sum(vals) for vals in zip(*rows)]
def scale(q,row): return [sp.Rational(q)*v for v in row]

def vertex_degree(v):
    r=[sp.Rational(0)]*45
    for c in range(3):
        for e in EDGES:
            if v in e: r[ix(c,e)]+=1
    return r

# Triangle mask 11: S={(2,3),(2,4),(3,4)}, remaining vertex d=5.
a11,_=fibre_row(11)
# s1 target color0 on A={0,1,5}, complement T={2,3,4}:
s1=[sp.Rational(0)]*45
A={0,1,5}; T={2,3,4}
for e in EDGES:
    if set(e)<=A: s1[ix(0,e)]+=1
    if set(e)<=T:
        s1[ix(1,e)]-=1; s1[ix(2,e)]-=1
# Fibre lhs <=0 equals s1 lhs minus x0(05)-x0(15).
tri_identity=add(s1, scale(-1,unit_vec(0,(0,5))), scale(-1,unit_vec(0,(1,5))))
assert list(map(sp.Rational,a11))==tri_identity
print('triangle-mask redundancy identity verified exactly')

# Mask0 identity using s2 singled color2 on complement edge01 + nonneg x1(01) + degree equality.
a0,_=fibre_row(0)
s2=[sp.Rational(0)]*45
A=set(C)
for c in (0,1):
    for e in EDGES:
        if set(e)<=A: s2[ix(c,e)]+=1
s2[ix(2,te)]-=1
# s2 <=1. Add -x1(01)<=0, plus E=1/2(D0+D1-D2-D3-D4-D5)=-1.
E=scale(sp.Rational(1,2), add(vertex_degree(0),vertex_degree(1),
                              scale(-1,vertex_degree(2)),scale(-1,vertex_degree(3)),
                              scale(-1,vertex_degree(4)),scale(-1,vertex_degree(5))))
mask0_identity=add(s2, scale(-1,unit_vec(1,te)), E)
assert list(map(sp.Rational,a0))==mask0_identity
# RHS 1+0-1=0, matching fibre rhs0.
print('mask0 redundancy identity verified exactly')

# Mask63 analog: s2 singled color1 + -x2(01) + same E.
a63,_=fibre_row(63)
s2b=[sp.Rational(0)]*45
for c in (0,2):
    for e in EDGES:
        if set(e)<=A: s2b[ix(c,e)]+=1
s2b[ix(1,te)]-=1
mask63_identity=add(s2b, scale(-1,unit_vec(2,te)), E)
assert list(map(sp.Rational,a63))==mask63_identity
print('mask63 redundancy identity verified exactly')

# Representative exact facet dimensions for all five proposed orbit types.
def equality_dim(a,b):
    active=[r for r in STATES if eval_ineq(a,b,r)==0]
    assert all(eval_ineq(a,b,r)>=0 for r in STATES)
    return len(active),affdim(active),sorted(set(eval_ineq(a,b,r) for r in STATES))

reps={}
# nonneg x0(01)>=0 -> -x0(01)<=0
reps['nonneg']=([-v for v in unit_vec(0,(0,1))],0)
# fibre choose mask1 (facet)
reps['fibre']=fibre_row(1)
# blossom S={0,1,2}: sum all color edges inside S <=1
bl=[0]*45
S={0,1,2}
for c in range(3):
    for e in EDGES:
        if set(e)<=S: bl[ix(c,e)]+=1
reps['blossom']=(bl,1)
# s1 target0 A=012, B=345
s1r=[0]*45
A1={0,1,2}; B1={3,4,5}
for e in EDGES:
    if set(e)<=A1: s1r[ix(0,e)]+=1
    if set(e)<=B1:
        s1r[ix(1,e)]-=1; s1r[ix(2,e)]-=1
reps['s1']=(s1r,0)
# s2 singled color0 complement edge01: sum c1,c2 inside C - x0(01)<=1
s2r=[0]*45
for c in (1,2):
    for e in EDGES:
        if set(e)<=set(C): s2r[ix(c,e)]+=1
s2r[ix(0,te)]-=1
reps['s2']=(s2r,1)

for name,(a,b) in reps.items():
    active,dim,slacks=equality_dim(a,b)
    assert dim==36
    assert slacks==[0,1]
    print(name, 'active=',active,'face_dim=',dim,'slacks=',slacks)

# Orbit counts under the natural S6 x S3 symmetry.
counts={
    'nonneg':45,
    'fibre_facets':45*58,
    'blossom':20,
    's1':60,
    's2':45,
}
assert counts['fibre_facets']==2610
assert sum(counts.values())==2780
print('candidate genuine-facet orbit counts:',counts)
print('total known genuine facets:',sum(counts.values()))
print('known non-bound facets:',sum(counts.values())-counts['nonneg'])
print('nonfacet fibre cuts redundant by symmetry:',45*(2+4))
