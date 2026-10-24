#!/usr/bin/env python3
"""
R03 exact checker: F3 cube-subspace sieve for iid Rademacher singularity.

Finite/exact components:
  (1) verifies the sharp 3/4 cube-loss lemma for all F3 linear forms
      on k<=8 Boolean variables;
  (2) computes exact counts of Boolean/partition subspaces
      N_{m,k}=sum_{r=k}^m binom(m,r) S(r,k);
  (3) uses retained exact counts of real-invertible k x k 0/1 matrices
      for k<=8 to sharpen the ordered-basis count;
  (4) evaluates the rigorous recurrence lower-bounding F3 invertibility;
  (5) prints the resulting explicit b_F3(n) envelope, including the new
      certified n=10 value.

This does not enumerate all 9x9 binary matrices and does not claim the exact
n=10 singularity probability.
"""
from itertools import product
from fractions import Fraction
from math import comb

def stirling2(n,k):
    if n==k==0: return 1
    if n==0 or k==0: return 0
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def partition_subspaces(m,k):
    return sum(comb(m,r)*stirling2(r,k) for r in range(k,m+1))

def falling_distinct_nonzero(k):
    x=1
    for j in range(k):
        x *= (2**k-1-j)
    return x

SING_REAL={
    1:1,
    2:10,
    3:338,
    4:42976,
    5:21040112,
    6:39882864736,
    7:292604283435872,
    8:8286284310367538176,
}
INV_REAL={k:2**(k*k)-s for k,s in SING_REAL.items()}

def ordered_basis_upper(k):
    d=falling_distinct_nonzero(k)
    return min(d,INV_REAL[k]) if k in INV_REAL else d

for k in range(1,9):
    total=2**k
    good_max=0
    bad_arg=None
    for a in product(range(3), repeat=k):
        special = all(x==0 for x in a) or (
            sum(x==1 for x in a)==1 and sum(x!=0 for x in a)==1
        )
        good=0
        for u in product((0,1), repeat=k):
            val=sum(ai*ui for ai,ui in zip(a,u))%3
            good += val in (0,1)
        if special:
            assert good==total
        else:
            assert 4*good <= 3*total
            if good>good_max:
                good_max=good; bad_arg=a
    print("linear-form-loss",k,"max_nonboolean",good_max,"of",total,
          "arg",bad_arg,"PASS")

m=9
print("partition-subspace-table m=9")
for k in range(1,m):
    N=partition_subspaces(m,k)
    D=falling_distinct_nonzero(k)
    A=ordered_basis_upper(k)
    print(k,"N",N,"distinct_bound",D,
          "real_inv_bound",INV_REAL.get(k),
          "basis_upper",A)

def f3_lower(m):
    if m==0:
        return Fraction(1,1)
    L=Fraction(2**m-1,2**m)
    for k in range(1,m):
        N=partition_subspaces(m,k)
        A=ordered_basis_upper(k)
        U=min(Fraction(1,1), Fraction(N*A,2**(m*k)))
        q=Fraction(2**k,2**m)
        L=(1-Fraction(3,4)*q)*L-Fraction(1,4)*q*U
        assert L>=0
    return L

print("F3-lower-table")
for mm in range(1,21):
    L=f3_lower(mm)
    print(mm,L,float(L))

n=10
m=n-1
L=f3_lower(m)
p_sing=1-L
b=2**n*p_sing-2*n*(n-1)
print("n10 L_F3",L,float(L))
print("n10 p_sing_upper",p_sing,float(p_sing))
print("n10 b_F3",b,float(b))

expected=Fraction(15469313101167294167,36028797018963968)
assert b==expected

old=Fraction(18818920154267,34359738368)
assert b<old
print("prior_F2_b10",old,float(old))
print("improvement",old-b,float(old-b))

print("uniform-envelope-samples")
for nn in range(2,16):
    LL=f3_lower(nn-1)
    bb=2**nn*(1-LL)-2*nn*(nn-1)
    print(nn,bb,float(bb))

print("SELF-CHECK PASS")
