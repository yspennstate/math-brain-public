# Deterministic sanity checks for fleet01/B01 20260924T110759Z.
# These checks support constants/algebra only; they are not an independent proof review.
import math
from mpmath import beta, gamma, cos, pi

q = 0.25
Cq = pi**q/(2*gamma(q)*cos(pi*q/2)*q*(0.5-q))
Jq = max(beta(0.5,q), beta(0.5,0.5-q)+beta(0.5-q,q))
lead = (Jq*Cq)**(2/3)
lead_row = lead*2**(1/12)
partner = 8 + 32*math.sqrt(5)*4**(-1/8)

assert abs(float(Cq)-3.179662567631707) < 1e-12
assert abs(float(Jq)-12.660413817789728) < 1e-12
assert abs(float(lead)-11.745890746379832) < 1e-12
assert abs(float(lead_row)-12.444337756165789) < 1e-12
assert abs(partner-68.1696494893823) < 1e-12
assert float(lead_row)*64 < 796.438

# Star eigenvalue check: [[eps,1],[1,0]] has product -1,
# so at least one singular/eigenvalue modulus is >=1 for every eps.
for eps in [-100,-7,-1,0,1,7,100]:
    disc = math.sqrt(eps*eps+4)
    lp = (eps+disc)/2
    lm = (eps-disc)/2
    assert abs(lp*lm + 1) < 1e-10
    assert max(abs(lp),abs(lm)) >= 1-1e-12

print('C_1/4 =', float(Cq))
print('J_1/4 =', float(Jq))
print('two-square lead =', float(lead))
print('row-projection lead =', float(lead_row))
print('partner constant =', partner)
print('64-scale bound =', float(lead_row)*64)
print('STATUS=PASS')
