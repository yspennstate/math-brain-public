#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import prod, factorial

# R03 run22 exact finite core.
# C263: exact collision-free residual identity via partition Möbius / signed Stirling.
# C264: finite CRT/Hadamard singularity certificate.
# The n=9 total singular count is included ONLY as an external-source input and is
# explicitly not promoted to a replay-certified campaign metric.

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A)
    if n==0: return 1
    prev=1
    sign=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((i for i in range(k+1,n) if A[i][k]),None)
            if r is None: return 0
            A[k],A[r]=A[r],A[k]
            sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n):
            A[i][k]=0
    return sign*A[-1][-1]

def signed_stirling_first(n,k):
    d=[[0]*(k+2) for _ in range(n+1)]
    d[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            d[i][j]=d[i-1][j-1]-(i-1)*d[i-1][j]
    return d[n][k]

def falling(x,m):
    if x<m: return 0
    ans=1
    for j in range(m):
        ans*=x-j
    return ans

def collision_free_count_formula(m):
    # C260 at V=0, grouped by number b+1 of partition blocks
    return sum(
        signed_stirling_first(m+1,b+1)*falling(2**b-1,m)
        for b in range(m+1)
    )

def good(A):
    m=len(A)
    rows=[tuple(r) for r in A]
    if any(not any(r) for r in rows): return False
    if len(set(rows))<m: return False
    cols=[tuple(A[i][j] for i in range(m)) for j in range(m)]
    if any(not any(c) for c in cols): return False
    if len(set(cols))<m: return False
    return True

# Full brute-force regression through m=4.
for m in range(1,5):
    g=0
    gs=0
    s=0
    for flat in product((0,1), repeat=m*m):
        A=[flat[i*m:(i+1)*m] for i in range(m)]
        z=(det_bareiss(A)==0)
        s+=z
        if good(A):
            g+=1
            gs+=z
    gf=collision_free_count_formula(m)
    assert g==gf
    assert gs==s-(2**(m*m)-gf)
    print("BRUTE",m,"good",g,"singular",s,"good_singular",gs,"PASS")

# Published/classified exact singular counts through m=8, used as regression.
S={
  1:1,
  2:10,
  3:338,
  4:42976,
  5:21040112,
  6:39882864736,
  7:292604283435872,
  8:8286284310367538176,
}
expected_r={
  2:Fraction(0),
  3:Fraction(0),
  4:Fraction(0),
  5:Fraction(225,256),
  6:Fraction(335475,65536),
  7:Fraction(149664375,8388608),
  8:Fraction(1658391558075,34359738368),
  9:Fraction(15544095862461075,140737488355328),
}
for m,s in S.items():
    gf=collision_free_count_formula(m)
    bad_collision=2**(m*m)-gf
    residual=s-bad_collision
    r=Fraction(2**(m+1)*residual,2**(m*m))
    assert r==expected_r[m+1]
    print("REGRESSION",m,"G",gf,"collision_singular",bad_collision,
          "residual",residual,"r",r,"PASS")

# Order m=9: exact collision count, but total singular input is source-backed only.
m=9
G9=collision_free_count_formula(m)
T9=2**81
collision9=T9-G9
S9_EXTERNAL=902_616_230_040_448_613_437_952
resid9_external=S9_EXTERNAL-collision9
r10_external=Fraction(2**10*resid9_external,T9)
print("M9 exact_G9",G9)
print("M9 exact_collision_singular",collision9)
print("M9 EXTERNAL_SOURCE_INPUT_NOT_REPLAY_CERTIFIED S9",S9_EXTERNAL)
print("M9 source_backed_candidate_residual",resid9_external)
print("M9 source_backed_candidate_r10",r10_external,float(r10_external))

# Current campaign-certified bound from R03-C262 for comparison only.
r10_current=Fraction(635840639911659887775,2305843009213693952)
print("current_certified_r10",r10_current,float(r10_current))
print("candidate_gap",r10_current-r10_external,float(r10_current-r10_external))
assert r10_external < r10_current

# C264 finite CRT + Hadamard certificate for m=9.
primes=[2,3,5,7,11,13]
Q=prod(primes)
# Hadamard: |det A| <= m^(m/2); avoid floating point by squaring.
assert Q*Q > m**m
print("CRT primes",primes,"Q",Q,"Q^2",Q*Q,"m^m",m**m,"PASS")
print("C264 statement: if det(A) is 0 mod every listed prime, then det(A)=0 over Z for every 9x9 binary A.")

print("SELF-CHECK PASS")
