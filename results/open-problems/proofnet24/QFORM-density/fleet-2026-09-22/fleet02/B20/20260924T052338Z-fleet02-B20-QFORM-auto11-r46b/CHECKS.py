import math
import numpy as np

CR2 = 3.929131770449763
pref = 3.0 * (6.0 * CR2) ** (2.0/3.0)
assert abs(pref - 24.66530466603276) < 1e-12

# r50 robust light-light scale
mu = 255.0 / 65536.0
s = mu / 2.0
D0 = 3.0 / 4096.0
kappa0 = 1.0 / 64.0
bound = pref * D0**(-1.0/3.0) * kappa0**(-1.0/6.0) * (s**4)**(-1.0/24.0)
assert bound < 1549.0

# owner-pinned unrestricted D5 receiver at Z5 >= 1/1024
D5bound = 10.0 * math.sqrt(2.0 * math.e)
assert D5bound < 23.317

# Exact Schur-cancellation stress family, epsilon=1/32.
eps = 1.0 / 32.0
u = np.array([1.0, 0.0])
a = np.array([0.0, 1.0])
v = np.array([1.0, 0.0])
c = np.array([0.0, 1.0])
N = eps**(-1) * np.outer(u, v) + np.outer(a, c)
Bcross = np.block([[N, u[:, None]], [v[None, :], np.array([[eps]])]])
S = N - eps**(-1) * np.outer(u, v)
svB = np.linalg.svd(Bcross, compute_uv=False)
svS = np.linalg.svd(S, compute_uv=False)
A = np.block([[np.zeros((3,3)), Bcross], [Bcross.T, np.zeros((3,3))]])
eig = np.linalg.eigvalsh(A)
assert np.allclose(svB, [eps**(-1)+eps, 1.0, 0.0], atol=1e-12)
assert svS[1] < 1e-12
assert np.allclose(eig, [-(eps**(-1)+eps), -1.0, 0.0, 0.0, 1.0, eps**(-1)+eps], atol=1e-12)

print('QFORM_B20_R46B_PAIR_R2_CHECK_PASS')
print('pair_R2_prefactor=', repr(pref))
print('r50_mu=', repr(mu))
print('post_schur_threshold=', repr(s))
print('r50_heavy_pair_bound=', repr(bound))
print('D5_threshold_bound=', repr(D5bound))
print('stress_cross_singular_values=', svB.tolist())
print('stress_schur_singular_values=', svS.tolist())
print('stress_full_eigenvalues=', eig.tolist())
