import math
import numpy as np

tau = 1/64
null_dev = 2*tau
bmin = math.sin(math.pi/6)**2 - 2*null_dev
Dlower = 0.25*(bmin*bmin - (2*tau)**2)
assert Dlower > 1/120

Cpair = math.sqrt(120)*(9.2 + math.log(10000/math.sqrt(120)))
Cpivot = 128*((0.5*tau))**(-0.25)
assert Cpair < 176
assert Cpivot < 431

m = 12
theta = 2*np.pi*np.arange(m)/m
R = np.column_stack([
    np.sqrt(2/m)*np.cos(theta),
    np.sqrt(2/m)*np.sin(theta),
    np.full(m, 1/np.sqrt(m)),
])
Lam = np.diag([1., 1., -1.])
A = R @ Lam @ R.T
assert np.max(np.abs(R.T @ R - np.eye(3))) < 1e-12
nz = np.linalg.eigvalsh(A)
nz = nz[np.abs(nz) > 1e-10]
assert np.max(np.abs(nz - np.array([-1.,1.,1.]))) < 1e-12
lev = np.sum(R*R, axis=1)
diag = np.diag(A)
assert np.max(np.abs(lev - 3/m)) < 1e-12
assert np.max(np.abs(diag - 1/m)) < 1e-12

v = R[0]/math.sqrt(lev[0])
n = np.array([math.cos(theta[0]), math.sin(theta[0]), 1.])/math.sqrt(2)
dist = np.linalg.norm(v-n)
assert dist > 0.16

c = .51
J = np.diag([1.,1.,-1.])
n0 = np.array([1.,0.,1.])/math.sqrt(2)
n1 = np.array([math.cos(math.pi/3), math.sin(math.pi/3), 1.])/math.sqrt(2)
b = c*(n0 @ J @ n1)
Dactual = b*b
grammax = np.linalg.eigvalsh(c*np.array([[1., n0@n1],[n0@n1,1.]])).max()
assert Dactual > Dlower
assert grammax < 1

print(f"tau={tau:.12f}")
print(f"null_distance_bound={null_dev:.12f}")
print(f"separated_null_bilinear_lower={bmin:.12f}")
print(f"pair_determinant_lower={Dlower:.12f}")
print(f"one_over_120={1/120:.12f}")
print(f"pair_bound_at_1_over_120={Cpair:.12f}")
print(f"heavy_fixed_pivot_bound={Cpivot:.12f}")
print(f"diffuse_m={m}")
print(f"parseval_error={np.max(np.abs(R.T@R-np.eye(3))):.3e}")
print(f"nonzero_eigenvalues={nz.tolist()}")
print(f"diffuse_leverage_minmax=({lev.min():.12f},{lev.max():.12f})")
print(f"diffuse_diagonal_minmax=({diag.min():.12f},{diag.max():.12f})")
print(f"diffuse_unit_ray_null_distance={dist:.12f}")
print(f"separated_exact_null_pair_D={Dactual:.12f}")
print(f"separated_exact_null_pair_frame_gram_maxeig={grammax:.12f}")
print("QFORM_B11_HEAVY_NULL_CLUSTER_CHECK_PASS")
