#!/usr/bin/env python3
"""
I0014 exact finite self-check, 2026-09-16.
Scope: finite rational checks supporting the base-2 normalization correction
for the Bradley displayed-test threshold. The universal asymptotic argument
is analytic in the run report; this script is a self-check, not an
independent theorem audit.
"""
from fractions import Fraction

K = 80
lo = sum((Fraction(1, j * (2**j)) for j in range(1, K+1)), Fraction(0))
hi = lo + Fraction(1, (K+1) * (2**K))

# Exact tail certificate:
# sum_{j>K} 1/(j 2^j) <= (1/(K+1))*sum_{j>K}2^-j = 1/((K+1)2^K)
assert lo < hi
assert lo > Fraction(693147180559, 10**12)
assert hi < Fraction(693147180560, 10**12)

# d_* = 2 / ln 2: using lo < ln2 < hi gives 2/hi < d_* < 2/lo.
dlo = Fraction(2,1) / hi
dhi = Fraction(2,1) / lo
assert dlo > Fraction(2885, 1000)
assert dhi < Fraction(2886, 1000)
assert dlo > 2

# Equality coefficient for beta=1/3, gamma=2/3, alpha=1:
# second asymptotic term is -(6/ln2) L^(1/3).
clo = Fraction(6,1) / hi
chi = Fraction(6,1) / lo
assert clo > Fraction(8656, 1000)
assert chi < Fraction(8657, 1000)

# Rational beta grid: equality exponent 2 gamma - 1 = 1 - 2 beta > 0.
betas = [Fraction(1,10), Fraction(1,4), Fraction(1,3), Fraction(2,5), Fraction(49,100)]
rows=[]
for beta in betas:
    gamma = 1-beta
    p = 2*gamma-1
    assert Fraction(0) < beta < Fraction(1,2)
    assert Fraction(1,2) < gamma < 1
    assert p == 1-2*beta
    assert p > 0
    rows.append((beta,gamma,p))

# Leading coefficient A(d_B)=(alpha/gamma)(2-d_B ln2).
# Rigorous sign checks at representative rational d_B using ln2 enclosure.
# For d_B=2, A>0 (because 2 ln2 < 2); prior d=2 literal-Bradley claim is false.
assert 2*hi < 2
# d_B=3: 3 ln2 > 2, so leading coefficient is negative.
assert 3*lo > 2

def dec(fr, digits=15):
    from decimal import Decimal, getcontext
    getcontext().prec = digits+10
    return Decimal(fr.numerator)/Decimal(fr.denominator)

print("I0014 BASE-2 BRADLEY THRESHOLD EXACT SELF-CHECK")
print(f"K={K}")
print(f"ln2 lower = {dec(lo,18)}")
print(f"ln2 upper = {dec(hi,18)}")
print(f"d*=2/ln2 lower = {dec(dlo,18)}")
print(f"d*=2/ln2 upper = {dec(dhi,18)}")
print(f"beta=1/3 equality |coefficient|=6/ln2 lower = {dec(clo,18)}")
print(f"beta=1/3 equality |coefficient|=6/ln2 upper = {dec(chi,18)}")
print("beta | gamma | equality exponent 1-2beta")
for beta,gamma,p in rows:
    print(f"{beta} | {gamma} | {p}")
print("literal d_B=2 leading sign: POSITIVE (condition fails at leading order)")
print("literal d_B=3 leading sign: NEGATIVE (condition succeeds at leading order)")
print("critical literal Bradley threshold: d_B*ln(2)=2, equality included analytically for beta<1/2")
print("ALL EXACT I0014 BASE2-THRESHOLD CHECKS PASSED")
