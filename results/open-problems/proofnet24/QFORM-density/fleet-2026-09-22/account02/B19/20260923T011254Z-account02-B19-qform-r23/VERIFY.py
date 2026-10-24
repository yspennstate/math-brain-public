import math
import numpy as np

# Constants used in REPORT.md
c_grouped = 12 * 6 ** (1/3)
c_r3 = 3 * math.sqrt(math.e) * 64 * 48 ** (1/6)
c_core = 2 * math.sqrt(30 * math.pi) * 96

assert c_grouped < 21.806
assert c_r3 < 604
assert c_core < 1864
assert 589/590 > 0.998
assert 589/1180 > 0.499

# Determinant normalization regression for the grouped branch.
delta = 0.2
H = np.diag([1.0, 1.0, delta])
Z = np.array([
    [1/math.sqrt(2),0,0],[1/math.sqrt(2),0,0],
    [0,1/math.sqrt(2),0],[0,1/math.sqrt(2),0],
    [0,0,1/math.sqrt(2)],[0,0,1/math.sqrt(2)]
])
assert np.linalg.norm(Z.T @ Z - np.eye(3), ord=np.inf) < 1e-12
U = Z @ np.sqrt(H)
assert np.linalg.norm(U.T @ U - H, ord=np.inf) < 1e-12
M = np.array([[2.0,0.2,0.1],[0.2,-1.5,0.3],[0.1,0.3,1.2]])
assert np.min(np.abs(np.linalg.eigvalsh(M))) > 1
K = np.sqrt(H) @ M @ np.sqrt(H)
assert abs(abs(np.linalg.det(K)) - abs(np.linalg.det(M))*delta) < 1e-12

print(f"grouped_diffuse_constant={c_grouped:.12f}")
print(f"r3_pairatom_constant={c_r3:.12f}")
print(f"heavy_core_eta_1_16_constant={c_core:.12f}")
print(f"r1_transverse={589/590:.12f}")
print(f"r1_half_transverse={589/1180:.12f}")
print("QFORM_B19_R23_CHECK_PASS")
