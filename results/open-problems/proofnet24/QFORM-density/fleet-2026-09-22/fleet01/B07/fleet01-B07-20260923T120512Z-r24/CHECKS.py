import numpy as np
import math

rng = np.random.default_rng(0)
viol = 0
min_slack = float('inf')
for _ in range(10000):
    p, q = rng.integers(1, 8, size=2)
    B = rng.normal(size=(2, 2))
    U = rng.normal(size=(2, q))
    V = rng.normal(size=(p, 2))
    D = rng.normal(size=(p, q))
    adj = np.array([[B[1, 1], -B[0, 1]], [-B[1, 0], B[0, 0]]])
    Delta = np.linalg.det(B)
    R = Delta * D - V @ adj @ U
    H = float(np.sum(R * R))
    F2 = float(np.sum(B * B) + np.sum(U * U) + np.sum(V * V) + np.sum(D * D))
    left_u, s, vh = np.linalg.svd(adj, full_matrices=False)
    s1, s2 = s
    pvec = left_u[:, 0]
    qvec = vh[0, :]
    main = s1 * np.linalg.norm(V @ pvec) * np.linalg.norm(qvec @ U)
    rhs = math.sqrt(H) - 0.5 * s2 * F2
    slack = main - rhs
    min_slack = min(min_slack, slack)
    if slack < -1e-10:
        viol += 1

print('tests=10000')
print(f'violations={viol}')
print(f'min_slack={min_slack:.16g}')
print(f'c6={10368**(1/6):.15f}')
print(f'exact_rank3_factor={6*10368**(1/6):.15f}')
print(f'd5_factor={27.388*10368**(1/6):.15f}')
print('STATUS=QFORM_DOUBLEPAIR_SINGULARVALUE_STAR_CHECK_PASS' if viol == 0 else 'STATUS=FAIL')
