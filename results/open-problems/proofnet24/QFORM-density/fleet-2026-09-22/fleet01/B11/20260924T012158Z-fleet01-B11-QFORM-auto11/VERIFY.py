import numpy as np

rng = np.random.default_rng(20260924)

def delta3(M):
    s = np.linalg.svd(np.asarray(M, dtype=float), compute_uv=False)
    s = np.sort(s)[::-1]
    if len(s) < 3:
        return 0.0
    return float(np.prod(s[:3]))

max_right = 0.0
max_left = 0.0
max_bilateral = 0.0

for _ in range(5000):
    beta, sigma, q = np.exp(rng.normal(size=3))
    d, q1, p1 = rng.normal(size=3)
    K = np.array([
        [beta, 0.0, 0.0],
        [d, q1, q],
        [p1, sigma, 0.0],
    ])
    target = beta * sigma * q
    max_right = max(max_right, abs(delta3(K) - target) / target)

    alpha, sigma, p = np.exp(rng.normal(size=3))
    d, q1, p1 = rng.normal(size=3)
    K = np.array([
        [alpha, d, q1],
        [0.0, p1, sigma],
        [0.0, p, 0.0],
    ])
    target = alpha * sigma * p
    max_left = max(max_left, abs(delta3(K) - target) / target)

    sigma, p, q = np.exp(rng.normal(size=3))
    d, q1, p1 = rng.normal(size=3)
    N = np.array([
        [d, q1, q],
        [p1, sigma, 0.0],
        [p, 0.0, 0.0],
    ])
    target = sigma * p * q
    max_bilateral = max(max_bilateral, abs(delta3(N) - target) / target)

A = np.array([
    [1, 1, 0,  1, 0, 0],
    [1, 2, 0,  0, 0, 1],
    [0, 0,-1,  0, 1, 0],
    [1, 0, 0,  2, 0,-1],
    [0, 0, 1,  0,-1, 0],
    [0, 1, 0, -1, 0, 1],
], dtype=float)

evals = np.linalg.eigvalsh(A)
expected = np.array([-2.0, 0.0, 0.0, 0.0, 3.0, 3.0])
assert np.max(np.abs(evals - expected)) < 1e-12
assert np.linalg.matrix_rank(A, tol=1e-10) == 3

K = A[np.ix_([0,1,2], [3,4,5])]
assert abs(np.linalg.det(K) + 1.0) < 1e-12
assert abs(delta3(K) - 1.0) < 1e-12

partner_bound = 3.0

print(f"right-only max relative error: {max_right:.3e}")
print(f"left-only max relative error: {max_left:.3e}")
print(f"bilateral max relative error: {max_bilateral:.3e}")
print("A_* eigenvalues:", " ".join(f"{x:.12g}" for x in evals))
print("rank(A_*):", np.linalg.matrix_rank(A, tol=1e-10))
print("det(K_R):", np.linalg.det(K))
print("Delta_3(K_R):", delta3(K))
print("partner density bound:", partner_bound)

assert max_right < 5e-12
assert max_left < 5e-12
assert max_bilateral < 5e-12

print("QFORM_B11_HUBAUGMENTED_TRICHOTOMY_CHECK_PASS")
