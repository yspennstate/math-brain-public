#!/usr/bin/env python3
from fractions import Fraction as F

def rank_q(A):
    A = [[F(x) for x in row] for row in A]
    m, n = len(A), len(A[0])
    r = 0
    pivots = []
    for c in range(n):
        p = next((i for i in range(r,m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        z = A[r][c]
        A[r] = [x/z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                z = A[i][c]
                A[i] = [A[i][j]-z*A[r][j] for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return r, pivots, A

def matvec(A, x):
    return [sum(F(a)*F(b) for a,b in zip(row,x)) for row in A]

# Canonical four-point planar support:
# p1=(0,0), p2=(1,0), p3=(0,1), p4=(1,1).
A4 = [
    [1,1,1,1],
    [0,1,0,1],
    [0,0,1,1],
]
r4, piv4, _ = rank_q(A4)
assert r4 == 3
c4 = [F(1),F(-1),F(-1),F(1)]
assert matvec(A4,c4) == [F(0),F(0),F(0)]
h4 = [F(0),F(0),F(0),F(1)]
assert sum(h4[i]*c4[i] for i in range(4)) == 1

# The barycentric inverse encoded by q=lambda_4:
# lambda=(1-s-t+q, s-q, t-q, q).
for s,t,q in [(F(1,5),F(1,4),F(1,20)), (F(2,5),F(1,3),F(1,10))]:
    lam = [1-s-t+q, s-q, t-q, q]
    assert matvec(A4,lam) == [F(1),s,t]
    assert sum(h4[i]*lam[i] for i in range(4)) == q

# A five-point planar support has hidden barycentric dimension 2.
# p5=(2,1). Choosing Q=(lambda_4,lambda_5) is injective on ker A.
A5 = [
    [1,1,1,1,1],
    [0,1,0,1,2],
    [0,0,1,1,1],
]
r5, piv5, _ = rank_q(A5)
assert r5 == 3
c51 = [F(1),F(-1),F(-1),F(1),F(0)]
c52 = [F(2),F(-2),F(-1),F(0),F(1)]
assert matvec(A5,c51) == [F(0),F(0),F(0)]
assert matvec(A5,c52) == [F(0),F(0),F(0)]
# Q|ker has matrix identity in this basis.
Q_c51 = [c51[3], c51[4]]
Q_c52 = [c52[3], c52[4]]
assert Q_c51 == [F(1),F(0)]
assert Q_c52 == [F(0),F(1)]

print("status=PASS")
print("four_point_rank=3")
print("four_point_kernel=(1,-1,-1,1)")
print("four_point_scalar_fiber_pairing=1")
print("five_point_rank=3")
print("five_point_hidden_dimension=2")
print("five_point_Q_restriction_det=1")
print("scope=exact finite linear-algebra self-check only; no semialgebraicity theorem certified")
