"""Finite sanity checks for fleet03/B12 r43.

These computations do NOT prove the theorem.  The proof in REPORT.md is analytic.
They check the deterministic inequalities used by the rank-two-tube transverse
Schur lemma on random matrices with an exact rank-two row-space component plus
an orthogonal residual tail.
"""
import math
import numpy as np

SEED = 20260923
TRIALS = 50000
rng = np.random.default_rng(SEED)
viol = [0, 0, 0, 0]
mins = [float("inf")] * 4
admissible = 0

for _ in range(TRIALS):
    m = int(rng.integers(3, 13))
    n = int(rng.integers(3, 15))

    U, _ = np.linalg.qr(rng.normal(size=(m, m)))
    c = float(rng.uniform(0.7, 4.0))
    bcap = min(c / (1.25 * m), float(rng.uniform(0.01, 0.25)))
    b = float(rng.uniform(0.001, bcap))
    rest = rng.uniform(-b, b, size=m - 1)
    rest[0] = rng.choice([-1.0, 1.0]) * b
    lam = rng.choice([-1.0, 1.0]) * c
    C = U @ np.diag(np.r_[lam, rest]) @ U.T
    u = U[:, 0]

    V, _ = np.linalg.qr(rng.normal(size=(n, 2)))
    P = V @ V.T
    raw = rng.normal(size=(m, n))
    B0 = raw @ P
    E0 = raw @ (np.eye(n) - P)
    eps = float(rng.uniform(0.0, 0.15))
    E = eps * E0
    B = B0 + E
    F = float(np.linalg.norm(E, 2))

    square_gram = C @ C + B @ B.T
    g = math.sqrt(max(float(np.linalg.eigvalsh(square_gram)[::-1][2]), 0.0))
    d2 = g * g - b * b - F * F
    if d2 <= 1.0e-12:
        continue
    d = math.sqrt(d2)

    H0 = c * c * np.outer(u, u) + B0 @ B0.T
    lam3 = float(np.linalg.eigvalsh(H0)[::-1][2])
    sv0 = np.linalg.svd(B0, compute_uv=False)

    W, _ = np.linalg.qr(B0)
    rank = np.linalg.matrix_rank(B0, tol=1.0e-10)
    W = W[:, :rank]
    delta = float(np.linalg.norm((np.eye(m) - W @ W.T) @ u))

    margins = [
        lam3 - d2,
        float(sv0[1]) - d,
        delta - d / c,
    ]

    i = int(np.argmax(np.abs(u)))
    a = float(C[i, i])
    if abs(a) <= 1.0e-12:
        continue
    keep = [j for j in range(m) if j != i]
    Bsharp = B[keep, :] - (C[keep, i] / a)[:, None] * B[i, :][None, :]
    svals = np.linalg.svd(Bsharp, compute_uv=False)
    s2sharp = float(svals[1])

    alpha = c / m - b
    if alpha <= 0.0:
        continue
    beta = max(0.0, (d / math.sqrt(m) - b) / (c / math.sqrt(m) + b))
    K = (c + b) / alpha
    lower = beta * d - K * F
    margins.append(s2sharp - lower)

    admissible += 1
    for j, margin in enumerate(margins):
        mins[j] = min(mins[j], float(margin))
        if margin < -2.0e-8:
            viol[j] += 1

print({
    "seed": SEED,
    "trials": TRIALS,
    "admissible": admissible,
    "violations": viol,
    "minimum_margins": mins,
})
