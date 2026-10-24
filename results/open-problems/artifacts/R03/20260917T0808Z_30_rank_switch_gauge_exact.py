#!/usr/bin/env python3
"""
R03 run30 exact self-check.

Checks:
(1) C281 gauge identity on all sign triples for d<=3, and against the
    previously certified d=4 Schur total from R03 run29.
(2) C282 determinant/cofactor identity for every singular binary matrix
    through d=4.
(3) Exact collision-free binary counts G_d, residual singular counts R_d,
    and rank-switch counts H_d^o through d=5.
(4) Exact one-step strongly-nonsingular hazards from the published/external
    exact counts a_d, d<=9.  These are arithmetic replays, not an independent
    re-enumeration of the external d=8,9 data.
All arithmetic is integer/rational.
"""
from itertools import combinations, product
from math import factorial
from fractions import Fraction

def det_bareiss(M):
    A=[list(map(int,row)) for row in M]
    n=len(A)
    if n == 0:
        return 1
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k] == 0:
            pivot=None
            for i in range(k+1,n):
                if A[i][k] != 0:
                    pivot=i
                    break
            if pivot is None:
                return 0
            A[k],A[pivot]=A[pivot],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n):
            A[i][k]=0
        for j in range(k+1,n):
            A[k][j]=0
    return sign*A[n-1][n-1]

def minor(M, ri, cj):
    n=len(M)
    return [[M[i][j] for j in range(n) if j != cj] for i in range(n) if i != ri]

def cofactor_sum(M):
    n=len(M)
    return sum(((-1)**(i+j))*det_bareiss(minor(M,i,j))
               for i in range(n) for j in range(n))

def bits_row(x,d):
    return [(x>>j)&1 for j in range(d)]

def collision_free_binary_rows(rows,d):
    # rows are already distinct and nonzero in the subset enumeration.
    cols=[tuple(row[j] for row in rows) for j in range(d)]
    return all(any(c) for c in cols) and len(set(cols)) == d

def enumerate_G_R_H(d):
    """
    Row-permutation quotient enumeration:
      G_d = collision-free binary dxd matrices
      R_d = collision-free real-singular binary dxd matrices
      H_d = those R_d with sign lift J-2X invertible.
    """
    G=R=H=0
    row_orbits=0
    for comb in combinations(range(1,1<<d), d):
        rows=[bits_row(x,d) for x in comb]
        if not collision_free_binary_rows(rows,d):
            continue
        row_orbits += 1
        mult=factorial(d)
        G += mult
        detx=det_bareiss(rows)
        if detx == 0:
            R += mult
            S=[[1-2*rows[i][j] for j in range(d)] for i in range(d)]
            if det_bareiss(S) != 0:
                H += mult
    return G,R,H,row_orbits

def sign_matrices(d):
    for mask in range(1<<(d*d)):
        yield [[1 if (mask>>(i*d+j))&1 else -1
                for j in range(d)] for i in range(d)]

def replace_col(A,j,b):
    d=len(A)
    return [[b[i] if k == j else A[i][k] for k in range(d)] for i in range(d)]

def schur_numer(A,b,c):
    detA=det_bareiss(A)
    nums=[det_bareiss(replace_col(A,j,b)) for j in range(len(A))]
    return sum(c[j]*nums[j] for j in range(len(A))), detA

def border_collision_free(A,b,c,branch):
    # branch is the forced bottom-right sign (+1 or -1).
    d=len(A)
    for j in range(d):
        col=[A[i][j] for i in range(d)]
        for s in (1,-1):
            if all(b[i] == s*col[i] for i in range(d)) and branch == s*c[j]:
                return False
    for i in range(d):
        row=A[i]
        for s in (1,-1):
            if all(c[j] == s*row[j] for j in range(d)) and branch == s*b[i]:
                return False
    return True

def direct_schur_counts(d):
    signs=list(product((-1,1), repeat=d))
    inv=plus=minus=0
    for A in sign_matrices(d):
        detA=det_bareiss(A)
        if detA == 0:
            continue
        inv += 1
        for b in signs:
            for c in signs:
                num,den=schur_numer(A,b,c)
                if num == den and border_collision_free(A,b,c,+1):
                    plus += 1
                elif num == -den and border_collision_free(A,b,c,-1):
                    minus += 1
    return inv,plus,minus

print("=== C281: gauge identity, exhaustive direct sign triples for d<=3 ===")
GRH={}
for d in range(1,6):
    GRH[d]=enumerate_G_R_H(d)

for d in range(1,4):
    inv,plus,minus=direct_schur_counts(d)
    H=GRH[d][2]
    pred_branch=(1<<(2*d))*H
    pred_total=2*pred_branch
    print(f"d={d}: invertible_sign={inv}, direct_plus={plus}, direct_minus={minus}, "
          f"pred_branch={pred_branch}, pred_total={pred_total}")
    assert plus == pred_branch
    assert minus == pred_branch

