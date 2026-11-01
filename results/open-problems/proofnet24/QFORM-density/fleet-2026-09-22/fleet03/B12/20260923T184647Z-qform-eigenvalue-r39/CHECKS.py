import json
import math
import numpy as np

rng = np.random.default_rng(12345)
trials = 10_000
violations = 0
min_margin = float('inf')

for _ in range(trials):
    n = 24
    m = 10
    X = rng.normal(size=(n, n))
    A = (X + X.T) / 2.0
    C = A[:m, :m]
    B = A[:m, m:]
    G = (A @ A)[:m, :m]

    sC = np.linalg.svd(C, compute_uv=False)
    sB = np.linalg.svd(B, compute_uv=False)
    lam = np.linalg.eigvalsh(G)[::-1]

    lhs = sC[2] ** 2 + sB[4] ** 2
    rhs = lam[6]
    margin = float(lhs - rhs)
    min_margin = min(min_margin, margin)
    if margin < -1e-9:
        violations += 1

A10 = 2.0 * math.sqrt(6.0 * math.pi * 10.0)
D5 = 15.0 * math.sqrt(3.0 * math.e) / 2.0
family_bound = math.sqrt(A10 * A10 + D5 * D5) / (7.0 / 4.0)

result = {
    'seed': 12345,
    'trials': trials,
    'matrix_dimension': 24,
    'carrier_size': 10,
    'checked_inequality': 's3(C)^2+s5(B)^2 >= lambda7((A^2)[H,H])',
    'violations_at_1e-9': violations,
    'minimum_margin': min_margin,
    'A10': A10,
    'D5': D5,
    'partner_family_bound': family_bound,
    'role': 'finite consistency check only; analytic proof is Weyl interlacing',
}
print(json.dumps(result, indent=2, sort_keys=True))
