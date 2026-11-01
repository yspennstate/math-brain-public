import math
import numpy as np

beta0 = 289/15984
partner = 58.7121947444*(8/beta0)**(1/3)
pivot = 512/(math.sqrt(3)*beta0)
pair = 32*math.sqrt(5)/beta0
cross = math.sqrt(765)/32*beta0
curv = beta0/math.sqrt(2)

print('beta0 =', beta0)
print('partner_fixed_puncture_at_beta0_over_8 =', partner)
print('pivot_constant_over_s =', pivot)
print('two_heavy_pair_constant_over_s =', pair)
print('unique_cross_energy_over_s =', cross)
print('unique_curvature_incidence_over_s =', curv)

rng = np.random.default_rng(20260923)
max_err = 0.0
for _ in range(1000):
    m = 8
    E, _ = np.linalg.qr(rng.normal(size=(m,3)))
    O, _ = np.linalg.qr(rng.normal(size=(3,3)))
    vals = np.array([1+rng.random()*3, 1+rng.random()*3, -(1+rng.random()*3)])
    C = O @ np.diag(vals) @ O.T
    i = int(rng.integers(m))
    z = E[i,:]
    a = float(z @ C @ z)
    Eminus = np.delete(E, i, axis=0)
    b = Eminus @ C @ z
    lhs = a*a + float(b @ b)
    rhs = float((C @ z) @ (C @ z))
    max_err = max(max_err, abs(lhs-rhs))

print('max_cross_energy_identity_error_1000 =', max_err)
assert partner < 447.392
assert pivot < 16349.218
assert pair < 3957.516
assert cross > 0.0156276
assert curv > 0.0127849
assert max_err < 1e-11
print('QFORM_B11_R42_UNIQUE_HEAVY_CHECK_PASS')
