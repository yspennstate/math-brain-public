from fractions import Fraction as F
from math import factorial

# fleet03/B13 exact certificates for candidate s8 < 349.

# Inner s5 retune.
assert F(677,8000) < F(291,1000)**2
assert F(1)-F(11,40)-F(291,1000)-4*F(107,1000) == F(3,500)
assert 25**8 < 2*23**8

e_partial_6 = sum(F(1, factorial(k)) for k in range(7))
# tail from 1/7! onward is at most a geometric series with ratio 1/8
assert e_partial_6 + F(1,4410) < F(68,25)

# C2 sqrt(2/h) < 105/2 after e<68/25 and 2^(-1/8)<23/25.
c2_majorant_sq = F(64*23**2*68*2000, 25**2*25*107)
assert c2_majorant_sq < F(105,2)**2
assert F(9,1000) > F(32,105)**4

# Logarithm certificates and scalar inner branch.
x = F(347,500)
assert sum(x**k/F(factorial(k),1) for k in range(5)) > 2
x = F(161,100)
assert sum(x**k/F(factorial(k),1) for k in range(8)) > 5
C_upper = F(22,7) + 4*F(347,500) + 8 + 8*F(161,100)
assert C_upper == F(23449,875) and C_upper < 27
assert F(27**2,1)/F(11,40) < F(103,2)**2

# Outer s8 collar radicals.
assert F(1,138) < F(1,11)**2
assert F(559,250)**2 < 5 < F(22361,10000)**2
assert F(3,23) < F(903,2500)**2

first = 1-F(1,44)-3*F(22361,10000)/44-2*F(903,2500)
second = 1-F(1,44)+3*F(559,250)/44
assert first == F(45061,440000)
assert second == F(12427,11000)
delta_lower = first*second
assert delta_lower == F(559973047,4840000000)
assert delta_lower > F(23,200)

# Robust anchor excludes two high leverages.
assert F(529,240000) > F(2025,937024)

# One-high completion with ||E||_F <= 1/5.
diag = F(4,5)-F(1,44)
row_sum = 2*(F(27,176)+F(1,5))
assert diag-row_sum == F(31,440)
assert F(529,6000000) > F(1,12000)

# Large-V3 branch <349.
assert F(99,70)**2 > 2
assert 2*9**6 > 9*7**6
assert F(47,4)**2 > 138
large_upper = 2*3*F(99,70)*F(68,25)*F(9,7)*F(47,4)
assert large_upper == F(2135727,6125)
assert large_upper < 349

# Outer scalar branch <349.
assert F(349)**2 - 44*F(105,2)**2 == 526

print('QFORM_B13_S8_349_EXACT_CHECK_PASS')
print('delta_lower =', delta_lower)
print('large_branch_upper =', large_upper)
print('scalar_square_margin = 526')
