#!/usr/bin/env python3
"""Exact finite certificate for P0282 (Chen's fixed-size LIS log-concavity conjecture).

No floating point and no permutation sampling are used.  Robinson--Schensted gives

    ell[n,k] = sum_{lambda |- n, lambda_1=k} (f^lambda)^2.

The dimensions f^lambda are computed recursively by the exact Young-lattice branching
rule, and the identity sum_lambda (f^lambda)^2 = n! is checked independently at every n.
The program then checks every integer log-concavity margin through N=60.
"""

from fractions import Fraction
from math import factorial

N = 60


def partitions(n, max_part=None):
    """Generate integer partitions of n as nonincreasing tuples."""
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, min(first, n - first)):
            yield (first,) + rest


def predecessor_dimension_sum(lam, previous):
    """Young branching rule f^lambda = sum_{corner boxes c} f^(lambda-c)."""
    total = 0
    length = len(lam)
    for i, a in enumerate(lam):
        nxt = lam[i + 1] if i + 1 < length else 0
        if a > nxt:  # removable corner in row i
            if a == 1 and i == length - 1:
                pred = lam[:-1]
            else:
                pred = lam[:i] + (a - 1,) + lam[i + 1 :]
            total += previous[pred]
    return total


small_expected = {
    1: [1],
    2: [1, 1],
    3: [1, 4, 1],
    4: [1, 13, 9, 1],
    5: [1, 41, 61, 16, 1],
    6: [1, 131, 381, 181, 25, 1],
}

previous = {(): 1}
total_partitions = 0
global_ratio = None
global_record = None
last_ell = None

for n in range(1, N + 1):
    current = {}
    ell = [0] * (n + 1)

    for lam in partitions(n):
        f = predecessor_dimension_sum(lam, previous)
        assert f > 0
        current[lam] = f
        ell[lam[0]] += f * f

    total_partitions += len(current)

    # Independent Plancherel/regular-representation check.
    assert sum(ell) == factorial(n), (n, sum(ell), factorial(n))

    if n in small_expected:
        assert ell[1:] == small_expected[n], (n, ell[1:], small_expected[n])

    # Boundary-defect formulas used in the accompanying written proof.
    assert ell[n] == 1
    if n >= 2:
        assert ell[n - 1] == (n - 1) ** 2
    if n >= 4:
        e2 = (n**4 - 6 * n**3 + 11 * n**2 - 6 * n + 2) // 2
        assert ell[n - 2] == e2
        delta_top = ell[n - 1] ** 2 - ell[n - 2] * ell[n]
        assert 2 * delta_top == n * (n - 2) * (n * n + 1)
    if n >= 6:
        e3 = (
            n**6
            - 12 * n**5
            + 52 * n**4
            - 98 * n**3
            + 79 * n**2
            - 22 * n
            + 6
        ) // 6
        assert ell[n - 3] == e3
        delta_next = ell[n - 2] ** 2 - ell[n - 3] * ell[n - 1]
        poly = (
            n**6
            - 6 * n**5
            + 8 * n**4
            + 12 * n**3
            - 39 * n**2
            + 10 * n
            + 2
        )
        assert 12 * delta_next == n * (n - 2) * poly

    # Source inequalities, all interior k.
    for k in range(2, n):
        delta = ell[k] ** 2 - ell[k - 1] * ell[k + 1]
        assert delta >= 0, (n, k, delta)
        denominator = ell[k - 1] * ell[k + 1]
        if denominator:
            ratio = Fraction(ell[k] ** 2, denominator)
            if global_ratio is None or ratio < global_ratio:
                global_ratio = ratio
                global_record = (
                    n,
                    k,
                    n - k,
                    delta,
                    ell[k - 1],
                    ell[k],
                    ell[k + 1],
                )

    previous = current
    last_ell = ell

assert len(previous) == 966467  # p(60)
assert total_partitions == 6639348  # sum_{n=1}^{60} p(n)
assert global_record is not None

n0, k0, defect0, delta0, em1, e0, ep1 = global_record

print("P0282 exact Robinson-Schensted / Young-branching certificate")
print(f"N_EXACT={N}")
print(f"partitions_at_N={len(previous)}")
print(f"total_partitions_processed={total_partitions}")
print("all_source_log_concavity_margins_nonnegative=True")
print("small_sequence_checks=True")
print("plancherel_factorial_checks=True")
print("boundary_formula_checks=True")
print(f"minimum_relative_ratio_location=(n={n0},k={k0},defect={defect0})")
print(f"minimum_relative_ratio_exact={global_ratio.numerator}/{global_ratio.denominator}")
print(f"minimum_relative_margin_exact={delta0}")
print(f"minimum_relative_ratio_triple=({em1},{e0},{ep1})")
print("scope_guard=finite verification through n=60 only; no all-n closure inferred")
print("ALL_EXACT_CHECKS_PASS")
