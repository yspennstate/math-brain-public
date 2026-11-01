import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)
errs = []
for _ in range(200):
    m = int(rng.integers(4, 10))
    d = int(rng.integers(3, 8))
    M = rng.normal(size=(m, d))
    i, k = rng.choice(m, 2, replace=False)
    u, v = M[i], M[k]
    G = np.array([[u @ u, u @ v], [u @ v, v @ v]])
    D = float(np.linalg.det(G))
    if D <= 1e-10:
        continue
    P = np.stack([u, v]).T @ np.linalg.inv(G) @ np.stack([u, v])
    Pperp = np.eye(d) - P
    R = sum(float(np.dot(Pperp @ M[l], Pperp @ M[l]))
            for l in range(m) if l not in (i, k))
    W = 0.0
    for l in range(m):
        if l in (i, k):
            continue
        for C in itertools.combinations(range(d), 3):
            W += float(np.linalg.det(M[np.ix_([i, k, l], C)]) ** 2)
    errs.append(abs(W - D * R) / (1.0 + abs(W)))

c_l3 = 3 ** (2 / 3) * 2 ** (1 / 3)
c_square = 2 ** (15 / 4) / 3 ** (1 / 4)
print(f"trials={len(errs)}")
print(f"max_normalized_pair_wedge_identity_error={max(errs):.16e}")
print(f"L3_density_constant={c_l3:.15f}")
print(f"square_lift_constant={c_square:.15f}")
assert max(errs) < 2e-12
assert abs(c_l3 - 2.620741394208897) < 1e-12
assert abs(c_square - 10.223089667940359) < 1e-12
print("STATUS=PASS")
