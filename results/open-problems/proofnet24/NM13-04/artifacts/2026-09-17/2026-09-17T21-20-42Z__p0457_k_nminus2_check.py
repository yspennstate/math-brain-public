#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter, deque
from fractions import Fraction
from math import factorial

def edges(n):
    return list(combinations(range(n), 2))

def lk_graph(n, order, k):
    E = edges(n)
    rank = {e:i for i,e in enumerate(order)}  # low weight -> high weight
    prefs = {}
    for v in range(n):
        inc = [e for e in E if v in e]
        inc.sort(key=rank.__getitem__)
        prefs[v] = set(inc[:k])
    return {e for e in E if e in prefs[e[0]] and e in prefs[e[1]]}

def complement(n,G):
    return set(edges(n))-G

def comps(n,E):
    A=[[] for _ in range(n)]
    for u,v in E:
        A[u].append(v); A[v].append(u)
    seen=set(); out=[]
    for s in range(n):
        if s in seen: continue
        seen.add(s); q=[s]; C=[]
        while q:
            u=q.pop(); C.append(u)
            for v in A[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        out.append(C)
    return out

def is_forest(n,E):
    return len(E)==n-len(comps(n,E))

def degrees(n,E):
    d=[0]*n
    for u,v in E:
        d[u]+=1; d[v]+=1
    return d

def is_star(n,H):
    d=degrees(n,H)
    return len(H)==n-1 and max(d)==n-1

def is_nonstar_double_star(n,H):
    if not is_forest(n,H) or len(H)!=n-1:
        return False
    d=degrees(n,H)
    for u,v in H:
        if d[u]>=2 and d[v]>=2 and d[u]+d[v]==n:
            if all(x in (u,v) or d[x]==1 for x in range(n)):
                return True
    return False

def diameter(n,G):
    if len(comps(n,G))!=1:
        return None
    A=[[] for _ in range(n)]
    for u,v in G:
        A[u].append(v); A[v].append(u)
    ans=0
    for s in range(n):
        dist=[-1]*n; dist[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in A[u]:
                if dist[v]<0:
                    dist[v]=dist[u]+1; q.append(v)
        ans=max(ans,max(dist))
    return ans

def predicted(n,H):
    if is_star(n,H):
        return None
    if is_nonstar_double_star(n,H):
        return 3
    return 2

def p_disconnected_formula(n):
    return Fraction((2**(n-1))*factorial(n), factorial(2*n-2))

def exhaustive(n):
    C=Counter()
    E=edges(n)
    for order in permutations(E):
        G=lk_graph(n,order,n-2)
        H=complement(n,G)
        assert is_forest(n,H), (n,order,H)
        got=diameter(n,G)
        assert got==predicted(n,H), (n,order,H,got,predicted(n,H))
        C["disconnected" if got is None else f"diameter_{got}"]+=1
    total=sum(C.values())
    empirical=Fraction(C["disconnected"], total)
    assert empirical==p_disconnected_formula(n), (n,empirical,p_disconnected_formula(n))
    return C,empirical

def make_order(n, high, top):
    E=edges(n)
    low=sorted([e for e in E if e not in high and e!=top])
    hi=sorted([e for e in E if e in high and e!=top])
    return tuple(low+hi+[top])

for n in (3,4):
    C,p=exhaustive(n)
    print(f"n={n} orders={sum(C.values())} classes={dict(sorted(C.items()))}")
    print(f"n={n} disconnected_probability={p} formula={p_disconnected_formula(n)}")

n=5
high={(0,1),(0,2),(0,3),(0,4)}
G=lk_graph(n,make_order(n,high,(0,1)),3); H=complement(n,G)
assert is_star(n,H) and diameter(n,G) is None
print("n=5 star/disconnected witness PASS",sorted(H))

high={(0,1),(0,2),(1,3),(1,4)}
G=lk_graph(n,make_order(n,high,(0,1)),3); H=complement(n,G)
assert is_nonstar_double_star(n,H) and diameter(n,G)==3
print("n=5 nonstar-double-star/diameter-3 witness PASS",sorted(H))

high={(0,1),(2,3),(2,4)}
G=lk_graph(n,make_order(n,high,(2,3)),3); H=complement(n,G)
assert is_forest(n,H) and not is_star(n,H) and not is_nonstar_double_star(n,H)
assert diameter(n,G)==2
print("n=5 diameter-2 witness PASS",sorted(H))

tri={(0,1),(0,2),(1,2)}
G=lk_graph(5,make_order(5,tri,(0,1)),2); H=complement(5,G)
assert tri.issubset(H) and not is_forest(5,H)
print("s=2 forest-extension obstruction PASS; missing triangle",sorted(tri))

print("ALL_EXACT_CHECKS_PASS")
