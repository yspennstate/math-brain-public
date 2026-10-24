from math import sqrt, exp

# r49 exact constants
eta0 = 0.0854140220382430396407996086186180828461692268928420935353231
assert eta0 < 11/128

eps = (11/72)**2
delta = 0.5 - eps - sqrt(2*eps)
sigma = (9/4)*(delta - 1/4)
assert eps == 121/5184
assert delta > 1/4
assert sigma > 3/128
assert 242*5184 < 1121**2

C_E3 = 3*(2**(4/3))*exp(1/3)
payment = C_E3*(128/3)
assert payment < 451

mu = 4.6565947316667495e-10
partner_paid = 48.307715 * mu**(-2/3)
partner_packet = (5/12447) * mu**4
assert partner_paid < 8.05e7
assert partner_packet > 1.88e-41

print({
    'epsilon': eps,
    'delta': delta,
    'sigma_star': sigma,
    '3/128': 3/128,
    'E3_payment_bound': payment,
    'partner_paid_bound': partner_paid,
    'partner_packet_lower': partner_packet,
    'rank12_tail_op_bound': 9/4 + 2**-16,
    'rank11_collapse_tail_op_bound': 9/4 + 2**-16 + 112*2**-20,
})
