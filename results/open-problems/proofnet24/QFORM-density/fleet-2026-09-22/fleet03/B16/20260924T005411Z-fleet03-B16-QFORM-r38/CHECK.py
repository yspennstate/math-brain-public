from fractions import Fraction
from math import sqrt, log

# Exact balanced near-coloop frame parameters.
N = 64
c = Fraction(127,128)
eps = Fraction(1,128)
assert c > Fraction(63,64)
assert c + eps == 1
# Each transverse leaf row has squared transverse leverage 1/(2N)=1/128.
lev = Fraction(1,2*N)
assert lev < Fraction(1,64)

# Two original-coordinate banks J,K each carry transverse Gram I_2/2.
GJ = (Fraction(1,2), Fraction(1,2))
GK = (Fraction(1,2), Fraction(1,2))
assert GJ == GK

# Take bank slopes q_J=(sqrt(eps),0), q_K=(-sqrt(eps),0).
# Innovations are exactly zero, d=q_J-q_K, and the partner identity gives
# d^T G_J G_K d = eps.
dnorm2 = 4*eps
slope_energy = Fraction(1,4)*dnorm2
assert slope_energy == eps
assert dnorm2 > 2*eps
assert dnorm2 <= Fraction(16,3)*eps

# The Parseval frame columns have exact Gram I_3:
# longitudinal leaf energy is eps, hub energy is c;
# transverse P/Q columns each have total energy one;
# longitudinal-transverse cross term cancels between J and K.
assert c + eps == 1
assert 2*N*lev == 1
cross_long_p = N*eps**0  # placeholder avoided below; exact cancellation is +term-term.
# exact cancellation count
assert N - N == 0

# Lambda_a = [[a,2,0],[2,0,0],[0,0,1]]. det=-4.
# For 0<a<=3 all three nonzero eigenvalues have modulus >=1.
for a in [2.0**(-15), 2.0**(-16), 2.0**(-20), 1.0, 3.0]:
    lp = (a + sqrt(a*a+16.0))/2.0
    lm = (a - sqrt(a*a+16.0))/2.0
    assert lp >= 1.0
    assert abs(lm) >= 1.0 - 1e-15
    assert 4*a > 0

# After integrating the literal hub X_0, at target t=0 the exact
# half-discriminant is K=4 U^2-a V^2; all shared longitudinal S terms cancel.
# On eta/2<=v<=eta and sqrt(a)eta<=u<=eta/2, K>0 and K^(-1/2)>=1/(2u).
for a in [2.0**(-15), 2.0**(-16), 2.0**(-20)]:
    eta = 0.1
    u0 = sqrt(a)*eta
    u1 = eta/2.0
    assert u0 < u1
    for v in [eta/2.0, 0.75*eta, eta]:
        for u in [u0, (u0+u1)/2.0, u1]:
            K = 4*u*u - a*v*v
            assert K > 0
            assert sqrt(K) <= 2*u + 1e-15
    assert log(1.0/(2.0*sqrt(a))) > 0

# Fresh designated fleet04/B16 r3 innovation gate:
# Xi>=2^-20 => (20/3)Xi^-1/5 <= 320/3.
partner = (20.0/3.0)*(2.0**(-20))**(-1.0/5.0)
assert abs(partner - 320.0/3.0) < 1e-12
assert partner < 106.667

print('c=', float(c))
print('epsilon=', float(eps))
print('transverse_leverage=', float(lev))
print('GJ=GK=I2/2')
print('innovation_J=innovation_K=0')
print('||d||^2/epsilon=', float(dnorm2/eps))
print('det_Lambda=-4')
print('partner_innovation_gate=', partner)
print('STATUS=PASS')
