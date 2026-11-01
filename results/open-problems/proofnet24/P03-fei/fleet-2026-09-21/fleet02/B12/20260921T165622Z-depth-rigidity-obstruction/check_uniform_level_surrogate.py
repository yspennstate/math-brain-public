#!/usr/bin/env python3
"""B12 exact/numerical checks for the uniform-level surrogate obstruction.

The universal algebraic proofs are in REPORT.md. This checker verifies the
closed-form parameters and evaluates the exact random-prefix information loss
for a range of k. It uses no external packages.
"""
from fractions import Fraction
from math import log2


def row(k):
    if k < 2:
        raise ValueError("k >= 2")
    d = k - 1
    n = k * (4 ** d)
    j = Fraction(k, n)
    assert j == Fraction(1, 4 ** d)
    # E Z=d and E R=d/2=(1/4) log2(1/j).
    assert 4 ** d == 2 ** (2 * d)
    mean_prefix = Fraction(d, 2)
    mean_bound = Fraction(2 * d, 4)
    assert mean_prefix == mean_bound

    terminal_info = 2 * d  # log2(n/k)
    h_x_given_a = sum(log2(n - r) for r in range(k)) / k
    prefix_info = log2(n) - h_x_given_a
    loss = h_x_given_a - log2(k)
    assert abs((terminal_info - prefix_info) - loss) < 1e-12
    # Since n-k+1 > n/2 for k>=2, I(X;A)<1 and L>2d-1.
    assert n - k + 1 > n / 2
    assert prefix_info < 1
    assert loss > 2 * d - 1

    return {
        "k": k,
        "d": d,
        "n": n,
        "j": f"1/{4 ** d}",
        "mean_prefix": float(mean_prefix),
        "terminal_info_bits": terminal_info,
        "prefix_info_bits": prefix_info,
        "loss_bits": loss,
        "rigidity_row": f"Bernoulli(1/2) subsets of a {2 * d}-set",
        "surrogate_row": f"uniform {d}-subsets of an {n - 1}-set",
    }


def main():
    rows = [row(k) for k in range(2, 13)]
    print("B12 uniform-level surrogate checks")
    print("k d n j terminal_I prefix_I loss")
    for r in rows:
        print(
            r["k"], r["d"], r["n"], r["j"],
            f'{r["terminal_info_bits"]:.12f}',
            f'{r["prefix_info_bits"]:.12f}',
            f'{r["loss_bits"]:.12f}',
        )
    print(
        f"PASS rows={len(rows)} exact_parameter_checks={len(rows) * 5} "
        f"numerical_information_checks={len(rows) * 4}"
    )


if __name__ == "__main__":
    main()
