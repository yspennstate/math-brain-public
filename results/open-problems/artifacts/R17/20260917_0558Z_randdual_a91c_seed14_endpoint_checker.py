#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=120

z=Fraction(256717,800000)
a=2*z
lam_hi=Fraction(
4785233721031882526855598446932313096811318563344907265553110124093161,
13999173439003619880786492129280000000000000000000000000000000000000000)
lam_lo=Fraction(
115456324921460150587109869990619020189572777159906527595486876816471999,
337766807523237062811867173355520000000000000000000000000000000000000000)

U_old=Fraction(82627917854239849,10**17)
U_new=Fraction(8262791785423984831,10**19)
L=Fraction(99083249,125000000)

assert 0 < lam_lo <= lam_hi < 1
assert U_new < U_old

def neglog_bounds(x,n):
    u=(1-x)/(1+x)
    s=Fraction(0); p=u
    for k in range(n):
        s += p/Fraction(2*k+1)
        p *= u*u
    lo=2*s
    hi=lo + 2*p/Fraction(2*n+1)/(1-u*u)
    return lo,hi

Alo,Ahi=neglog_bounds(a,100)
Hlo,Hhi=neglog_bounds(lam_hi,220)
Llo,Lhi=neglog_bounds(lam_lo,220)

p,q=U_new.numerator,U_new.denominator
margin=p*Hlo-2*q*Ahi
assert margin>0

B_fixed_lo=2*Alo/Lhi
B_fixed_hi=2*Ahi/Hlo
assert B_fixed_lo < B_fixed_hi < U_new

improvement=U_old-U_new
width=U_new-L
fixed_gap=B_fixed_hi-B_fixed_lo

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("R17-C024 exact endpoint / seed-14 stochastic-rounding dual Collatz bracket")
print("z =",z)
print("lambda_lower =",lam_lo)
print("lambda_upper =",lam_hi)
print("EXACT_NEW_ENDPOINT_MARGIN_POSITIVE=PASS")
print("margin_decimal =",dec(margin))
print("fixed_z_B_lower_decimal =",dec(B_fixed_lo))
print("fixed_z_B_upper_decimal =",dec(B_fixed_hi))
print("fixed_z_B_bracket_width_decimal =",dec(fixed_gap))
print("CERTIFIED_NEW_UPPER =",U_new)
print("CERTIFIED_NEW_UPPER_DECIMAL =",dec(U_new))
print("PREVIOUS_UPPER =",U_old)
print("UPPER_DECREASE =",improvement)
print("UPPER_DECREASE_DECIMAL =",dec(improvement))
print("CERTIFIED_NEW_WIDTH =",width)
print("CERTIFIED_NEW_WIDTH_DECIMAL =",dec(width))
print("ALL_EXACT_CHECKS_PASS")
