#!/usr/bin/env python3
"""Finite diagnostics for account03/B06 r55.

These checks are not proofs. They test the exact pair-pivot identity, the exact-null
principal spectral inequality, and the approximate-null lower bound on fixed-seed
random matrices.
"""
import math
import numpy as np

RNG = np.random.default_rng(20260924)
C0 = 2.0 - math.sqrt(3.0)
C1 = (3.0 + math.sqrt(21.0)) / 2.0
EPS_STAR = C0 / (2.0 * C1)
TAU_STAR = EPS_STAR / math.sqrt(2.0)


def s3(a):
    s = np.linalg.svd(a, compute_uv=False)
    return s[2] if len(s) >= 3 else 0.0


def pair_identity_trials():
    worst = 0.0
    for n in range(4, 10):
        for _ in range(1000):
            b = 1.0 + RNG.random()
            P = np.array([[RNG.uniform(-0.5, 0.5), b],
                          [b, RNG.uniform(-0.5, 0.5)]])
            assert np.linalg.det(P) < 0.0
            r = RNG.normal(size=2)
            a = RNG.normal()
            m = n - 3
            M = RNG.normal(size=(2, m))
            h = RNG.normal(size=m)
            C = RNG.normal(size=(m, m))
            C = (C + C.T) / 2.0
            A = np.block([
                [P, r[:, None], M],
                [r[None, :], np.array([[a]]), h[None, :]],
                [M.T, h[:, None], C],
            ])
            Pinvr = np.linalg.solve(P, r)
            q = np.r_[-Pinvr, 1.0, np.zeros(m)]
            ss = a - r @ Pinvr
            star = h - M.T @ Pinvr
            target = np.r_[np.zeros(2), ss, star]
            worst = max(worst, np.linalg.norm(A @ q - target))
    return worst


def exact_null_trials():
    worst_gap = 0.0
    for n in range(4, 12):
        for _ in range(1000):
            u = np.zeros(n)
            z = RNG.normal(size=3)
            z /= np.linalg.norm(z)
            u[:3] = z
            i = int(np.argmax(np.abs(u)))
            w, V = np.linalg.eigh(np.eye(n) - np.outer(u, u))
            U = V[:, w > 0.5]
            Q, _ = np.linalg.qr(RNG.normal(size=(n - 1, n - 1)))
            ev = np.sign(RNG.normal(size=n - 1)) * (0.1 + 3.0 * RNG.random(n - 1))
            A0 = Q @ np.diag(ev) @ Q.T
            A = U @ A0 @ U.T
            keep = [j for j in range(n) if j != i]
            C = A[np.ix_(keep, keep)]
            lhs = s3(C)
            rhs = (abs(u[i]) ** 2) * s3(A)
            worst_gap = max(worst_gap, rhs - lhs)
    return worst_gap


def approximate_null_trials():
    worst_gap = 0.0
    for n in range(4, 10):
        for _ in range(1000):
            u = np.zeros(n)
            z = RNG.normal(size=3)
            z /= np.linalg.norm(z)
            u[:3] = z
            i = int(np.argmax(np.abs(u)))
            assert abs(u[i]) >= 1.0 / math.sqrt(3.0) - 1e-14
            A = RNG.normal(size=(n, n))
            A = (A + A.T) / 2.0
            scale = s3(A)
            if scale < 1e-10:
                continue
            A /= scale
            eps = np.linalg.norm(A @ u)
            keep = [j for j in range(n) if j != i]
            C = A[np.ix_(keep, keep)]
            rhs = C0 - C1 * eps
            worst_gap = max(worst_gap, rhs - s3(C))
    return worst_gap


if __name__ == "__main__":
    e1 = pair_identity_trials()
    e2 = exact_null_trials()
    e3 = approximate_null_trials()
    print("QFORM_B06_R55_CHECK_PASS")
    print(f"C0={C0:.15g}")
    print(f"C1={C1:.15g}")
    print(f"EPS_STAR={EPS_STAR:.15g}")
    print(f"TAU_STAR={TAU_STAR:.15g}")
    print(f"pair_identity_max_abs_error={e1:.6e}")
    print(f"exact_null_spectral_worst_violation={e2:.6e}")
    print(f"approx_null_spectral_worst_violation={e3:.6e}")
    assert e1 < 1e-10
    assert e2 < 1e-10
    assert e3 < 1e-10
