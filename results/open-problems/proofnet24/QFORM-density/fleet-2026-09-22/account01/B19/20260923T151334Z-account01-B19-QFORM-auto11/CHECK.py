from decimal import Decimal, getcontext
import math
getcontext().prec=50

tau=Decimal(2) ** Decimal(-20)
beta=(Decimal(1)/Decimal(12800)-tau-2*tau*tau)/2
rho=Decimal(63)*(1-tau)**2/Decimal(16384)
eps=(beta/2).sqrt() + (Decimal(259)/Decimal(192)*rho).sqrt()
kappa=Decimal(6)/Decimal(64)-eps
sqrt_e=Decimal(str(math.sqrt(math.e)))
bound=Decimal(6)*sqrt_e/kappa
anchor=Decimal('0.5')*kappa**6
self_cross=(Decimal(1)/Decimal(64)-tau)**2/4
partner_bound=Decimal(96)*sqrt_e/Decimal(7)

assert kappa>0
assert bound < Decimal('570.603')
assert anchor > Decimal('1.3575e-11')
assert self_cross > Decimal('0.0000610277')
assert partner_bound < Decimal('22.612')

print('tau', tau)
print('beta', beta)
print('rho_star', rho)
print('epsilon_star', eps)
print('kappa', kappa)
print('D3_paid_bound', bound)
print('third_volume_anchor', anchor)
print('self_bank_cross_F2', self_cross)
print('partner_r35_paving_bound', partner_bound)
print('QFORM_B19_AUTO11_PAVING_CHECK_PASS')
