import math
import numpy as np

rng = np.random.default_rng(240924)

C_mixed = 3 * 2**(5/3)
C_mixed_gate = 16 * C_mixed
C_shear_gate = 4 * 8 * 8
C_half_gate = 128 * math.sqrt(2)
hub_diag_gate = 4031/8192
align_q2 = 512/4031
align_p2 = 3519/4031

eps = 1/128
m = 16384
stress_eigs = [eps + 1/eps, 1.0, -1.0]
stress_leverage = 2/m
stress_pair = 1/math.sqrt(m)
stress_density = 3 * 2**(4/3) * eps**(1/3)

max_mix = 0.0
max_shear = 0.0
max_lev = 0.0
for _ in range(5000):
    M = rng.normal(size=(2, 7))
    G = M @ M.T
    if abs(np.linalg.det(G)) < 1e-10:
        continue
    r = rng.normal(size=2)
    r /= np.linalg.norm(r)
    w = M.T @ r
    p = 0 if abs(r[1]) >= abs(r[0]) else 1
    rperp = r[1-p]
    v = w / np.linalg.norm(w)
    C0 = np.vstack([v, M[p]])
    lhs = np.linalg.det(C0 @ C0.T)
    rhs = rperp**2 * np.linalg.det(G) / np.dot(w, w)
    max_mix = max(max_mix, abs(lhs-rhs)/(1+abs(rhs)))

    B = rng.normal(size=(2,2))
    B = (B+B.T)/2
    lam = rng.normal()
    br = r @ B @ r
    kappa = 1-lam*br
    if kappa <= 1e-8:
        continue
    if abs(br) > 1e-10:
        alpha = (1-math.sqrt(kappa))/br
    else:
        alpha = lam/2
    T = np.eye(2) - alpha*np.outer(B@r, r)
    C = T @ M
    lhs2 = np.linalg.det(C @ C.T)
    rhs2 = kappa*np.linalg.det(G)
    max_shear = max(max_shear, abs(lhs2-rhs2)/(1+abs(rhs2)))
    invG = np.linalg.inv(G)
    invC = np.linalg.inv(C@C.T)
    levM = np.array([M[:,i]@invG@M[:,i] for i in range(M.shape[1])])
    levC = np.array([C[:,i]@invC@C[:,i] for i in range(C.shape[1])])
    max_lev = max(max_lev, np.max(np.abs(levM-levC)))

print('mixed_base_constant', C_mixed)
print('mixed_gate_constant', C_mixed_gate)
print('real_shear_gate_constant', C_shear_gate)
print('half_potential_gate_constant', C_half_gate)
print('hub_diagonal_gate', hub_diag_gate)
print('alignment_rq2_upper', align_q2)
print('alignment_rp2_lower', align_p2)
print('stress_nonzero_eigenvalues_over_L', *stress_eigs)
print('stress_arm_leverage', stress_leverage)
print('stress_hub2_light_pair_upper_over_L', stress_pair)
print('stress_density_coefficient', stress_density)
print('max_mixed_determinant_relative_error', max_mix)
print('max_shear_determinant_relative_error', max_shear)
print('max_leverage_absolute_error', max_lev)

assert C_mixed_gate < 152.391
assert C_shear_gate == 256
assert C_half_gate < 181.020
assert stress_pair < 1/64
assert stress_leverage < 1/2
assert abs(stress_density-1.5) < 1e-12
assert max_mix < 1e-12
assert max_shear < 1e-11
assert max_lev < 1e-11
print('QFORM_B08_R31_CHECK_PASS')
