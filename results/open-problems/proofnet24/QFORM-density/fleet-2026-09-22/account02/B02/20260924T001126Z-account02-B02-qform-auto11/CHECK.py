#!/usr/bin/env python3
"""Deterministic corroboration for account02/B02 20260924T001126Z.

The proof is in REPORT.md. This checker only verifies exact finite-cut
combinatorics of the seven-coordinate obstruction and the displayed constants.
It uses only the Python standard library.
"""
from fractions import Fraction
import itertools, math

N=7  # h,y1,z1,y2,z2,u,v

def aval(i,j,eps=1):
    if i==j:
        return 0
    a,b=sorted((i,j))
    if (a,b) in {(0,1),(0,2),(3,4)}:
        return 1
    if (a,b)==(5,6):
        return eps
    return 0

def det(M):
    n=len(M)
    if n==0: return 1
    if n==1: return M[0][0]
    out=0
    for j,x in enumerate(M[0]):
        if x:
            minor=[row[:j]+row[j+1:] for row in M[1:]]
            out += (-1)**j*x*det(minor)
    return out

def Ek(I,J,k,eps=1):
    if len(I)<k or len(J)<k:
        return 0
    total=0
    for S in itertools.combinations(I,k):
        for T in itertools.combinations(J,k):
            d=det([[aval(i,j,eps) for j in T] for i in S])
            total += d*d
    return total

vals=set(); max_e3=0; e4_violations=0; cuts=0
for assign in itertools.product((0,1,2), repeat=N):
    I=[i for i,a in enumerate(assign) if a==1]
    J=[i for i,a in enumerate(assign) if a==2]
    if len(I)>=3 and len(J)>=3:
        cuts += 1
        e3=Ek(I,J,3,1)
        vals.add(e3)
        max_e3=max(max_e3,e3)
        e4_violations += (Ek(I,J,4,1)!=0)

assert vals == {0,1,2}
assert max_e3 == 2
assert e4_violations == 0

# A disjoint cut can contain at most one orientation of the u-v edge, so every
# 3x3 determinant is affine in eps. At eps=0 every crossing has rank <=2.
# Thus the exact E3 values are {0,eps^2,2eps^2}; E5 is identically zero.

coef=Fraction(63,4096)*Fraction(8,3125)
C3=10.345084
C_v1=C3*float(coef)**(-1/6)
C_target=C_v1*float(Fraction(1,4))**(-1/6)
C_D5=5*math.e/math.sqrt(2)

assert abs(float(coef)-3.9375e-5)<1e-18
assert abs(C_v1-56.08722161207775)<1e-12
assert abs(C_target-70.66547113917542)<1e-12
assert abs(C_D5-9.61057757039779)<1e-12

print({
  "cuts_checked": cuts,
  "E3_over_eps2_values": sorted(vals),
  "max_E3_over_eps2": max_e3,
  "E4_violations": e4_violations,
  "heavy_zero_pivot_E3_prefactor": float(coef),
  "V1_density_prefactor": C_v1,
  "V1_gt_1_over_4_absolute_bound": C_target,
  "sharp_HY_D5_constant": C_D5,
  "status": "PASS"
})