# Cross-check against the already independently certified d=4 Schur total from run29.
RUN29_D4_XI = 589824
assert (1<<(2*4+1))*GRH[4][2] == RUN29_D4_XI
print(f"d=4 retained-run29 cross-check: 2^(2d+1)*H_4={RUN29_D4_XI}")

print("\n=== C282: rank-one sign-lift/cofactor identity, exhaustive binary d<=4 ===")
for d in range(1,5):
    singular=0
    for mask in range(1<<(d*d)):
        X=[[ (mask>>(i*d+j))&1 for j in range(d)] for i in range(d)]
        if det_bareiss(X) != 0:
            continue
        singular += 1
        S=[[1-2*X[i][j] for j in range(d)] for i in range(d)]
        lhs=det_bareiss(S)
        cof=cofactor_sum(X)
        rhs=(((-1)**(d+1))*(2**(d-1))*cof)
        assert lhs == rhs
        assert (lhs != 0) == (cof != 0)
    print(f"d={d}: all {singular} singular binary matrices satisfy "
          "det(J-2X)=(-1)^(d+1)2^(d-1)*sum(cofactors)")

print("\n=== Exact collision-free finite sequence ===")
for d in range(1,6):
    G,R,H,orbits=GRH[d]
    print(f"d={d}: row_orbits={orbits}, G_d={G}, R_d={R}, H_d={H}")
assert GRH[4][:3] == (24360,1800,1152)
assert GRH[5][:3] == (15198120,2683800,1342800)

print("\n=== Strong-nonsingular one-step hazards from exact external counts ===")
# Exact totals a_d from Orellana Mateo--Urschel--West public computation:
sns = {
    1: 1,
    2: 4,
    3: 68,
    4: 5008,
    5: 1603232,
    6: 2224232640,
    7: 13288620860672,
    8: 339148010221571072,
    9: 36646054311185413881216,
}
# P_d = a_d / 2^(d^2); h_d = 1 - P_{d+1}/P_d.
for d in range(1,9):
    Pd=Fraction(sns[d], 1<<(d*d))
    Pnext=Fraction(sns[d+1], 1<<((d+1)*(d+1)))
    h=1-Pnext/Pd
    print(f"d={d}: h_d={h} = {float(h):.15f}")
    assert 0 <= h <= 1

print("\n=== Dense sign pivot-chain multiplicity: C283 finite audit ===")
import itertools
def is_sns(M):
    d=len(M)
    return all(det_bareiss([row[:k] for row in M[:k]]) != 0 for k in range(1,d+1))

def dephased_sign_matrices(d):
    # Unique row/column-sign gauge: first row and first column are +1.
    interior=(d-1)*(d-1)
    for mask in range(1<<interior):
        A=[[1]*d for _ in range(d)]
        for i in range(1,d):
            for j in range(1,d):
                bit=(mask>>((i-1)*(d-1)+(j-1)))&1
                A[i][j]=1 if bit else -1
        yield A

def valid_flag(A,p,q):
    d=len(A)
    for k in range(1,d+1):
        sub=[[A[p[i]][q[j]] for j in range(k)] for i in range(k)]
        if det_bareiss(sub)==0:
            return False
    return True

def pivot_multiplicity(A):
    d=len(A)
    perms=list(itertools.permutations(range(d)))
    return sum(valid_flag(A,p,q) for p in perms for q in perms)

for d in range(2,5):
    vals=[]
    for A in dephased_sign_matrices(d):
        if det_bareiss(A)!=0:
            vals.append(pivot_multiplicity(A))
    floor=(1<<(d-1))*factorial(d)
    print(f"d={d}: dephased invertibles={len(vals)}, min m(A)={min(vals)}, "
          f"C283 floor=2^(d-1)d!={floor}, max={max(vals)}")
    assert min(vals) >= floor

print("\n=== Sign-SNS / binary-SNS dephasing identity ===")
# Directly enumerate dephased sign representatives through sign size 5.
for d in range(2,6):
    deph_sns=sum(is_sns(A) for A in dephased_sign_matrices(d))
    expected=sns[d-1]
    full_sign_sns=(1<<(2*d-1))*deph_sns
    print(f"sign size d={d}: dephased_SNS={deph_sns}=binary a_{d-1}; "
          f"full sign SNS={full_sign_sns}")
    assert deph_sns == expected

print("\n=== Exact aggregate Schur hazard under a strongly-nonsingular sign core ===")
# P(sign-SNS at size d)=P(binary-SNS at size d-1), exactly.
# Therefore Pr_{A SNS_d,b,c}[c^T A^-1 b in {+-1}]
# = 2*(1 - P_SNS_sign(d+1)/P_SNS_sign(d))
# = 2 * binary one-step hazard from (d-1) to d.
for d in range(2,10):
    Pprev=Fraction(sns[d-1], 1<<((d-1)*(d-1)))
    Pnext=Fraction(sns[d], 1<<(d*d))
    schur_prob=2*(1-Pnext/Pprev)
    print(f"sign core d={d}: aggregate Schur ±1 probability={schur_prob} "
          f"= {float(schur_prob):.15f}")
    assert 0 <= schur_prob <= 1

print("\nSELF-CHECK PASS")
