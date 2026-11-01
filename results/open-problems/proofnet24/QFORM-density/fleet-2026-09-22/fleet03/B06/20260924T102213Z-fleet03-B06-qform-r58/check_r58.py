import math
import numpy as np

rng = np.random.default_rng(58)
mx = 0.0
for _ in range(3000):
    n = int(rng.integers(4, 11))
    r = int(rng.integers(1, 4))
    V, _ = np.linalg.qr(rng.normal(size=(n, r)))
    M = rng.normal(size=(r, r)); M = (M + M.T)/2
    R = V @ M @ V.T
    for q in range(n):
        v = V[q]
        rq = R[q,q]
        c = np.delete(R[q], q)
        rhs = v @ (M @ M) @ v - rq*rq
        mx = max(mx, abs(c@c-rhs))

# Exact threshold arithmetic.
delta = 1/6
tau = eta = 1/96
ratio = eta/(delta-tau)
alpha_min = 1/(1+ratio*ratio)
assert abs(alpha_min - 225/226) < 1e-15
kappa0 = (tau + math.sqrt(tau*tau+4*eta*eta))/2
assert abs(kappa0 - (1+math.sqrt(5))/192) < 1e-15
sigma_star = 1/3 - 3*kappa0
sigma0 = sigma_star - 1/6
assert sigma0 > 0.116
assert 3*math.e/sigma0 < 70.238

# Controlled near-coloop cancellation examples.
for eps in (1e-4, 1e-3, 3e-3):
    n=7
    S=rng.normal(size=(n,n)); S=S-S.T
    Q,_=np.linalg.qr(np.eye(n)+eps*S)
    V=Q[:,:3]
    M=np.diag([1.0,1.3,-1.7])
    R=V@M@V.T
    q=0
    rq=R[q,q]
    d=-rq+tau/2
    a=d+rq
    c=np.delete(R[q],q)
    if abs(d)>delta and abs(a)<tau and np.linalg.norm(c)<eta:
        assert np.sum(V[q]**2)>225/226

print('QFORM_B06_R58_CHECK_PASS')
print('max_cross_identity_error', mx)
print('alpha_min', alpha_min)
print('kappa0', kappa0)
print('sigma_star', sigma_star)
print('sigma0', sigma0)
print('diffuse_bound', 3*math.e/sigma0)
