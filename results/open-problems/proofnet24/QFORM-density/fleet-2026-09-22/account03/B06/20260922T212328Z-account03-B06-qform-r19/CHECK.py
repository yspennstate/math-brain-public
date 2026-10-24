from fractions import Fraction
from math import sqrt
import random

# Live constants.
Cmin = Fraction(1067, 2000)
kappa = Fraction(1, 4096)
Rmax = 2*kappa/Cmin
lead2 = Cmin - Rmax
print('Cmin=', float(Cmin))
print('kappa=', float(kappa))
print('rank1_tail_sq_max=', Rmax, float(Rmax))
print('rank1_tail_norm_max=', sqrt(float(Rmax)))
print('lead_sigma_sq_min=', lead2, float(lead2))
print('relative_tail_max=', sqrt(float(Rmax/lead2)))

# Analytic constant: q=2 regularized determinant -> L^{3/2},
# optimized L3-to-square Abel transducer, then g=gamma/16.
import math
C_abel = 8/(3**0.75)
C_l3base = (9*math.e/2)**(2/3)
C_square_F = C_abel * (9*math.e/2)**0.5
C_live = 4*C_square_F*(float(kappa)**(-1/12))
print('C_abel=', C_abel)
print('C_square_F=', C_square_F)
print('C_live=', C_live)
assert C_live < 99
assert float(Rmax) < 0.000916
assert sqrt(float(Rmax)) < 0.0303
assert sqrt(float(Rmax/lead2)) < 0.0415

# Check the 3x3 Sylvester identity on random integer matrices:
# det([[a,b_s,b_t],[c_k,D_ks,D_kt],[c_l,D_ls,D_lt]]) * a
# = det([[a D_ks-c_k b_s, a D_kt-c_k b_t],
#        [a D_ls-c_l b_s, a D_lt-c_l b_t]])
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

for _ in range(1000):
    a, bs, bt, ck, cl, dks, dkt, dls, dlt = [random.randint(-9,9) for _ in range(9)]
    A = [[a,bs,bt],[ck,dks,dkt],[cl,dls,dlt]]
    lhs = a*det3(A)
    m11=a*dks-ck*bs; m12=a*dkt-ck*bt
    m21=a*dls-cl*bs; m22=a*dlt-cl*bt
    rhs=m11*m22-m12*m21
    assert lhs == rhs
print('sylvester_random_integer_checks=1000 PASS')
print('STATUS=PASS')
