import math
import numpy as np

rho0 = math.sqrt(29/3072)
theta0 = 2**-12
Cstar = 2**(15/4) * 3**(-3/8)
balanced = Cstar * theta0**(-1/4) * rho0**(-1/8)
assert balanced < 96
assert 34*math.sqrt(9) == 102

rng = np.random.default_rng(20260923)
max_rel = 0.0
for _ in range(100):
    g1, g2 = rng.uniform(0.05, 0.95, 2)
    G = np.diag([1.0, g1, g2])
    P = np.diag([1.0, math.sqrt(g1), math.sqrt(g2)])
    S = np.array([[0.0, math.sqrt(1-g1), 0.0],
                  [0.0, 0.0, math.sqrt(1-g2)]])
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    M = Q @ np.diag([1.2, -1.7, 2.5]) @ Q.T
    C = P @ M @ S.T
    sv = np.linalg.svd(C, compute_uv=False)
    rho = sv[0] * sv[1]
    u = np.array([1.0, 0.0, 0.0])
    z = np.linalg.solve(G, np.linalg.solve(M, u))
    q = z @ G @ z
    r = P @ z / math.sqrt(q)
    B = P @ M @ P.T
    Rperp = np.linalg.norm(B @ r)
    theta = math.sqrt(g1*g2*(1-g1)*(1-g2))
    rhs = abs(np.linalg.det(M)) * theta
    rel = abs(rho*Rperp-rhs) / max(1.0, abs(rhs))
    max_rel = max(max_rel, rel)
    assert rel < 1e-12

print(f"rho0={rho0:.15f}")
print(f"Cstar={Cstar:.15f}")
print(f"balanced_bound={balanced:.15f}")
print(f"max_random_identity_relative_error={max_rel:.3e}")
print("QFORM_B19_R27_FRAME_DEFECT_CHECK_PASS")
