import math
import numpy as np

rng = np.random.default_rng(20260924)
violations = 0
min_margin = float("inf")
min_simple_margin = float("inf")
N = 10000

for _ in range(N):
    m = int(rng.integers(2, 10))
    q = int(rng.integers(1, m))

    Uf, _ = np.linalg.qr(rng.normal(size=(m, m)))
    Vf, _ = np.linalg.qr(rng.normal(size=(m, m)))
    singulars = np.sort(10.0 ** rng.uniform(-3.0, 1.0, size=m))[::-1]
    F = Uf @ np.diag(singulars) @ Vf.T

    K = Vf[:, m-q:]
    Kperp = Vf[:, :m-q]

    W = rng.normal(size=(m + 3, m))
    b = np.linalg.svd(W @ K, compute_uv=False)[-1]
    a = singulars[m-q-1]
    c = np.linalg.norm(W @ Kperp, 2)

    S = a*a + b*b + c*c
    disc = max(0.0, S*S - 4.0*a*a*b*b)
    rho = math.sqrt((S - math.sqrt(disc)) / 2.0)
    simple = a*b / math.sqrt(S)

    actual = np.linalg.svd(np.vstack([F, W]), compute_uv=False)[-1]
    margin = actual - rho
    simple_margin = rho - simple

    min_margin = min(min_margin, margin)
    min_simple_margin = min(min_simple_margin, simple_margin)
    if margin < -1e-9 or simple_margin < -1e-9:
        violations += 1

print({
    "seed": 20260924,
    "instances": N,
    "violations": violations,
    "minimum_actual_minus_rho": min_margin,
    "minimum_rho_minus_simple_bound": min_simple_margin,
})
