import math
import numpy as np

# Constants in REPORT.md
eta = 1.0/16.0
C_raw = 4.0*math.sqrt(2.0)*math.exp(0.25)
C_inv = 4.0*(2.0**0.75)*math.exp(0.25)
C_torsion = C_inv*(eta**-0.5)*((3.0/(1.0-eta))**0.25)
C_zero = 2.0*math.sqrt(2.0)*(3.0**0.25)*(eta**-0.5)*((1.0-eta)**-0.25)
assert C_raw < 7.264
assert C_inv < 8.638
assert C_torsion < 46.212
assert C_zero < 15.132

# Target-valid rank-one-core regression matrix.
A = np.array([[1.0,1.0,1.0],
              [1.0,1.0,-1.0],
              [1.0,-1.0,0.0]])
ev = np.linalg.eigvalsh(A)
expected = np.array([-math.sqrt(2.0), math.sqrt(2.0), 2.0])
assert np.max(np.abs(ev-expected)) < 1e-12

# Rank-one physical pair and invariant resource.
E = A[:2,:2]
assert abs(np.linalg.det(E)) < 1e-12
assert np.linalg.matrix_rank(E, tol=1e-12) == 1
sigma = 2.0
r = np.array([1.0,1.0])/math.sqrt(2.0)
n = np.array([-1.0,1.0])/math.sqrt(2.0)
H = np.array([[1.0,-1.0]])
assert np.linalg.norm(E - sigma*np.outer(r,r)) < 1e-12
assert abs(np.linalg.norm(H@n)-math.sqrt(2.0)) < 1e-12
C_example = C_inv/(sigma*np.linalg.norm(H@n))**0.5
assert C_example < 5.137

# Direct physical completion agrees: a=1, b=1, u=1, v=-1,
# hence w=v-(b/a)u=-2 and |a|*||w||=2.
a,b = 1.0,1.0
u,v = 1.0,-1.0
w = v-(b/a)*u
C_direct = C_raw/(abs(a)*abs(w))**0.5
assert abs(C_direct-C_example) < 1e-12

# Wedge invariance under the (r,n) rotation: det(H^T H) for a
# one-row H vanishes; a separate two-row deterministic test checks the
# identity det Gram([u,v]) = det Gram([Hr,Hn]).
H2 = np.array([[2.0,-1.0],[1.0,3.0],[4.0,2.0]])
R = np.column_stack([r,n])
left = np.linalg.det(H2.T@H2)
right = np.linalg.det((H2@R).T@(H2@R))
assert abs(left-right) < 1e-10
assert np.linalg.norm(H2@n) + 1e-15 >= math.sqrt(left)/np.linalg.norm(H2@r)

print('QFORM_B09_R25_CHECK_PASS')
print('C_raw', C_raw)
print('C_inv', C_inv)
print('C_torsion', C_torsion)
print('C_zero', C_zero)
print('example_eigenvalues', ev.tolist())
print('C_example', C_example)
