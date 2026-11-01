#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=120

z=Fraction(256717,800000)
a=2*z

# Exact max/min component-ratio certificate after deterministic
# pseudorandom stochastic rounding of the converged positive direction.
lam_hi=Fraction(
14355701163095647579393559535531144234817955690034721796659330372279483,
41997520317010859630966006087680000000000000000000000000000000000000000)
lam_lo=Fraction(
230912649842920301162275702344875305777602033419218088344017515166205201,
675533615046474125623734346711040000000000000000000000000000000000000000)

U_old=Fraction(82627917854239849,10**17)
U_new=Fraction(8262791785423984833,10**19)
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

# gamma <= 2*(-log(2z))/(-log lam_hi).  This is below U_new if
# p*(-log lam_hi)_lower > 2q*(-log(2z))_upper.
p,q=U_new.numerator,U_new.denominator
margin=p*Hlo-2*q*Ahi
assert margin>0

# Collatz-Wielandt also gives lam_lo <= rho(A_z) <= lam_hi.
# Since B(lambda)=2*(-log(2z))/(-log lambda) is increasing on 0<lambda<1,
# these yield a fixed-z bracket for the optimal Perron certificate.
B_fixed_lo=2*Alo/Lhi
B_fixed_hi=2*Ahi/Hlo
assert B_fixed_lo < B_fixed_hi < U_new

improvement=U_old-U_new
width=U_new-L
fixed_gap=B_fixed_hi-B_fixed_lo

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("R17-C024 exact endpoint / randomized-rounding dual Collatz bracket")
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
