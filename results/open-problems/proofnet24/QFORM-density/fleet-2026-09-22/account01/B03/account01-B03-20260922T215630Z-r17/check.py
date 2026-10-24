import math

Cstar = 16*math.sqrt(2)/(3**(3/4))
print('Cstar=', repr(Cstar))
print('sqrt2pi*Cstar=', repr(math.sqrt(2*math.pi)*Cstar))

for eta in (1e-2,1e-4,1e-8):
    m=(1+eta)/(2*eta)
    D=1/eta
    rho=math.pi*m/(4*math.sqrt(D))
    A0=2*math.sqrt(2)/math.sqrt(m)
    if rho >= 1:
        ub=A0*(2+math.log(rho))
    else:
        ub=2*math.sqrt(2*math.pi)*D**(-0.25)
    exact=(2*math.sqrt(2*eta)/math.sqrt(1+eta))*math.log(
        ((math.sqrt(1+eta)+1+math.sqrt(eta))**2)/(2*math.sqrt(eta))
    )
    assert ub >= exact
    print(f'eta={eta:g} rho={rho:.12g} ub={ub:.12g} exact={exact:.12g} ratio={ub/exact:.12g}')

# At rho=1 the two layer-cake branches agree exactly.
A=3.0
B=A*A
lhs=A*(2+math.log(B/(A*A)))
rhs=2*math.sqrt(B)
assert abs(lhs-rhs)<1e-12
print('boundary=', lhs, rhs)
print('QFORM_B03_DEFINITE_PAIR_LOG_BRIDGE_PASS')
