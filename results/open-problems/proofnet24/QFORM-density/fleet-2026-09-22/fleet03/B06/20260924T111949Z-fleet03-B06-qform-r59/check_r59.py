import math
import numpy as np

rng = np.random.default_rng(12345)
NTRIAL = 20000
weighted = 0
min_ratio = float('inf')

for _ in range(NTRIAL):
    n = int(rng.integers(4, 20))
    X = rng.normal(size=(n, 3))
    U, _ = np.linalg.qr(X)
    U = U[:, :3]
    q = int(rng.integers(0, n))
    z = rng.normal(size=3)
    zn = np.linalg.norm(z)
    if zn < 1e-12:
        continue

    alpha = np.sum(U * U, axis=1)
    c = U @ z
    idx = [j for j in range(n) if j != q]
    S = float(np.sum(c[idx] ** 2))
    if S < 1e-14:
        continue

    H = [j for j in idx if alpha[j] > 0.5]
    L = [j for j in idx if j not in H]
    SH = float(np.sum(c[H] ** 2)) if H else 0.0

    if SH >= S / 2:
        assert H
        assert max(abs(c[j]) for j in H) + 1e-12 >= math.sqrt(S / 10)
        continue

    G = sum((np.outer(U[j], U[j]) for j in L), np.zeros((3, 3)))
    if np.trace(G) < 2:
        E = [q] + H
        assert float(np.sum(alpha[E])) > 1 - 1e-11
        continue

    zh = z / zn
    _, _, Vh = np.linalg.svd(zh.reshape(1, 3))
    Pbasis = Vh[1:].T
    a = float(zh @ G @ zh)
    b = Pbasis.T @ G @ zh
    C = Pbasis.T @ G @ Pbasis
    K = a * C - np.outer(b, b)
    evals = np.linalg.eigvalsh(K)
    Pmass = float(evals[-1])
    target = S / (4 * zn * zn)
    assert Pmass + 1e-11 >= target
    weighted += 1
    min_ratio = min(min_ratio, Pmass / target)

print('QFORM_B06_R59_CHECK_PASS')
print('trials', NTRIAL)
print('weighted_branch_samples', weighted)
print('minimum_ratio', min_ratio)
print('live_eta_currency', 1/(4*96**2))
