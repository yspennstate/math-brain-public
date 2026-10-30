from fractions import Fraction
from math import sqrt

cstar = Fraction(63,64)*Fraction(4093,4096)
dthr = cstar/Fraction(32,1)
pair = 4*sqrt(30)*float(dthr)**(-3/8)
bank = cstar/Fraction(4,1)
cross = Fraction(3,8)*Fraction(63,64)

assert cstar == Fraction(257859,262144)
assert float(cstar) > 0.9836
assert pair < 81
assert float(bank) > 0.2459
assert cross == Fraction(189,512)

# Matrix-partition second moment / Markov ledger.
# E||S||_F^2 < 1/128 and threshold ||S||_op >=1/4 implies ||S||_F^2>=1/16.
assert Fraction(1,128)/Fraction(1,16) == Fraction(1,8)

# Weight-partition Chebyshev ledger under max d_i < N/32.
# Var W < N^2/128 and deviation threshold N/4.
assert Fraction(1,128)/Fraction(1,16) == Fraction(1,8)
assert Fraction(1,8)+Fraction(1,8) < 1

# Two-dimensional LPP after whitening: cap 2 / sqrt(det G), det G >=1/16.
assert 2/sqrt(Fraction(1,16)) == 8

# Rank-two affine half-Riesz: 128*(det G)^(-1/4), det G>=1/16.
assert abs(128*float(Fraction(1,16))**(-1/4)-256) < 1e-12

# Cross-bank area minimum for eigenvalues x,y in [1/4,3/4] occurs at corners.
def area(x,y):
    return x+y-2*x*y
vals=[area(x,y) for x in (Fraction(1,4),Fraction(3,4)) for y in (Fraction(1,4),Fraction(3,4))]
assert min(vals) == Fraction(3,8)

print('cstar=', float(cstar))
print('cstar/32=', float(dthr))
print('pair_bound=', pair)
print('bank_negative_mass_lower=', float(bank))
print('cross_triple_mass_lower_for_D=1=', float(cross))
print('matrix_balance_failure_bound=', float(Fraction(1,8)))
print('weight_balance_failure_bound=', float(Fraction(1,8)))
print('2d_projection_density_cap=', 8)
print('rank2_half_riesz_factor=', 256)
print('STATUS=PASS')
