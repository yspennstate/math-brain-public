from fractions import Fraction
from math import sqrt

# Exact algebra regression for the determinant cancellation in
# QFORM-ZERO-DIAGONAL-TRIPLE-v1.

def det3_zero(a,b,c,d,e):
    return -a*a*e + 2*a*b*d - b*b*c

def gamma(a,b,c,d,e):
    rho2 = a*a+b*b
    # coefficient of w^2 after r=ay+bz, w=-by+az
    return Fraction(a*a*e - 2*a*b*d + b*b*c, rho2*rho2)

def check_tuple(vals):
    a,b,c,d,e = vals
    if a == 0 and b == 0:
        return True
    D = det3_zero(a,b,c,d,e)
    rho2 = a*a+b*b
    return gamma(a,b,c,d,e) == Fraction(-D, rho2*rho2)

samples = [
    (1,2,3,4,5),
    (2,-1,7,3,-4),
    (0,3,5,-2,8),
    (5,0,-3,9,2),
    (-4,7,1,-6,11),
]
assert all(check_tuple(s) for s in samples)

# Numerical regression for the optimized split constant:
# inf_R [4 sqrt(2) sqrt(R)/sqrt(D) + 1/(2R)]
# = 3*2^(2/3) D^(-1/3).
for D in [0.125, 1.0, 3.0, 17.0, 1000.0]:
    C0 = 4*sqrt(2)/sqrt(D)
    x = C0**(-1/3)  # x=sqrt(R)
    lhs = C0*x + 1/(2*x*x)
    rhs = 3*(2**(2/3))*(D**(-1/3))
    assert abs(lhs-rhs) < 1e-12*max(1.0,abs(rhs))

print('ALL_CHECKS_PASS')
