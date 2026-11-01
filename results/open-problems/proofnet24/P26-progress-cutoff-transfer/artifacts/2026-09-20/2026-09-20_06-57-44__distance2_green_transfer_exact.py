#!/usr/bin/env python3
from fractions import Fraction
from collections import deque

# P26 T08 exact sanity checker: distance-2 Green/shell transfer.
# This certifies only finite/algebraic identities used in the analytic proof.

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][h]*B[h][j] for h in range(k)) for j in range(m)] for i in range(n)]

def petersen():
    n=10
    E=set()
    for i in range(5):
        E.add(tuple(sorted((i,(i+1)%5))))
        E.add(tuple(sorted((i,i+5))))
        E.add(tuple(sorted((5+i,5+((i+2)%5)))))
    A=[[0]*n for _ in range(n)]
    for u,v in E:
        A[u][v]=A[v][u]=1
    return A

A=petersen()
n=len(A)
d=3
assert all(sum(row)==d for row in A)
A_sq=matmul(A,A)
B=[[A_sq[i][j]-(d if i==j else 0) for j in range(n)] for i in range(n)]

# Exact graph-distance verification: B is adjacency of exact-distance-2 graph.
dist=[[99]*n for _ in range(n)]
for s in range(n):
    dist[s][s]=0
    Q=deque([s])
    while Q:
        u=Q.popleft()
        for v in range(n):
            if A[u][v] and dist[s][v]==99:
                dist[s][v]=dist[s][u]+1
                Q.append(v)

for i in range(n):
    for j in range(n):
        assert B[i][j] in (0,1)
        assert B[i][j] == (1 if dist[i][j]==2 else 0)
assert all(sum(row)==d*(d-1) for row in B)

# Exact kernel polynomial identity Q_2=(d P^2-I)/(d-1).
q=d-1
for i in range(n):
    for j in range(n):
        lhs=Fraction(B[i][j],d*q)
        rhs=Fraction(A_sq[i][j],d*(d-1)) - (Fraction(1,d-1) if i==j else Fraction(0))
        assert lhs==rhs

# Connectedness of the Petersen distance-2 graph.
seen={0}; Q=deque([0])
while Q:
    u=Q.popleft()
    for v in range(n):
        if B[u][v] and v not in seen:
            seen.add(v); Q.append(v)
assert len(seen)==n

# General algebra checks.
for d in range(3,51):
    q=d-1
    D=d*q
    gap=Fraction((d-2)**2,d*q)
    psi_edge=Fraction(3*d-4,d*q)
    assert gap>0 and psi_edge+gap==1
    assert q*q < D-1  # strict output-vs-tree branching mismatch
    v=Fraction(2*(d-2),d-1)
    sigma2=Fraction(4*(q*q+1),d*q)
    tau2=sigma2/(v**3)
    assert v>0 and sigma2>0 and tau2>0

# Concrete degree-6 LPS output constants.
d=6; q=5; D=30
gap=Fraction((d-2)**2,d*q)
v=Fraction(2*(d-2),d-1)
sigma2=Fraction(4*(q*q+1),d*q)
tau2=sigma2/(v**3)
center=Fraction(d-1,2*(d-2))
assert gap==Fraction(8,15)
assert v==Fraction(8,5)
assert sigma2==Fraction(52,15)
assert tau2==Fraction(325,384)
assert center==Fraction(5,8)
assert Fraction(q*q,D-1)==Fraction(25,29)

# Direct non-Ramanujan edge separation at d=6:
# transformed base Ramanujan edge is 7/15 while the degree-30
# Ramanujan threshold is sqrt(29)/15, and 7^2>29.
assert 7*7 > 29

print("PETERSEN_DISTANCE2_DEGREE = 6")
print("D6_OUTPUT_DEGREE =", D)
print("D6_GAP_LOWER_BOUND =", f"{gap.numerator}/{gap.denominator}")
print("D6_RADIAL_SPEED =", f"{v.numerator}/{v.denominator}")
print("D6_VARIANCE_RATE =", f"{sigma2.numerator}/{sigma2.denominator}")
print("D6_PROFILE_TAU_SQUARED =", f"{tau2.numerator}/{tau2.denominator}")
print("D6_CENTER_COEFF =", f"{center.numerator}/{center.denominator}")
print("D6_BRANCH_RATIO =", "25/29")
print("P26_T08_DISTANCE2_GREEN_TRANSFER_EXACT_PASS")
