"""Finite numerical check for QFORM-TWO-STAGE-SCHUR-TRANSPORT-v1.
This is supplementary evidence only; REPORT.md contains the algebraic proof.
"""
import numpy as np

rng = np.random.default_rng(20260922)
max_e1 = 0.0
max_e2 = 0.0
min_psd1 = float("inf")
min_psd2 = float("inf")
used_general = 0

for _ in range(500):
    n, rank = 5, 3
    M0 = rng.normal(size=(n, n)); M0 = (M0 + M0.T) / 2
    if abs(M0[0, 0]) < 0.3:
        M0[0, 0] += 1.0 if M0[0, 0] >= 0 else -1.0
    U = rng.normal(size=(n, rank))
    Theta = rng.normal(size=(rank, rank)); Theta = (Theta + Theta.T) / 2
    M = M0 + U @ Theta @ U.T
    a = M0[0, 0]; a1 = M[0, 0]
    if abs(a1) < 0.15:
        continue
    b = M0[1:, 0]; C = M0[1:, 1:]
    u = U[0, :]; W = U[1:, :]
    S0 = C - np.outer(b, b) / a
    S1 = M[1:, 1:] - np.outer(M[1:, 0], M[1:, 0]) / a1
    D = W - np.outer(b, u) / a
    K1 = Theta - np.outer(Theta @ u, Theta @ u) / a1
    max_e1 = max(max_e1, np.linalg.norm(S1 - (S0 + D @ K1 @ D.T), 2))
    s = S0[0, 0]; s1 = S1[0, 0]
    if abs(s) < 0.15 or abs(s1) < 0.15:
        continue
    c = S0[1:, 0]
    T0 = S0[1:, 1:] - np.outer(c, c) / s
    c1 = S1[1:, 0]
    T1 = S1[1:, 1:] - np.outer(c1, c1) / s1
    r = D[0, :]; Z = D[1:, :]
    K2 = K1 - np.outer(K1 @ r, K1 @ r) / s1
    E = Z - np.outer(c, r) / s
    max_e2 = max(max_e2, np.linalg.norm(T1 - (T0 + E @ K2 @ E.T), 2))
    used_general += 1

for _ in range(500):
    n, rank = 4, 3
    R = rng.normal(size=(n, n)); M0 = R @ R.T + np.eye(n)
    U = rng.normal(size=(n, rank))
    V = rng.normal(size=(rank, rank)); Theta = V @ V.T
    M = M0 + U @ Theta @ U.T
    a = M0[0, 0]; a1 = M[0, 0]
    b = M0[1:, 0]; C = M0[1:, 1:]
    S0 = C - np.outer(b, b) / a
    S1 = M[1:, 1:] - np.outer(M[1:, 0], M[1:, 0]) / a1
    min_psd1 = min(min_psd1, np.linalg.eigvalsh(S1 - S0).min())
    s = S0[0, 0]; s1 = S1[0, 0]
    c = S0[1:, 0]; c1 = S1[1:, 0]
    T0 = S0[1:, 1:] - np.outer(c, c) / s
    T1 = S1[1:, 1:] - np.outer(c1, c1) / s1
    min_psd2 = min(min_psd2, np.linalg.eigvalsh(T1 - T0).min())

print(f"general_trials_used={used_general}")
print(f"max_first_identity_error={max_e1:.17g}")
print(f"max_second_identity_error={max_e2:.17g}")
print(f"min_first_PSD_increment_eigenvalue={min_psd1:.17g}")
print(f"min_second_PSD_increment_eigenvalue={min_psd2:.17g}")
print("PASS" if max_e1 < 1e-10 and max_e2 < 1e-10 and min_psd1 > -1e-10 and min_psd2 > -1e-10 else "FAIL")
