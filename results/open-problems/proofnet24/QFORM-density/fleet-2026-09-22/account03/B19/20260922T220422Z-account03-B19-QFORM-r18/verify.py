import itertools
import math
import numpy as np

rng = np.random.default_rng(20260922)
max_rel = 0.0
for _ in range(1000):
    V = rng.normal(size=(3, 3))
    if abs(np.linalg.det(V)) < 1e-3:
        continue
    V = V / np.linalg.norm(V, axis=0, keepdims=True)
    lam = np.exp(rng.uniform(-2, 2, size=3))
    D = np.diag(np.sqrt(lam))
    M = rng.normal(size=(3, 3))
    M = (M + M.T) / 2
    M += np.diag([2.3, -1.7, 1.1])
    if abs(np.linalg.det(M)) < 1e-6:
        continue
    B = D @ V.T @ M @ V @ D
    mu = abs(np.linalg.det(M)) * np.prod(lam) * np.linalg.det(V) ** 2
    rel = abs(abs(np.linalg.det(B)) - mu) / max(mu, 1e-15)
    max_rel = max(max_rel, rel)
assert max_rel < 1e-8, max_rel

for _ in range(100):
    nJ, nK = 6, 4
    Uj = rng.normal(size=(nJ, 3))
    Uk = rng.normal(size=(nK, 3))
    weights = {}
    total = 0.0
    for i in range(nJ):
        for j in range(i + 1, nJ):
            for k in range(nK):
                w = np.linalg.det(np.stack([Uj[i], Uj[j], Uk[k]])) ** 2
                weights[(i, j, k)] = w
                total += w
    best = 0.0
    for bits in itertools.product([0, 1], repeat=nJ):
        separated = sum(w for (i, j, _), w in weights.items() if bits[i] != bits[j])
        best = max(best, separated)
    assert best + 1e-10 >= total / 2

base = 64 * math.sqrt(10)
b10 = 512 * math.sqrt(10)
assert abs(base - 202.3857702507763) < 1e-12
assert abs(b10 - 1619.0861620062103) < 1e-12

print(f"max determinant relative error: {max_rel:.3e}")
print(f"64*sqrt(10) = {base:.15f}")
print(f"512*sqrt(10) = {b10:.15f}")
print("QFORM_B19_R18_RANKONE_BANK_AGGREGATE_CHECK_PASS")
