import numpy as np
from statistics import median


def sv(M):
    return np.linalg.svd(M, compute_uv=False)


def schur(A, r):
    B = A[:r, :r]
    C = A[:r, r:]
    D = A[r:, r:]
    return D - C.T @ np.linalg.solve(B, C)


def sym(rng, n):
    Z = rng.normal(size=(n, n))
    return (Z + Z.T) / 2


def stress_packet(rng, n, q):
    E = sym(rng, n)
    if q:
        U, _ = np.linalg.qr(rng.normal(size=(n, q)))
        coeff = rng.choice([-1.0, 1.0], size=q) * 10.0 ** rng.uniform(0, 3, size=q)
        E = E + U @ np.diag(coeff) @ U.T
    return E


def check_schur(N=10000, seed=20260923):
    rng = np.random.default_rng(seed)
    margins = []
    violations = 0
    for _ in range(N):
        n = int(rng.integers(8, 15))
        M = int(rng.integers(2, 5))
        A0 = sym(rng, n)
        Es, Q, Delta = [], 0, 0.0
        for _ in range(M):
            q = int(rng.integers(0, min(3, n - 3) + 1))
            E = stress_packet(rng, n, q)
            Es.append(E)
            Q += q
            s = sv(E)
            Delta += s[q] if q < n else 0.0
        A = A0 + sum(Es)
        r = int(rng.integers(1, min(3, n - 2) + 1))
        if n - r - Q < 1:
            continue
        k = int(rng.integers(1, n - r - Q + 1))
        S = schur(A, r)
        lhs = sv(S)[k - 1]
        rhs = max(0.0, sv(A0)[k + r + Q - 1] - Delta)
        margin = lhs - rhs
        margins.append(margin)
        if margin < -1e-8:
            violations += 1
    return len(margins), violations, min(margins), median(margins)


def check_core(N=10000, seed=20260924):
    rng = np.random.default_rng(seed)
    margins = []
    violations = 0
    for _ in range(N):
        n = int(rng.integers(8, 15))
        h = int(rng.integers(4, n + 1))
        M = int(rng.integers(2, 5))
        A0 = sym(rng, n)
        Es, Q, Delta = [], 0, 0.0
        for _ in range(M):
            q = int(rng.integers(0, min(3, h - 3) + 1))
            E = stress_packet(rng, n, q)
            Es.append(E)
            Q += q
            s = sv(E)
            Delta += s[q] if q < n else 0.0
        if Q > h - 3:
            continue
        A = A0 + sum(Es)
        lhs = sv(A[:h, :h])[2]
        rhs = max(0.0, sv(A0[:h, :h])[2 + Q] - Delta)
        margin = lhs - rhs
        margins.append(margin)
        if margin < -1e-8:
            violations += 1
    return len(margins), violations, min(margins), median(margins)


if __name__ == '__main__':
    print('schur', check_schur())
    print('core ', check_core())
