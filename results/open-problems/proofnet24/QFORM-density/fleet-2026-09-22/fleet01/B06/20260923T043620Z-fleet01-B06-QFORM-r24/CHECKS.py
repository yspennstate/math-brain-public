import math
import random

# Constants from Theorem 2.1 / one-sided branch.
C_general = 3 * 2**(4/3)
C_partner = C_general * math.e**(1/3)
C_onesided = 3 * 2**(5/3) * math.e**(1/3)
print('C_general=', repr(C_general))
print('C_with_partner=', repr(C_partner))
print('C_onesided=', repr(C_onesided))
assert C_onesided < 13.293

# Algebra check: if v,q are orthonormal and h=beta*v+m*q,
# det Gram(h,v)=m^2, independently of beta.
for _ in range(1000):
    theta = random.uniform(-math.pi, math.pi)
    v = (math.cos(theta), math.sin(theta))
    q = (-math.sin(theta), math.cos(theta))
    beta = random.uniform(-20, 20)
    m = 10 ** random.uniform(-3, 3)
    h = (beta*v[0] + m*q[0], beta*v[1] + m*q[1])
    hh = h[0]*h[0] + h[1]*h[1]
    vv = 1.0
    hv = h[0]*v[0] + h[1]*v[1]
    detG = hh*vv - hv*hv
    assert math.isclose(detG, m*m, rel_tol=5e-9, abs_tol=1e-9)

# Spectral scaling check used in (3.12): if gamma*sigma^2=s1*s2*s3
# and m_R=rho*y with gamma=rho^2/|a|, then
# sigma^2*m_R^2/|a|=(s1*s2*s3)*y^2 >= s3^3*y^2.
for _ in range(1000):
    s3 = 10 ** random.uniform(-2, 2)
    s2 = s3 * (1 + random.random()*20)
    s1 = s2 * (1 + random.random()*20)
    y2 = random.uniform(0.5000001, 1.0)
    lhs = s1*s2*s3*y2
    rhs = s3**3*y2
    assert lhs + 1e-12 >= rhs

print('QFORM_B06_R24_CHECK_PASS')
