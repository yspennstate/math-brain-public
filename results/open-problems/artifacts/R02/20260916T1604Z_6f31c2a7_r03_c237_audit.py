#!/usr/bin/env python3
# R02 independent exact core for R03-C237, 2026-09-16T1604Z.
from fractions import Fraction
from math import comb

print("R02 independent audit of R03-C237")

# Exact positivity of gamma = log2(64/35)-3/4:
# gamma>0 iff (64/35)^4>8.
delta = 64**4 - 8*35**4
assert delta == 4_772_216 > 0
print("64^4 - 8*35^4 =", delta)

# Exact Littlewood-Offord/Sperner ceiling at k=7,8.
p7 = Fraction(comb(7,3), 2**7)
p8 = Fraction(comb(8,4), 2**8)
assert p7 == p8 == Fraction(35,128)
print("p7 = p8 =", p7)

# Independent finite sanity check over a long exact range.
mx = Fraction(0,1)
arg = None
for k in range(7,2001):
    pk = Fraction(comb(k,k//2), 2**k)
    assert pk <= Fraction(35,128)
    if pk > mx:
        mx,arg = pk,k
assert mx == Fraction(35,128) and arg == 7
print("exact p_k check k=7..2000: PASS")

# Analytic recurrence behind the all-k claim:
# p_{2m+2}=p_{2m+1}, and
# p_{2m+3}/p_{2m+2}=(2m+3)/(2m+4)<1.
for m in range(3,1000):
    p_odd = Fraction(comb(2*m+1,m), 2**(2*m+1))
    p_even = Fraction(comb(2*m+2,m+1), 2**(2*m+2))
    p_next = Fraction(comb(2*m+3,m+1), 2**(2*m+3))
    assert p_even == p_odd
    assert p_next / p_even == Fraction(2*m+3,2*m+4)
    assert p_next < p_even
print("pair recurrence check m=3..999: PASS")

# Dyadic proof constants for log2 n <= sqrt(n)/4 for n>=4096.
# If 2^m <= n < 2^(m+1), m>=12, then log2 n<m+1 and
# sqrt(n)/4 >= 2^(m/2-2). Base: 13<=16. Induction uses
# (m+2)/(m+1)<=14/13<sqrt(2), certified by squaring.
assert 13 <= 16
assert 14**2 < 2*13**2
print("dyadic log inequality induction constants: PASS")

print("R02-AUDIT-R03-C237-03 = PASS (claim-scoped)")
