from itertools import combinations, combinations_with_replacement, permutations
from collections import defaultdict, Counter
from fractions import Fraction
from math import gcd
from functools import reduce
import sympy as sp

E1 = [
    (1,1),(1,2),(2,3),(2,4),(3,1),(3,3),(3,5),(4,2),
    (4,4),(4,5),(5,2),(5,3),(5,6),(6,1),(6,4),(6,6),
]
SOURCE_E2 = [
    ((1,4),(6,5)),((1,5),(2,2)),((3,6),(6,2)),((2,6),(4,3)),
    ((1,6),(2,5)),((3,4),(5,1)),((1,3),(4,1)),((5,5),(6,3)),
]
S=set(E1)
ALL={(i,j) for i in range(1,7) for j in range(1,7)}
C=sorted(ALL-S)
PAIRS=[tuple(sorted(p)) for p in combinations(C,2)]
P=1000003

def product_key(p,q):
    return (tuple(sorted((p[0],q[0]))), tuple(sorted((p[1],q[1]))))

def hinge_centers(pair):
    (r1,c1),(r2,c2)=pair
    out=[]
    for r0,c0 in E1:
        if ((r1,c0) in S and (r0,c1) in S and
            (r2,c0) in S and (r0,c2) in S):
            out.append((r0,c0))
    return out

good=[p for p in PAIRS if not hinge_centers(p)]
assert len(good)==134
pair_to_idx={p:i for i,p in enumerate(good)}
source_idx=[pair_to_idx[tuple(sorted(p))] for p in SOURCE_E2]

base_keys={product_key(a,b) for a,b in combinations(E1,2)}
assert len(base_keys)==120
allkeys=[(ri,cj) for ri in combinations_with_replacement(range(1,7),2)
                 for cj in combinations_with_replacement(range(1,7),2)]
rowid={k:i for i,k in enumerate(k for k in allkeys if k not in base_keys)}
assert len(rowid)==321

def cand_base_cols(pair):
    a,b=pair
    cols=[]
    for c in E1:
        d={}
        for x in (a,b):
            k=product_key(x,c)
            if k not in base_keys:
                r=rowid[k]
                d[r]=d.get(r,0)+1
        cols.append(d)
    return cols

def cross_col(a,b):
    d={}
    for x in a:
        for y in b:
            k=product_key(x,y)
            if k not in base_keys:
                r=rowid[k]
                d[r]=d.get(r,0)+1
    return {r:v for r,v in d.items() if v}

cand_cols=[cand_base_cols(g) for g in good]

def rank_mod(cols):
    basis={}
    rank=0
    for vec in cols:
        v={r:(x%P) for r,x in vec.items() if x%P}
        while v:
            c=min(v)
            if c not in basis:
                inv=pow(v[c],P-2,P)
                v={r:(x*inv)%P for r,x in v.items() if (x*inv)%P}
                basis[c]=v
                rank+=1
                break
            b=basis[c]; a=v[c]
            nv=dict(v)
            for r,x in b.items():
                y=(nv.get(r,0)-a*x)%P
                if y: nv[r]=y
                elif r in nv: del nv[r]
            v=nv
    return rank

def rank_q(cols):
    basis={}
    rank=0
    for vec in cols:
        v={r:Fraction(x) for r,x in vec.items() if x}
        while v:
            c=min(v)
            if c not in basis:
                a=v[c]
                v={r:x/a for r,x in v.items() if x/a}
                basis[c]=v
                rank+=1
                break
            b=basis[c]; a=v[c]
            nv=dict(v)
            for r,x in b.items():
                y=nv.get(r,Fraction(0))-a*x
                if y: nv[r]=y
                elif r in nv: del nv[r]
            v=nv
    return rank

def exact_dim(cols):
    rm=rank_mod(cols)
    if rm==len(cols):
        return 0
    return len(cols)-rank_q(cols)

def cols_for(ids):
    ids=tuple(ids)
    cols=[]
    for i in ids:
        cols += cand_cols[i]
    for i,j in combinations(ids,2):
        cols.append(cross_col(good[i],good[j]))
    return cols

compat=[[False]*134 for _ in range(134)]
pair_bad=[]
for i in range(134):
    for j in range(i+1,134):
        if set(good[i]) & set(good[j]):
            continue
        d=exact_dim(cols_for((i,j)))
        if d:
            pair_bad.append((i,j,d))
        else:
            compat[i][j]=compat[j][i]=True
