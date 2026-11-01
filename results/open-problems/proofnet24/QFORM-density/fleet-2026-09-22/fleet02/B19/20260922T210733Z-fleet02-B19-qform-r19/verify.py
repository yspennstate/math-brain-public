import math
import numpy as np

rng = np.random.default_rng(1902)

def nonzero_singular_product(C, rank=3):
    s = np.linalg.svd(C, compute_uv=False)
    return float(np.prod(s[:rank]))

max_rel = 0.0
checked = 0
for _ in range(500):
    m = int(rng.integers(3, 10))
    n = int(rng.integers(3, 10))
    L = rng.normal(size=(m, 3))
    R = rng.normal(size=(n, 3))
    M = rng.normal(size=(3, 3))
    if np.linalg.matrix_rank(L) < 3 or np.linalg.matrix_rank(R) < 3:
        continue
    if abs(np.linalg.det(M)) < 1e-5:
        continue
    C = L @ M @ R.T
    lhs = nonzero_singular_product(C)
    rhs = abs(np.linalg.det(M)) * math.sqrt(
        np.linalg.det(L.T @ L) * np.linalg.det(R.T @ R)
    )
    max_rel = max(max_rel, abs(lhs-rhs)/rhs)
    checked += 1

max_gram_rel = 0.0
for _ in range(500):
    m = int(rng.integers(3, 12))
    alpha = rng.normal(size=m)
    beta = rng.normal(size=m)
    gamma = rng.normal(size=m)
    B = np.column_stack([beta, gamma])
    S = B.T @ B
    if np.linalg.det(S) < 1e-7:
        continue
    q = B.T @ alpha
    rho2 = alpha @ alpha - q @ np.linalg.solve(S, q)
    U = np.column_stack([alpha, beta, gamma])
    lhs = np.linalg.det(U.T @ U)
    rhs = np.linalg.det(S) * rho2
    scale = max(1.0, abs(lhs), abs(rhs))
    max_gram_rel = max(max_gram_rel, abs(lhs-rhs)/scale)

c0 = 7/9
detM0 = 1/2
H0 = 2*math.sqrt(640)
span_constant = (
    3 * 2**(2/3) * H0**(2/3)
    * c0**(-1/3) * detM0**(-1/3)
)
cross_rho_coefficient = (
    3*math.e
    * (math.sqrt(640/c0)/detM0)**(1/3)
)

assert checked >= 450
assert max_rel < 1e-8
assert max_gram_rel < 1e-9
assert span_constant < 89.251
assert cross_rho_coefficient < 31.452

print(f"rectangular_identity_cases={checked}")
print(f"rectangular_identity_max_rel={max_rel:.3e}")
print(f"gram_schur_max_scaled_error={max_gram_rel:.3e}")
print(f"span_endpoint_constant={span_constant:.12f}")
print(f"cross_bound_coefficient={cross_rho_coefficient:.12f} * rho^(-1/3)")
print("QFORM_B19_R19_LEAKAGE_BOUNDARY_CHECK_PASS")
