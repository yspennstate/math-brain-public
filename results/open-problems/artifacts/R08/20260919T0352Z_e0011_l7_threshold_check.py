from fractions import Fraction
from math import log10, factorial

def lg(x):
    return log10(x.numerator)-log10(x.denominator)

pboot=Fraction(6183007688263727208881325190913,1204952248442880000000000000000000000000)
p150=Fraction(20193231009117236036,580023299851226806640625)
p167=Fraction(9763107163899290190848,350499257108203128488308305)
p178=Fraction(11133436709205330292,456147586622526713121501)
p187=Fraction(22544728691405487104,1022833101788426753598015)
p197=Fraction(26015322500884764075008,1314271656156778872998881905)
p201=Fraction(7168864776621912190976,514520327344022846669179035)
p218=Fraction(1672277727444803056,105910938933255255436245)
p222=Fraction(40628945155674655856,2670355970159927065747101)
plan198=Fraction(2048,74183769)
b13=pboot*p150*p167*p178*p187*p197*p201*p218*p222*plan198

p191=Fraction(32174057841088741889352078572126208,1524916181058564276415872049475569582080)
p211=Fraction(57085003286130579675209813685436416,3382506790988617846636155362604881018880)
plan191=Fraction(8192,276124689)
K7=pboot*p150*p167*p178*p191*p211*p211*plan191
q_needed=b13/K7
qword=Fraction(32,87)**21 * Fraction(21**21,factorial(21)) * Fraction(2**14,194**21)
ratio=q_needed/qword
assert q_needed>qword
print('PASS exact R08/E0011 L7 threshold arithmetic')
print('log10_b13=',repr(lg(b13)))
print('log10_K7_without_terminal=',repr(lg(K7)))
print('log10_q_needed_to_beat_b13=',repr(lg(q_needed)))
print('q_needed_decimal=',repr(float(q_needed)))
print('log10_qword=',repr(lg(qword)))
print('orders_short=',repr(lg(ratio)))
print('ratio_needed_decimal=',repr(float(ratio)))
print('q_needed_exact=',f'{q_needed.numerator}/{q_needed.denominator}')
print('qword_exact=',f'{qword.numerator}/{qword.denominator}')
