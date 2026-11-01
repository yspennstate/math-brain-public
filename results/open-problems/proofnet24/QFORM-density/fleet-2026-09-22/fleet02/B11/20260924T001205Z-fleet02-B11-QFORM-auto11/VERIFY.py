import math
import numpy as np

# Concrete target-valid matrix Q*=2HY+2HZ+2YZ+2UV.
A = np.array([
    [0.,1.,1.,0.,0.],
    [1.,0.,1.,0.,0.],
    [1.,1.,0.,0.,0.],
    [0.,0.,0.,0.,1.],
    [0.,0.,0.,1.,0.],
])
eigs = np.linalg.eigvalsh(A)
assert np.allclose(eigs, [-1., -1., -1., 1., 2.])
assert np.sum(np.abs(eigs) >= 1 - 1e-12) == 5

# The elementary cap integral in Theorem 1.
# K>0: integral min(1,2Ks)^2/s^2 in its split form = 4K.
for K in [0.1, 1.0, 7.3]:
    s0 = 1.0/(2.0*K)
    piece1 = 4*K*K*s0
    piece2 = 1.0/s0
    assert abs(piece1 + piece2 - 4*K) < 1e-12

# Constants quoted in the report.
assert abs(8*math.sqrt(5) - 17.88854381999832) < 1e-12
assert abs(math.pi*math.sqrt(2) - 4.442882938158366) < 1e-12
assert abs(2**(7/4) - 3.363585661014858) < 1e-12

# If |phi(t)| <= min(1,K/t^2), inversion gives 2 sqrt(K)/pi.
# For K=2 sqrt(2) pi^2/|sigma| this equals 2^(7/4)|sigma|^-1/2.
for sigma in [0.2, 1.0, 5.0]:
    Kphi = 2*math.sqrt(2)*math.pi**2/abs(sigma)
    inv = 2*math.sqrt(Kphi)/math.pi
    rhs = 2**(7/4)/math.sqrt(abs(sigma))
    assert abs(inv-rhs) < 1e-12

print('QFORM_B11_R45_HYPERBOLIC_L2_CHECK_PASS')
