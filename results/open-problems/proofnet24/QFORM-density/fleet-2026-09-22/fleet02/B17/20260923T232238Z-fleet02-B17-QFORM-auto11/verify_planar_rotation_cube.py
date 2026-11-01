#!/usr/bin/env python3
"""Deterministic checks for QFORM-PLANAR-ROTATION-CUBE-GLOBAL-v1."""
import math

# A(a,b) = [[a,0,b],[0,1,0],[b,0,-a]], with a^2+b^2=1.
# Direct multiplication gives A^2=diag(a^2+b^2,1,a^2+b^2)=I,
# trace(A)=1 and det(A)=-(a^2+b^2)=-1, hence spectrum {1,1,-1}.
for a,b in [(1.0,0.0),(0.0,1.0),(3/5,4/5),(-5/13,12/13)]:
    assert abs(a*a+b*b-1.0) < 1e-14
    A = ((a,0.0,b),(0.0,1.0,0.0),(b,0.0,-a))
    A2 = [[sum(A[i][k]*A[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            assert abs(A2[i][j]-(1.0 if i==j else 0.0)) < 1e-14

K = 4*math.pi/3
sharp = 3*math.sqrt(2)
partner = 2**(13/6)*math.sqrt(3/math.pi)*math.gamma(5/4)**(2/3)
midpoint_tip = 2 + math.log(2)
assert K < sharp
assert partner < sharp
assert midpoint_tip < K
# Rational certificate used in the report: pi<22/7 and 88<63*sqrt(2).
assert 7744 < 7938
print('PASS QFORM-PLANAR-ROTATION-CUBE-GLOBAL-v1')
print('4pi/3 =', repr(K))
print('3sqrt2 =', repr(sharp))
print('gap =', repr(sharp-K))
print('partner C_2H1G =', repr(partner))
print('midpoint tip 2+log2 =', repr(midpoint_tip))
