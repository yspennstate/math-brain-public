import math
import numpy as np

rng = np.random.default_rng(20260923)

C_grp = (2**(4/3)+1)*math.sqrt(3)*2**0.25
C_b06 = (2**(4/3)+1)*math.sqrt(3)*math.e**0.25
C_r32 = 2*math.sqrt(10)*7**0.9

print('C_grp', C_grp)
print('C_b06_one_two', C_b06)
print('C_r32', C_r32)
print('theta_half_exact_rank2', C_grp*2**0.25)
print('theta_half_any_rank', C_r32*2**0.25)

max_det_error = 0.0
router_violations = 0
N = 5000
theta = 0.5
for _ in range(N):
    L = 10**rng.uniform(-2, 2)
    R = 10**rng.uniform(math.log10(3), 2)
    u = rng.normal(size=2)*L
    v = rng.normal(size=2)*L
    C0 = L*np.diag([R, 1/R])
    C = C0 - np.outer(u, v)/L
    lhs = np.linalg.det(C)
    rhs = L**2*(1 - u[0]*v[0]/(L**2*R) - R*u[1]*v[1]/L**2)
    max_det_error = max(max_det_error, abs(lhs-rhs)/(1+abs(rhs)))
    if abs(lhs) < theta*L**2:
        weighted = abs(u[0]*v[0]/(L**2*R) + R*u[1]*v[1]/L**2)
        if not weighted > 1-theta-1e-12:
            router_violations += 1

print('det_identity_tests', N)
print('max_det_rel_like_error', max_det_error)
print('theta_half_router_violations', router_violations)
assert C_grp < 7.251
assert C_b06 < 7.829
assert C_r32 < 36.45
assert C_grp*2**0.25 < 8.622
assert C_r32*2**0.25 < 43.34
assert max_det_error < 1e-12
assert router_violations == 0
print('QFORM_B08_R38_CHECK_PASS')
