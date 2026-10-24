from decimal import Decimal, getcontext
from math import exp, sqrt
getcontext().prec = 50
beta = Decimal('0.01651671529470044')
c0 = Decimal('0.11907425120090158')
tau0 = beta*beta*c0
qbad = Decimal('0.697782346546711')
print('tau0 =', tau0)
print('tau0/8 =', tau0/Decimal(8))
print('tau0/4 =', tau0/Decimal(4))
print('tau0^2/16 =', tau0*tau0/Decimal(16))
print('matrix_good_lower =', Decimal(1)-qbad)
print('partner_scalar_event_lower_at_1/72 = 0.7')
print('intersection_union_margin =', Decimal('0.7')-qbad)
print('joint_scalar_density_cap =', exp(1.5)*sqrt(72.0))
print('skew_omega_lower =', float(tau0)*sqrt(7.0)/4.0)
