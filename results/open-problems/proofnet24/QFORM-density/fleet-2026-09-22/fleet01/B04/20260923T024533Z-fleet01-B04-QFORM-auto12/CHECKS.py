import math
import numpy as np

# fleet02/B04 exact-coloop family, evaluated at epsilon=1e-6.
eps = 1e-6
U = np.array([
    [1.0,0.0,0.0],
    [0.0,1/math.sqrt(2),0.0],
    [0.0,0.5,0.5],
    [0.0,0.0,1/math.sqrt(2)],
    [0.0,-0.5,0.5],
])
V = np.array([
    [-2/3, 2/15, 11/15],
    [ 2/3,-1/3,  2/3],
    [ 1/3,14/15,  2/15],
])
M = U @ np.diag([eps,2.0,2.0]) @ V.T
print('UtU_error', np.max(np.abs(U.T@U-np.eye(3))))
print('VtV_error', np.max(np.abs(V.T@V-np.eye(3))))
print('detV', np.linalg.det(V))
print('singular_values', np.linalg.svd(M,compute_uv=False))

Z2 = 16 + 8*eps**2
p1 = eps**2/(2+eps**2)
p2 = (4+eps**2)/(2*(2+eps**2))
alphas = [p1,p2/2,p2/2,p2/2,p2/2]
print('Z2', Z2)
print('E2_row_marginals', alphas, 'sum', sum(alphas))

Vbound = 8*math.e**0.25 * Z2**(-1/8)
Vlimit = 4*math.sqrt(2)*math.e**0.25
print('new_E2_bound', Vbound)
print('uniform_E2_limit', Vlimit)

gamma = 1/4
k = eps**2/(1/16+eps**2)
theta = k + 128/65
D = (1+16*eps**2)*65**2
ridge = 16*3**(-5/8)*math.sqrt(math.e)*math.sqrt(3*theta/(3*theta-4))*D**(-1/(4*theta))
print('ridge_k', k)
print('ridge_theta', theta)
print('ridge_D', D)
print('partner_ridge_bound', ridge)

A = np.zeros((9,9))
A[0,0] = 1
A[1:6,6:9] = M
A[6:9,1:6] = M.T
print('target_spectrum', np.linalg.eigvalsh(A))
