import math
import numpy as np

TAU = 2.0**-20
RHO = 63.0*(1.0-TAU)**2/16384.0
F_STRONG = 0.45371767356977310051366104529082816402565236001582
F_WEAK_SPECIFIC_CUT = 0.00006102770589677675
THETA = 1.0/64.0

leg = 3.0*RHO/8.0
cross_strong = F_STRONG/8.0
z_strong = leg**2 * THETA * cross_strong
bound_strong = 6.0*math.sqrt(math.e)*z_strong**(-1.0/6.0)
anchor_strong = z_strong/2.0

# A specific cut with energy E implies total ordered off-diagonal energy F>=2E.
cross_weak = (2.0*F_WEAK_SPECIFIC_CUT)/8.0
z_weak = leg**2 * THETA * cross_weak
bound_weak = 6.0*math.sqrt(math.e)*z_weak**(-1.0/6.0)

assert leg > 0.00144195
assert cross_strong > 0.0567147
assert z_strong > 1.8425e-9
assert bound_strong < 282.529
assert anchor_strong > 9.2127e-10
assert cross_weak > 1.52569e-5
assert bound_weak < 1111.989

# Numerical regression of the exact restricted-rank-two determinant identity and
# monotonicity under adding SVD-tail columns.
rng = np.random.default_rng(20260923)
max_identity_error = 0.0
for _ in range(200):
    m, k = 12, 10
    U, _ = np.linalg.qr(rng.normal(size=(m,2)))
    V, _ = np.linalg.qr(rng.normal(size=(k,2)))
    sig = np.array([2.3,0.7])
    N2 = U @ np.diag(sig) @ V.T

    Qu, _ = np.linalg.qr(np.column_stack([U, rng.normal(size=(m,3))]))
    Qv, _ = np.linalg.qr(np.column_stack([V, rng.normal(size=(k,3))]))
    Ut, Vt = Qu[:,2:5], Qv[:,2:5]
    tail_sig = np.array([0.51,0.23,0.09])
    N = N2 + Ut @ np.diag(tail_sig) @ Vt.T

    mask = rng.random(m) < 0.5
    if mask.sum() < 2 or (~mask).sum() < 2:
        continue
    for side in (mask, ~mask):
        G = U[side].T @ U[side]
        exact = np.prod(sig)*math.sqrt(max(0.0,np.linalg.det(G)))
        got = np.prod(np.linalg.svd(N2[side],compute_uv=False)[:2])
        max_identity_error = max(max_identity_error, abs(got-exact))
        actual = np.prod(np.linalg.svd(N[side],compute_uv=False)[:2])
        assert actual + 1e-10 >= exact

assert max_identity_error < 1e-10

# Exterior-volume inequality: for rank-two A and arbitrary C,
# e3([A,C]^T[A,C]) >= (s1(A)s2(A))^2 ||(I-P_A)C||_F^2.
from itertools import combinations
max_lower_ratio = 0.0
for _ in range(100):
    m, k, ell = 8, 6, 5
    U, _ = np.linalg.qr(rng.normal(size=(m,2)))
    V, _ = np.linalg.qr(rng.normal(size=(k,2)))
    sig = np.array([1.9,0.8])
    A = U @ np.diag(sig) @ V.T
    C = rng.normal(size=(m,ell))
    M = np.concatenate([A,C],axis=1)
    sq = np.linalg.svd(M,compute_uv=False)**2
    e3 = sum(sq[i]*sq[j]*sq[q] for i,j,q in combinations(range(len(sq)),3))
    P = U @ U.T
    lower = (np.prod(sig)**2)*np.linalg.norm((np.eye(m)-P)@C,'fro')**2
    assert e3 + 1e-9 >= lower
    if e3 > 0:
        max_lower_ratio = max(max_lower_ratio, lower/e3)

print(f"tau={TAU:.18g}")
print(f"rho_star={RHO:.18g}")
print(f"balanced_leg_product_lower={leg:.18g}")
print(f"strong_self_cross_energy_lower={cross_strong:.18g}")
print(f"strong_D3_volume_lower={z_strong:.18g}")
print(f"strong_D3_density_bound={bound_strong:.12f}")
print(f"strong_heavy_row_anchor_lower={anchor_strong:.18g}")
print(f"weak_self_cross_energy_lower={cross_weak:.18g}")
print(f"weak_D3_volume_lower={z_weak:.18g}")
print(f"weak_D3_density_bound={bound_weak:.12f}")
print(f"max_restricted_identity_error={max_identity_error:.3e}")
print(f"max_exterior_lower_ratio_seen={max_lower_ratio:.6f}")
print("QFORM_B19_R37_BALANCED_TRIANGLE_CHECK_PASS")
