from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 60

# Exact prime-witness coefficient of q_*(u)=4u(1-u).
r = Fraction(967, 2048)
q = lambda x: 4*x*(1-x)
Lq = Fraction(57,256)*q(Fraction(3,8)) + Fraction(465,256)*q(Fraction(1,2)) - q(r)
assert Lq == Fraction(1078193, 1048576)

# Only coarse source-certified constants are used for the displayed frontier.
d0 = Decimal('0.0176114')
kappa_upper = Decimal('0.069645')
LqD = Decimal(Lq.numerator) / Decimal(Lq.denominator)

frontier = {}
for s in ['0', '0.005', '0.01', '0.015']:
    E = Decimal(s)
    frontier[s] = (d0 - LqD*E) / kappa_upper

threshold = d0 / LqD
cap = Decimal('6.521851214') + threshold
shape_E_001 = d0 - (Decimal(1121)/Decimal(1024))*Decimal('0.01')

assert frontier['0'] > Decimal('0.2528738602')
assert frontier['0.005'] > Decimal('0.1790534157')
assert frontier['0.01'] > Decimal('0.1052329711')
assert frontier['0.015'] > Decimal('0.0314125266')
assert threshold > Decimal('0.01712763055')
assert cap > Decimal('6.5389788445')
assert shape_E_001 == Decimal('0.006664134375')

print('Lq_exact =', Lq)
print('Lq_decimal =', LqD)
for E, value in frontier.items():
    print(f'K_lower(E={E}) = {value}')
print('zero_AND_loss_center_increment =', threshold)
print('zero_AND_loss_total_center =', cap)
print('shape_residual_E_0.01 =', shape_E_001)
print('PASS')
