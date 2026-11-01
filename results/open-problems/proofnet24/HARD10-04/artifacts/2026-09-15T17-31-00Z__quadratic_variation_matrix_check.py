"""HARD10-04 finite-dimensional quadratic-variation checker.

This script checks only the matrix algebra used in the 2026-09-15T17:22:40Z
report.  It is not a DLA simulation and is not evidence for the unresolved
existence/value of the planar DLA growth exponent.

We sample k<=3, construct a symmetric positive-semidefinite nonnegative return
matrix Q with row sums <=0.74<3/4, set H=(I-Q)^(-1), then sample a positive
new-boundary harmonic-mass vector w.  The report uses

    g = H w,
    W = 1^T w,
    d = w^T H w,
    p = (1/4) 1^T g,
    v = w/W,
    rho = v^T H v.

It checks the consequences

    I <= H <= 4 I,
    p <= W <= 4 p,
    W^2/3 <= d <= 4 W^2,
    d = W^2 rho,
    1/3 <= rho <= 4.

The random matrices are only algebraic test cases satisfying the hypotheses;
they are not asserted to arise from actual DLA clusters.
"""

import random
import numpy as np


def run_trial() -> None:
    k = random.randint(1, 3)

    # Nonnegative PSD symmetric matrix, then scale its maximum row sum below 3/4.
    m = np.random.random((k, k))
    q = m @ m.T
    max_row_sum = float(q.sum(axis=1).max())
    if max_row_sum > 0:
        q *= 0.74 / max_row_sum

    q_eigs = np.linalg.eigvalsh(q)
    assert q_eigs.min() >= -1e-10
    assert q.sum(axis=1).max() <= 0.7400000001

    h = np.linalg.inv(np.eye(k) - q)
    h_eigs = np.linalg.eigvalsh(h)
    assert h_eigs.min() >= 1.0 - 1e-9
    assert h_eigs.max() <= 4.0 + 1e-9

    w = np.random.exponential(1.0, size=k)
    g = h @ w

    W = float(w.sum())
    d = float(w @ h @ w)
    p = float(g.sum() / 4.0)
    v = w / W
    rho = float(v @ h @ v)

    assert p <= W + 1e-9
    assert W <= 4.0 * p + 1e-9

    assert d >= W * W / 3.0 - 1e-9
    assert d <= 4.0 * W * W + 1e-9

    assert abs(d - W * W * rho) <= 1e-8 * max(1.0, abs(d))
    assert rho >= 1.0 / 3.0 - 1e-9
    assert rho <= 4.0 + 1e-9


def main() -> None:
    random.seed(20260915)
    np.random.seed(20260915)
    for _ in range(10_000):
        run_trial()
    print("10,000 finite-dimensional quadratic-variation checks passed.")


if __name__ == "__main__":
    main()
