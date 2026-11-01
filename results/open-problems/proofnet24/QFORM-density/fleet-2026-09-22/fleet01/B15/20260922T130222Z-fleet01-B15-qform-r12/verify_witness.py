import itertools
import math
import numpy as np


def build_A(m: int) -> np.ndarray:
    n = 2 * m + 1
    e0 = np.zeros(n)
    e0[0] = 1.0
    u = np.zeros(n)
    u[1 : m + 1] = 1.0 / math.sqrt(m)
    v = np.zeros(n)
    v[m + 1 : 2 * m + 1] = 1.0 / math.sqrt(m)
    return np.outer(e0, e0) + np.outer(u, u) - np.outer(v, v)


def check(m: int):
    A = build_A(m)
    ev = np.linalg.eigvalsh(A)
    assert np.allclose(ev[[0, -2, -1]], [-1, 1, 1], atol=1e-10)
    assert np.count_nonzero(np.abs(ev) > 1e-10) == 3

    best = 0.0
    inv3 = inv4 = 0
    for k in (3, 4):
        for J in itertools.combinations(range(A.shape[0]), k):
            s = np.linalg.svd(A[np.ix_(J, J)], compute_uv=False)
            if s[-1] > 1e-10:
                if k == 3:
                    inv3 += 1
                else:
                    inv4 += 1
                best = max(best, float(s[-1]))
    assert abs(best - 1.0 / m) < 1e-10
    assert inv3 == m * m
    assert inv4 == 0

    # Exhaust all cuts for modest m. The report gives the exact rank<=2 proof
    # for every m because each cross block is a sum of two rank-one blocks.
    max_cross_rank = None
    if A.shape[0] <= 11:
        max_cross_rank = 0
        n = A.shape[0]
        for mask in range(1, 1 << (n - 1)):
            S = [i for i in range(n) if (mask >> i) & 1]
            T = [i for i in range(n) if i not in S]
            if not S or not T:
                continue
            r = np.linalg.matrix_rank(A[np.ix_(S, T)], tol=1e-10)
            max_cross_rank = max(max_cross_rank, int(r))
        assert max_cross_rank <= 2

    return best, inv3, inv4, max_cross_rank


if __name__ == '__main__':
    for m in (2, 3, 5, 10):
        print(m, check(m))
    print('PASS (finite numerical diagnostic only; analytic proof is in REPORT.md)')
