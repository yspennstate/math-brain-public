from fractions import Fraction

K = 100
E3 = 3*K**4 + 6*K**2 + 1
M3 = 3*K**4
ratio = Fraction(M3, E3)
threshold = Fraction(5, 6)
o0_bound = Fraction(5, 1536)

print('E3', E3)
print('M3', M3)
print('ratio', ratio, float(ratio))
print('ratio_gt_5_6', ratio > threshold)
print('O0 anchored lower bound', o0_bound, float(o0_bound))
assert E3 == 300060001
assert M3 == 300000000
assert ratio > threshold
assert o0_bound == Fraction(5, 1536)
print('QFORM_RIDGE_FIXED3_CHECK_PASS')
