"""Exact/numerical checks for QFORM-NULL-COLOOP-PROJECTION-PRODUCT-v1."""
from fractions import Fraction
import math

# determinant of [[0,b,0],[b,c11,c12],[0,c12,c22]]
# direct cofactor expansion = -b^2*c22.
def det3(b,c11,c12,c22):
    return -b*b*c22

tests=[(2,3,5,7), (Fraction(3,5),Fraction(-2,7),Fraction(11,13),Fraction(-17,19))]
for b,c11,c12,c22 in tests:
    direct = 0*(c11*c22-c12*c12)-b*(b*c22-0*c12)+0
    assert direct == det3(b,c11,c12,c22)

# For F(z)=8 M sqrt(z/D)+1/(2z),
# F'(z)=4M/(sqrt(D)*sqrt(z)) - 1/(2z^2).
# Critical point z=D^(1/3)/(4 M^(2/3)).
for M,D in [(1.0,1.0),(2.0,1.0),(3.5,7.25)]:
    z = D**(1/3)/(4*M**(2/3))
    near = 8*M*math.sqrt(z/D)
    far = 1/(2*z)
    target_near = 4*M**(2/3)*D**(-1/3)
    target_far = 2*M**(2/3)*D**(-1/3)
    assert abs(near-target_near) < 1e-12
    assert abs(far-target_far) < 1e-12
    assert abs((near+far)-6*M**(2/3)*D**(-1/3)) < 1e-12

# bathtub integral: integral_{-1/2}^{1/2}|x|^-1/2 dx=2 sqrt(2)
assert abs(4*math.sqrt(0.5)-2*math.sqrt(2)) < 1e-15

partner_constant = 6*2**(2/3)
assert partner_constant < 9.525
print(f"partner_constant={partner_constant:.15f}")
print("STATUS=PASS")
