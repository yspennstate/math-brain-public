import numpy as np

rng = np.random.default_rng(20260921)
max_rel = 0.0
bad_rank = 0

for _ in range(5000):
    sigma = 10.0 ** rng.uniform(-2.0, 2.0)
    p = rng.normal(size=int(rng.integers(1, 5)))
    q = rng.normal(size=int(rng.integers(1, 5)))
    if np.linalg.norm(p) < 1e-12 or np.linalg.norm(q) < 1e-12:
        continue
    d, p1, q1 = rng.normal(size=3)

    # rows: e,u,E0 ; columns: f,v,F0
    N = np.zeros((2 + len(p), 2 + len(q)))
    N[0, 0] = d
    N[0, 1] = q1
    N[0, 2:] = q
    N[1, 0] = p1
    N[1, 1] = sigma
    N[2:, 0] = p

    sv = np.linalg.svd(N, compute_uv=False)
    lhs = float(np.prod(sv[:3]))
    rhs = float(abs(sigma) * np.linalg.norm(p) * np.linalg.norm(q))
    max_rel = max(max_rel, abs(lhs-rhs) / max(1.0, rhs))

    alpha = 10.0 ** rng.uniform(-1.0, 1.0)
    beta = 10.0 ** rng.uniform(-1.0, 1.0)
    # rows: hub,e,u,E0 ; cols: hub,f,v,F0
    B = np.zeros((3 + len(p), 3 + len(q)))
    B[0, 1] = beta
    B[1, 0] = alpha
    B[1, 1] = d
    B[1, 2] = q1
    B[1, 3:] = q
    B[2, 1] = p1
    B[2, 2] = sigma
    B[3:, 1] = p
    sb = np.linalg.svd(B, compute_uv=False)
    rank = int(np.sum(sb > 1e-9 * sb[0]))
    bad_rank += int(rank != 3)

bad_nonzero_pivot = 0
for _ in range(2000):
    a, alpha, beta, sigma, p, q = rng.uniform(0.1, 2.0, size=6)
    d, p1, q1 = rng.normal(size=3)
    B = np.array([
        [a,     beta,  0.0,   0.0],
        [alpha, d,     q1,    q],
        [0.0,   p1,    sigma, 0.0],
        [0.0,   p,     0.0,   0.0],
    ])
    sb = np.linalg.svd(B, compute_uv=False)
    rank = int(np.sum(sb > 1e-10 * sb[0]))
    bad_nonzero_pivot += int(rank != 4)

assert bad_rank == 0
assert bad_nonzero_pivot == 0
assert max_rel < 1e-12
print(f"max_relative_identity_error={max_rel:.3e}")
print("bilateral_zero_pivot_rank3_failures=0/5000")
print("nonzero_pivot_bilateral_rank4_failures=0/2000")
print("QFORM_B11_RANK1_DOUBLELEAK_CHECK_PASS")
