import math
import numpy as np

K0 = 113*math.sqrt(2)/7 + 49/32
print('K0', repr(K0))
print('sqrtK0', repr(math.sqrt(K0)))
print('sqrt_2piK0', repr(math.sqrt(2*math.pi*K0)))
print('fourK0', repr(4*K0))
print('blockdiag_balanced_bound', repr(K0/math.sqrt(5)))
print('contaminated_4d_bound', repr(4*math.sqrt(26)*(95/4)**(-0.25)))

B = np.array([[1.0,2.0],[2.0,-1.0]])
C = 0.5*np.eye(2)
M = np.block([[B,C],[C,B]])
A = np.zeros((5,5))
A[:4,:4] = M
A[4,4] = 2.0
A[:4,4] = 0.05
A[4,:4] = 0.05
print('eig_M', np.linalg.eigvalsh(M))
print('eig_A', np.linalg.eigvalsh(A))
print('min_abs_eig_A', np.min(np.abs(np.linalg.eigvalsh(A))))
print('coupling_norm', np.linalg.norm(np.full(4,0.05)))
S = B - C.T @ np.linalg.inv(B) @ C
print('S', S)
print('S_op', np.linalg.norm(S,2))
print('Delta', abs(np.linalg.det(B)))
print('kappa', np.min(np.linalg.svd(B,compute_uv=False)))
print('Delta_kappa_s', abs(np.linalg.det(B))*np.min(np.linalg.svd(B,compute_uv=False))*np.linalg.norm(S,2))
