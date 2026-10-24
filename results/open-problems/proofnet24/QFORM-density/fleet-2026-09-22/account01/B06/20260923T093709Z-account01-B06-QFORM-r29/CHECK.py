# Finite numerical sanity check only; the REPORT.md proofs are exact and do not depend on this file.
import itertools
import numpy as np

rng = np.random.default_rng(1)

def e3_minor(M):
    r, c = M.shape
    ans = 0.0
    for R in itertools.combinations(range(r), 3):
        for C in itertools.combinations(range(c), 3):
            ans += np.linalg.det(M[np.ix_(R, C)]) ** 2
    return ans

ratios = []
for _ in range(100):
    ns, nt = 4, 5
    a = rng.normal(size=nt)
    b = rng.normal(size=ns)
    C = rng.normal(size=(ns, nt))
    M = np.block([[np.zeros((1, 1)), a[None, :]], [b[:, None], C]])
    p = b / np.linalg.norm(b)
    q = a / np.linalg.norm(a)
    CP = (np.eye(ns) - np.outer(p, p)) @ C @ (np.eye(nt) - np.outer(q, q))
    rhs = np.linalg.norm(a) ** 2 * np.linalg.norm(b) ** 2 * np.linalg.norm(CP, 'fro') ** 2
    ratios.append(e3_minor(M) / rhs)

budget_pass = True
worst_slack = float('inf')
for _ in range(100):
    m = 5
    a = rng.normal(size=m)
    lam = rng.normal()
    eps = rng.normal(size=m)
    eps -= a * np.dot(a, eps) / np.dot(a, a)
    b = lam * a + eps
    C = rng.normal(size=(m, m))
    C = (C + C.T) / 2
    A = np.block([[np.zeros((2, 2)), np.vstack([a, b])], [np.column_stack([a, b]), C]])
    u = a / np.linalg.norm(a)
    P = np.eye(m) - np.outer(u, u)
    budget = np.linalg.norm(eps) + np.linalg.norm(P @ C @ P, 2)
    s3 = np.linalg.svd(A, compute_uv=False)[2]
    worst_slack = min(worst_slack, budget - s3)
    budget_pass &= (s3 <= budget + 1e-10)

print('BORDERED_E3_RATIO_MIN', min(ratios))
print('BORDERED_E3_RATIO_MAX', max(ratios))
print('TRANSVERSE_BUDGET_ALL_PASS', budget_pass)
print('TRANSVERSE_BUDGET_MIN_SLACK', worst_slack)
