#!/usr/bin/env python3
# R03 run31 exact checker: affine-cube-section normalization / excess identity.
# Standard library only; exhaustive for d=2,3,4.

from fractions import Fraction
from itertools import product
from collections import Counter

def det_bareiss(a):
    a = [list(map(int,row)) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n-1):
        if a[k][k] == 0:
            sw = next((i for i in range(k+1,n) if a[i][k] != 0), None)
            if sw is None:
                return 0
            a[k], a[sw] = a[sw], a[k]
            sign *= -1
        piv = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j] = (a[i][j]*piv - a[i][k]*a[k][j]) // prev
        prev = piv
        for i in range(k+1,n):
            a[i][k] = 0
    return sign*a[n-1][n-1]

def replace_col(A,j,col):
    B=[list(r) for r in A]
    for i,x in enumerate(col):
        B[i][j]=x
    return B

def solve_R_one(A):
    d=len(A)
    D=det_bareiss(A)
    assert D != 0
    one=[1]*d
    return tuple(Fraction(det_bareiss(replace_col(A,j,one)), D) for j in range(d))

def solve_A_b(A,b):
    d=len(A)
    D=det_bareiss(A)
    assert D != 0
    return tuple(Fraction(det_bareiss(replace_col(A,j,b)), D) for j in range(d))

def dot(x,w):
    return sum(Fraction(xi)*wi for xi,wi in zip(x,w))

def is_signed_unit(w):
    nz=[i for i,z in enumerate(w) if z != 0]
    return len(nz)==1 and abs(w[nz[0]])==1

def matrices_pm(d):
    for vals in product((-1,1), repeat=d*d):
        yield [list(vals[i*d:(i+1)*d]) for i in range(d)]

EXPECTED = {
    2: {
        "I":8,
        "hist":Counter({(2,True):8}),
        "sum_excess":0,
        "sum_nontriv_excess":0,
    },
    3: {
        "I":192,
        "hist":Counter({(4,True):144,(3,False):48}),
        "sum_excess":144,
        "sum_nontriv_excess":0,
    },
    4: {
        "I":22272,
        "hist":Counter({(8,True):11136,(6,False):9216,(4,False):1920}),
        "sum_excess":62976,
        "sum_nontriv_excess":18432,
    },
}

for d in (2,3,4):
    cube=list(product((-1,1), repeat=d))
    I=0
    hist=Counter()
    sum_ex=0
    sum_non=0
    for R in matrices_pm(d):
        D=det_bareiss(R)
        if D==0:
            continue
        I += 1
        w=solve_R_one(R)
        # R w = 1 exactly.
        for row in R:
            assert dot(row,w)==1
        C=[x for x in cube if dot(x,w)==1]
        M=len(C)
        # One-sided section and antipodal two-level section relation N=2M.
        S=[x for x in cube if dot(x,w) in (1,-1)]
        assert len(S)==2*M
        # The d rows form distinct points in C.
        assert len({tuple(r) for r in R})==d
        assert all(tuple(r) in C for r in R)
        triv=is_signed_unit(w)
        # w=+/-e_j iff one column of R is constant +/-1.
        constcol=any(
            all(R[i][j]==1 for i in range(d)) or all(R[i][j]==-1 for i in range(d))
            for j in range(d)
        )
        assert triv==constcol
        hist[(M,triv)] += 1
        sum_ex += M-d
        if not triv:
            sum_non += M-d

    exp=EXPECTED[d]
    assert I==exp["I"], (d,I)
    assert hist==exp["hist"], (d,hist)
    assert sum_ex==exp["sum_excess"], (d,sum_ex)
    assert sum_non==exp["sum_nontriv_excess"], (d,sum_non)

    # Exact Schur/basis-excess normalization:
    # each R has 2^d preimages (A,b); each affine extra point has
    # two c preimages (+/-); hence successful collision-deleted triples
    # are 2^(d+1) * sum_R (M(R)-d).
    T=(2**(d+1))*sum_ex
    T_non=(2**(d+1))*sum_non
    denom=2**(d*d+2*d)
    q=Fraction(T,denom)
    q_non=Fraction(T_non,denom)
    Pinv=Fraction(I,2**(d*d))
    Eex=Fraction(sum_ex,I)
    Enon=Fraction(sum_non,I)
    assert q == Pinv*Eex/Fraction(2**(d-1))
    assert q_non == Pinv*Enon/Fraction(2**(d-1))

    print(f"d={d}")
    print(f"  invertible_sign_matrices={I}")
    print(f"  histogram_(M,trivial)={sorted(hist.items())}")
    print(f"  sum_excess={sum_ex}")
    print(f"  sum_nontrivial_excess={sum_non}")
    print(f"  E_excess={Eex} = {float(Eex):.15g}")
    print(f"  E_nontrivial_excess={Enon} = {float(Enon):.15g}")
    print(f"  q_all={q} = {float(q):.15g}")
    print(f"  q_nontrivial={q_non} = {float(q_non):.15g}")

# Direct 2^d-to-1 gauge-map check for d=2,3.
for d in (2,3):
    cube=list(product((-1,1), repeat=d))
    fibers=Counter()
    for A in matrices_pm(d):
        if det_bareiss(A)==0:
            continue
        for b in cube:
            wA=solve_A_b(A,b)
            R=[[b[i]*A[i][j] for j in range(d)] for i in range(d)]
            wR=solve_R_one(R)
            assert wA==wR
            key=tuple(tuple(r) for r in R)
            fibers[key]+=1
    assert fibers
    assert set(fibers.values())=={2**d}
    print(f"d={d} gauge_fibers={len(fibers)}, each_fiber={2**d}")

print("SELF-CHECK PASS")
