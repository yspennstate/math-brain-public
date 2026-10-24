"""Diagnostic checker for QFORM-CONDITIONAL-WHITENED-DIFFUSE-v1 identities.

This is not a proof. It numerically checks Cauchy--Binet / determinant-lemma
identities used in REPORT.md on reproducible random orthonormal 3-frames.
"""
import itertools
import numpy as np

rng = np.random.default_rng(123)
max_err = 0.0
for n in (6, 8, 12):
    q, _ = np.linalg.qr(rng.normal(size=(n, 3)))
    U = q[:, :3]
    weights = {
        I: float(np.linalg.det(U[list(I), :]) ** 2)
        for I in itertools.combinations(range(n), 3)
    }
    max_err = max(max_err, abs(sum(weights.values()) - 1.0))
    H = []
    for _ in range(4):
        L = [i for i in range(n) if i not in H]
        S = U[L, :].T @ U[L, :]
        detS = float(np.linalg.det(S))
        surviving = sum(w for I, w in weights.items() if set(I).issubset(L))
        max_err = max(max_err, abs(detS - surviving))
        if detS <= 1e-13:
            break
        Sinv = np.linalg.inv(S)
        lev = {i: float(U[i] @ Sinv @ U[i]) for i in L}
        for i in L:
            num = sum(
                w for I, w in weights.items()
                if i in I and set(I).issubset(L)
            )
            max_err = max(max_err, abs(lev[i] - num / surviving))
        if detS < 1/8 or max(lev.values()) <= 1/2:
            break
        i = max(lev, key=lev.get)
        old_det = detS
        old_lev = lev[i]
        H.append(i)
        L2 = [j for j in range(n) if j not in H]
        new_det = float(np.linalg.det(U[L2, :].T @ U[L2, :]))
        max_err = max(max_err, abs(new_det - old_det * (1 - old_lev)))

print(f"PASS max_abs_error={max_err:.3e}")
assert max_err < 1e-12
