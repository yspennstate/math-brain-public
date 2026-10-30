from fractions import Fraction
import math

R = [
    [Fraction(1,2), Fraction(1,2), Fraction(1,2)],
    [Fraction(1,2), Fraction(-1,2), Fraction(-1,2)],
    [Fraction(-1,2), Fraction(1,2), Fraction(-1,2)],
    [Fraction(-1,2), Fraction(-1,2), Fraction(1,2)],
]
lam = [Fraction(2), Fraction(3), Fraction(-1)]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def qbil(x,y):
    return sum(lam[k]*x[k]*y[k] for k in range(3))

for a in range(3):
    for b in range(3):
        val = sum(R[i][a]*R[i][b] for i in range(4))
        assert val == (1 if a == b else 0)

r0, r1 = R[0], R[1]
C00, C01, C11 = qbil(r0,r0), qbil(r0,r1), qbil(r1,r1)
detC = C00*C11-C01*C01
Delta = dot(r0,r0)*dot(r1,r1)-dot(r0,r1)**2
detL = lam[0]*lam[1]*lam[2]
s = detL*Delta/detC

assert C00 == 1 and C01 == 0 and C11 == 1
assert detC == 1
assert Delta == Fraction(1,2)
assert detL == -6
assert s == -3

vnum = [Fraction(0), Fraction(1), Fraction(-1)]
nums = [dot(r,vnum) for r in R]
assert nums[0] == 0 and nums[1] == 0
assert nums[2] == 1 and nums[3] == -1
assert Fraction(nums[2]**2 + nums[3]**2, 2) == 1

constant = 16.0*math.sqrt(15.0)*math.exp(0.25)
assert 79.568 < constant < 79.569

print('QFORM_AFFINE_TWOPIVOT_CHECK_PASS')
print('detC=', detC)
print('Delta=', Delta)
print('detLambda=', detL)
print('s=', s)
print('tail_Z_norm2=1')
print('constant=', format(constant, '.15f'))