assert len(pair_bad)==122
assert Counter(d for _,_,d in pair_bad)==Counter({1:98,2:24})

triple_total=0
triple_bad=[]
for i in range(134):
    for j in range(i+1,134):
        if not compat[i][j]: continue
        for k in range(j+1,134):
            if not compat[i][k] or not compat[j][k]: continue
            triple_total+=1
            cols=cols_for((i,j,k))
            rm=rank_mod(cols)
            if rm<len(cols):
                d=len(cols)-rank_q(cols)
                if d:
                    triple_bad.append((i,j,k,d))
assert triple_total==195272
assert len(triple_bad)==256
assert Counter(d for *_,d in triple_bad)==Counter({1:256})
triple_set={x[:3] for x in triple_bad}

def primitive_null(ids):
    cols=cols_for(ids)
    used=sorted({r for col in cols for r in col})
    pos={r:i for i,r in enumerate(used)}
    M=sp.zeros(len(used),len(cols))
    for j,col in enumerate(cols):
        for r,x in col.items(): M[pos[r],j]=x
    ns=M.nullspace()
    assert len(ns)==1
    v=ns[0]
    den=sp.ilcm(*[q.q for q in v])
    vals=[int(q*den) for q in v]
    g=reduce(gcd,[abs(x) for x in vals if x])
    vals=[x//g for x in vals]
    first=next(x for x in vals if x)
    if first<0: vals=[-x for x in vals]
    return vals

support_dist=Counter()
cross_dist=Counter()
coeff_abs=Counter()
for i,j,k,d in triple_bad:
    vals=primitive_null((i,j,k))
    supp=[q for q,x in enumerate(vals) if x]
    support_dist[len(supp)]+=1
    cross=sum(q in (48,49,50) for q in supp)
    cross_dist[(len(supp),cross)]+=1
    coeff_abs[tuple(sorted(abs(vals[q]) for q in supp))]+=1
assert support_dist==Counter({3:208,5:24,2:16,4:8})
assert cross_dist==Counter({(3,0):168,(3,1):40,(5,1):24,(2,1):16,(4,0):8})
assert all(set(k)=={1} for k in coeff_abs)

def map_cell(p,rp,cp): return (rp[p[0]-1],cp[p[1]-1])
autos=[]
for rp in permutations(range(1,7)):
    for cp in permutations(range(1,7)):
        if {map_cell(p,rp,cp) for p in E1}==S:
            autos.append((rp,cp))
assert len(autos)==8

def map_pair(p,a):
    rp,cp=a
    return tuple(sorted(map_cell(x,rp,cp) for x in p))
def map_triple(t,a):
    return tuple(sorted(pair_to_idx[map_pair(good[i],a)] for i in t))
seen=set(); orbit_reps=[]; orbit_sizes=[]
for t in sorted(triple_set):
    if t in seen: continue
    orb={map_triple(t,a) for a in autos}
    assert orb<=triple_set
    seen |= orb
    orbit_reps.append(min(orb)); orbit_sizes.append(len(orb))
assert len(orbit_reps)==42
assert Counter(orbit_sizes)==Counter({8:23,4:17,2:2})

for t in combinations(sorted(source_idx),3):
    assert t not in triple_set

print('PAIRWISE_COMPATIBLE vertices=134 pair_nonfaces=122 pair_dim_counts={1:98,2:24}')
print('TRIPLE_TESTS pairwise_compatible_cell_disjoint=195272 exact_triple_nonfaces=256 all_dim1=True')
print('TRIPLE_NONFACE_ORBITS count=42 orbit_sizes={2:2,4:17,8:23}')
print('PRIMITIVE_CIRCUITS support_sizes={2:16,3:208,4:8,5:24}')
print('PRIMITIVE_CIRCUITS cross_product_counts={(2,1):16,(3,0):168,(3,1):40,(4,0):8,(5,1):24}')
print('PRIMITIVE_CIRCUITS coefficients_abs_all_one=True')
print('SOURCE_WITNESS all_56_triples_survive=True')
for rep in orbit_reps[:12]:
    vals=primitive_null(rep)
    supp=[(q,vals[q]) for q in range(len(vals)) if vals[q]]
    print('ORBIT_REP ids=%s pairs=%s support=%s' % (rep,[good[i] for i in rep],supp))
print('ALL_EXACT_CHECKS_PASS')
