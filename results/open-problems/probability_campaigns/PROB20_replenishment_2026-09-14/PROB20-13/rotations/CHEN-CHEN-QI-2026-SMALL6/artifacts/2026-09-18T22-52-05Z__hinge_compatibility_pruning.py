from itertools import combinations
from fractions import Fraction
from collections import defaultdict, Counter
from functools import lru_cache

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
PRIME=1000003

def product_key(p,q):
    return (tuple(sorted((p[0],q[0]))), tuple(sorted((p[1],q[1]))))

def displayed_forms(extra_pairs):
    return [(p,) for p in E1] + [tuple(p) for p in extra_pairs]

def coeff_matrix(extra_pairs):
    forms=displayed_forms(extra_pairs)
    N=len(forms)
    vars_=list(combinations(range(N),2))
    bykey=defaultdict(lambda: defaultdict(int))
    for vid,(a,b) in enumerate(vars_):
        for p in forms[a]:
            for q in forms[b]:
                bykey[product_key(p,q)][vid]+=1
    rows=[dict(d) for d in bykey.values()]
    return rows,len(vars_)

def rank_mod(rows,ncols,p=PRIME):
    rows=[{j:(v%p) for j,v in r.items() if v%p} for r in rows]
    rank=0
    col_to_row={}
    for r in rows:
        while r:
            c=min(r)
            if c not in col_to_row:
                inv=pow(r[c],p-2,p)
                r={j:(v*inv)%p for j,v in r.items() if (v*inv)%p}
                col_to_row[c]=r
                rank+=1
                break
            piv=col_to_row[c]
            a=r[c]
            nr=dict(r)
            for j,v in piv.items():
                nv=(nr.get(j,0)-a*v)%p
                if nv: nr[j]=nv
                elif j in nr: del nr[j]
            r=nr
    return rank

def rank_q(rows,ncols):
    rows=[{j:Fraction(v) for j,v in r.items() if v} for r in rows]
    pivots={}
    rank=0
    for r in rows:
        while r:
            c=min(r)
            if c not in pivots:
                a=r[c]
                r={j:v/a for j,v in r.items() if v/a}
                pivots[c]=r
                rank+=1
                break
            piv=pivots[c]
            a=r[c]
            nr=dict(r)
            for j,v in piv.items():
                nv=nr.get(j,Fraction(0))-a*v
                if nv: nr[j]=nv
                elif j in nr: del nr[j]
            r=nr
    return rank

def kernel_dim(extra_pairs):
    rows,ncols=coeff_matrix(extra_pairs)
    rm=rank_mod(rows,ncols)
    if rm==ncols:
        return 0
    rq=rank_q(rows,ncols)
    return ncols-rq

def hinge_centers(pair):
    (r1,c1),(r2,c2)=pair
    out=[]
    for r0,c0 in E1:
        if ((r1,c0) in S and (r0,c1) in S and
            (r2,c0) in S and (r0,c2) in S):
            out.append((r0,c0))
    return out

def arms(h):
    r0,c0=h
    return sorted((r,c) for r,c in C if (r,c0) in S and (r0,c) in S)

# 1) Single-pair hinge classification.
hinge_bad=[]
good=[]
dim_counts=Counter()
center_mult=Counter()
for p in PAIRS:
    hs=hinge_centers(p)
    d=kernel_dim([p])
    dim_counts[d]+=1
    assert (d>0)==bool(hs), (p,d,hs)
    if hs:
        assert d==1
        assert len(hs)==1
        hinge_bad.append(p)
        center_mult[hs[0]]+=1
    else:
        good.append(p)
assert len(hinge_bad)==56 and len(good)==134
assert dim_counts==Counter({0:134,1:56})
arm_sizes={h:len(arms(h)) for h in E1}
assert Counter(arm_sizes.values())==Counter({2:8,4:8})
assert sum((n*(n-1))//2 for n in arm_sizes.values())==56
assert all(center_mult[h]==(arm_sizes[h]*(arm_sizes[h]-1))//2 for h in E1)

# 2) Pairwise necessary compatibility graph among hinge-free E2 pair-squares.
forbidden=[]
compatible=0
pair_dim_counts=Counter()
for i,a in enumerate(good):
    A=set(a)
    for b in good[i+1:]:
        if A & set(b):
            continue
        d=kernel_dim([a,b])
        pair_dim_counts[d]+=1
        if d:
            forbidden.append((a,b,d))
        else:
            compatible+=1
assert compatible==7125
assert len(forbidden)==122
assert pair_dim_counts==Counter({0:7125,1:98,2:24})

# 3) Exact residual count of 8-edge matchings on 20 complement cells after hinge-only pruning.
idx={x:i for i,x in enumerate(C)}
adj=[0]*20
for a,b in good:
    i,j=idx[a],idx[b]
    adj[i]|=1<<j
    adj[j]|=1<<i

@lru_cache(None)
def count_matchings(mask,k):
    if k==0: return 1
    if mask.bit_count()<2*k: return 0
    i=(mask & -mask).bit_length()-1
    # i may be a hole
    total=count_matchings(mask & ~(1<<i),k)
    nbr=adj[i] & mask & ~((1<<(i+1))-1)
    while nbr:
        bit=nbr & -nbr
        j=bit.bit_length()-1
        total += count_matchings(mask & ~(1<<i) & ~(1<<j),k-1)
        nbr-=bit
    return total
residual=count_matchings((1<<20)-1,8)
assert residual==643815003

# 4) Source witness survives all necessary filters.
source_pairs=[tuple(sorted(x)) for x in SOURCE_E2]
assert all(p in good for p in source_pairs)
for a,b in combinations(source_pairs,2):
    assert not (set(a)&set(b))
    assert kernel_dim([a,b])==0

print('HINGE_SINGLE_PAIR_CLASSIFICATION total=190 forbidden=56 allowed=134 kernel_dims={0:134,1:56}')
print('HINGE_CENTER_SIZE_DISTRIBUTION size2=8 size4=8 double_count=56 unique_center=True')
for h in sorted(E1):
    print('HINGE_ARMS center=%s size=%d arms=%s' % (h,arm_sizes[h],arms(h)))
print('PAIRWISE_COMPATIBILITY_GRAPH vertices=134 disjoint_tests=7247 compatible_edges=7125 forbidden=122 kernel_dims={0:7125,1:98,2:24}')
print('HINGE_ONLY_RESIDUAL_N24_MATCHINGS_8_EDGES_4_HOLES=%d' % residual)
print('SOURCE_WITNESS_FILTER_CHECK all_8_vertices_allowed=True all_28_pairwise_compatible=True')
for a,b,d in forbidden[:8]:
    print('FORBIDDEN_EXAMPLE a=%s b=%s kernel_dim=%d' % (a,b,d))
print('ALL_EXACT_CHECKS_PASS')
