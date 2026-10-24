import math

tau=2**-20
beta=(1/12800-tau-2*tau*tau)/2
rho=63*(1-tau)**2/16384
delta=math.sqrt(beta)/4
eta=(rho*delta)**2
core=15*beta/16
assert abs(beta-3.8585661932302174e-05)<1e-18
assert abs(rho-0.003845207509588222)<1e-18
assert abs(delta-0.0015529339557009132)<1e-18
assert abs(eta-3.56570603332105e-11)<1e-24
assert abs(core-3.6174058061533286e-05)<1e-18
q=5/4
Cq=3*math.e/((3-2*q)*math.sqrt(q))
Bq=Cq*eta**(-1/6)
B1=3*math.e*eta**(-1/6)
assert Bq < 805
assert B1 < 450
assert eta/4 > 8.9e-12
print('tau',tau)
print('beta',beta)
print('rho_star',rho)
print('delta_0',delta)
print('eta_3',eta)
print('15beta/16',core)
print('q=5/4 constant',Cq)
print('q=5/4 density bound',Bq)
print('q=1 density bound',B1)
print('eta_3/4',eta/4)
print('QFORM_B19_R34_STAR4_E3_CHECK_PASS')
