from itertools import combinations
from functools import lru_cache
from fractions import Fraction

N = 9
COVERS = [
    (0,1),(0,3),(1,4),(1,5),(2,5),(3,5),
    (4,7),(5,6),(5,8),(6,7)
]

def transitive_closure(n, edges):
    R = [[False]*n for _ in range(n)]
    for a,b in edges:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    assert not any(R[i][i] for i in range(n))
    return R

R = transitive_closure(N, COVERS)

def incomparable(i,j):
    return i != j and not R[i][j] and not R[j][i]

max_antichain = []
for mask in range(1<<N):
    S = [i for i in range(N) if (mask>>i)&1]
    if len(S) <= len(max_antichain):
        continue
    if all(incomparable(i,j) for i,j in combinations(S,2)):
        max_antichain = S
assert len(max_antichain) == 3

adj = [set() for _ in range(N)]
for i,j in combinations(range(N),2):
    if incomparable(i,j):
        adj[i].add(j); adj[j].add(i)
seen={0}; stack=[0]
while stack:
    v=stack.pop()
    for w in adj[v]:
        if w not in seen:
            seen.add(w); stack.append(w)
assert len(seen)==N

def autonomous(S):
    S=set(S)
    for z in range(N):
        if z in S: continue
        rels=set()
        for s in S:
            if R[z][s]: rels.add(-1)
            elif R[s][z]: rels.add(1)
            else: rels.add(0)
        if len(rels) != 1:
            return False
    return True

autos=[]
for k in range(2,N):
    for S in combinations(range(N),k):
        if autonomous(S):
            autos.append(S)
assert autos == []

# Every unordered partition into three chains is a proper 3-coloring
# of the incomparability graph. Fix color(0)=0 and quotient color labels
# by sorting the three resulting vertex sets.
covers3=set()
colors=[None]*N
colors[0]=0
def rec(i):
    if i==N:
        if set(colors)=={0,1,2}:
            parts=tuple(sorted(tuple(v for v in range(N) if colors[v]==c) for c in range(3)))
            covers3.add(parts)
        return
    if i==0:
        rec(1); return
    for c in range(3):
        if all(colors[w] != c for w in adj[i] if colors[w] is not None):
            colors[i]=c
            rec(i+1)
            colors[i]=None
rec(0)

def profile(C,q):
    C=tuple(sorted(C))
    lam=0
    rho=len(C)
    for j,c in enumerate(C,1):
        if R[c][q]:
            lam=max(lam,j)
        if R[q][c]:
            rho=min(rho,j-1)
    assert lam <= rho
    return (lam,rho)

def proper_contains(I,J):
    return I != J and I[0] <= J[0] and J[1] <= I[1]

def nested_pairs(C):
    C=set(C)
    Q=[v for v in range(N) if v not in C]
    ans=[]
    for u,v in combinations(Q,2):
        if not incomparable(u,v):
            continue
        Iu=profile(C,u); Iv=profile(C,v)
        if proper_contains(Iu,Iv) or proper_contains(Iv,Iu):
            ans.append((u,v,Iu,Iv))
    return ans

cover_stats=[]
for cov in sorted(covers3):
    ns=[nested_pairs(C) for C in cov]
    assert all(len(x)>=1 for x in ns)
    cover_stats.append((cov,tuple(len(x) for x in ns)))

assert len(covers3)==16
assert min(min(ns) for _,ns in cover_stats)==1

pred=[0]*N
for v in range(N):
    for u in range(N):
        if R[u][v]:
            pred[v] |= 1<<u

@lru_cache(None)
def count(mask):
    if mask == (1<<N)-1:
        return 1
    return sum(count(mask|1<<v) for v in range(N)
               if not ((mask>>v)&1) and (pred[v] & ~mask)==0)

E=count(0)
exts=[]
def enum(mask,seq):
    if mask == (1<<N)-1:
        exts.append(tuple(seq)); return
    for v in range(N):
        if not ((mask>>v)&1) and (pred[v] & ~mask)==0:
            enum(mask|1<<v,seq+[v])
enum(0,[])
assert len(exts)==E==109

balanced=[]
for i,j in combinations(range(N),2):
    if not incomparable(i,j):
        continue
    a=sum(L.index(i)<L.index(j) for L in exts)
    q=Fraction(a,E)
    if Fraction(1,3) <= q <= Fraction(2,3):
        balanced.append((i,j,q))
assert balanced

print("covers", COVERS)
print("width", len(max_antichain), "witness", max_antichain)
print("incomparability_connected", True)
print("proper_autonomous_subsets", len(autos))
print("three_chain_covers", len(covers3))
print("minimum_nested_pairs_on_any_deleted_chain", min(min(ns) for _,ns in cover_stats))
for cov,ns in cover_stats:
    print("chain_cover", cov, "nested_counts", ns)
print("linear_extensions", E)
print("balanced_pairs", [(i,j,str(q)) for i,j,q in balanced])
print("POS3_NO_NESTING_FREE_DELETION_COUNTEREXAMPLE_PASS")
