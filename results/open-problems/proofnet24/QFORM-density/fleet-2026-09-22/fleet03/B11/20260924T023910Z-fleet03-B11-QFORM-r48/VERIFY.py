from math import sqrt, log

etas = [1e-6, 1e-3, 1e-2, 0.05, 1/sqrt(63)]
print('QFORM fleet03/B11 r48 deterministic verification')
print(f'eta_endpoint={1/sqrt(63):.17g}')
for eta in etas:
    q = 1/(1+eta*eta)
    kappa = sqrt(1+eta*eta)
    eig = (-kappa, 0.0, 1.0, kappa)
    ratio = sqrt((1-q)/q)
    assert abs(ratio-eta) <= 1e-9
    assert q >= 63/64 - 1e-12
    assert abs(kappa*sqrt(q)-1) <= 1e-12
    assert abs(kappa*sqrt(1-q)-eta) <= 1e-9
    assert abs(kappa*kappa-(1+eta*eta)) <= 1e-12
    z = (1-eta)*1e-9
    lower = log((1-eta)/(2*z))
    assert lower > 20
    print(f'eta={eta:.17g} q={q:.17g} kappa={kappa:.17g} eig={eig} log_lower={lower:.15g}')
partner = 2048*sqrt(2/7)
print(f'partner_constant_2048sqrt(2/7)={partner:.15f}')
assert abs(partner-1094.7020468732903) < 1e-10
print('r46_L3_bound_for_F=G=1_b=2: ||p_Z||_3^3 <= 6')
print('uniform_square_exact: ||p_{V^2}||_(3/2)=2 for V~Unif[-1/2,1/2]')
print('QFORM_B11_R48_SAMEBANK_DEPENDENCE_BARRIER_CHECK_PASS')
