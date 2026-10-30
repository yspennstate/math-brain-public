import math
import numpy as np

# Deterministic sanity checks for QFORM-STRICTN3-CLIQUE-FACTOR-IMPOSSIBLE-v1.
tau = 1/128
q = math.sqrt(tau + tau*tau)
delta_clique = tau + q
delta_triangle = tau + 2*q
partner_const = 6 / (2**(1/3))
triangle_tau_crit = (2*math.sqrt(3)-3)/3

assert delta_clique < 1
assert delta_triangle < 1
assert tau < 1/3
assert tau < triangle_tau_crit

# Cancellation stress: huge hidden diagonal cancellation at one clique coordinate.
n = 8
sigma = 100.0
u = np.array([1.0] + [0.0005]*(n-1))
A = sigma*np.outer(u,u)
np.fill_diagonal(A, 0.0)

max_pair_det = 0.0
for i in range(n):
    for j in range(i+1,n):
        det2 = A[i,i]*A[j,j] - A[i,j]**2
        max_pair_det = max(max_pair_det, abs(det2))
assert max_pair_det < tau

svals = np.linalg.svd(A, compute_uv=False)
assert svals[2] < delta_clique

# Explicit rank-two approximant from the proof.
r = abs(sigma)*u*u
heavy = np.where(r >= q)[0]
assert len(heavy) <= 1
Ddiag = np.diag(A - sigma*np.outer(u,u)).copy()
R = sigma*np.outer(u,u)
if len(heavy) == 1:
    h = int(heavy[0])
    R[h,h] += Ddiag[h]
err = np.linalg.norm(A-R,2)
assert err < delta_clique
assert np.linalg.matrix_rank(R, tol=1e-10) <= 2

# Partner control core.
K = np.array([[0.,1.,1.],[1.,0.,1.],[1.,1.,0.]])
assert abs(np.linalg.det(K)-2.0) < 1e-12
keigs = np.linalg.eigvalsh(K)
assert np.allclose(keigs, [-1.,-1.,2.])

print('QFORM_B18_R22_CHECK_PASS')
print('tau=', tau)
print('q=', q)
print('tau_plus_q=', delta_clique)
print('tau_plus_2q=', delta_triangle)
print('triangle_tau_critical=', triangle_tau_crit)
print('partner_zero_pivot_constant=', partner_const)
print('stress_max_pair_det=', max_pair_det)
print('stress_singular_values=', svals.tolist())
print('stress_rank2_approx_error=', err)
