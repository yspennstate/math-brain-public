from itertools import combinations
from math import sqrt, pi, e, erfc, log

eta = sqrt(2*pi*e)*erfc(1/sqrt(2))
assert abs(eta-1.311359084837597) < 1e-14

# Stress matrix uses pair H={1,2}; exact Schur complement is recorded in REPORT.md.
D = 16.0
kappa = (sqrt(73)-3)/2
R = 16*sqrt(6**2+10**2+14**2)
rho = 2**(11/4)*D/sqrt(kappa*R)
assert rho > sqrt(2)
exact = D**(-0.5)*(4+eta+2*log(rho/sqrt(2)))
assert abs(exact-1.8202432195622835) < 1e-13

# q=1 certificate from the already-proved arbitrary-self compiler.
H = D/(sqrt(2)*R)
Cstar = 2+log(2)+eta
q1 = 8*sqrt(H/kappa)+Cstar/sqrt(D)
assert abs(q1-1.9476932346662073) < 1e-13
assert q1 > exact

# fleet02/B04 r22 on its unperturbed A_*: a_i=4, v_i=1,...,5.
pairs=list(combinations(range(5),2))
c={p:16*(p[1]-p[0])**2 for p in pairs}
J=sum(c[P]*c[Q] for P in pairs for Q in pairs if set(P).isdisjoint(Q))
assert J == 158720
partner = 3*2**(4/3)*J**(-1/6)
assert abs(partner-1.0273599697935472) < 1e-13

print('QFORM_B04_R35_ARBITRARYSELF_EXACT_OPT_CHECK_PASS')
print('eta=',repr(eta))
print('R=',repr(R),'rho=',repr(rho),'exact=',repr(exact),'q1=',repr(q1))
print('partner_J=',J,'partner_bound=',repr(partner))
