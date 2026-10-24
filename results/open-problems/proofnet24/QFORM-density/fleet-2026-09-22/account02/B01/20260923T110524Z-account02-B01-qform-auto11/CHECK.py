import math
import numpy as np

N = 8
eps = 0.1
sigma = 1/eps
u1 = np.ones(N)/math.sqrt(N)
u2 = np.array([1 if i % 2 == 0 else -1 for i in range(N)], dtype=float)/math.sqrt(N)
v1 = u1.copy()
v2 = u2.copy()
K = sigma*(np.outer(u1,v1)+np.outer(u2,v2))
H = eps*np.array([[1.0,2.0],[2.0,1.0]])
A = np.block([
    [np.zeros((N,N)), K, np.zeros((N,2))],
    [K.T, np.zeros((N,N)), np.zeros((N,2))],
    [np.zeros((2,N)), np.zeros((2,N)), H],
])

eig = np.linalg.eigvalsh(A)
nonzero = eig[np.abs(eig)>1e-9]
svals = np.linalg.svd(K, compute_uv=False)
const = 2**(21/8)*3**(-1/8)

expected = np.array([-sigma,-sigma,-eps,3*eps,sigma,sigma])
assert np.max(np.abs(nonzero-expected)) < 1e-10
assert np.linalg.matrix_rank(K, tol=1e-9) == 2
assert abs(svals[0]-sigma) < 1e-10 and abs(svals[1]-sigma) < 1e-10
assert abs(np.linalg.det(H)+3*eps**2) < 1e-12
assert abs(const-5.377291522273554) < 1e-12
print('nonzero_eigenvalues=', nonzero.tolist())
print('rank_K=2')
print('singular_values_K=', svals[:2].tolist())
print('det_H=', float(np.linalg.det(H)))
print('compiled_constant=', const)
print('STATUS=PASS')
