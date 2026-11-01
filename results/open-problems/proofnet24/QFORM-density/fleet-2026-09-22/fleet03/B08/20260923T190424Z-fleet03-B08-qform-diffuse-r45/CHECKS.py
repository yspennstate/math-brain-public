import math
import numpy as np

rng = np.random.default_rng(450845)


def e2(M):
    s = np.linalg.svd(M, compute_uv=False)
    x = s * s
    return ((x.sum()) ** 2 - (x * x).sum()) / 2


max_err = 0.0
min_ratio = float("inf")
violations = 0
NTEST = 5000

for _ in range(NTEST):
    m1 = int(rng.integers(2, 10))
    m2 = int(rng.integers(2, 10))
    M1 = rng.normal(size=(2, m1))
    M2 = rng.normal(size=(2, m2))
    U1 = np.linalg.qr(M1.T, mode="reduced")[0][:, :2]
    U2 = np.linalg.qr(M2.T, mode="reduced")[0][:, :2]
    P1 = U1 @ U1.T
    P2 = U2 @ U2.T
    T0 = rng.normal(size=(m1, m2))
    T = T0 - P1 @ T0 @ P2

    QB = np.linalg.qr(rng.normal(size=(2, 2)))[0]
    B = QB @ np.diag([rng.uniform(0.1, 4), -rng.uniform(0.1, 4)]) @ QB.T
    R = rng.normal(size=(2, 2))
    Binv = np.linalg.inv(B)
    K = R - Binv
    C = M1.T @ R @ M2 + T
    CB = C - M1.T @ Binv @ M2

    N1 = M1 @ U1
    N2 = M2 @ U2
    lhs_comp = U1.T @ CB @ U2
    rhs_comp = N1.T @ K @ N2
    max_err = max(max_err, float(np.max(np.abs(lhs_comp - rhs_comp))))

    lhs = float(e2(CB))
    rhs = float(np.linalg.det(rhs_comp) ** 2)
    if rhs > 1e-16:
        min_ratio = min(min_ratio, lhs / rhs)
    if lhs + 1e-8 < rhs:
        violations += 1

C_pair = 16.510052499365923
s_star = 1 / (64 * math.sqrt(896))
C_mismatch = C_pair * s_star ** (-5 / 19)
C_zero_hub = 2 * math.sqrt(math.pi) * s_star ** (-0.5)

print(f"tests={NTEST}")
print(f"max_compression_error={max_err:.17g}")
print(f"min_E2_to_compression_minor_ratio={min_ratio:.17g}")
print(f"violations={violations}")
print(f"s_star={s_star:.17g}")
print(f"normalized_mismatch_constant={C_mismatch:.17g}")
print(f"zero_hub_constant={C_zero_hub:.17g}")
assert violations == 0
print("QFORM_B08_R45_CHECK_PASS")
