from fractions import Fraction
import math

m = Fraction(3501, 8000)

# Case A: pi*sqrt(2)/m < 11, using pi<22/7 and sqrt(2)<3/2.
assert Fraction(33, 7) / m < 11

# Case B: the exact numerical theorem constant is <73.
K = 3 * 400 ** (1/3)
C_indef = K * float(m**5 / 20) ** (-1/6)
assert C_indef < 73

# A completely rational coarse verification gives <80:
# 400^(1/3)<8 and m>7/16.
assert m > Fraction(7, 16)
assert Fraction(24**6 * 20 * 16**5, 7**5) < 80**6

# Case C: 128*(m^2/16)^(-1/4) < 387, checked by fourth powers.
assert Fraction(128**4 * 16, 1) / (m*m) < 387**4
C_triple = 128 * float(m*m / 16) ** (-1/4)
assert C_triple < 387

# Sign-frustrated moderate cell has |g|>1/2+1/sqrt(2)>1/4.
frustrated_gap = 0.5 + 1 / math.sqrt(2)
assert frustrated_gap > 0.25

# Partner second-row threshold at tau=1/4.
assert Fraction(1, 4) / 9 == Fraction(1, 36)

# Exact Schur determinant identity on rational calibration points.
def det3(a,b,c,x,y,z):
    return a*b*c + 2*x*y*z - a*z*z - b*y*y - c*x*x

def schur_det(a,b,c,x,y,z):
    d = b - x*x/a
    f = c - y*y/a
    e = z - x*y/a
    return d*f - e*e

samples = [
    tuple(map(Fraction, (2,3,5,1,1,-1))),
    tuple(map(Fraction, (3,4,7,2,-1,3))),
    (Fraction(7,3), Fraction(5,2), Fraction(11,4), Fraction(2,3), Fraction(-5,4), Fraction(7,5)),
]
for vals in samples:
    a,b,c,x,y,z = vals
    assert det3(a,b,c,x,y,z) == a * schur_det(a,b,c,x,y,z)

print("PASS QFORM r15 constants/algebra")
print("indefinite-pair displayed constant =", C_indef)
print("physical-triple displayed constant =", C_triple)
print("sign-frustrated normalized determinant gap =", frustrated_gap)
