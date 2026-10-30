from fractions import Fraction
from math import sqrt, pi


def schur_difference(a,b,d,x,v,u,w,r):
    lhs = a*x*x + d*v*v + 2*b*x*v + 2*x*u + 2*v*w + r
    rhs = d*(v + (b*x+w)/d)**2 + (a-b*b/d)*x*x + 2*x*(u-(b/d)*w) + r - w*w/d
    return lhs-rhs


tests = [
    tuple(map(Fraction, [1,1,1,2,3,4,5,6])),
    (Fraction(4,9), Fraction(2,3), Fraction(1), Fraction(-3,5), Fraction(7,4), Fraction(5,8), Fraction(-2,7), Fraction(11,13)),
    (Fraction(9,4), Fraction(-3,2), Fraction(1), Fraction(5,6), Fraction(-8,9), Fraction(-7,10), Fraction(2,3), Fraction(-4,11)),
]

for idx,t in enumerate(tests,1):
    print(f"schur_diff_{idx}={schur_difference(*t)}")

K3 = 2*sqrt(pi)/(3**0.25)
combined = K3 * (3**0.75)
physical_constant = combined * (2**0.25)
print(f"K3={K3:.16f}")
print(f"combined={combined:.16f}")
print(f"2sqrt3pi={2*sqrt(3*pi):.16f}")
print(f"physical_constant={physical_constant:.16f}")
assert all(schur_difference(*t) == 0 for t in tests)
assert abs(combined - 2*sqrt(3*pi)) < 1e-14
print("STATUS=PASS")
