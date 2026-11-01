#!/usr/bin/env python3
# Exact checker for R03-X39: a 7x7 binary rank-six matrix with an
# all-distinct full left null vector but a sparse zero-sum right null vector.
# Standard library only; determinants use Bareiss exact integer elimination.

B = [
    [0,0,1,1,0,1,1],
    [0,1,0,1,1,0,0],
    [0,0,1,1,1,1,0],
    [1,0,1,0,0,1,0],
    [1,0,1,0,1,0,1],
    [1,1,1,1,0,0,0],
    [1,1,0,0,1,1,1],
]
u = [2,7,-5,6,1,-4,-3]       # u^T B = 0
v = [1,-1,-1,1,0,0,0]        # B v = 0

def det_bareiss(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    prev, sign = 1, 1
    for k in range(n-1):
        p = next((i for i in range(k,n) if A[i][k] != 0), None)
        if p is None:
            return 0
        if p != k:
            A[k], A[p] = A[p], A[k]
            sign *= -1
        piv = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z = A[i][j]*piv - A[i][k]*A[k][j]
                if k:
                    assert z % prev == 0
                    z //= prev
                A[i][j] = z
        prev = piv
    return sign*A[n-1][n-1]

def delete_row_col(A, ri, cj):
    n = len(A)
    return [[A[i][j] for j in range(n) if j != cj]
            for i in range(n) if i != ri]

def matvec(A, x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]

def leftvec(x, A):
    n = len(A)
    return [sum(x[i]*A[i][j] for i in range(n)) for j in range(n)]

n = len(B)
assert det_bareiss(B) == 0
rank_cert = det_bareiss(delete_row_col(B,0,0))
assert rank_cert == 2              # nonzero 6x6 minor => rank(B)=6
assert matvec(B,v) == [0]*n
assert leftvec(u,B) == [0]*n
assert all(x != 0 for x in u)
assert len({abs(x) for x in u}) == n
assert sorted(abs(x) for x in u) == list(range(1,n+1))
assert sum(1 for x in v if x != 0) == 4
assert sum(v) == 0
Jminus2B = [[1-2*B[i][j] for j in range(n)] for i in range(n)]
assert det_bareiss(Jminus2B) == 0

print("R03-X39 exact obstruction")
print("det(B) =", det_bareiss(B))
print("rank certificate det(B delete row0,col0) =", rank_cert)
print("u^T B =", leftvec(u,B))
print("B v =", matvec(B,v))
print("u =", u)
print("sorted |u_i| =", sorted(abs(x) for x in u))
print("v =", v)
print("support(v) =", sum(1 for x in v if x != 0), "sum(v) =", sum(v))
print("det(J-2B) =", det_bareiss(Jminus2B))
print("SELF-CHECK PASS")
