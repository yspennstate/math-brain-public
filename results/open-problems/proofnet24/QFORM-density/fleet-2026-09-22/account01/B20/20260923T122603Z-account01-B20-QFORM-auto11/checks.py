from fractions import Fraction
from math import sqrt, e

# N3 star threshold alpha=1/60.
tau = Fraction(1,64)
alpha = Fraction(1,60)
S_lower = alpha - tau*tau
edge_cap = tau + tau*tau
bank_floor = (S_lower-edge_cap)/2
assert S_lower == Fraction(1009,61440)
assert edge_cap == Fraction(65,4096)
assert bank_floor == Fraction(17,61440)

leaf_cross_F2 = Fraction(63,64)**2 / 4
retained_top4 = Fraction(63,64)*leaf_cross_F2
assert leaf_cross_F2 == Fraction(3969,16384)
assert retained_top4 == Fraction(250047,1048576)

# D5 payment on the complementary diffuse fifth-volume branch.
Z5 = (Fraction(1,64)**4) * (leaf_cross_F2**5) / 120
D5_bound = 5*sqrt(2*e)*float(Z5)**(-0.1)
assert D5_bound < 201.787

# Spectral-window P_{|A|>=1/16} theorem at leverage epsilon=1/50.
epsilon = Fraction(1,50)
# delta = 1/2 - sqrt(2epsilon) - epsilon, and sqrt(2epsilon)=1/5 exactly.
delta = Fraction(1,2)-Fraction(1,5)-epsilon
eta = Fraction(1,16)
sigma = delta-eta
gamma = Fraction(2,3)*sigma
range_leverage = epsilon/delta
assert delta == Fraction(7,25)
assert sigma == Fraction(87,400)
assert gamma == Fraction(29,200)
assert range_leverage == Fraction(1,14)

# Exact rational proof of the ridge leverage gate:
# 1/sqrt(2) > 7/10, 1/sqrt(14) < 15/56, and
# 7/10 - 15/56 = 121/280 > 25/58 = eta/gamma.
assert Fraction(1,2) > Fraction(49,100)
assert Fraction(1,14) < Fraction(225,3136)
assert Fraction(121,280) > Fraction(25,58)

ridge_bracket = 1/sqrt(14) + Fraction(25,58)
assert float(ridge_bracket)**2 < 0.5

theta = Fraction(27,13)
assert theta > 2
ridge_bound = sqrt(e)/(sqrt(2)*float(gamma))*float(theta/(theta-2))
closed_form = 5400*sqrt(e)/(29*sqrt(2))
assert abs(ridge_bound-closed_form) < 1e-12
assert ridge_bound < 217.085

# Residual spectral annulus [1/16,1).
annulus_leverage = Fraction(1,50)-Fraction(1,60)
annulus_energy = Fraction(1,16)**2 * annulus_leverage
assert annulus_leverage == Fraction(1,300)
assert annulus_energy == Fraction(1,76800)

print('S_lower=', S_lower)
print('edge_cap=', edge_cap)
print('bank_floor=', bank_floor)
print('leaf_cross_F2=', leaf_cross_F2)
print('retained_top4=', retained_top4)
print('D5_bound=', D5_bound)
print('delta=', delta, 'sigma=', sigma, 'gamma=', gamma, 'range_leverage=', range_leverage)
print('ridge_bracket_sq=', float(ridge_bracket)**2)
print('theta=', theta)
print('ridge_bound=', ridge_bound)
print('annulus_leverage=', annulus_leverage, 'annulus_energy=', annulus_energy)
print('STATUS=PASS')
