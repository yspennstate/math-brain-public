"""Exact-arithmetic self-check for NM13-09 / P0245 order-4 Cayley formulas.

This is a self-check, not the proof of the continuous-parameter theorem.
It solves the finite absorbing cover-time system over Q for selected rational
transition laws and compares against the closed forms proved in the run report.
"""
from fractions import Fraction as F

def solve(A,b):
    n=len(b)
    A=[row[:] + [b[i]] for i,row in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if A[r][c])
        A[c],A[p]=A[p],A[c]
        q=A[c][c]
        A[c]=[x/q for x in A[c]]
        for r in range(n):
            if r!=c and A[r][c]:
                q=A[r][c]
                A[r]=[A[r][j]-q*A[c][j] for j in range(n+1)]
    return [A[i][-1] for i in range(n)]

def cover_time_uniform(P):
    n=len(P); full=(1<<n)-1
    states=[]; idx={}
    for S in range(1<<n):
        for i in range(n):
            if (S>>i)&1:
                idx[(i,S)]=len(states); states.append((i,S))
    m=len(states)
    A=[[F(0) for _ in range(m)] for _ in range(m)]
    b=[F(1) for _ in range(m)]
    for k,(i,S) in enumerate(states):
        if S==full:
            A[k][k]=F(1); b[k]=F(0); continue
        A[k][k]=F(1)
        for j,p in enumerate(P[i]):
            if p:
                A[k][idx[(j,S|(1<<j))]]-=p
    h=solve(A,b)
    return sum(h[idx[(i,1<<i)]] for i in range(n))/n

def v4(a,b,c):
    d=F(1)-a-b-c
    q=[d,a,b,c]
    P=[[q[i^j] for j in range(4)] for i in range(4)]
    formula=F(1,a+b)+F(1,a+c)+F(1,b+c)+F(1,a+b+c)
    return P,formula

def z4(a,b):
    d=F(1)-2*a-b
    q=[d,a,b,a]
    P=[[q[(j-i)%4] for j in range(4)] for i in range(4)]
    formula=F(2,a+b)+F(1,2*a)+F(1,2*a+b)
    return P,formula

TARGET=F(11,2)
tests=[
    ("V4_K4",)+v4(F(1,3),F(1,3),F(1,3)),
    ("V4_loop",)+v4(F(1,5),F(1,4),F(1,6)),
    ("V4_boundary",)+v4(F(1,2),F(1,2),F(0)),
    ("Z4_K4",)+z4(F(1,3),F(1,3)),
    ("Z4_loop",)+z4(F(1,5),F(1,4)),
    ("Z4_cycle",)+z4(F(1,2),F(0)),
]
print("P0245 order-4 Cayley exact self-check")
for name,P,formula in tests:
    ct=cover_time_uniform(P)
    assert ct==formula,(name,ct,formula)
    assert ct>=TARGET,(name,ct)
    print(f"{name}: cover={ct}; formula={formula}; ratio_to_11/2={ct/TARGET}")
assert tests[0][2]==TARGET and tests[3][2]==TARGET
print("ALL_EXACT_CHECKS_PASS")
