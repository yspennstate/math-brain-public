"""Finite sanity checks for QFORM hostile-inertia addition theorem.

These computations are NOT part of the proof.  The proof is min-max +
Cauchy interlacing; this script only checks random finite instances and
prints the quantitative finite-core constants used in REPORT.md.
"""
import math
import numpy as np

rng = np.random.default_rng(20260923)


def orthogonal(n):
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    return q


def count_ge(vals, L, tol=1e-9):
    return int(np.sum(vals >= L - tol))


trials = 2000
for trial in range(trials):
    n = int(rng.integers(6, 16))
    k = int(rng.integers(0, n - 3))
    r = int(rng.integers(0, n - k - 2))
    L = float(0.2 + 2.8 * rng.random())

    # A0 has at least n-k eigenvalues >= L.
    q0 = orthogonal(n)
    good = L + 4.0 * rng.random(n - k)
    exceptional = rng.uniform(-12.0, 0.9 * L, size=k)
    A0 = q0 @ np.diag(np.concatenate([exceptional, good])) @ q0.T

    # E has exactly r negative eigenvalues and arbitrarily many nonnegative ones.
    qe = orthogonal(n)
    neg = -(1e-4 + 50.0 * rng.random(r))
    nonneg = 50.0 * rng.random(n - r)
    E = qe @ np.diag(np.concatenate([neg, nonneg])) @ qe.T

    A = A0 + E
    vals = np.linalg.eigvalsh(A)
    expected = n - k - r
    assert count_ge(vals, L) >= expected

    # Every physical principal core of size d+3 must retain 3 eigenvalues >=L.
    d = k + r
    m = d + 3
    H = rng.choice(n, size=m, replace=False)
    B = A[np.ix_(H, H)]
    vals_B = np.linalg.eigvalsh(B)
    assert count_ge(vals_B, L) >= 3

print(f"random_inertia_interlacing_trials={trials}: PASS")
for d in range(0, 8):
    m = d + 3
    C = 2.0 * math.sqrt(6.0 * math.pi * m)
    print(f"d={d} m={m} generic_finite_core_constant={C:.12f}")
print(f"d=0_positive_definite_pair_sharpening={math.pi:.12f}")
