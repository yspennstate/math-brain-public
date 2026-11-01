#!/usr/bin/env python3
"""
R13 exact finite-core checker for the n=7 Boolean Komlos improvement.

All acceptance tests are integer/rational. No floating-point inequality is used.

Finite lemma checked:
For every downset F subset 2^[7] of Hamming diameter <=4, let M be its
set of maximal members, h=|M|, d_j=# {M in M: j in M}, and b=|F|.
Uniformly choose a maximal member, then thin coordinate j independently
with retention theta_j=min(1,h/(2 d_j)) (theta_j=0 if d_j=0).
The resulting mean sign c has
    ||c||_2^2 = sum_j max(h-2 d_j,0)^2 / h^2
and this checker verifies
    b * sum_j max(h-2 d_j,0)^2 <= 48 h^2
for every possible maximal-antichain type.

Enumeration is exact:
 rank 0/1: direct;
 rank 2: every graph on 7 vertices plus any subset of isolated singleton maxima;
 rank 3: every pairwise-compatible triple clique, represented by the exact
         star/top classification, plus every compatible pair maximum and
         every optional uncovered singleton maximum;
 rank 4: a single 4-set (any other maximal member would be contained in it).
"""
from itertools import combinations
from math import gcd

N=7
PAIR_TUPLES=list(combinations(range(N),2))
PAIR_MASKS=[sum(1<<i for i in c) for c in PAIR_TUPLES]

def pop(x): return x.bit_count()

def submasks(m):
    s=m
    while True:
        yield s
        if s==0: break
        s=(s-1)&m

def closure_size(maxs):
    F={0}
    for m in maxs:
        F.update(submasks(m))
    return len(F)

def cert(maxs):
    h=len(maxs)
    ds=[sum((m>>j)&1 for m in maxs) for j in range(N)]
    num=sum(max(h-2*d,0)**2 for d in ds)
    b=closure_size(maxs)
    lhs=b*num
    rhs=48*h*h
    return lhs,rhs,b,num,h,ds

def frac(a,b):
    g=gcd(a,b)
    return f"{a//g}/{b//g}"

print("R13 n=7 diameter-four exact checker")

# Rank 0: F={empty}. Mean sign is all +1.
assert 1*7 <= 48
print("rank0_cases = 1")

# Rank 1: maximal family is any nonempty set of k singleton maxima.
rank1=0
rank1_max=(0,1,None)
for k in range(1,N+1):
    maxs=[1<<j for j in range(k)]
    lhs,rhs,b,num,h,ds=cert(maxs)
    assert lhs<=rhs
    rank1+=1
    if lhs*rank1_max[1] > rank1_max[0]*rhs:
        rank1_max=(lhs,rhs,k)
print("rank1_orbit_cases =",rank1)
print("rank1_max_ratio =",frac(rank1_max[0],rank1_max[1]),"at k =",rank1_max[2])

# Rank 2: every graph E on [7], and any subset of isolated vertices may be
# included as singleton maxima. Every rank-2 maximal antichain is uniquely
# of this form.
rank2_cases=0
rank2_max=(0,1,None)
deg=[0]*N
gray=0
for idx in range(1<<len(PAIR_TUPLES)):
    if idx:
        newgray=idx^(idx>>1)
        oldgray=(idx-1)^((idx-1)>>1)
        bit=(newgray^oldgray).bit_length()-1
        i,j=PAIR_TUPLES[bit]
        if (newgray>>bit)&1:
            deg[i]+=1; deg[j]+=1
        else:
            deg[i]-=1; deg[j]-=1
        gray=newgray
    else:
        gray=0
    edges=[PAIR_MASKS[k] for k in range(len(PAIR_MASKS)) if (gray>>k)&1]
    isolated=[j for j,d in enumerate(deg) if d==0]
    for sm in range(1<<len(isolated)):
        singles=[1<<isolated[t] for t in range(len(isolated)) if (sm>>t)&1]
        maxs=edges+singles
        if not maxs:
            continue
        lhs,rhs,b,num,h,ds=cert(maxs)
        assert lhs<=rhs
        rank2_cases+=1
        if lhs*rank2_max[1] > rank2_max[0]*rhs:
            rank2_max=(lhs,rhs,(gray,sm,b,num,h,tuple(ds)))
