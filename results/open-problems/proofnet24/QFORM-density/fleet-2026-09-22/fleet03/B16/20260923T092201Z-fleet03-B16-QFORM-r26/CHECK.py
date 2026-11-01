from fractions import Fraction
from math import sqrt

# Algebra/constants for QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SCHUR-v1.
# Strict target family uses B_r = 6 M_r, M_r=[[-r,1,0],[1,0,1],[0,1,-1]], 0<=r<=1/10.

cmin = Fraction(63,64)
rmax = Fraction(1,10)

# det M_r = 1+r; Frobenius norm squared = 5+r^2.
# For a 3x3 invertible matrix, s_min >= |det| / ||M||_op^2 >= |det| / ||M||_F^2.
# Thus on [0,1/10], s_min(M_r)>=1/(5+1/100)=100/501 and s_min(6M_r)>=600/501>1.
assert Fraction(600,501) > 1

# In B_r, b=-6 and det B_r=216(1+r), so |b det B_r|=1296(1+r)=6^4(1+r).
assert 6*216 == 1296 == 6**4

# Schur complement after the V-coordinate: delta=-6r, kappa=6, lambda=6.
# theta=kappa^2-delta*lambda=36(1+r)=-det(B)/b.
# det(B)=216(1+r), b=-6 => -det(B)/b=36(1+r).
for rr in (0.0, 0.01, 0.1):
    theta = 36*(1+rr)
    rhs = -216*(1+rr)/(-6)
    assert abs(theta-rhs) < 1e-12

# With L_X=1, L_U=L_V=sqrt(2), gamma=sqrt(c), the theorem gives
# 8*sqrt(2)*sqrt(sqrt(2)/sqrt(c))*[1296(1+r)]^{-1/4}
# = (4/3)*2^(3/4)c^{-1/4}(1+r)^{-1/4}.
C = (4/3)*(2**(3/4))*float(cmin)**(-1/4)
C0 = (2/3)*(2**(3/4))*float(cmin)**(-1/4)
assert C < 2.252
assert C0 < 1.126

# Designated fleet04/B16 application: d>=1/64 -> 12*d^{-1/6} <=24.
partner = 12*(1/64)**(-1/6)
assert abs(partner-24) < 1e-12

print('family_spectral_lower_bound', float(Fraction(600,501)))
print('family_uniform_bound_nonzero', C)
print('family_exact_null_bound', C0)
print('partner_d_ge_1_64_bound', partner)
print('STATUS=PASS')
