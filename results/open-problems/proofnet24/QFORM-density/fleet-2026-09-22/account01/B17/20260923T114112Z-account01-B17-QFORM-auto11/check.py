from fractions import Fraction as F
from math import sqrt

# Exact Taylor check for exp(x/24)*sinc(sqrt(x)/2), x=ell*t^2.
e = [F(1), F(1,24), F(1,2*24**2), F(1,6*24**3)]
s = [F(1), -F(1,24), F(1,1920), -F(1,322560)]
c = [sum(e[k]*s[n-k] for k in range(n+1)) for n in range(4)]
assert c == [F(1), F(0), -F(1,2880), -F(1,181440)]

def a(x):
    return F(57) + F(6)*x - F(39)*x*x

assert a(F(0)) == 57
assert a(F(1)) == 24
assert 2*a(F(1,3))/F(640) == F(41,240)
assert 3*a(F(1,3))/F(640) == F(41,160)
assert F(57*2-33,640) == F(81,640)
assert F(57*3-33,640) == F(69,320)

# Exact fully coupled core B_*^2=I.
B = [
    [F(1,3), F(-2,3), F(-2,3)],
    [F(-2,3), F(1,3), F(-2,3)],
    [F(-2,3), F(-2,3), F(1,3)],
]
B2 = [[sum(B[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert B2 == [[F(int(i == j)) for j in range(3)] for i in range(3)]

print('QFORM_B17_THREE_PARTIAL_HEAVY_CHECK_PASS')
print('series:', c)
print('partner_equal_two_u*=41/240 =', float(F(41,240)))
print('three_equal_u*=41/160 =', float(F(41,160)))
print('equal_two_orientation_min=81/640 =', float(F(81,640)))
print('equal_three_orientation_min=69/320 =', float(F(69,320)))
print('3sqrt2 =', 3*sqrt(2))
