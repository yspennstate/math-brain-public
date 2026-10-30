"""Finite sanity checks for QFORM-RELATIVE-NORMALITY-DEFECT-SHIELD-v1.
Not part of the proof.
"""
import numpy as np

rng = np.random.default_rng(20260924)


def invsqrt_psd(G):
    w, V = np.linalg.eigh(G)
    return (V * (w ** -0.5)) @ V.T


def check_random(num=2000):
    worst_gap = -1e100
    violations = 0
    for _ in range(num):
        p, m = 10, 7
        M = rng.normal(size=(p, m))
        N = 2.0 * rng.normal(size=(p, m))
        G = M.T @ M
        Gi = invsqrt_psd(G)
        B = Gi @ M.T @ N @ Gi
        H = 0.5 * (B + B.T)
        K = 0.5 * (B - B.T)
        D = np.eye(m) + H
        rho = 0.7
        w, U = np.linalg.eigh(D)
        Up = U[:, w >= rho]
        Um = U[:, w <= -rho]
        C = Up.T @ K @ Um
        lhs = np.linalg.norm(C, 2) if C.size else 0.0
        nu = np.linalg.norm(B.T @ B - B @ B.T, 2)
        rhs = nu / (4.0 * rho)
        gap = lhs - rhs
        worst_gap = max(worst_gap, gap)
        if gap > 5e-10:
            violations += 1
    return worst_gap, violations


def check_stress():
    R2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
    J4 = np.block([[R2, np.zeros((2, 2))], [np.zeros((2, 2)), R2]])
    J3 = np.array([[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    C = np.vstack([np.eye(3), np.zeros((1, 3))])
    eps = 1.0 / 8.0
    H0 = np.diag([0.0] * 4 + [-2.0] * 3)
    rows = []
    for L in (0.0, 1.0, 10.0, 100.0, 10000.0):
        K = np.block([[L * J4, eps * C], [-eps * C.T, L * J3]])
        B = H0 + K
        nu = np.linalg.norm(B.T @ B - B @ B.T, 2)
        smin = np.linalg.svd(2.0 * (np.eye(7) + B), compute_uv=False)[-1]
        rows.append((L, nu, smin))
        assert abs(nu - 0.5) < 1e-8
        assert smin + 1e-10 >= 1.75
    return rows


if __name__ == "__main__":
    worst_gap, violations = check_random()
    print("random_worst_lhs_minus_rhs", worst_gap)
    print("random_violations", violations)
    for row in check_stress():
        print("stress", row)
