#!/usr/bin/env python3
from fractions import Fraction
from collections import deque
import sympy as sp


def partitions_cycles(n, min_part=3):
    out=[]
    def rec(rem, maxpart, cur):
        if rem==0:
            out.append(tuple(cur)); return
        for p in range(min(maxpart, rem), min_part-1, -1):
            rec(rem-p, p, cur+[p])
    rec(n,n,[])
    return out


def cycle_union(parts):
    n=sum(parts); A=[[0]*n for _ in range(n)]
    base=0
    for m in parts:
        for i in range(m):
            u=base+i; v=base+(i+1)%m
            A[u][v]=A[v][u]=1
        base += m
    return A


def complement(A):
    n=len(A)
    return [[0 if i==j else 1-A[i][j] for j in range(n)] for i in range(n)]


def degrees(A): return [sum(r) for r in A]

def connected(A):
    n=len(A); seen={0}; q=deque([0])
    while q:
        u=q.popleft()
        for v,e in enumerate(A[u]):
            if e and v not in seen:
                seen.add(v); q.append(v)
    return len(seen)==n

def diameter(A):
    n=len(A); D=0
    for s in range(n):
        dist=[-1]*n; dist[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v,e in enumerate(A[u]):
                if e and dist[v]<0:
                    dist[v]=dist[u]+1; q.append(v)
        assert min(dist)>=0
        D=max(D,max(dist))
    return D

x=sp.symbols('x')
parts=partitions_cycles(8)
print('cycle_partitions', parts)
assert parts==[(8,), (5,3), (4,4)]
rows=[]
for p in parts:
    H=cycle_union(p); G=complement(H)
    assert degrees(H)==[2]*8
    assert degrees(G)==[5]*8
    assert connected(G)
    D=diameter(G)
    A=sp.Matrix(G)
    L=sp.diag(*degrees(G))-A
    cp=sp.factor(L.charpoly(x).as_expr())
    eig=L.eigenvals()
    eig_sorted=sorted(eig.keys(), key=lambda z: float(sp.N(z)))
    mu=sp.simplify(eig_sorted[1])
    rows.append((p,D,cp,mu))
    print('parts',p,'diam',D,'charpoly',cp,'mu',mu)

mu_by={p:mu for p,D,cp,mu in rows}
assert sp.simplify(mu_by[(8,)]-4)==0
assert sp.simplify(mu_by[(4,4)]-4)==0
assert sp.simplify(mu_by[(5,3)]-(sp.Rational(11,2)-sp.sqrt(5)/2))==0
assert all(D==2 for _,D,_,_ in rows)
min_mu=min([float(sp.N(mu)) for _,_,_,mu in rows])
mins=[p for p,D,cp,mu in rows if abs(float(sp.N(mu))-min_mu)<1e-12]
assert mins==[(8,), (4,4)]
print('mu_min_types', mins)
print('source_asymptotic_benchmark', Fraction(3*8,5+1))
print('raw_finite_excess_for_minimizers', Fraction(2)-Fraction(3*8,6))
print('NOTE finite case is PARTIAL only; does not instantiate asymptotic Conjecture 5.4 sequence hypothesis')
print('ALL_EXACT_CHECKS_PASSED')
