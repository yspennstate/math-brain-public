from fractions import Fraction
from math import comb, factorial


def Bint(a: int, b: int) -> Fraction:
    """Exact beta function B(a,b) for positive integers a,b."""
    return Fraction(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def delta_beta_gini(n: int, k: int) -> Fraction:
    r = n - 1 - k
    return 2 * Bint(n - 1, n - 1) / (Bint(k, k) * Bint(r, r))


def delta_central_binomial(n: int, k: int) -> Fraction:
    r = n - 1 - k
    m = n - 1
    return Fraction(k * r, m) * Fraction(
        comb(2 * k, k) * comb(2 * r, r), comb(2 * m, m)
    )


def delta_direct_beta_binomial(n: int, k: int) -> Fraction:
    """
    Independent direct finite sum from the one-edge event.

    q=1-U.  Root proposes iff A~Bin(n-2,q) has A>=r.
    Opposite endpoint rejects iff B~Bin(n-2,q) has B<=r-1.
    Integrate over q in [0,1] exactly.
    """
    r = n - 1 - k
    N = n - 2
    p = Fraction(0, 1)
    for a in range(r, N + 1):
        for b in range(0, r):
            p += (
                comb(N, a)
                * comb(N, b)
                * Bint(a + b + 1, 2 * N - a - b + 1)
            )
    return (n - 1) * p


def run() -> None:
    count = 0
    for n in range(3, 41):
        for k in range(1, n - 1):
            count += 1
            d_direct = delta_direct_beta_binomial(n, k)
            d_beta = delta_beta_gini(n, k)
            d_cb = delta_central_binomial(n, k)
            assert d_direct == d_beta == d_cb

            r = n - 1 - k
            assert delta_beta_gini(n, k) == delta_beta_gini(n, r)

            if k + 1 <= n - 2:
                ratio = delta_beta_gini(n, k + 1) / delta_beta_gini(n, k)
                expected = Fraction((2 * k + 1) * (r - 1), k * (2 * r - 1))
                assert ratio == expected
                if r > k + 1:
                    assert ratio > 1
                elif r == k + 1:
                    assert ratio == 1
                else:
                    assert ratio < 1

    print("P0458 exact mean-deficit self-check")
    print("checked_all_(n,k)_pairs_n_3_to_40 =", count)
    print("direct_beta_binomial_equals_beta_gini_equals_central_binomial = PASS")
    print("complement_symmetry = PASS")
    print("adjacent_ratio_and_unimodality_sign = PASS")

    for r in (1, 2, 3):
        vals = []
        for n in (max(r + 2, 5), 10, 20):
            k = n - 1 - r
            if 1 <= k <= n - 2:
                vals.append((n, delta_beta_gini(n, k)))
        print("r", r, ":", ", ".join(f"n={n}: delta={d}" for n, d in vals))

    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    run()
