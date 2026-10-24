import math
import numpy as np

# Constants in QFORM-RANK1-CROSSING-SQRT-SMALLBALL-v1 and
# QFORM-INDEFINITE-PAIR-RANK1-SCHUR-CROSSING-v1.
H1 = math.exp(0.5) * (2.0 ** 0.25) * math.gamma(0.25)
C1 = 4.0 * math.sqrt(2.0 * H1)
print(f"H1={H1:.15f}")
print(f"C1={C1:.15f}")
assert abs(H1 - 7.108628442830306) < 1e-12
assert abs(C1 - 15.082311168072676) < 1e-12

# Target-valid diffuse model: physical indefinite pair plus a flat rank-one
# cross block.  Its nonzero spectrum must be {-L,-L,L,L} for every m.
for m in (2, 3, 5, 10, 50):
    L = 1.7
    r = np.ones(m) / math.sqrt(m)
    A = np.zeros((2 + 2*m, 2 + 2*m))
    A[0, 1] = A[1, 0] = L
    C = L * np.outer(r, r)
    A[2:2+m, 2+m:] = C
    A[2+m:, 2:2+m] = C.T
    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev) > 1e-9]
    assert len(nz) == 4
    assert np.max(np.abs(np.sort(nz) - np.array([-L, -L, L, L]))) < 1e-10
    assert abs(np.linalg.svd(C, compute_uv=False)[0] - L) < 1e-10
    assert abs(np.max(np.abs(C)) - L/m) < 1e-12
print("DIFFUSE_MODEL_SPECTRUM_PASS")

# Rank-one common-plane singular-value inequality:
# sigma_1(M1^T J M2) >= s_2(M1) s_2(M2) sigma_1(J), rank(J)=1.
rng = np.random.default_rng(83043)
min_ratio = float("inf")
for _ in range(5000):
    m1 = int(rng.integers(2, 9))
    m2 = int(rng.integers(2, 9))
    M1 = rng.normal(size=(2, m1))
    M2 = rng.normal(size=(2, m2))
    u = rng.normal(size=2); u /= np.linalg.norm(u)
    v = rng.normal(size=2); v /= np.linalg.norm(v)
    j = 10.0 ** float(rng.uniform(-2, 2))
    J = j * np.outer(u, v)
    C = M1.T @ J @ M2
    sigma = np.linalg.svd(C, compute_uv=False)[0]
    beta1 = np.linalg.svd(M1, compute_uv=False)[-1]
    beta2 = np.linalg.svd(M2, compute_uv=False)[-1]
    rhs = j * beta1 * beta2
    ratio = sigma / rhs
    min_ratio = min(min_ratio, ratio)
    assert sigma + 1e-10 >= rhs
print(f"RANK1_ARM_MIN_RATIO={min_ratio:.12f}")
print("QFORM_B08_R43_RANK1_CHECK_PASS")
