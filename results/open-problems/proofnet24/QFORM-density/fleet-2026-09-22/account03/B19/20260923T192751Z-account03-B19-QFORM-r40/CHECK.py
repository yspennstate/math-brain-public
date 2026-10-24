import math
import numpy as np

S = 1.0/(480.0*math.sqrt(7626.0))
C0 = 3.0*(2.0**(1.0/3.0))*math.sqrt(6.0)
Cschur = C0*(2.0**0.25)*(1.0/64.0)**(-0.5)*(S/2.0)**(-0.25)
Cstar = 5.0*((675.0/256.0)**0.2)
Coverlap = Cstar*(2.0**0.4)*S**(-0.4)*(1.0/64.0)**(-0.2)
Cpartner = 34.0*math.sqrt(math.log(64.0*math.e))

print('S_floor', S)
print('C0', C0)
print('schur_gate', Cschur)
print('overlap_gate', Coverlap)
print('partner_1over64_gate', Cpartner)
assert Cschur < 1499.0
assert Coverlap < 1300.0
assert Cpartner < 78.0

rng = np.random.default_rng(12345)
max_resid = 0.0
for _ in range(1000):
    M = rng.normal(size=(2,7))
    if np.linalg.matrix_rank(M) < 2:
        continue
    S0 = math.sqrt(max(0.0, np.linalg.det(M @ M.T)))
    alpha = rng.normal(size=2)
    s = alpha @ M
    r = rng.normal(size=2)
    a = float(rng.normal())
    if abs(a) < 0.1:
        a += 0.3
    C = M - np.outer(r,s)/a
    sv = np.linalg.svd(C, compute_uv=False)
    Delta = sv[0]*sv[1]
    rhs = S0*abs(1.0-(alpha @ r)/a)
    resid = abs(Delta-rhs)/max(1.0,abs(Delta),abs(rhs))
    max_resid = max(max_resid,resid)
print('max_identity_residual', max_resid)
assert max_resid < 1e-12
print('QFORM_B19_R40_CHECK_PASS')
