"""Finite diagnostics for QFORM-RANK2-TRANSLATION-HALFRIESZ-v1.
These checks support algebra only; they are not the proof.
"""
import math
import numpy as np

rng = np.random.default_rng(20260922)
max_rel_schur = 0.0
count = 0
for n in range(3, 12):
    for _ in range(200):
        G = rng.normal(size=(n, 2))
        U, _ = np.linalg.qr(G)
        O, _ = np.linalg.qr(rng.normal(size=(2, 2)))
        vals = np.array([
            rng.uniform(.5, 3) * rng.choice([-1, 1]),
            rng.uniform(.5, 3) * rng.choice([-1, 1]),
        ])
        Lam = O @ np.diag(vals) @ O.T
        i = int(rng.integers(0, n))
        u = U[i, :]
        c = float(u @ u)
        a = float(u @ Lam @ u)
        if c < 1e-12 or abs(a) < 1e-8:
            continue
        J = [j for j in range(n) if j != i]
        UJ = U[J, :]
        b = UJ @ Lam @ u
        HJJ = UJ @ Lam @ UJ.T
        S = HJJ - np.outer(b, b) / a
        ev = np.linalg.eigvalsh(S)
        kappa = ev[np.argmax(abs(ev))]
        target = c * np.linalg.det(Lam) / a
        rel = abs(kappa - target) / max(1.0, abs(target))
        max_rel_schur = max(max_rel_schur, rel)
        count += 1

max_rel_zero = 0.0
count_zero = 0
for _ in range(1000):
    lam1 = rng.uniform(.5, 3)
    lam2 = -rng.uniform(.5, 3)
    c = rng.uniform(.51, .99)
    ratio = -lam2 / lam1
    v2sq = c / (ratio + 1)
    v1sq = ratio * v2sq
    u = np.array([math.sqrt(v1sq), math.sqrt(v2sq)])
    Lam = np.diag([lam1, lam2])
    a = float(u @ Lam @ u)
    bnorm2 = float(u @ Lam @ (np.eye(2) - np.outer(u, u)) @ Lam @ u)
    target = c * abs(np.linalg.det(Lam))
    rel = abs(bnorm2 - target) / max(1.0, target)
    max_rel_zero = max(max_rel_zero, rel)
    count_zero += 1

print(f"schur_cases={count}")
print(f"schur_max_relative_error={max_rel_schur:.18e}")
print(f"zero_pivot_cases={count_zero}")
print(f"zero_pivot_max_relative_error={max_rel_zero:.18e}")
print("STATUS=PASS" if max_rel_schur < 2e-14 and max_rel_zero < 2e-14 else "STATUS=FAIL")
