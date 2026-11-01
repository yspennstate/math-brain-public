#!/usr/bin/env python3
"""Finite regression checks for REPORT.md; not part of the proof."""
import itertools
import numpy as np

for n in (5, 8, 16, 96):
    k = np.arange(n)
    theta = 2*np.pi*k/n
    R = np.column_stack((
        np.ones(n)/np.sqrt(n),
        np.sqrt(2/n)*np.cos(theta),
        np.sqrt(2/n)*np.sin(theta),
    ))
    P = R @ R.T
    err = np.linalg.norm(R.T @ R - np.eye(3), ord=2)
    eig = np.linalg.eigvalsh(P)
    max_smin = 0.0
    max_det = 0.0
    for I in itertools.combinations(range(n), 3):
        B = P[np.ix_(I, I)]
        max_smin = max(max_smin, np.linalg.eigvalsh(B)[0])
        max_det = max(max_det, np.linalg.det(B))
    print(f"n={n}")
    print(f"  orthogonality_error={err:.17g}")
    print(f"  max_diag={np.diag(P).max():.17g}  3/n={3/n:.17g}")
    print(f"  max_triple_smin={max_smin:.17g}  upper={3/n:.17g}")
    print(f"  max_triple_det={max_det:.17g}  hadamard_upper={27/n**3:.17g}")
    print(f"  top_eigs={eig[-3:]}")
