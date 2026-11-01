import math
import numpy as np

for R in (3.0, 10.0, 1000.0):
    A = np.array([
        [1,0,0,0,0],
        [0,0,0,R,0],
        [0,0,0,0,1/R],
        [0,R,0,0,0],
        [0,0,1/R,0,0],
    ], dtype=float)
    assert np.allclose(np.linalg.eigvalsh(A), [-R,-1/R,1/R,1,R])
    H = np.diag([R,1/R])
    assert abs(np.linalg.det(H)**2 - 1) < 1e-12
    for rho in (1e-3, 1.0, 1e3):
        K = H @ H.T @ np.linalg.inv(rho*rho*np.eye(2) + H @ H.T)
        k = np.diag(K)
        assert k.sum() <= 2*k.max() + 1e-12

C = (2**(4/3)+1)*math.sqrt(3)*2**0.25
assert abs(C-7.250055108887958) < 1e-12
print("PASS")
print("C_grp =", C)
