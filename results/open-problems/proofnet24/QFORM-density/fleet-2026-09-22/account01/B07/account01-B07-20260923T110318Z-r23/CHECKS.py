import numpy as np

rng = np.random.default_rng(2309231103)
max_ratio = 0.0
violations = 0
for _ in range(20000):
    p = int(rng.integers(1, 8))
    q = int(rng.integers(1, 8))
    B = rng.normal(size=(2, 2))
    U = rng.normal(size=(2, q))
    V = rng.normal(size=(p, 2))
    D = rng.normal(size=(p, q))
    delta = np.linalg.det(B)
    adj = np.array([[B[1, 1], -B[0, 1]], [-B[1, 0], B[0, 0]]])
    T = delta * D - V @ adj @ U
    H = float(np.sum(T * T))
    x2 = float(np.sum(B * B))
    F2 = x2 + float(np.sum(U * U) + np.sum(V * V) + np.sum(D * D))
    rhs = 0.25 * x2 * F2 * F2
    ratio = H / rhs if rhs else 0.0
    max_ratio = max(max_ratio, ratio)
    if H > rhs * (1 + 1e-10):
        violations += 1

print(f"tests=20000 violations={violations} max_ratio={max_ratio:.15f}")
assert violations == 0
print("QFORM_DOUBLEPAIR_EDGE_CHECK_PASS")
