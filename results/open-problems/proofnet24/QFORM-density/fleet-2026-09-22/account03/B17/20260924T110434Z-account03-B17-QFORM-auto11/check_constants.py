from fractions import Fraction
from math import sin, pi, sqrt, exp

# Exact Householder matrix B=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]].
B = [[Fraction(6,7), Fraction(-2,7), Fraction(-3,7)],
     [Fraction(-2,7), Fraction(3,7), Fraction(-6,7)],
     [Fraction(-3,7), Fraction(-6,7), Fraction(-2,7)]]

def mm(A,C):
    return [[sum(A[i][k]*C[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

I = [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]
assert mm(B,B) == I
assert all(B[i][j] != 0 for i in range(3) for j in range(3))
assert sum(B[i][i] for i in range(3)) == 1  # reflection eigenvalues 1,1,-1

# Pure-standard-library adaptive Simpson quadrature for K(-7/6).
def simpson(f,a,b):
    c=(a+b)/2.0
    return (b-a)*(f(a)+4.0*f(c)+f(b))/6.0

def adaptive_simpson(f,a,b,eps=1e-13,maxdepth=30):
    whole=simpson(f,a,b)
    def rec(a,b,eps,whole,depth):
        c=(a+b)/2.0
        left=simpson(f,a,c)
        right=simpson(f,c,b)
        delta=left+right-whole
        if depth <= 0 or abs(delta) <= 15.0*eps:
            return left+right+delta/15.0
        return rec(a,c,eps/2.0,left,depth-1)+rec(c,b,eps/2.0,right,depth-1)
    return rec(a,b,eps,whole,maxdepth)

d = 7.0/6.0
K = adaptive_simpson(lambda u: 1.0/sqrt(1.0+d*sin(u)**2), 0.0, pi/2.0)
C_source_valid = sqrt(14.0/3.0)*K
C_elementary = pi*sqrt(7.0/6.0)
partner = 3.0*sqrt(2.0)*exp(-0.03)

assert abs(K-1.2827167711454015) < 1e-12
assert abs(C_source_valid-2.7709849277641085) < 1e-12
assert C_source_valid < C_elementary < partner
assert partner-C_source_valid > 1.3462

# Coarse symbolic-separation surrogates used in the report:
# pi<22/7 and exp(-0.03)>1-0.03=0.97.
lhs_upper=(11.0/7.0)*sqrt(14.0/3.0)
rhs_lower=2.91*sqrt(2.0)
assert lhs_upper < rhs_lower

print('PASS QFORM_HOUSEHOLDER_ONEHEAVY_GAUSSIANPAIR_GLOBAL')
print('K(-7/6)=', repr(K))
print('source_valid_global_constant=', repr(C_source_valid))
print('elementary_upper=', repr(C_elementary))
print('partner_lower=', repr(partner))
print('partner_minus_exact_bound=', repr(partner-C_source_valid))
print('partner_minus_elementary_bound=', repr(partner-C_elementary))
