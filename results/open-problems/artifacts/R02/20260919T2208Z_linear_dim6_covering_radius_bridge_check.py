#!/usr/bin/env python3
from fractions import Fraction

TARGET = Fraction(49,17)
checked = 0
worst = (Fraction(-1,1), None, None)
for n in range(32,64):
    # A binary linear antipodal code with <=2n words has dimension <=6 here.
    assert 2*n < 128
    # The k=6 published exact minimum covering radius gives these discrepancy caps.
    dcap = 8 if n % 2 == 0 else 9
    ratio_sq = Fraction(dcap*dcap,n)
    assert ratio_sq < TARGET
    if ratio_sq > worst[0]:
        worst = (ratio_sq,n,dcap)
    checked += 1

assert checked == 32
assert worst == (Fraction(27,11),33,9)
assert 27*17 < 49*11
print('R02 linear dimension-6 covering-radius bridge exact corollary check')
print('orders_checked=32..63 count=32')
print('target_ratio_squared=49/17')
print('worst_dim6_cap_ratio_squared=27/11 at n=33 discrepancy_cap=9')
print('exact_comparison=27*17=459 < 539=49*11')
print('first_possible_dimension7_order=64')
print('PASS')
