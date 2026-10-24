import math
import numpy as np

SEED = 20260923
THETA = 7/64
rng = np.random.default_rng(SEED)

def e2(M):
    lam = np.linalg.svd(M, compute_uv=False)**2
    return ((lam.sum())**2 - (lam*lam).sum())/2

q = math.sqrt(1/THETA - 1)
kappa = (1+q)**2
accepted = 0
shear_violations = 0
min_s3_ratio = float('inf')
max_tail_identity_error = 0.0

for _ in range(1000):
    P = np.array([[1.0, 0.2], [-0.1, 0.9]]) + 0.1*rng.normal(size=(2,2))
    if abs(np.linalg.det(P)) < 0.2:
        continue
    R = 0.12*rng.normal(size=(2,3))
    C = 0.12*rng.normal(size=(3,2))
    U, _ = np.linalg.qr(rng.normal(size=(3,2)))
    V, _ = np.linalg.qr(rng.normal(size=(3,2)))
    s1 = 0.4 + 0.6*rng.random()
    s2 = 10**rng.uniform(-4, -0.2)
    S = U @ np.diag([s1,s2]) @ V.T
    Pinv = np.linalg.inv(P)
    M = C @ Pinv @ R + S
    N = np.block([[P,R],[C,M]])
    D = abs(np.linalg.det(P))
    E2 = e2(N)
    if D*D/E2 < THETA:
        continue
    accepted += 1
    L = C @ Pinv
    K = Pinv @ R
    if np.linalg.norm(L,2) > q+1e-10 or np.linalg.norm(K,2) > q+1e-10:
        shear_violations += 1
    u, ss, vh = np.linalg.svd(S, full_matrices=False)
    S1 = ss[0]*np.outer(u[:,0],vh[0])
    N0 = np.block([[P,R],[C,C@Pinv@R+S1]])
    mstar = min(np.linalg.svd(P,compute_uv=False)[-1], ss[0])
    atheta = mstar/kappa
    sN0 = np.linalg.svd(N0,compute_uv=False)
    min_s3_ratio = min(min_s3_ratio, sN0[2]/atheta)
    tail_error = abs(np.linalg.norm(N-N0,2)-ss[1])
    max_tail_identity_error = max(max_tail_identity_error, tail_error)

print('accepted', accepted)
print('shear_violations', shear_violations)
print('min_s3_N0_over_atheta', repr(min_s3_ratio))
print('max_tail_identity_error', repr(max_tail_identity_error))
print('q_theta', repr(q))
print('kappa_theta', repr(kappa))
print('volume_constant', repr((24*math.sqrt(3)*math.e/5)*kappa))
print('rank2_constant', repr(4*math.sqrt(math.e)*kappa**0.25))
