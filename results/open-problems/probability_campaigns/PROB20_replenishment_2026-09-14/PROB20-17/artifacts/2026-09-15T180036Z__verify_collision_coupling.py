"""PROB20-17 checker for the 2026-09-15T180036Z collision-coupling run.

Proved statement checked numerically (not used as proof): for PSD A,B,
    Q31_pair >= 4(x+y) = 2 Q22_pair - 4 p^2,
where
    p = ||AB||,
    x = ||A^2 B^2||,
    y = ||ABAB||,
    Q22_pair = 2(x+y+p^2).

The script also records diagnostic minima for the still-UNPROVED targets
    x+y >= 2 p^2
and
    x*y >= p^4.
Random tests are corroborative only.
"""

import numpy as np


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_psd(d, rng, complex_=False, spread=7.0):
    if complex_:
        Z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        Q, _ = np.linalg.qr(Z)
        vals = np.exp(rng.uniform(-spread, 0.0, size=d))
        vals /= vals.max()
        return Q @ np.diag(vals) @ Q.conj().T
    Z = rng.normal(size=(d, d))
    Q, _ = np.linalg.qr(Z)
    vals = np.exp(rng.uniform(-spread, 0.0, size=d))
    vals /= vals.max()
    return Q @ np.diag(vals) @ Q.T


def pair_stats(A, B):
    p = opnorm(A @ B)
    x = opnorm(A @ A @ B @ B)
    y = opnorm(A @ B @ A @ B)

    words31 = [
        A @ A @ A @ B,
        A @ A @ B @ A,
        A @ B @ A @ A,
        B @ A @ A @ A,
        B @ B @ B @ A,
        B @ B @ A @ B,
        B @ A @ B @ B,
        A @ B @ B @ B,
    ]
    q31 = sum(opnorm(W) for W in words31)
    q22 = 2.0 * (x + y + p * p)
    return p, x, y, q31, q22


def main():
    rng = np.random.default_rng(20260915)
    minima = {
        "proved_coupling_ratio": float("inf"),
        "conjectural_pair_sum_ratio": float("inf"),
        "conjectural_pair_product_ratio": float("inf"),
    }

    for complex_ in (False, True):
        for d in (2, 3, 4, 6):
            for _ in range(3000):
                A = rand_psd(d, rng, complex_=complex_)
                B = rand_psd(d, rng, complex_=complex_)
                p, x, y, q31, q22 = pair_stats(A, B)

                # Exact bookkeeping identity for the 2+2 layer.
                assert abs(q22 - 2.0 * (x + y + p * p)) <= 1e-12 * max(1.0, q22)

                # New proved Bhatia-Davis consequence.
                assert q31 + 1e-10 >= 4.0 * (x + y)
                assert q31 + 1e-10 >= 2.0 * q22 - 4.0 * p * p

                denom = 2.0 * q22 - 4.0 * p * p
                if denom > 1e-14:
                    minima["proved_coupling_ratio"] = min(
                        minima["proved_coupling_ratio"], q31 / denom
                    )

                # Diagnostics only: these inequalities are NOT proved by this script/report.
                if p > 1e-12:
                    minima["conjectural_pair_sum_ratio"] = min(
                        minima["conjectural_pair_sum_ratio"],
                        (x + y) / (2.0 * p * p),
                    )
                    minima["conjectural_pair_product_ratio"] = min(
                        minima["conjectural_pair_product_ratio"],
                        x * y / (p ** 4),
                    )

    print("diagnostic minima over real/complex PSD tests:")
    for key, value in minima.items():
        print(f"{key}: {value:.16g}")
    print("All proved-coupling diagnostics passed.")
    print("The pair-sum and pair-product ratios are diagnostic only.")


if __name__ == "__main__":
    main()
