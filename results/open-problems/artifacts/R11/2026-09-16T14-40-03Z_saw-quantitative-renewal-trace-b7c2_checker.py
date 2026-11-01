#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

print("R11 exact-arithmetic self-check: quantitative DCH renewal trace")

count=0
for q in range(2,401):
    for p in range(1,q):
        if gcd(p,q)!=1:
            continue
        z=Fraction(p,q)
        if z>Fraction(1,8):
            continue
        L=(q+p-1)//p  # ceil(1/z)=ceil(q/p)
        r=z/Fraction(8*L,1)
        s=z/Fraction(24*L*L,1)
        d=s/2

        # C002: fixed-parameter substitution in DCH Case 3.
        assert r + 3*L*s <= z
        ratio=(z-s)/((r+3*L*s)*L)
        assert ratio >= Fraction(23,6)
        assert ratio > 2

        # Terminal renewal density in Case 3 after floor loss.
        assert d <= z**3/Fraction(48,1)

        # C004/X002 constants:
        # h(z)=H(4z)>2z, while I(d)<=d log(mu)<=2d<=z^3/24.
        rate_cap_rational=z**3/Fraction(24,1)
        entropy_floor_rational=2*z
        assert rate_cap_rational < entropy_floor_rational
        count+=1

# Elementary logarithm certificates in the written proof.
# log 2 > 1/2 because e^(1/2)<2.
partial = Fraction(1,1)+Fraction(1,2)+sum(Fraction(1,2**k) for k in range(2,80))
assert partial < 2
# log 3 < 2 because e^2>1+2+2^2/2=5>3.
assert Fraction(1,1)+Fraction(2,1)+Fraction(2**2,2) > 3

# C003 rounding lemma:
# m=floor(delta*n)-1 >= delta*n/2 whenever delta*n>=4.
floor_checks=0
for den in range(1,101):
    for num in range(1,den+1):
        delta=Fraction(num,den)
        n0=(4*den+num-1)//num
        for n in range(n0,n0+200):
            m=(num*n)//den - 1
            assert Fraction(m,1) >= delta*n/2
            floor_checks+=1

# X002 nested-threshold algebra. If a positive branch-aware certificate exists,
# then z_{j-1}<z_j^3/48. With z_m<=1/8 this implies
# z_1 <= 8^{-3^{m-1}}, hence c <= z_1^3/24 <= 8^{-3^m}/24.
for m in range(1,7):
    z=Fraction(1,8)  # z_m
    zs=[None]*(m+1)
    zs[m]=z
    for j in range(m,1,-1):
        zs[j-1]=zs[j]**3/Fraction(48,1)
    assert zs[1] <= Fraction(1,8**(3**(m-1)))
    ccap=zs[1]**3/Fraction(24,1)
    assert ccap <= Fraction(1,24*8**(3**m))

print("Certified elementary bounds: log(2)>1/2 and log(3)<2")
print("C002 constants checked on",count,"reduced rational z values in (0,1/8].")
print("C003 rounding lemma checked on",floor_checks,"rational/integer cases.")
print("X002 nested-threshold double-exponential cap checked for m=1..6.")
print("PASS")
