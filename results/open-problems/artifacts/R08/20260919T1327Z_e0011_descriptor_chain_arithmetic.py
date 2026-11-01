#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
from math import factorial, log10
H=7992
LAM=Fraction(429,20)
ELOW=Fraction(404137989405027915949426787307487232,838927307267511894486612536194485579338859375)
P_OLD=Fraction(1623954643648339957527036988793658815878576937278711215614557574564814758157052098047783941784544594218630807061108979453508534372898458711501358833636985872713,11563560585041286174049986736836747564269286100016621400644770549067593869164859124184409145298656907804725977267604059964962468210045987717120000000000000000000000000000000000000000000000000000000)
vals={}
for line in Path(__file__).with_name('20260919T1327Z_e0011_guard_refined_descriptor_check.out').read_text().splitlines():
    f=line.split()
    if len(f)==3 and f[0]=='DATA': vals[int(f[1])]=int(f[2])
assert set(vals)==set(range(18,41))
S=sum((LAM**n)*Fraction(vals[n],factorial(n)*H**n) for n in vals)
P=ELOW*S
R=P/P_OLD
assert P>P_OLD
assert 3*R>20
print('PASS exact R08/E0011 descriptor-chain arithmetic')
print('P_new_exact=',f'{P.numerator}/{P.denominator}')
print('ratio_exact=',f'{R.numerator}/{R.denominator}')
print('ratio_gt_20_over_3=',3*R>20)
print('ratio_decimal=',repr(float(R)))
print('log10_ratio=',repr(log10(R.numerator)-log10(R.denominator)))
print('log10_b21_diagnostic=',repr(-49.25315461739025 + log10(R.numerator)-log10(R.denominator)))
