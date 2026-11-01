import math
import numpy as np

# Exact constants used in REPORT.md.
C_null = 6.0 * math.e * (6.0 ** (1.0/3.0))
C_partner = 5.0 * math.sqrt(2.0 * math.e) * 64.0
assert C_null < 29.637
assert C_partner < 746.127
assert 6 * 24 == 144

# det [[0,s,0],[s,d,g],[0,g,f]] = -s^2 f.
for s,d,g,f in [(2.0,3.0,-5.0,7.0),(-1.5,-2.0,4.0,-3.0),(0.25,9.0,2.0,11.0)]:
    K = np.array([[0.0,s,0.0],[s,d,g],[0.0,g,f]])
    assert abs(np.linalg.det(K) + s*s*f) < 1e-10

# Fixed-row Cauchy--Binet identity for an orthonormal 3-frame.
rng = np.random.default_rng(20260923)
for n in [4,7,13]:
    Z = rng.normal(size=(n,3))
    R, _ = np.linalg.qr(Z)
    for i in range(n):
        ell = float(R[i] @ R[i])
        total = 0.0
        for j in range(n):
            if j == i: continue
            for k in range(j+1,n):
                if k == i: continue
                total += np.linalg.det(R[[i,j,k],:])**2
        assert abs(total-ell) < 5e-12

# Principal-triple determinant packet identity for A0=R K R^T.
for n in [5,9]:
    Z = rng.normal(size=(n,3))
    R, _ = np.linalg.qr(Z)
    D = np.diag([1.3,-2.1,0.8])
    O, _ = np.linalg.qr(rng.normal(size=(3,3)))
    K = O @ D @ O.T
    A = R @ K @ R.T
    detK = abs(np.linalg.det(K))
    for i in range(n):
        lhs = 0.0
        for j in range(n):
            if j == i: continue
            for k in range(j+1,n):
                if k == i: continue
                T = [i,j,k]
                lhs += abs(np.linalg.det(A[np.ix_(T,T)]))
        rhs = detK * float(R[i] @ R[i])
        assert abs(lhs-rhs) < 2e-10

# Singular-value congruence lower bound used in (2.6).
for _ in range(100):
    O1, _ = np.linalg.qr(rng.normal(size=(3,3)))
    O2, _ = np.linalg.qr(rng.normal(size=(3,3)))
    sl = np.array([1.0, 0.9, 0.45])
    sm = np.array([3.0, -1.7, 1.1])
    L = O1 @ np.diag(sl) @ O2.T
    V, _ = np.linalg.qr(rng.normal(size=(3,3)))
    M = V @ np.diag(sm) @ V.T
    K = L.T @ M @ L
    assert np.linalg.svd(K, compute_uv=False)[-1] + 1e-12 >= (sl.min()**2) * min(abs(sm))

print(f"null_scalar_constant={C_null:.12f}")
print(f"partner_D5_gamma_1_over_64={C_partner:.12f}")
print("diffuse_scaled_constant=144")
print("QFORM_B19_R23_GROUPED_NULL_HEAVYROW_CHECK_PASS")
