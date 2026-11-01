import math

rho = 1/(156*math.sqrt(2))
alpha0 = 4/(math.sqrt(7)+math.sqrt(3))**2
c0 = alpha0*rho/2
gamma0 = math.sqrt(3)*rho/2
Bstar = 4/c0

assert 0 < alpha0 < 1
assert abs(2*math.sqrt(Bstar/c0)-Bstar) < 1e-9
assert gamma0 > 1/312
assert c0 > 0

# exact iteration identity T^k(B)=Bstar^(1-2^-k) B^(2^-k)
def T(B):
    return 2*math.sqrt(B/c0)
for B in [1.0, 66.546, Bstar, 1e6]:
    x=B
    for k in range(1,8):
        x=T(x)
        y=Bstar**(1-2**(-k))*B**(2**(-k))
        assert abs(x-y) <= 1e-10*max(1,abs(y))
        assert x <= max(Bstar,B)*(1+1e-12)

print('QFORM_SIGNED_SCHUR_RECURRENCE_CHECK_PASS')
print('rho=',repr(rho))
print('alpha0=',repr(alpha0))
print('c0=',repr(c0))
print('gamma0=',repr(gamma0))
print('Bstar=',repr(Bstar))
