"""Deterministic corroborative checker for PROB20-17 run 2026-09-16T043741Z.

Numerics are not part of the proof. This script checks:
  * the block-orbit spectral-radius lower bound on random complex PSD pairs;
  * the strict n=4 commuting example where the augmented certificate succeeds
    but the earlier pure-power certificate fails;
  * the rank-one overlap-band theorem on clustered non-equiangular frames.
"""

from __future__ import annotations

import itertools
import math
import numpy as np

SEED = 20260916043741
rng = np.random.default_rng(SEED)


def psd(d: int) -> np.ndarray:
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    A = X @ X.conj().T
    nrm = np.linalg.norm(A, 2)
    return A / nrm if nrm else A


def mpow(A: np.ndarray, k: int) -> np.ndarray:
    return np.linalg.matrix_power(A, k)


def rho(A: np.ndarray) -> float:
    vals = np.linalg.eigvals(A)
    return float(np.max(np.abs(vals))) if vals.size else 0.0


def block_ratio(A: np.ndarray, B: np.ndarray, r: int, s: int) -> float:
    a = float(np.linalg.norm(A, 2))
    b = float(np.linalg.norm(B, 2))
    p = float(np.linalg.norm(A @ B, 2))
    if a == 0 or b == 0 or p == 0:
        return math.inf
    gamma = p / (a * b)
    lhs = rho(mpow(A, r) @ mpow(B, s))
    rhs = (a**r) * (b**s) * (gamma ** max(r, s))
    return lhs / rhs


def owner_averages(mats: list[np.ndarray]) -> tuple[float, float]:
    n = len(mats)
    distinct = 0.0
    for sig in itertools.permutations(range(n)):
        W = np.eye(mats[0].shape[0], dtype=complex)
        for j in sig:
            W = W @ mats[j]
        distinct += np.linalg.norm(W, 2)
    distinct /= math.factorial(n)

    repeated = 0.0
    for word in itertools.product(range(n), repeat=n):
        W = np.eye(mats[0].shape[0], dtype=complex)
        for j in word:
            W = W @ mats[j]
        repeated += np.linalg.norm(W, 2)
    repeated /= n**n
    return float(distinct), float(repeated)


def matching_mean_4(gamma: np.ndarray) -> float:
    return float(
        (
            gamma[0, 1] * gamma[2, 3]
            + gamma[0, 2] * gamma[1, 3]
            + gamma[0, 3] * gamma[1, 2]
        )
        / 3.0
    )


def check_block_orbit() -> float:
    minimum = math.inf
    for d in (2, 3, 5):
        for _ in range(60):
            A, B = psd(d), psd(d)
            for n in (4, 5, 6):
                for r in range(1, n):
                    s = n - r
                    minimum = min(minimum, block_ratio(A, B, r, s))
    assert minimum >= 1.0 - 2e-12, minimum
    return minimum


def check_strict_n4_example(t: float = 0.13) -> dict[str, float]:
    n = 4
    mats = []
    for i in range(n):
        diag = np.full(n, t, dtype=float)
        diag[i] = 1.0
        mats.append(np.diag(diag))

    a = np.array([np.linalg.norm(A, 2) for A in mats], dtype=float)
    gamma = np.ones((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            gamma[i, j] = gamma[j, i] = np.linalg.norm(mats[i] @ mats[j], 2) / (a[i] * a[j])

    pure_lower = float(np.sum(a**n) / n**n)
    lhs_upper = matching_mean_4(gamma)
    g = float(gamma[0, 1])
    augmented_lower = float((1.0 + 6.0 * g**2 + 12.0 * g**3) / 64.0)
    L, R = owner_averages(mats)

    assert pure_lower < lhs_upper
    assert lhs_upper <= augmented_lower + 1e-14
    assert L <= R + 1e-14
    return {
        "pure_lower": pure_lower,
        "matching_upper": lhs_upper,
        "augmented_lower": augmented_lower,
        "actual_left": L,
        "actual_right": R,
    }


def rank_one_transfer(scales: np.ndarray, G: np.ndarray) -> tuple[float, float]:
    n = len(scales)
    q = np.sqrt(scales)
    M = np.diag(q) @ G @ np.diag(q)
    repeated = float(np.real(q @ np.linalg.matrix_power(M, n - 1) @ q) / n**n)

    hp = 0.0
    for sig in itertools.permutations(range(n)):
        w = 1.0
        for r in range(n - 1):
            w *= G[sig[r], sig[r + 1]]
        hp += w
    hp /= math.factorial(n)
    distinct = float(np.prod(scales) * hp)
    return distinct, repeated


def clustered_vectors(n: int, d: int, eps: float) -> np.ndarray:
    base = rng.normal(size=d) + 1j * rng.normal(size=d)
    base /= np.linalg.norm(base)
    U = []
    for _ in range(n):
        z = rng.normal(size=d) + 1j * rng.normal(size=d)
        z -= base * np.vdot(base, z)
        zn = np.linalg.norm(z)
        if zn < 1e-14:
            z = np.roll(base, 1)
            z -= base * np.vdot(base, z)
            zn = np.linalg.norm(z)
        z /= zn
        u = base + eps * z
        u /= np.linalg.norm(u)
        U.append(u)
    return np.stack(U, axis=0)


def check_rank_one_band() -> tuple[int, float, float]:
    accepted = 0
    min_margin = math.inf
    min_ratio = math.inf
    for n in (4, 5, 6):
        d = n + 2
        for _ in range(80):
            eps = rng.uniform(0.08, 0.45)
            U = clustered_vectors(n, d, eps)
            G = np.abs(U @ U.conj().T)
            np.fill_diagonal(G, 1.0)
            off = G[~np.eye(n, dtype=bool)]
            gminus = float(np.min(off))
            gplus = float(np.max(off))

            scales = np.exp(rng.uniform(-1.5, 1.5, size=n))
            S = float(np.sum(scales))
            kappa = (S / n) ** n / float(np.prod(scales))
            dminus = (1.0 + (n - 1) * gminus) / n
            rhs = dminus * kappa ** (1.0 / (n - 1))
            if gplus <= rhs:
                accepted += 1
                min_margin = min(min_margin, rhs - gplus)
                L, R = rank_one_transfer(scales, G)
                if L > 0:
                    min_ratio = min(min_ratio, R / L)
                assert L <= R + 2e-12 * max(1.0, R)

    assert accepted > 0
    return accepted, min_margin, min_ratio


def main() -> None:
    block_min = check_block_orbit()
    example = check_strict_n4_example()
    accepted, band_margin, owner_ratio = check_rank_one_band()

    print(f"seed={SEED}")
    print(f"min_block_ratio={block_min:.16g}")
    for k, v in example.items():
        print(f"strict_n4_{k}={v:.16g}")
    print(f"rank_one_band_accepted={accepted}")
    print(f"rank_one_band_min_margin={band_margin:.16g}")
    print(f"rank_one_band_min_owner_ratio={owner_ratio:.16g}")


if __name__ == "__main__":
    main()
