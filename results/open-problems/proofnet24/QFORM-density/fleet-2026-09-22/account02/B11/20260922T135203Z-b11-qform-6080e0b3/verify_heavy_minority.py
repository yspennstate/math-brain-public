import math
import numpy as np

rng = np.random.default_rng(26092211)

def random_orthogonal():
    M = rng.normal(size=(3,3))
    Q, _ = np.linalg.qr(M)
    if np.linalg.det(Q) < 0:
        Q[:,0] *= -1
    return Q

checked = 0
near_null = 0
for _ in range(2000):
    vals = np.array([
        1 + 4*rng.random(),
        1 + 4*rng.random(),
        -(1 + 4*rng.random())
    ])
    O = random_orthogonal()
    H = O @ np.diag(vals) @ O.T
    a = H[0,0]
    if a >= -1e-10:
        continue
    h = H[0,1:]
    C = H[1:,1:]
    S = C - np.outer(h,h)/a
    eigS = np.linalg.eigvalsh(S)
    assert eigS.min() > -1e-8
    assert abs(np.linalg.det(S) - np.linalg.det(H)/a) <= 1e-8*max(1.0,abs(np.linalg.det(S)))
    assert np.linalg.eigvalsh(H@H - np.eye(3)).min() > -1e-8
    if abs(a) < 0.25:
        assert h@h > 15/16 - 1e-8
        near_null += 1
    checked += 1

c = 3/4
H0 = np.array([[0.,0.,1.],[0.,1.,0.],[1.,0.,0.]])
T = np.array([
    [math.sqrt(c),0.,0.],
    [math.sqrt(1-c),0.,0.],
    [0.,1.,0.],
    [0.,0.,1.]
])
A = T @ H0 @ T.T
spec = np.linalg.eigvalsh(A)
assert np.allclose(spec, [-1.,0.,1.,1.], atol=1e-12)
assert abs(A[0,0]) < 1e-12
assert abs(np.sum(A[0,1:]**2) - c) < 1e-12

print("QFORM_HEAVY_MINORITY_RAYLEIGH_CHECK_PASS")
print("random_minority_cases", checked)
print("near_null_cases", near_null)
print("branch_constant_delta_1_4", 4*math.sqrt(math.pi*math.e))
print("null_example_spectrum", spec.tolist())
print("null_example_cross_row_sqnorm", float(np.sum(A[0,1:]**2)))
