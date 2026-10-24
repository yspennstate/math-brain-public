from functools import lru_cache
from collections import Counter
from fractions import Fraction
import math

ASSERTIONS = 0

def ck(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def C(n):
    return math.comb(2*n,n)//(n+1)

@lru_cache(None)
def triangulations(a,b):
    # Convex interval polygon a,a+1,...,b.
    if b-a <= 2:
        return (frozenset(),)
    out=set()
    for k in range(a+1,b):
        for L in triangulations(a,k):
            for R in triangulations(k,b):
                D=set(L)|set(R)
                if k-a > 1:
                    D.add((a,k))
                if b-k > 1:
                    D.add((k,b))
                out.add(frozenset(D))
    return tuple(out)

def is_edge(D,u,v,N):
    a,b=sorted((u,v))
    return b == a+1 or (a == 0 and b == N-1) or (a,b) in D

def root_index(D,n):
    N=n+2
    hits=[]
    for k in range(1,n+1):
        if is_edge(D,0,k,N) and is_edge(D,k,n+1,N):
            hits.append(k)
    ck(len(hits)==1, ("root", n, D, hits))
    return hits[0]

def flip(D,e,n):
    N=n+2
    a,c=e
    opp=[]
    for b in range(N):
        if b in (a,c):
            continue
        if is_edge(D,a,b,N) and is_edge(D,b,c,N):
            opp.append(b)
    ck(len(opp)==2, ("opp", n, e, opp))
    b,d=opp
    ne=tuple(sorted((b,d)))
    nd=set(D)
    nd.remove(e)
    nd.add(ne)
    return frozenset(nd)

print("P13 P0223 oriented-projection exact self-check")
for n in range(2,9):
    T=triangulations(0,n+1)
    ck(len(T)==C(n), ("Catalan count", n, len(T), C(n)))

    fibers=Counter(root_index(D,n) for D in T)
    expected_fibers=Counter({
        k:C(k-1)*C(n-k) for k in range(1,n+1)
    })
    ck(fibers==expected_fibers, ("fibers", n, fibers, expected_fibers))

    seen=set()
    cross=Counter()
    root_change_directed=0
    for D in T:
        i=root_index(D,n)
        local_changes=0
        for e in D:
            D2=flip(D,e,n)
            j=root_index(D2,n)
            if i != j:
                local_changes += 1
                root_change_directed += 1
            key=frozenset((D,D2))
            if key in seen:
                continue
            seen.add(key)
            if i != j:
                a,b=sorted((i,j))
                cross[(a,b)] += 1

        target=1 if i in (1,n) else 2
        ck(local_changes==target, ("local root degree", n, i, local_changes, target))

    expected_cross=Counter({
        (i,j):C(i-1)*C(j-i-1)*C(n-j)
        for i in range(1,n+1) for j in range(i+1,n+1)
    })
    ck(cross==expected_cross, ("cross", n, cross, expected_cross))

    ck(sum(cross.values())==C(n)-C(n-1),
       ("root-changing undirected", n, sum(cross.values()), C(n)-C(n-1)))

    expected_directed=2*(C(n)-C(n-1))
    ck(root_change_directed==expected_directed,
       ("root-changing directed", n, root_change_directed, expected_directed))

    p_change=Fraction(root_change_directed, C(n)*(n-1))
    ck(p_change==Fraction(3,2*n-1), ("stationary root change", n, p_change))

    # Exact projection kernel, row sums, and detailed balance.
    Delta=n-1
    pi=[Fraction(C(i-1)*C(n-i),C(n)) for i in range(1,n+1)]
    P=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i < j:
                P[i-1][j-1]=Fraction(C(j-i-1)*C(n-j), Delta*C(n-i))
            elif j < i:
                P[i-1][j-1]=Fraction(C(j-1)*C(i-j-1), Delta*C(i-1))
        P[i-1][i-1]=1-sum(P[i-1])
        ck(P[i-1][i-1] == 1-Fraction(1 if i in (1,n) else 2,Delta),
           ("diag",n,i,P[i-1][i-1]))

    for i in range(n):
        ck(sum(P[i])==1, ("row",n,i))
        for j in range(n):
            ck(pi[i]*P[i][j]==pi[j]*P[j][i], ("DB",n,i,j))

    vals=[C(k-1)*C(n-k) for k in range(1,n+1)]
    min_indices=[k+1 for k,v in enumerate(vals) if v==min(vals)]
    target_min=[(n+1)//2] if n%2==1 else [n//2,n//2+1]
    ck(min_indices==target_min, ("central minima",n,min_indices,target_min))

    print("n",n,
          "states",len(T),
          "root_change_edges",sum(cross.values()),
          "P_change",p_change,
          "central_indices",min_indices)

print("ASSERTIONS",ASSERTIONS)
print("ALL_EXACT_P0223_ORIENTED_PROJECTION_CHECKS_PASS")
