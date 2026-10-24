#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
import math

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def solve_c(rs):
    mu=sum(rs)
    if abs(mu-1.0) < 1e-14:
        return 0.0
    def f(c):
        prod=1.0
        for r in rs:
            prod *= (1-c*r)
        return 1-c-prod
    lo=1e-12
    hi=1.0
    assert f(lo)>0
    assert f(hi)<=1e-14
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def hmax(rs):
    mu=sum(rs)
    if abs(mu-1.0)<1e-12:
        return -sum(r*math.log2(r) for r in rs if r>0)
    c=solve_c(rs)
    return (sum(h2(c*r) for r in rs)-h2(c))/c

def walsh_int_from_positive(pos, n=4):
    vals=[1 if x in pos else -1 for x in range(1<<n)]
    out=[]
    for S in range(1<<n):
        z=0
        for x,v in enumerate(vals):
            z += v * (-1 if ((x&S).bit_count()&1) else 1)
        out.append(z)
    return out

# Named partner account03/B17 exact quarter/half witness.
G0={0,1,2}
G1={0,1,2,4,5,6,7}
a=walsh_int_from_positive(G0)
b=walsh_int_from_positive(G1)
num0=[(3*a[S]+b[S])**2 for S in range(16)]
num1=[3*(b[S]-a[S])**2 for S in range(16)]
assert Counter(num0)==Counter({64:12,256:2,1024:2})
assert Counter(num1)==Counter({192:4,0:12})
assert sum(num0)+sum(num1)==4096
assert num0[0]==1024
vnum=4096-num0[0]
assert vnum==3072
rs=[Fraction(sum(num1),vnum)]
for j in range(4):
    rs.append(Fraction(sum(num0[S]+num1[S] for S in range(16) if (S>>j)&1),vnum))
assert rs==[Fraction(1,4),Fraction(1,6),Fraction(1,6),Fraction(5,12),Fraction(2,3)]
assert sum(rs)==Fraction(5,3)

nums=[]
for S in range(16):
    if S and num0[S]:
        nums.append(num0[S])
    if num1[S]:
        nums.append(num1[S])
assert Counter(nums)==Counter({64:12,192:4,256:2,1024:1})
H=-sum((n/vnum)*math.log2(n/vnum) for n in nums)
H_exact=7/3 + 3/4*math.log2(3)
assert abs(H-H_exact)<1e-14
rsf=[float(x) for x in rs]
c=solve_c(rsf)
poly=10*c**4-199*c**3+1500*c**2-5292*c+3456
assert abs(poly)<1e-10
Hm=hmax(rsf)
K=Hm-H
C0=6.4548
D=5*C0/16-7/4
R_partner=D/(3/4)
B=R_partner-K
assert 0.8262277822693<c<0.8262277822695
assert 0.2860393237304<K<0.2860393237306
assert B>0.0701273429

# Mandatory recursive-majority multiscale preflight.
for m in [8,12,20]:
    mu=(1.5)**m
    K_lower=mu*(m-4)+2
    assert K_lower>0
    C=6.5584452830718245
    B_upper=mu*(C-m)-C+2
    R=(C-4)*(mu-1)
    assert abs((B_upper+K_lower)-R)<1e-8*max(1.0,R)

# Binary zero-KL sanity: a law on nonempty subsets of two coordinates is
# uniquely determined by its two marginals.
tests=[(0.2,0.3,0.5),(0.0,0.4,0.6),(0.7,0.1,0.2)]
for p1,p2,p12 in tests:
    assert abs(p1+p2+p12-1)<1e-12
    r1=p1+p12; r2=p2+p12
    assert abs((r1+r2-1)-p12)<1e-12
    assert abs((1-r2)-p1)<1e-12
    assert abs((1-r1)-p2)<1e-12

print("PASS")
print("partner_r =", [str(x) for x in rs])
print("partner_c =", format(c,'.16f'))
print("partner_H =", format(H,'.15f'))
print("partner_Hmax =", format(Hm,'.15f'))
print("partner_Kocc =", format(K,'.15f'))
print("partner_R_Gamma0 =", format(R_partner,'.15f'))
print("partner_Binf_Gamma0 =", format(B,'.15f'))
for m in [8,12,20]:
    mu=(1.5)**m
    print("RM3",m,"I",format(mu,'.9f'),"Kocc_lower",format(mu*(m-4)+2,'.9f'),
          "Binf_upper_Cshape",format(mu*(6.5584452830718245-m)-6.5584452830718245+2,'.9f'))
