#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, log10

def lg(q):
    return log10(q.numerator)-log10(q.denominator)

# Sound upstream factors inherited from the b14/b17_rob construction.
pboot=Fraction(6183007688263727208881325190913,1204952248442880000000000000000000000000)
p150=Fraction(20193231009117236036,580023299851226806640625)
p167=Fraction(9763107163899290190848,350499257108203128488308305)
p178=Fraction(11133436709205330292,456147586622526713121501)
p187=Fraction(22544728691405487104,1022833101788426753598015)
p197=Fraction(26015322500884764075008,1314271656156778872998881905)
p218=Fraction(1672277727444803056,105910938933255255436245)
p222=Fraction(40628945155674655856,2670355970159927065747101)
plan198=Fraction(2048,74183769)
Kup=pboot*p150*p167*p178*p187*p197*p218*p222*plan198

# Latest sound robust terminal factor.
prob=Fraction(
11357683958175627230527864078759314996182455956063867773,
501147979136821382564885299200000000000000000000000000000000)
b17=Kup*prob

# B2 architecture cap: even replacing the terminal stage by certainty leaves Kup.
assert Kup < Fraction(4,10**46)
assert Kup < Fraction(63,64)

# Current robust terminal event: 5 old CO + 5 old O2 + 3 new CO + 4 new O2.
accepted_weight = 8*72 + 9*36
assert accepted_weight == 900
owned_weight = 36*214
assert owned_weight == 7704
a=Fraction(accepted_weight,owned_weight)
assert a == Fraction(25,214)

# Current lambda and effective accepted-arrival mean.
lam=Fraction(429,200)
x=a*lam
assert x == Fraction(429,1712)

# Bound all omitted n>=9 accepted histories, even if every such history succeeds.
# t_{n+1}/t_n=x/(n+1)<=x/10 for n>=9.
tail_ub=(x**9/Fraction(factorial(9),1))/(1-x/Fraction(10,1))
assert tail_ub < Fraction(1,90_000_000_000)
assert tail_ub/prob < Fraction(1,2_050_000)

# Diagnostic from the exact Bellman minima in the preceding executed checker:
# MINS[2]=4320. Conditional on exactly two accepted marks, every entrance
# descriptor therefore has robust target probability >= 4320/900^2=2/375.
two_step=Fraction(4320,accepted_weight**2)
assert two_step == Fraction(2,375)

print("PASS exact R08/E0011 architecture-cap and tail certificate")
print("Kup_exact=",f"{Kup.numerator}/{Kup.denominator}")
print("log10_Kup=",repr(lg(Kup)))
print("Kup_float=",repr(float(Kup)))
print("b17_rob_float=",repr(float(b17)))
print("log10_b17_rob=",repr(lg(b17)))
print("terminal_robust_float=",repr(float(prob)))
print("accepted_fraction=",f"{a.numerator}/{a.denominator}")
print("effective_accepted_mean=",f"{x.numerator}/{x.denominator}")
print("tail_n_ge_9_upper_exact=",f"{tail_ub.numerator}/{tail_ub.denominator}")
print("tail_n_ge_9_upper_float=",repr(float(tail_ub)))
print("tail_over_terminal_upper=",repr(float(tail_ub/prob)))
print("tail_lt_1_over_90_billion=",tail_ub < Fraction(1,90_000_000_000))
print("tail_over_terminal_lt_1_over_2050000=",tail_ub/prob < Fraction(1,2_050_000))
print("robust_two_accepted_mark_floor=",f"{two_step.numerator}/{two_step.denominator}")
