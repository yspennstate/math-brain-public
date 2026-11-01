import itertools
import math
import numpy as np

C3 = 16 * math.sqrt(30) * 2 ** 0.25
rng = np.random.default_rng(20260922)

print(f"C3={C3:.15f}")
print(f"2C3={2*C3:.15f}")

for K in (3, 4, 7, 12):
    M = rng.normal(size=(K, 3))
    Q, _ = np.linalg.qr(M)
    T = Q.T
    Lambda = np.diag([1.2, -1.7, 2.3])
    C = T.T @ Lambda @ T
    ws = []
    err = 0.0
    for S in itertools.combinations(range(K), 3):
        TS = T[:, S]
        w = float(np.linalg.det(TS) ** 2)
        ws.append(w)
        detC = float(np.linalg.det(C[np.ix_(S, S)]))
        err = max(err, abs(detC - float(np.linalg.det(Lambda)) * w))
    assert abs(sum(ws) - 1) < 1e-12
    assert max(ws) + 1e-12 >= 1 / math.comb(K, 3)
    assert err < 1e-12
    print(
        f"K={K} sum_w={sum(ws):.16f} max_w={max(ws):.16f} "
        f"floor={1/math.comb(K,3):.16f} det_err={err:.3e}"
    )

for m in (1, 2, 5, 20):
    w = m ** -3
    n = m ** 3
    avg = n * w * C3 * w ** (-1 / 3)
    assert abs(n * w - 1) < 1e-12
    assert abs(avg - C3 * m) < 1e-10
    print(
        f"stress m={m} volume_mass={n*w:.16f} "
        f"sampled_cost={C3*m:.12f} bank_bound={2*C3:.12f}"
    )

print("STATUS=PASS")
