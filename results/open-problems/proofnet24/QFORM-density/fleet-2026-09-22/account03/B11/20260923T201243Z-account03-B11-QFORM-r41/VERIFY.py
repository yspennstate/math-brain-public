from fractions import Fraction
import math
import numpy as np

beta0 = Fraction(34,111) * Fraction(17,288)
kappa_star = Fraction(34,111) * Fraction(17,288)**2
assert beta0 == Fraction(289,15984)
assert abs(float(beta0) - 0.01808058058058058) < 1e-15
assert abs(float(kappa_star) - 0.001067256492603715) < 1e-15
assert abs(float(beta0)/math.sqrt(2) - 0.012784901136318331) < 1e-15

# Deterministic Parseval-frame sanity checks for the extension-diffusion inequality.
# w_j = sqrt(2/m)(cos(2*pi*j/m), sin(2*pi*j/m)) gives sum w_j w_j^T = I_2.
for m in (74, 100, 200):
    th = 2*np.pi*np.arange(m)/m
    W = np.sqrt(2/m)*np.stack([np.cos(th), np.sin(th)], axis=1)
    assert np.linalg.norm(W.T@W - np.eye(2), ord=2) < 1e-12
    delta = np.max(np.sum(W*W, axis=1))
    for j in range(m):
        q = (W[j,0]*W[:,1] - W[j,1]*W[:,0])**2
        T = q.sum()
        star_ratio = (T*T - (q*q).sum())/(T*T)
        assert star_ratio + 1e-12 >= 1-delta

print('beta0 =', float(beta0))
print('kappa_star =', float(kappa_star))
print('beta0/sqrt(2) =', float(beta0)/math.sqrt(2))
print('hard-branch extension lower ratio =', 35/36)
print('QFORM_B11_R41_CURVATURE_DIFFUSION_CHECK_PASS')
