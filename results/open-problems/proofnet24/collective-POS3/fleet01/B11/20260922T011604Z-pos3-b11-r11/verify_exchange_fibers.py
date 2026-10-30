#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import defaultdict

def closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for a,b in edges: R[a][b]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]: R[i][j]=True
    return R

def linext(R):
    n=len(R)
    out=[]
    for p in permutations(range(n)):
        pos=[0]*n
        for i,x in enumerate(p): pos[x]=i
        if all(not R[a][b] or pos[a]<pos[b] for a in range(n) for b in range(n)):
            out.append(p)
    return out

def inc(R,a,b):
    return a!=b and not R[a][b] and not R[b][a]

def critical(R,x,y):
    n=len(R)
    Dx={z for z in range(n) if R[z][x]}
    Dy={z for z in range(n) if R[z][y]}
    Ux={z for z in range(n) if R[x][z]}
    Uy={z for z in range(n) if R[y][z]}
    return Dx <= Dy and Uy <= Ux

def exchange(R,L,x,y):
    L=list(L); ix=L.index(x); iy=L.index(y)
    assert ix < iy
    A=L[:ix]; M=L[ix+1:iy]; B=L[iy+1:]
    D=[z for z in M if R[z][y]]
    U=[z for z in M if R[x][z]]
    assert set(D).isdisjoint(U)
    N=[z for z in M if z not in D and z not in U]
    return tuple(A+D+[y]+N+[x]+U+B)

def neutral_target(R,L,x,y):
    L=list(L); iy=L.index(y); ix=L.index(x)
    if iy >= ix: return False
    return all(inc(R,z,x) and inc(R,z,y) for z in L[iy+1:ix])

def width(R):
    n=len(R); ans=0
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        if all(inc(R,a,b) for a,b in combinations(S,2)):
            ans=max(ans,len(S))
    return ans

def incomparability_connected(R):
    n=len(R)
    adj=[[] for _ in range(n)]
    for a,b in combinations(range(n),2):
        if inc(R,a,b):
            adj[a].append(b); adj[b].append(a)
    seen={0}; stack=[0]
    while stack:
        a=stack.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b); stack.append(b)
    return len(seen)==n

def autonomous(R,S):
    S=set(S); n=len(R)
    for z in range(n):
        if z in S: continue
        rel=[]
        for s in S:
            rel.append(1 if R[z][s] else -1 if R[s][z] else 0)
        if len(set(rel)) != 1: return False
    return True

def has_proper_autonomous_nonchain(R):
    n=len(R)
    for r in range(2,n):
        for S in combinations(range(n),r):
            if autonomous(R,S) and any(inc(R,a,b) for a,b in combinations(S,2)):
                return True
    return False

def valid_ext(R,L):
    pos={x:i for i,x in enumerate(L)}
    return all(not R[a][b] or pos[a] < pos[b] for a in range(len(R)) for b in range(len(R)))

def exhaustive_exchange_check(n):
    potential=list(combinations(range(n),2))
    pair_cases=0
    closure_seen=set()
    for mask in range(1<<len(potential)):
        R=closure(n,[potential[i] for i in range(len(potential)) if mask>>i&1])
        key=tuple(tuple(row) for row in R)
        if key in closure_seen: continue
        closure_seen.add(key)
        LE=linext(R)
        for x in range(n):
            for y in range(n):
                if not inc(R,x,y): continue
                plus=[L for L in LE if L.index(x)<L.index(y)]
                minus=[L for L in LE if L.index(y)<L.index(x)]
                image=defaultdict(list)
                for L in plus:
                    T=exchange(R,L,x,y)
                    assert valid_ext(R,T)
                    assert T.index(y)<T.index(x)
                    image[T].append(L)
                neutral={L for L in minus if neutral_target(R,L,x,y)}
                assert set(image)==neutral
                assert (set(image)==set(minus)) == critical(R,x,y)
                Rmiss=len(minus)-len(image)
                lhs=len(plus)-2*len(minus)
                rhs=sum(len(v)-2 for v in image.values())-2*Rmiss
                assert lhs==rhs
                pair_cases += 1
    return len(closure_seen), pair_cases

def nested_interval_check(max_m=6):
    checked=0
    for m in range(max_m+1):
        ints=[(a,b) for a in range(m+1) for b in range(a,m+1)]
        for A in ints:
            for B in ints:
                if not (A[0] <= B[0] and B[1] <= A[1]): continue
                uv={(s,t) for s in range(A[0],A[1]+1) for t in range(B[0],B[1]+1) if s<=t}
                vu={(s,t) for s in range(B[0],B[1]+1) for t in range(A[0],A[1]+1) if s<=t}
                core_uv={(s,t) for (s,t) in uv if B[0] <= s <= B[1]}
                core_vu={(s,t) for (s,t) in vu if B[0] <= t <= B[1]}
                assert len(core_uv)==len(core_vu)
                assert len(uv)-len(core_uv) == sum(1 for s,t in uv if s < B[0])
                assert len(vu)-len(core_vu) == sum(1 for s,t in vu if t > B[1])
                checked += 1
    return checked

R=closure(5,[(0,1),(0,4),(1,3),(2,3)])
LE=linext(R)
x,y=2,4
plus=[L for L in LE if L.index(x)<L.index(y)]
minus=[L for L in LE if L.index(y)<L.index(x)]
fib=defaultdict(list)
for L in plus: fib[exchange(R,L,x,y)].append(L)
assert len(LE)==11 and len(plus)==8 and len(minus)==3
assert width(R)==3 and incomparability_connected(R)
assert not has_proper_autonomous_nonchain(R)
assert critical(R,x,y)
assert sorted(len(v) for v in fib.values())==[2,2,4]
lower_rev=sum(L.index(x)<L.index(0) for L in LE)
upper_rev=sum(L.index(3)<L.index(y) for L in LE)
union=sum((L.index(x)<L.index(0)) or (L.index(3)<L.index(y)) for L in LE)
inter=sum((L.index(x)<L.index(0)) and (L.index(3)<L.index(y)) for L in LE)
assert (lower_rev,upper_rev,union,inter)==(3,3,5,1)

closures4,pairs4=exhaustive_exchange_check(4)
closures5,pairs5=exhaustive_exchange_check(5)
nested=nested_interval_check()

print("POS3_EXCHANGE_FIBER_CHECK_PASS")
print(f"witness_extensions={len(LE)} majority={len(plus)} minority={len(minus)} fibers={sorted(len(v) for v in fib.values())}")
print(f"witness_reversals=lower:{lower_rev}/11 upper:{upper_rev}/11 union:{union}/11 intersection:{inter}/11")
print(f"exhaustive_n4=closures:{closures4} ordered_incomparable_pairs:{pairs4}")
print(f"exhaustive_n5=closures:{closures5} ordered_incomparable_pairs:{pairs5}")
print(f"nested_interval_pairs_checked={nested}")
