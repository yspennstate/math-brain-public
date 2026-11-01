from math import sqrt, e
from fractions import Fraction

# Concrete q>1 spectral-window branch.
delta = 59/1000
kappa = 1/1000
q = 4/3
r = 27/100
g = 0.5 - delta - sqrt(2*delta)
sigma = g - kappa
gate = (sqrt(delta/g) + kappa/(r*sigma))**2
theta0 = 3/(1+r*r)
C = sqrt(e)/(sqrt(2*q)*r*sigma) * theta0/(theta0-2*q)

assert g > 0.09748
assert sigma > 0.09648
assert Fraction(34352,100000)**2 > Fraction(59,500)
assert Fraction(59,1000)/Fraction(9748,100000) < Fraction(778,1000)**2
assert Fraction(1,1000)/(Fraction(27,100)*Fraction(9648,100000)) < Fraction(384,10000)
assert (Fraction(778,1000)+Fraction(384,10000))**2 < Fraction(2,3)
assert gate < q/2
assert theta0 > 2*q
assert C < 837

# Limiting two-part/q-ridge leverage threshold.
delta_star = (39-6*sqrt(30))/98
assert 0.0626 < delta_star < 0.0627

# Wider fleet02/B08 physical-core interface at leverage 1/16.
delta2 = 1/16
g2 = 0.5-delta2-sqrt(2*delta2)
sigma2 = g2-0.001
paid = 987/sigma2
S = 0.0526286782826*sigma2**3
G = 0.0372140952985*sigma2
E2 = 3.5960948148e-7*sigma2**4
reserve = 2.2475592592e-8*sigma2**4
bicore = 0.0101283938578*sigma2

assert sigma2 > 0.082
assert paid < 11900
assert S > 3.003e-5
assert G > 0.003086
assert E2 > 1.702e-11
assert reserve > 1.063e-12
assert bicore > 0.000840

print('QFORM_B08_R26_QGT1_RIDGE_CHECK_PASS')
print(f'g={g:.15f}')
print(f'sigma={sigma:.15f}')
print(f'ridge_gate={gate:.15f} < q/2={q/2:.15f}')
print(f'theta0={theta0:.15f} > 2q={2*q:.15f}')
print(f'density_constant={C:.12f}')
print(f'delta_star={delta_star:.15f}')
print(f'sigma_1_16={sigma2:.15f}')
print(f'partner_paid={paid:.12f}')
print(f'partner_S={S:.15e}')
print(f'partner_G={G:.15e}')
print(f'partner_E2={E2:.15e}')
print(f'partner_reserve={reserve:.15e}')
print(f'partner_BICORE={bicore:.15e}')
