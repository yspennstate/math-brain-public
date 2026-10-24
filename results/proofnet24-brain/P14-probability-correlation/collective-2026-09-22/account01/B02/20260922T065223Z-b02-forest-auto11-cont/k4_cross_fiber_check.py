from itertools import combinations
from collections import defaultdict

# Edge order on K4:
# 0=e=12, 1=a=13, 2=b=14, 3=c=23, 4=d=24, 5=f=34.
K4_EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def is_forest(n, edges, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            u=find(u); v=find(v)
            if u==v:
                return False
            p[u]=v
    return True

def forest_masks(n,edges):
    return [m for m in range(1<<len(edges)) if is_forest(n,edges,m)]

def rayleigh_monomials_k4(ei,fi):
    un=[j for j in range(6) if j not in (ei,fi)]
    F=forest_masks(4,K4_EDGES)
    P={(0,0):defaultdict(int),(1,0):defaultdict(int),
       (0,1):defaultdict(int),(1,1):defaultdict(int)}
    for m in F:
        st=((m>>ei)&1,(m>>fi)&1)
        ex=tuple((m>>j)&1 for j in un)
        P[st][ex]+=1
    def conv(A,B):
        out=defaultdict(int)
        for x,cx in A.items():
            for y,cy in B.items():
                out[tuple(a+b for a,b in zip(x,y))]+=cx*cy
        return out
    t=conv(P[(1,0)],P[(0,1)])
    d=conv(P[(0,0)],P[(1,1)])
    out=defaultdict(int,t)
    for x,c in d.items(): out[x]-=c
    return {k:v for k,v in out.items() if v}

def expected_disjoint():
    # Variables (a,b,c,d): ad(1+a)(1+d)+bc(1+b)(1+c)-2abcd.
    out=defaultdict(int)
    for ex in [(1,0,0,1),(2,0,0,1),(1,0,0,2),(2,0,0,2)]:
        out[ex]+=1
    for ex in [(0,1,1,0),(0,2,1,0),(0,1,2,0),(0,2,2,0)]:
        out[ex]+=1
    out[(1,1,1,1)]-=2
    return dict(out)

def expected_adjacent():
    # Marks e=12, f=13. Unmarked variables (p,q,r,s)=(14,23,24,34).
    # Delta = q^2 S^2 + q S(S+2rs) + rs(1+r)(1+s), S=1+p+r+s.
    def add(A,B):
        C=defaultdict(int,A)
        for k,v in B.items(): C[k]+=v
        return dict(C)
    def mul(A,B):
        C=defaultdict(int)
        for x,cx in A.items():
            for y,cy in B.items():
                C[tuple(a+b for a,b in zip(x,y))]+=cx*cy
        return dict(C)
    one={(0,0,0,0):1}
    p={(1,0,0,0):1}; q={(0,1,0,0):1}; r={(0,0,1,0):1}; s={(0,0,0,1):1}
    S=one
    for X in [p,r,s]: S=add(S,X)
    q2=mul(q,q); rs=mul(r,s)
    term1=mul(q2,mul(S,S))
    term2=mul(q,mul(S,add(S,{(0,0,1,1):2})))
    term3=mul(rs,mul(add(one,r),add(one,s)))
    return {k:v for k,v in add(add(term1,term2),term3).items() if v}

D=rayleigh_monomials_k4(0,5)
assert D==expected_disjoint(), (D,expected_disjoint())
A=rayleigh_monomials_k4(0,1)
assert A==expected_adjacent(), (A,expected_adjacent())
assert all(v>=0 for v in A.values())
assert D[(1,1,1,1)]==-2

# Exact fixed-union/intersection fibre on K4 for disjoint marks.
F=forest_masks(4,K4_EDGES)
domain=target=0
for X in F:
    for Y in F:
        if (X&Y)!=0 or (X|Y)!=(1<<6)-1:
            continue
        st=((X>>0)&1,(X>>5)&1,(Y>>0)&1,(Y>>5)&1)
        if st==(0,0,1,1): domain+=1
        if st==(1,0,0,1): target+=1
assert (domain,target)==(4,2)

# Unit K4 total counts and Rayleigh gap.
cnt=defaultdict(int)
for X in F:
    cnt[((X>>0)&1,(X>>5)&1)]+=1
gap=cnt[(1,0)]*cnt[(0,1)]-cnt[(0,0)]*cnt[(1,1)]
assert (cnt[(0,0)],cnt[(1,0)],cnt[(0,1)],cnt[(1,1)],gap)==(15,9,9,5,6)

# Parallel-collapse regression: replace K4 edge 23 by two parallel physical edges
# and edge 34 by two parallel physical edges. Query e=12 and one copy of 34.
MG_EDGES=[(0,1),(0,2),(0,3),(1,2),(1,2),(1,3),(2,3),(2,3)]
W=[3,2,5,7,11,13,17,19]
def weighted_counts(edges,weights,ei,fi):
    Z=Ze=Zf=Zef=0
    for m in range(1<<len(edges)):
        if not is_forest(4,edges,m): continue
        wt=1
        for i,w in enumerate(weights):
            if (m>>i)&1: wt*=w
        Z+=wt
        if (m>>ei)&1: Ze+=wt
        if (m>>fi)&1: Zf+=wt
        if ((m>>ei)&1) and ((m>>fi)&1): Zef+=wt
    return Z,Ze,Zf,Zef,Ze*Zf-Z*Zef
z=weighted_counts(MG_EDGES,W,0,6)
zc=weighted_counts(K4_EDGES,[W[0],W[1],W[2],W[3]+W[4],W[5],W[6]+W[7]],0,5)
assert z[0]==zc[0] and z[1]==zc[1]
assert z[2]*(W[6]+W[7])==zc[2]*W[6]
assert z[3]*(W[6]+W[7])==zc[3]*W[6]
assert z[4]*(W[6]+W[7])==zc[4]*W[6]

print('K4_DISJOINT_NEGATIVE_FIBRE_COEFF',D[(1,1,1,1)])
print('K4_FIXED_FIBRE_DOMAIN_TARGET',domain,target)
print('K4_UNIT_COUNTS_00_10_01_11_GAP',cnt[(0,0)],cnt[(1,0)],cnt[(0,1)],cnt[(1,1)],gap)
print('K4_ADJACENT_ALL_COEFFS_NONNEG',len(A),min(A.values()))
print('PARALLEL_COLLAPSE_WEIGHTED_GAP',z[-1])
print('STATUS=PASS')
