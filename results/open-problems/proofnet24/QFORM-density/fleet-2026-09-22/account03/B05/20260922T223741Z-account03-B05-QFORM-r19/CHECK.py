"""Diagnostic checks for account03/B05 r19.
The proof is analytic; this file checks constants and the aggregate Schur identity numerically.
"""
import math
import numpy as np

C = 8 * 2**(3/4) * math.sqrt(5)
print("prefactor", repr(C))
assert abs(C - 30.084824744691147) < 1e-12
print("square_lift_prefactor", repr(2*math.sqrt(C)))

rng = np.random.default_rng(123)
checked = 0
for _ in range(100):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    M = Q @ np.diag([2.0, -1.5, 0.8]) @ Q.T
    T1 = rng.normal(size=(3, 2))
    v2 = rng.normal(size=3); v2 /= np.linalg.norm(v2)
    v3 = rng.normal(size=3); v3 /= np.linalg.norm(v3)
    lam2, lam3 = 1.3, 0.7
    T23 = np.column_stack([math.sqrt(lam2)*v2, math.sqrt(lam3)*v3])
    B = T23.T @ M @ T23
    if np.linalg.det(B) >= -1e-8:
        continue
    N = M - M @ T23 @ np.linalg.inv(B) @ T23.T @ M
    S = T1.T @ N @ T1
    assert np.linalg.matrix_rank(S, tol=1e-8) == 1
    D = abs(np.linalg.det(B))
    mu = abs(np.linalg.det(M))*lam2*lam3*sum(
        np.linalg.det(np.column_stack([T1[:,i],v2,v3]))**2 for i in range(2)
    )
    assert abs(D*abs(np.trace(S))-mu) <= 1e-9 * max(1.0, mu)
    checked += 1

assert checked >= 10
print("aggregate_schur_identity_trials", checked)
print("PASS")