print("rank2_exact_configs =",rank2_cases)
print("rank2_max_ratio =",frac(rank2_max[0],rank2_max[1]))
print("rank2_max_witness_stats =",rank2_max[2])

# Rank 3: generate every nonempty clique of triples with pairwise union <=4.
# Analytically every such clique is either a subfamily of the 5 triples
# through a fixed pair (star), or a subfamily of the 4 triples inside a
# fixed 4-set (top). Duplicates are removed exactly.
Hs=set()
for Ptuple in combinations(range(N),2):
    P=sum(1<<i for i in Ptuple)
    leaves=[P|(1<<x) for x in range(N) if not ((P>>x)&1)]
    for mask in range(1,1<<len(leaves)):
        H=frozenset(leaves[i] for i in range(len(leaves)) if (mask>>i)&1)
        Hs.add(H)
for Qtuple in combinations(range(N),4):
    Q=sum(1<<i for i in Qtuple)
    ts=[Q^(1<<i) for i in Qtuple]
    for mask in range(1,1<<len(ts)):
        H=frozenset(ts[i] for i in range(len(ts)) if (mask>>i)&1)
        Hs.add(H)

assert len(Hs)==756
for H in Hs:
    assert all(pop(a|b)<=4 for a in H for b in H)

rank3_cases=0
rank3_max=(0,1,None)
for H in Hs:
    allowed=[]
    for p in PAIR_MASKS:
        if any((p & ~h)==0 for h in H):
            continue
        if all(pop(p|h)<=4 for h in H):
            allowed.append(p)
    for em in range(1<<len(allowed)):
        E=[allowed[i] for i in range(len(allowed)) if (em>>i)&1]
        used=0
        for m in H: used |= m
        for m in E: used |= m
        uncovered=[j for j in range(N) if not ((used>>j)&1)]
        for sm in range(1<<len(uncovered)):
            S=[1<<uncovered[t] for t in range(len(uncovered)) if (sm>>t)&1]
            maxs=list(H)+E+S
            for i,a in enumerate(maxs):
                for j,bm in enumerate(maxs):
                    if i==j: continue
                    assert (a & ~bm)!=0
                    assert pop(a|bm)<=4
            lhs,rhs,b,num,h,ds=cert(maxs)
            assert lhs<=rhs
            rank3_cases+=1
            if lhs*rank3_max[1] > rank3_max[0]*rhs:
                rank3_max=(lhs,rhs,(tuple(sorted(H)),tuple(E),tuple(S),b,num,h,tuple(ds)))
print("triple_cliques =",len(Hs))
print("rank3_exact_configs =",rank3_cases)
print("rank3_max_ratio =",frac(rank3_max[0],rank3_max[1]))
print("rank3_max_witness_stats =",rank3_max[2])

# Rank 4: if a maximal 4-set Q exists, any other maximal member M would have
# |Q union M|<=4, so M subset Q, contradicting maximality. Therefore F=2^Q.
Q=sum(1<<i for i in range(4))
lhs,rhs,b,num,h,ds=cert([Q])
assert (lhs,rhs,b,num,h)==(48,48,16,3,1)
print("rank4_cases_up_to_labels = 1")
print("rank4_ratio = 1/1 (equality)")

# Threshold arithmetic for t0=sqrt(21)/2.
assert 48*4*7 == 64*21
assert (1<<(N-1))==64
print("threshold_square = 21/4")
print("row_charge_coefficient = 64/7")
print("global_bad_incidence_strict_upper = 64")
print("antipodal_sign_classes = 64")

# Exact obstruction to any strictly smaller threshold using only a universal
# rowwise bad-cardinality / row-energy charge: r=(c,c,c,0,0,0,0).
assert 48*7 == 64*21/4
print("three_equal_coordinate_obstruction_boundary = 48/(21/4) = 64/7")

print("ALL_EXACT_CHECKS_PASS")
