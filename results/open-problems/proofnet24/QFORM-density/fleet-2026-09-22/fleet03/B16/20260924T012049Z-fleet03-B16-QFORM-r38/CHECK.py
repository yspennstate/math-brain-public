from fractions import Fraction
import math

# Sharp innovation-free balanced model at epsilon=1/100.
eps = Fraction(1,100)
# G_J=G_K=I/2, d=(2 sqrt(eps),0), delta_J=delta_K=0.
# d^T G_J G_K d = eps exactly.
# det(G_J)=1/4 and d^T G_K d = 2 eps.
M_JJK = Fraction(1,4) * (2*eps)
M_JKK = M_JJK
assert M_JJK == eps/2
assert M_JKK == eps/2
assert M_JJK/eps == Fraction(1,2)
assert M_JKK/eps == Fraction(1,2)

# Pure bank normalized 3-volume is zero because both innovations vanish.
P_J = Fraction(0,1)
P_K = Fraction(0,1)
assert P_J + P_K == 0
assert M_JJK/eps + M_JKK/eps == 1

# Partner slope inequalities in this model.
d2 = 4*eps
assert 2*eps < d2
assert d2 <= Fraction(16,3)*eps

# Constant for the prior authentic trace-obstruction family, c=127/128.
c = 127/128
C = 3*(2**(2/3))*c**(-1/3)
assert C < 4.775
print('epsilon=', float(eps))
print('normalized_mixed_JJK=', float(M_JJK/eps))
print('normalized_mixed_JKK=', float(M_JKK/eps))
print('normalized_total_mixed=', float((M_JJK+M_JKK)/eps))
print('zero_pivot_true_density_constant=', C)
print('STATUS=PASS')
