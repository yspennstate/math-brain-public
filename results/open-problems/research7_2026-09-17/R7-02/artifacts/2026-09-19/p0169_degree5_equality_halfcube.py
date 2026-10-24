#!/usr/bin/env python3
"""Exact equality-profile certificate for the 11-variable d=5 sparse dual.

This exhausts all integer Newton layer profiles of a degree<=5 Boolean
symmetrization on 11 variables that attain the proven signed singleton upper
bound 17/8.  It certifies in particular that every such equality profile has
constant Fourier coefficient zero.  No realizability of any surviving profile
is asserted.
"""
from fractions import Fraction
from math import comb

N=11
TARGET16=34

def b_from_u(u,k):
    return sum(u[j]*comb(N-j,k-j) for j in range(6) if j<=k)

def objective16(u):
    return -16*u[1]-16*u[2]-12*u[3]-8*u[4]-5*u[5]

def kraw(n,j,k):
    return sum(((-1)**r)*comb(k,r)*comb(n-k,j-r)
               for r in range(j+1) if r<=k and j-r<=n-k)

def level_sums(bs):
    out=[]
    for j in range(6):
        num=0
        for k,b in enumerate(bs):
            num += (2*b-comb(N,k))*kraw(N,j,k)
        out.append(Fraction(num,2**N))
    return tuple(out)

# Equality in L=(b0-b11)/16+(b3-b8)/80 <=17/8 forces
# b0=1,b11=0,b3=C(11,3)=165,b8=0.
profiles=[]
u0=1
for u1 in range(-11,1):
    # 0<=b2<=55 gives a complete finite range for u2.
    u2_lo=-comb(11,2)-10*u1
    u2_hi=-10*u1
    for u2 in range(u2_lo,u2_hi+1):
        # b3=165 determines u3 exactly.
        u3=165-comb(11,3)-comb(10,2)*u1-comb(9,1)*u2
        # b11=0: u4+u5=-(u0+u1+u2+u3).
        S=-(u0+u1+u2+u3)
        # objective16=34 determines u4.
        numer=-(TARGET16+16*u1+16*u2+12*u3+5*S)
        if numer%3:
            continue
        u4=numer//3
        u5=S-u4
        u=(u0,u1,u2,u3,u4,u5)
        if objective16(u)!=TARGET16:
            continue
        bs=tuple(b_from_u(u,k) for k in range(N+1))
        if bs[0]!=1 or bs[3]!=165 or bs[8]!=0 or bs[11]!=0:
            continue
        if all(0<=bs[k]<=comb(N,k) for k in range(N+1)):
            profiles.append((u,bs))

expected_u=[
    (1,-5,37,-108,125,-50),
    (1,-4,30,-90,105,-42),
    (1,-3,23,-72,85,-34),
    (1,-2,16,-54,65,-26),
    (1,-1,9,-36,45,-18),
]
assert [u for u,_ in profiles]==expected_u
assert len(profiles)==5
fourier=[level_sums(bs) for _,bs in profiles]
for A in fourier:
    assert A[0]==0
    assert A[1]==Fraction(17,8)
    assert A[2]==0 and A[4]==0
# all profiles are aggregate-antipodal as a consequence of the exact constraints
for _,bs in profiles:
    assert all(bs[N-k]==comb(N,k)-bs[k] for k in range(N+1))

print('P0169 d=5 eleven-variable equality-profile certificate')
print('arithmetic=integer/Fraction; floating_point=False')
print('equality_profile_count',len(profiles))
for idx,(u,bs) in enumerate(profiles,1):
    print('profile',idx,'u',list(u))
    print('profile',idx,'b',list(bs))
    print('profile',idx,'level_fourier_sums_A0_to_A5',[str(x) for x in fourier[idx-1]])
print('all_equality_profiles_constant_coefficient_zero',True)
print('all_equality_profiles_antipodal_layer_complementarity',True)
print('REALIZABILITY_NOT_ASSERTED')
print('ASSERTIONS_PASS')
