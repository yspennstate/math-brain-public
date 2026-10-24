from decimal import Decimal, getcontext
getcontext().prec = 60

tau = Decimal(2) ** Decimal(-20)
beta = (Decimal(1)/Decimal(12800) - tau - Decimal(2)*tau*tau)/Decimal(2)
E0 = (Decimal(1)-tau)**2/Decimal(4)
rho = Decimal(63)*(Decimal(1)-tau)**2/Decimal(16384)
G = rho*rho*beta/Decimal(4)

# STAR4 R2 plus top-four capture: x1 < 256 x2 and x3,x4 <= x2,
# so (63/64) E < x1+x2+x3+x4 < 259 x2, E>E0.
x2_lb = Decimal(63)*E0/(Decimal(64)*Decimal(259))
assert abs(x2_lb/rho - Decimal(64)/Decimal(259)) < Decimal('1e-50')

# If both selected-volume payment/anchor exits fail then Gamma_J,Gamma_K<=G.
# Gamma_J >= rho^2 d_J^2 => d_J^2 < beta/4.
# Hence ||P2 u||^2 > 3 beta/4 and Gamma_J >= x2 x3 ||P2u||^2,
# giving x3 < 4G/(3 beta x2_lb) = (259/192) rho.
x3_ub = Decimal(4)*G/(Decimal(3)*beta*x2_lb)
assert abs(x3_ub/rho - Decimal(259)/Decimal(192)) < Decimal('1e-50')

eps = (beta/Decimal(2)).sqrt() + x3_ub.sqrt()
bank_norm_lb = Decimal(3)/Decimal(4) - eps
offdiag_op_lb = bank_norm_lb - tau
F_lb = offdiag_op_lb**2
cut_F_lb = F_lb/Decimal(4)

assert eps < Decimal('0.077')
assert bank_norm_lb > Decimal('0.673')
assert F_lb > Decimal('0.453')
assert cut_F_lb > Decimal('0.113')

for name, value in [
    ('tau', tau), ('beta', beta), ('E0', E0), ('rho_star', rho),
    ('G_star', G), ('x2_lower', x2_lb), ('x3_upper', x3_ub),
    ('error_op_upper', eps), ('winning_selfbank_op_lower', bank_norm_lb),
    ('winning_offdiag_F_lower', F_lb), ('bipartite_cross_F_lower', cut_F_lb),
]:
    print(f'{name}={value}')

print('QFORM_B19_R36_THIRD_RESOURCE_ROUTING_CHECK_PASS')
