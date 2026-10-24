#!/usr/bin/env python3
"""Exact finite core for HARD7-06 run 3.

This script verifies, using only Python Fraction/integer arithmetic, the
alpha=1/4 minority-profile witness for 6-regular 3-uniform hypergraph
2-colorings and the exact local two-replica Hessian on the full feasible
homogeneous tangent space.

It is a self-check of the finite algebraic core, not a proof of the
asymptotic source conjecture.
"""
from fractions import Fraction as F
from math import comb

def matmul(A,B):
    assert len(A[0]) == len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(x) for x in zip(*A)]

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def sub(A,B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def scalar(c,A):
    return [[c*x for x in row] for row in A]

def kron(A,B):
    return [[A[i//len(B)][j//len(B[0])] *
             B[i%len(B)][j%len(B[0])]
             for j in range(len(A[0])*len(B[0]))]
            for i in range(len(A)*len(B))]

def inv(A):
    n = len(A)
    M = [row[:] + eye(n)[i] for i,row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c,n) if M[r][c])
        M[c],M[piv] = M[piv],M[c]
        d = M[c][c]
        M[c] = [x/d for x in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                q = M[r][c]
                M[r] = [M[r][j] - q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def det(A):
    n = len(A)
    M = [row[:] for row in A]
    out = F(1)
    for c in range(n):
        piv = next((r for r in range(c,n) if M[r][c]), None)
        if piv is None:
            return F(0)
        if piv != c:
            M[c],M[piv] = M[piv],M[c]
            out = -out
        d = M[c][c]
        out *= d
        for r in range(c+1,n):
            if M[r][c]:
                q = M[r][c]/d
                for j in range(c,n):
                    M[r][j] -= q*M[c][j]
    return out

def rank_pivots(A):
    M = [r[:] for r in A]
    m,n = len(M),len(M[0])
    r = 0
    pivots = []
    for c in range(n):
        piv = next((i for i in range(r,m) if M[i][c]), None)
        if piv is None:
            continue
        M[r],M[piv] = M[piv],M[r]
        d = M[r][c]
        M[r] = [x/d for x in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                q = M[i][c]
                M[i] = [M[i][j] - q*M[r][j] for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return pivots

# Raw single-vertex minority-incidence profile q = Bin(6,1/3).
qnum = [64,192,240,160,60,12,1]
assert sum(qnum) == 729
assert sum(r*qnum[r] for r in range(7)) == 2*729
assert sum((r-2)**2*qnum[r] for r in range(7)) == F(4,3)*729

# alpha = 1/4: p = (3/4) q + (1/4) delta_2.
alpha = F(1,4)
pnum = [64,192,483,160,60,12,1]
D = 972
assert sum(pnum) == D
assert sum(r*pnum[r] for r in range(7)) == 2*D
var = F(sum((r-2)**2*pnum[r] for r in range(7)), D)
assert var == 1
kappa = (3*var-4)/20
assert kappa == F(-1,20)
assert kappa == -alpha/5

# Exact positivity of the first-moment exponent s_1(p).
# D*s_1 = D log(2D/81) + sum n_r log C(6,r) - sum n_r log n_r.
# At D=972, 2D/81 = 24, so positivity is the integer inequality below.
lhs = 24**D
rhs = 1
for r,nr in enumerate(pnum):
    lhs *= comb(6,r)**nr
    rhs *= nr**nr
assert lhs > rhs

# Endpoint alpha=1/3. Convexity of D(p_alpha||q), with derivative 0 at
# alpha=0, implies s_1 is nonincreasing; hence positivity at this endpoint
# certifies positivity on [0,1/3].
p13num = [128,384,1209,320,120,24,2]
D13 = 2187
assert sum(p13num) == D13
assert sum(r*p13num[r] for r in range(7)) == 2*D13
lhs13 = 54**D13
rhs13 = 1
for r,nr in enumerate(p13num):
    lhs13 *= comb(6,r)**nr
    rhs13 *= nr**nr
assert lhs13 > rhs13

# Edge centered basis: e=3m-1, b=s, c=s(3m-1), Gram diag(2,1,2).
G = [[F(2),0,0],[0,F(1),0],[0,0,F(2)]]
# Variable port-to-port conditional operator.
Tv = [[kappa,0,0],[0,F(1),0],[0,0,kappa]]
# Proper NAE-3 factor port-to-port conditional operator.
Tf = [[F(-1,2),0,0],
      [0,F(-1,3),F(-2,3)],
      [0,F(-1,3),F(5,6)]]
# Enumerate the six proper NAE-3 sign triples and recover G Tf exactly.
states = []
for s0 in (-1,1):
    for s1 in (-1,1):
        for s2 in (-1,1):
            ss = (s0,s1,s2)
            if s0 == s1 == s2:
                continue
            mm = tuple(int(ss[i] != ss[(i+1)%3] and ss[i] != ss[(i+2)%3])
                       for i in range(3))
            states.append((ss,mm))
assert len(states) == 6
def basis(s,m):
    return (3*m-1, s, s*(3*m-1))
Cf = [[F(0) for _ in range(3)] for _ in range(3)]
for ss,mm in states:
    a,b = basis(ss[0],mm[0]), basis(ss[1],mm[1])
    for i in range(3):
        for j in range(3):
            Cf[i][j] += F(a[i]*b[j], 6)
GTf = matmul(G,Tf)
assert Cf == GTf
assert GTf == transpose(GTf)

# Recover the variable role-channel correlation from the profile moments.
# For two distinct ports, E[m_i m_j]=E[R(R-1)]/(6*5).
ER2minusR = F(sum(r*(r-1)*pnum[r] for r in range(7)), D)
cov_m = ER2minusR/F(30) - F(1,9)
assert cov_m / F(2,9) == kappa
GTv = matmul(G,Tv)
assert GTv == transpose(GTv)

I9 = eye(9)
Lv = add(I9, scalar(F(5), kron(Tv,Tv)))
Lf = add(I9, scalar(F(2), kron(Tf,Tf)))
pivots = rank_pivots(Lf)
assert pivots == [0,1,3,4,5]
R = [[Lf[i][j] for j in pivots] for i in range(9)]
X = [[F(int(i == pivots[j])) for j in range(5)] for i in range(9)]
G9 = kron(G,G)
Lvi = inv(Lv)

# In range coordinates K = R a, an exact preimage for the factor lift is X a
# because Lf X = R.  The sign-relevant Hessian matrix (outer positive factor
# d/2=3 omitted) is
#   B = R^T G9 (R - Lv^{-1}R - X).
B = matmul(transpose(R), matmul(G9, sub(sub(R,matmul(Lvi,R)),X)))

B_expected = [
    [F(-53,9),0,0,0,0],
    [0,F(-2804,729),0,0,0],
    [0,0,F(-2804,729),0,0],
    [0,0,0,F(-535,13122),F(-850,6561)],
    [0,0,0,F(-850,6561),F(-6380,6561)],
]
assert B == B_expected
assert B == transpose(B)

# Sylvester: all leading principal minors of -B are positive.
mins = [det([[-B[i][j] for j in range(k)] for i in range(k)])
        for k in range(1,6)]
mins_expected = [
    F(53,9),
    F(148612,6561),
    F(416708048,4782969),
    F(111469402840,31381059609),
    F(20835402400,10460353203),
]
assert mins == mins_expected
assert all(x > 0 for x in mins)

# General-alpha determinant threshold from the on-page symbolic reduction:
# det(last 2x2 block) has the sign of 13 a^2 + 16 a - 2.
poly = 13*alpha*alpha + 16*alpha - 2
assert poly == F(13,16) + 4 - 2
assert poly > 0
# alpha_c=(3 sqrt(10)-8)/13 < 1/4 exactly:
# 3 sqrt(10) < 45/4 iff 90 < 2025/16.
assert 90*16 < 2025

print("alpha =", alpha)
print("profile_counts =", pnum, "/", D)
print("profile_mean = 2")
print("profile_variance =", var)
print("role_port_correlation_kappa =", kappa)
print("first_moment_integer_certificate_alpha_1/4 = PASS")
print("  left_bits =", lhs.bit_length(), "right_bits =", rhs.bit_length())
print("first_moment_integer_certificate_alpha_1/3 = PASS")
print("  left_bits =", lhs13.bit_length(), "right_bits =", rhs13.bit_length())
print("factor_range_pivots =", pivots)
print("B_alpha_1/4 =")
for row in B:
    print(" ", [str(x) for x in row])
print("leading_principal_minors_of_minus_B =")
for x in mins:
    print(" ", x)
print("13*alpha^2+16*alpha-2 =", poly)
print("alpha_c < 1/4 exact_square_check = PASS")
print("ALL_EXACT_CHECKS_PASS")
