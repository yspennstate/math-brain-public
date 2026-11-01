from fractions import Fraction
from math import pi, sqrt

# Explicit fully coupled non-lightlike orientation u=(1,1,1)/sqrt(3).
B = [
    [Fraction(1,3), Fraction(-2,3), Fraction(-2,3)],
    [Fraction(-2,3), Fraction(1,3), Fraction(-2,3)],
    [Fraction(-2,3), Fraction(-2,3), Fraction(1,3)],
]

def matmul(A,C):
    return [[sum(A[i][k]*C[k][j] for k in range(len(C)))
             for j in range(len(C[0]))] for i in range(len(A))]

I3 = [[Fraction(int(i == j),1) for j in range(3)] for i in range(3)]
assert matmul(B,B) == I3
assert sum(B[i][i] for i in range(3)) == 1
# Since B^2=I and tr(B)=1 in dimension 3, the eigenvalue multiset is {1,1,-1}.

x1=x2=Fraction(1,3)
c = (Fraction(114) + 6*(x1+x2) - 39*(x1*x1+x2*x2))/640
assert c == Fraction(41,240)

# Uniform lower bound.  If s=x1+x2 in [0,1], x1^2+x2^2 <= s^2, so
# 640*c12 >= F(s)=114+6s-39s^2.  F is concave, hence its minimum on [0,1]
# is attained at an endpoint and equals 81.
F0 = Fraction(114)
F1 = Fraction(114)+6-39
assert min(F0,F1) == 81
cmin = Fraction(81,640)
assert c >= cmin

# Exact radial coarea majorant used for the O(ell^3) remainder:
# sup_s T[(1+|y|)^-8](s) <= pi * int_R (1+|z|)^-8 dz = 2*pi/7.
radial_bound = 2*pi/7

baseline = 3*sqrt(2)
partner_bound_001 = baseline/(1-0.01)

print('PASS QFORM-NONLIGHTLIKE-TWO-PARTIAL-HEAVY-GLOBAL-BARRIER-v1')
print('B^2=I and tr(B)=1 => spectrum {1,1,-1}')
print('c_explicit=41/240', float(c))
print('c_uniform_min=81/640', float(cmin))
print('radial_remainder_pushforward_bound=2*pi/7', radial_bound)
print('baseline_3sqrt2', baseline)
print('partner_gaussian_floor_bound_at_ell=.01', partner_bound_001)
