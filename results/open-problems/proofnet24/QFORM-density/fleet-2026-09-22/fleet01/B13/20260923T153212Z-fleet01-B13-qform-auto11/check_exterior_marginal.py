"""Deterministic seeded diagnostic for QFORM-EXTERIOR-MARGINAL-ENERGY-v1.
Not part of the proof.  Brute-forces all squared 3-minors on small random matrices.
"""
import itertools
import numpy as np

rng = np.random.default_rng(1)
max_fraction = 0.0
cases = 0
for p, q in [(5, 9), (7, 6), (6, 12)]:
    for _ in range(100):
        M = rng.normal(size=(p, q))
        sv = np.linalg.svd(M, compute_uv=False)
        if len(sv) < 3 or sv[2] <= 1e-12:
            continue
        row_mass = np.zeros(p)
        col_mass = np.zeros(q)
        Z = 0.0
        for S in itertools.combinations(range(p), 3):
            for T in itertools.combinations(range(q), 3):
                d2 = float(np.linalg.det(M[np.ix_(S, T)]) ** 2)
                Z += d2
                for i in S:
                    row_mass[i] += d2
                for j in T:
                    col_mass[j] += d2
        alpha = row_mass / Z
        beta = col_mass / Z
        row_bound = 3.0 * np.sum(M * M, axis=1) / sv[2] ** 2
        col_bound = 3.0 * np.sum(M * M, axis=0) / sv[2] ** 2
        max_fraction = max(
            max_fraction,
            float(np.max(alpha / row_bound)),
            float(np.max(beta / col_bound)),
        )
        assert np.all(alpha <= row_bound + 1e-10)
        assert np.all(beta <= col_bound + 1e-10)
        cases += 1

print(f"cases={cases}")
print(f"max_observed_marginal_to_bound_ratio={max_fraction:.16f}")
