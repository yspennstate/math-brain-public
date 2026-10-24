#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
from math import log10

H=7992
LAM=Fraction(429,20)
ELOW=Fraction(
404137989405027915949426787307487232,
838927307267511894486612536194485579338859375)
P_OLD_ARCHIVED=Fraction(
1623954643648339957527036988793658815878576937278711215614557574564814758157052098047783941784544594218630807061108979453508534372898458711501358833636985872713,
11563560585041286174049986736836747564269286100016621400644770549067593869164859124184409145298656907804725977267604059964962468210045987717120000000000000000000000000000000000000000000000000000000)

path=Path(__file__).with_name('20260919T1327Z_e0011_horizontal_descriptor_glue_check.out')
scalar={}; relation={}
for line in path.read_text().splitlines():
    f=line.split()
    if len(f)==4 and f[0]=='DATA':
        n=int(f[1]); scalar[n]=int(f[2]); relation[n]=int(f[3])
assert set(scalar)==set(range(18,41))
assert all(relation[n]>=scalar[n] for n in scalar)
assert sum(relation[n]>scalar[n] for n in scalar)==11

def poisson_lower(coeff):
    s=Fraction(0)
    fact=1
    for n in range(41):
        if n: fact*=n
        a=coeff.get(n,0)
        if a:
            s += LAM**n * Fraction(a,H**n*fact)
    return ELOW*s

P0=poisson_lower(scalar)
P1=poisson_lower(relation)
assert P0==P_OLD_ARCHIVED
assert P1>P0
assert 4*P1>5*P0
R=P1/P0
print('PASS exact R08/E0011 descriptor-gluing arithmetic')
print('strict_coefficients=',sum(relation[n]>scalar[n] for n in scalar))
print('P_scalar_matches_archived=',P0==P_OLD_ARCHIVED)
print('P_relation_exact=',f'{P1.numerator}/{P1.denominator}')
print('ratio_exact=',f'{R.numerator}/{R.denominator}')
print('ratio_gt_5_over_4=',4*P1>5*P0)
print('ratio_decimal=',repr(float(R)))
print('log10_ratio=',repr(log10(R.numerator)-log10(R.denominator)))
print('log10_b21_diagnostic=',repr(-49.25315461739025 + log10(R.numerator)-log10(R.denominator)))
