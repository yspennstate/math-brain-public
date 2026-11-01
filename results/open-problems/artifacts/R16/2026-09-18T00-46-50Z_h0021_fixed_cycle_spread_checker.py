#!/usr/bin/env python3
from itertools import permutations, product
from fractions import Fraction

def build_tree(r,k):
    a,b=1,k-2
    F=[(i*k+x,i*k+x+1) for i in range(r) for x in range(k-1)]
    M=[(i*k+b,(i+1)*k+a) for i in range(r-1)]
    return a,b,F,M

def verify_tree(r,k):
    a,b,F,M=build_tree(r,k)
    n=r*k
    E=F+M
    deg=[0]*n
    adj=[[] for _ in range(n)]
    for u,v in E:
        deg[u]+=1; deg[v]+=1
        adj[u].append(v); adj[v].append(u)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    used=[x for e in M for x in e]
    assert len(E)==n-1
    assert len(seen)==n
    assert max(deg)<=3
    assert len(set(used))==2*len(M)

def support_union(r,k):
    a,b,F,M=build_tree(r,k)
    n=r*k
    U=set()
    for s in range(n):
        for perm in permutations(range(r)):
            for ori in product((0,1), repeat=r):
                def image(comp,pos):
                    off=pos if ori[comp]==0 else k-1-pos
                    return (s+perm[comp]*k+off)%n
                for i in range(r-1):
                    u=image(i,b); v=image(i+1,a)
                    if u>v: u,v=v,u
                    U.add((u,v))
    return U

print("R16 fixed-cycle block spread obstruction exact small-case self-check")
for r in range(2,6):
    for k in range(5,9):
        verify_tree(r,k)
        U=support_union(r,k)
        n=r*k; m=r-1
        bound=3*n*r
        assert len(U)<=bound
        q_exact_lb=Fraction(m,len(U))
        q_proved_lb=Fraction(m,bound)
        assert q_exact_lb>=q_proved_lb
        print(f"r={r} k={k} n={n} m={m} |U|={len(U)} <=3nr={bound}; "
              f"singleton q lower bound exact-support={q_exact_lb}, proved={q_proved_lb}")
print("ALL_EXACT_CHECKS_PASS")
