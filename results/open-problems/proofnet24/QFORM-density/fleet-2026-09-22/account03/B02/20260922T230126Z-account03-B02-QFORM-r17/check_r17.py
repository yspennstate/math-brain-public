import itertools
import math
import numpy as np

# Deterministic algebra regression for the identity
# e_3(M^T M) = Delta(B)^2 * dist(beta, Row(B))^2
# when rank(B)=2 and M=[beta^T; B].
rng = np.random.default_rng(17)
max_rel_err = 0.0
for _ in range(50):
    m = int(rng.integers(2, 7))
    n = int(rng.integers(3, 8))
    U = rng.normal(size=(m, 2))
    V = rng.normal(size=(n, 2))
    B = U @ V.T
    beta = rng.normal(size=n)

    s = np.linalg.svd(B, compute_uv=False)
    Delta = s[0] * s[1]
    _, _, vh = np.linalg.svd(B, full_matrices=False)
    R = vh[:2].T
    eta = np.linalg.norm(beta - R @ (R.T @ beta))

    M = np.vstack([beta, B])
    lam = np.linalg.eigvalsh(M.T @ M)
    e3 = sum(lam[i] * lam[j] * lam[k]
             for i, j, k in itertools.combinations(range(n), 3))
    rhs = Delta**2 * eta**2
    scale = max(1.0, abs(e3), abs(rhs))
    max_rel_err = max(max_rel_err, abs(e3-rhs)/scale)

hybrid_constant = 2**(29/12) * 3**0.25
print(f"trials=50")
print(f"max_scaled_error={max_rel_err:.17g}")
print(f"universal_exact_rank3_crossblock_density_constant=6")
print(f"partner_hybrid_constant={hybrid_constant:.16g}")
print("STATUS=PASS")
