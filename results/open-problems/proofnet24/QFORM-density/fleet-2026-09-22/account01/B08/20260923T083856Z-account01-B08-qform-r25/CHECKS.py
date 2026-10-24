import math
import numpy as np

rng = np.random.default_rng(2026092308)


def incident_row_energy(B, i):
    ri = B[i]
    ans = 0.0
    for k in range(B.shape[0]):
        if k == i:
            continue
        rk = B[k]
        ans += float(np.dot(ri, ri) * np.dot(rk, rk) - np.dot(ri, rk) ** 2)
    return ans


def projected_identity(B, i):
    ri = B[i]
    nr = float(np.linalg.norm(ri))
    if nr == 0.0:
        return 0.0
    u = ri / nr
    W = B - (B @ u)[:, None] * u[None, :]
    return nr * nr * float(np.sum(W * W))


max_identity_error = 0.0
min_margin = float("inf")
for _ in range(1000):
    m = int(rng.integers(2, 9))
    n = int(rng.integers(2, 9))
    B = rng.normal(size=(m, n))
    i = int(rng.integers(0, m))
    H = incident_row_energy(B, i)
    P = projected_identity(B, i)
    max_identity_error = max(max_identity_error, abs(H - P))
    s = np.linalg.svd(B, compute_uv=False)
    tail = float(np.sum(s[1:] ** 2))
    lower = float(np.dot(B[i], B[i])) * tail
    min_margin = min(min_margin, H - lower)
    assert H + 1e-9 >= lower
    assert abs(H - P) < 1e-9

# Column statement follows by transpose; check independently.
for _ in range(200):
    B = rng.normal(size=(6, 7))
    j = int(rng.integers(0, B.shape[1]))
    Hc = incident_row_energy(B.T, j)
    Pc = projected_identity(B.T, j)
    s = np.linalg.svd(B, compute_uv=False)
    lower = float(np.dot(B[:, j], B[:, j])) * float(np.sum(s[1:] ** 2))
    assert Hc + 1e-9 >= lower
    assert abs(Hc - Pc) < 1e-9

# Stress family from the report.
A4 = np.array(
    [[0.0, 1.0, 0.0, 1.0],
     [1.0, 0.0, 1.0, 0.0],
     [0.0, 1.0, 0.0, 1.0],
     [1.0, 0.0, 1.0, 0.0]]
)
A = np.zeros((5, 5))
A[:4, :4] = A4
A[4, 4] = 1.0
spec = np.linalg.eigvalsh(A)
assert np.allclose(spec, [-2.0, 0.0, 0.0, 1.0, 2.0], atol=1e-10)
B = A[np.ix_([0, 1], [2, 3])]
sv = np.linalg.svd(B, compute_uv=False)
assert np.allclose(sv, [1.0, 1.0], atol=1e-12)
assert abs(incident_row_energy(B, 0) - 1.0) < 1e-12
assert abs(incident_row_energy(B.T, 0) - 1.0) < 1e-12
M_hub_leaf = A[np.ix_([0, 2], [1, 3])]
assert np.linalg.matrix_rank(M_hub_leaf, tol=1e-12) == 1
assert np.allclose(M_hub_leaf, np.ones((2, 2)))

# Constants.
C_E2 = 12 * 2 ** (5 / 6) * math.e ** (5 / 24)
C_star = 12 * 2 ** (17 / 24) * math.e ** (5 / 24)
rho = math.sqrt(3) - math.sqrt(2)
tau = rho * rho / (1 + rho)
C_k1 = C_E2 / math.sqrt(tau)
C_partner_star_d = C_star * math.sqrt(120)
C_partner_star_L = C_partner_star_d / math.sqrt(tau)

print("QFORM_B08_R25_CHECK_PASS")
print("max_identity_error", repr(max_identity_error))
print("min_lower_bound_margin", repr(min_margin))
print("stress_spectrum", [float(x) for x in spec])
print("stress_cross_singular_values", [float(x) for x in sv])
print("stress_hub_leaf_rank", int(np.linalg.matrix_rank(M_hub_leaf)))
print("C_E2", repr(C_E2))
print("C_star", repr(C_star))
print("tau", repr(tau))
print("C_k1", repr(C_k1))
print("C_partner_star_d", repr(C_partner_star_d))
print("C_partner_star_L", repr(C_partner_star_L))
