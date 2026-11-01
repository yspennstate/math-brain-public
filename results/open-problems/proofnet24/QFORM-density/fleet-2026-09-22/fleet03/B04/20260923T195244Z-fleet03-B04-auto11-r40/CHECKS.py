from fractions import Fraction
from itertools import combinations
from math import pi, sqrt

A = [
[1,1,1,1,1],
[1,1,1,3,2],
[1,1,1,2,-1],
[1,3,2,1,1],
[1,2,-1,1,1],
]

def det(M):
    M = [[Fraction(x) for x in row] for row in M]
    n = len(M)
    if n == 0:
        return Fraction(1)
    sign = 1
    out = Fraction(1)
    for j in range(n):
        p = next((i for i in range(j,n) if M[i][j] != 0), None)
        if p is None:
            return Fraction(0)
        if p != j:
            M[j],M[p] = M[p],M[j]
            sign *= -1
        pivot = M[j][j]
        out *= pivot
        for k in range(j,n):
            M[j][k] /= pivot
        for i in range(j+1,n):
            q = M[i][j]
            if q:
                for k in range(j,n):
                    M[i][k] -= q*M[j][k]
    return sign*out

def submatrix(M, rows, cols):
    return [[M[i][j] for j in cols] for i in rows]

def char_det_at(x):
    M = [[(Fraction(x) if i==j else Fraction(0))-Fraction(A[i][j]) for j in range(5)] for i in range(5)]
    return det(M)

def proposed_char(x):
    x=Fraction(x)
    return (x*x-5)*(x**3-5*x*x-9*x+5)

# Degree-five identity is certified at more than six exact points.
for x in [-3,-2,-1,0,1,2,6,7]:
    assert char_det_at(x) == proposed_char(x)

def Ck(k):
    tot=Fraction(0)
    for S in combinations(range(5),3):
        for T in combinations(range(5),3):
            if len(set(S)&set(T)) == k:
                d=det(submatrix(A,S,T))
                tot += d*d
    return tot

assert [Ck(k) for k in range(4)] == [0,484,1728,198]

def C1h(h):
    O=[i for i in range(5) if i!=h]
    tot=Fraction(0)
    for U in combinations(O,2):
        for V in combinations(O,2):
            if set(U).isdisjoint(V):
                d=det(submatrix(A,(h,)+U,(h,)+V))
                tot += d*d
    return tot

assert [C1h(h) for h in range(5)] == [84,124,76,124,76]

# Pivot h=1 in zero-based indexing, i.e. physical coordinate 2.
h=1
O=[0,2,3,4]
a=Fraction(A[h][h])
S=[]
for i in O:
    row=[]
    for j in O:
        row.append(Fraction(A[i][j])-Fraction(A[i][h])*Fraction(A[h][j])/a)
    S.append(row)
assert S == [
[0,0,-2,-1],
[0,0,-1,-3],
[-2,-1,-8,-5],
[-1,-3,-5,-3],
]

# J={1,5}, K={3,4} in one-based original indexing.
B = submatrix(S,[0,3],[1,2])
assert B == [[0,-2],[-3,-5]]
assert det(B) == -6
Z2 = det(B)**2
assert Z2 == 36

D=Fraction(0)
for U in combinations(range(4),2):
    for V in combinations(range(4),2):
        if set(U).isdisjoint(V):
            q=det(submatrix(S,U,V))
            D += q*q
assert D == 124
assert C1h(h) == a*a*D

K2 = pi*2**(7/4)
l2sq = 2**(11/4)
one_half = 8*2**(3/8)
pivot_c = 8*2**(7/8)
example = one_half*36**(-1/8)
peer = 4*sqrt(2)*6**(-1/4)

assert abs(K2-10.567016002364247) < 1e-12
assert abs(l2sq-6.727171322029716) < 1e-12
assert abs(one_half-10.374716437208077) < 1e-12
assert abs(pivot_c-14.672064691274740) < 1e-12
assert abs(example-6.628853526064557) < 1e-12
assert abs(peer-3.6144080144393793) < 1e-12

def cubic(x):
    return x**3-5*x**2-9*x+5
assert cubic(6)<0<cubic(7)
assert cubic(-2)<0<cubic(-1)

print("QFORM_B04_R40_CHECK_PASS")
print("Ck", [int(Ck(k)) for k in range(4)])
print("C1h", [int(C1h(h)) for h in range(5)])
print("Z2", int(Z2), "D", int(D))
print("K2_sharp", K2)
print("one_copy_half_riesz", one_half)
print("pivoted_C1_front", pivot_c)
print("example_bound", example)
print("peer_exact_rank2_comparison", peer)
