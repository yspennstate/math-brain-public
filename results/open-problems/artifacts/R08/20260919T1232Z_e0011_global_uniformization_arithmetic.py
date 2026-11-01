#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, log10
from pathlib import Path

OUT = Path(__file__).with_name('20260919T1232Z_e0011_global_uniformization_dp.out')
if not OUT.exists():
    OUT = Path('/tmp/r08_global2.out')
lines = OUT.read_text().splitlines()
assert lines[0].strip() == 'H 7992 N 40'
H=7992
back={}
fwd={}
for line in lines[1:]:
    if line.startswith('PASS'): break
    n,b,f=line.split()
    back[int(n)]=int(b); fwd[int(n)]=int(f)
assert min(back)==18 and max(back)==40
assert all(v==0 for v in fwd.values())
assert back[18]==1335241765123705160600345389301760
assert back[22]==21594360744990667130171544797248513823121711562752
assert back[30]==3430163092891565906095118909235211804747824182107317023868347474414853817368576
assert back[40]==3238122226406033110010001541728022258844508450664395979649766319648774405894871547125803946961701103992832

# Rational exponential lower bound at lambda = 429/20 = 21 + 9/20.
# e < 87/32 follows from sum_{k=0}^7 1/k! plus the geometric tail
# 1/8! * (1 + 1/9 + 1/9^2 + ...) = 9/(8*8!).
s7=sum(Fraction(1,factorial(k)) for k in range(8))
e_ub=s7+Fraction(9,8*factorial(8))
assert e_ub < Fraction(87,32)
# For x=9/20<1 the alternating exponential series has decreasing terms;
# the odd partial sum S5 is a strict lower bound on exp(-x).
x=Fraction(9,20)
s5=sum(Fraction((-1)**k,factorial(k))*x**k for k in range(6))
assert s5>0
exp_lb=Fraction(32,87)**21*s5
lam=Fraction(429,20)
series=Fraction(0,1)
for n,z in back.items():
    series += Fraction(z,H**n)*lam**n/Fraction(factorial(n),1)
global_lb=exp_lb*series

# Exact product of the eight old separately timed fixed-window factors,
# reproduced from the previous exact R08 stopping-frontier checker.
old=Fraction(
16946887982981099613821774804202543667509311462476912028568316115607833420406078379041971105450473739351666188715000952232074065544640591602092763665069397508096,
490273736936502388875210578804028109467775779340352736092320355483884900515738733577039063637641927574925758611699116504283587927814562992810884100490347652798323517866096802474467175006866455078125)
ratio=global_lb/old
assert global_lb > 4*old
assert ratio > 4
# Also verify the deterministic physical horizon.
T=Fraction(4,222)*lam
assert T==Fraction(143,370)

print('PASS exact R08/E0011 global fixed-top arithmetic')
print('lambda = 429/20')
print('T = 143/370')
print('exp_lower =', f'{exp_lb.numerator}/{exp_lb.denominator}')
print('global_corridor_lower =', f'{global_lb.numerator}/{global_lb.denominator}')
print('old_eight_window_product =', f'{old.numerator}/{old.denominator}')
print('exact_ratio =', f'{ratio.numerator}/{ratio.denominator}')
print('ratio_decimal =', float(ratio))
print('log10_ratio_diagnostic =', log10(float(ratio)))
print('global_corridor_decimal =', float(global_lb))
print('old_corridor_decimal =', float(old))
print('B25_forward_pointwise_min_envelope_zero_through_40 =', all(v==0 for v in fwd.values()))
