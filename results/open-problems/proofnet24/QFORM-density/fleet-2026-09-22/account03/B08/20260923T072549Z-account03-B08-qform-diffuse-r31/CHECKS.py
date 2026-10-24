from fractions import Fraction
from math import sqrt
from random import Random

# Exact Desnanot-Jacobi regression:
# a*det([[a,b,x],[c,d,y],[s,t,n]])
# = (ad-bc)*(an-sx) - (ay-cx)*(at-bs).
def det3(a,b,x,c,d,y,s,t,n):
    return a*(d*n-y*t)-b*(c*n-y*s)+x*(c*t-d*s)

rng = Random(31)
for _ in range(1000):
    vals = [Fraction(rng.randint(-9,9)) for _ in range(9)]
    a,b,x,c,d,y,s,t,n = vals
    lhs = a*det3(a,b,x,c,d,y,s,t,n)
    delta = a*d-b*c
    W = a*n-s*x
    U = a*y-c*x
    V = a*t-b*s
    rhs = delta*W-U*V
    assert lhs == rhs

sqrtD_floor = 1/(75*sqrt(3))
factor_floor = 1/(600*sqrt(3))
dj_split_floor = 1/270000
partner_joint_constant = 1200*sqrt(3)
clean_endpoint_constant = 2*sqrt(2)*sqrt(600*sqrt(3))

print('QFORM_B08_R31_CHECK_PASS')
print('sqrtD_floor', sqrtD_floor)
print('factor_floor', factor_floor)
print('DJ_split_floor', dj_split_floor)
print('partner_joint_constant', partner_joint_constant)
print('clean_endpoint_constant', clean_endpoint_constant)
