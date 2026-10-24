"""Stronger finite sanity check for account03/B12 r43.

The first checker used generic singular-value perturbation and paid a -K F term.
That is unnecessary here: B0=B P and E=B(I-P) occupy orthogonal column
subspaces, so after the physical Schur row map their row Grams still add with
zero cross term.  This checker tests the stronger analytic lower bound

  s2(Bsharp) >= beta*d,

with d^2=lambda_3(C^2+BB^T)-b^2-||E||_op^2 and
beta=(d/sqrt(m)-b)/(c/sqrt(m)+b), whenever beta>0.

Random tests are sanity checks only; REPORT.md contains the proof.
"""
import math
import numpy as np

SEED = 20260924
TRIALS = 50000
rng = np.random.default_rng(SEED)
admissible = 0
violations = 0
minimum_margin = float("inf")

for _ in range(TRIALS):
    m = int(rng.integers(3, 13))
    n = int(rng.integers(3, 15))

    U, _ = np.linalg.qr(rng.normal(size=(m, m)))
    c = float(rng.uniform(0.7, 4.0))
    bcap = min(c / (1.25 * m), float(rng.uniform(0.01, 0.25)))
    b = float(rng.uniform(0.001, bcap))
    rest = rng.uniform(-b, b, size=m - 1)
    rest[0] = rng.choice([-1.0, 1.0]) * b
    C = U @ np.diag(np.r_[rng.choice([-1.0, 1.0]) * c, rest]) @ U.T
    u = U[:, 0]

    V, _ = np.linalg.qr(rng.normal(size=(n, 2)))
    P = V @ V.T
    raw = rng.normal(size=(m, n))
    B0 = raw @ P
    E0 = raw @ (np.eye(n) - P)
    E = float(rng.uniform(0.0, 0.4)) * E0
    B = B0 + E
    F = float(np.linalg.norm(E, 2))

    gram = C @ C + B @ B.T
    g = math.sqrt(max(float(np.linalg.eigvalsh(gram)[::-1][2]), 0.0))
    d2 = g * g - b * b - F * F
    if d2 <= 1.0e-10:
        continue
    d = math.sqrt(d2)
    if d / math.sqrt(m) <= b:
        continue

    i = int(np.argmax(np.abs(u)))
    a = float(C[i, i])
    if abs(a) <= 1.0e-12:
        continue
    keep = [j for j in range(m) if j != i]
    Bsharp = B[keep, :] - (C[keep, i] / a)[:, None] * B[i, :][None, :]
    s2sharp = float(np.linalg.svd(Bsharp, compute_uv=False)[1])

    beta = (d / math.sqrt(m) - b) / (c / math.sqrt(m) + b)
    lower = beta * d
    margin = s2sharp - lower
    minimum_margin = min(minimum_margin, margin)
    admissible += 1
    if margin < -2.0e-8:
        violations += 1

print({
    "seed": SEED,
    "trials": TRIALS,
    "admissible": admissible,
    "violations": violations,
    "minimum_margin": minimum_margin,
})
