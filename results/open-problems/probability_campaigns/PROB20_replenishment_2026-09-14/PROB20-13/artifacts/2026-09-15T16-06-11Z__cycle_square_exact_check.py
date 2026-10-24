"""Exact rational corroboration for the PROB20-13 C_n^2 theorem.

This script is corroborative, not an independent proof. It checks the exact
primal/dual identities in the 2026-09-15T16-03-22Z report for n=5,...,80,
and the C_8^2 obstruction to uniform graph-metric dual optimality.

All mathematical checks use integer/Fraction arithmetic only.
"""

from fractions import Fraction as F
from math import ceil, floor


def cycle_dist(n, a, b):
    d = (b - a) % n
    return min(d, n - d)


def mean_cycle_dist(n):
    total = sum(cycle_dist(n, a, b) for a in range(n) for b in range(n))
    return F(total, n * n)


def mean_square_graph_dist(n):
    total = 0
    for a in range(n):
        for b in range(n):
            r = cycle_dist(n, a, b)
            total += (r + 1) // 2
    return F(total, n * n)


def theory_F(n):
    return F(4, 3) * mean_cycle_dist(n)


def expected_step_counts(n):
    t1 = F(0)
    t2 = F(0)
    pair_mass = F(1, n * n)

    for a in range(n):
        for b in range(n):
            r = cycle_dist(n, a, b)
            if r == 0:
                n1 = n2 = F(0)
            elif r == 1:
                n1, n2 = F(1), F(0)
            elif r == 2:
                n1, n2 = F(0), F(1)
            else:
                lo = floor(F(r, 3))
                hi = ceil(F(r, 3))
                assert hi <= r // 2
                for B in {lo, hi}:
                    assert r - 2 * B >= 0
                p_hi = F(r, 3) - lo if hi != lo else F(0)
                assert F(0) <= p_hi <= F(1)
                n2 = F(r, 3)
                n1 = F(r, 3)

            t1 += pair_mass * n1
            t2 += pair_mass * n2

    return t1, t2


def common_neighbors_c8(a, b):
    n = 8

    def nbrs(x):
        return {(x + 1) % n, (x - 1) % n, (x + 2) % n, (x - 2) % n}

    return nbrs(a) & nbrs(b)


def check_n(n):
    assert n >= 5
    bar = mean_cycle_dist(n)

    if n % 2 == 0:
        assert bar == F(n, 4)
        closed = F(n, 3)
    else:
        assert bar == F(n * n - 1, 4 * n)
        closed = F(n * n - 1, 3 * n)

    value = theory_F(n)
    assert value == closed

    cap = F(1, 4 * n)
    dual_norm = n * cap * F(4, 3) + n * cap * F(8, 3)
    assert dual_norm == 1
    assert F(4, 3) * bar == value

    t1, t2 = expected_step_counts(n)
    assert t1 == t2 == bar / 3
    assert (t1 / n) / cap == value

    # D(C_n^2)=ceil(floor(n/2)/2), computed with integers only.
    half_cycle_diameter = n // 2
    D = (half_cycle_diameter + 1) // 2
    if n >= 6:
        assert value <= 2 * D

    return n, bar, value, D, t1, t2


def main():
    rows = [check_n(n) for n in range(5, 81)]

    f8 = theory_F(8)
    uniform_graph_metric_dual = 2 * mean_square_graph_dist(8)
    assert f8 == F(8, 3)
    assert uniform_graph_metric_dual == F(5, 2)
    assert f8 > uniform_graph_metric_dual

    cn01 = common_neighbors_c8(0, 1)
    cn02 = common_neighbors_c8(0, 2)
    assert cn01 == {2, 7}
    assert cn02 == {1}

    print("exact C_n^2 checks passed for n=5,...,80")
    for row in rows[:4] + rows[-2:]:
        print(row)
    print("C8^2 F =", f8)
    print("C8^2 uniform graph-metric dual =", uniform_graph_metric_dual)
    print("common neighbors {0,1} =", sorted(cn01))
    print("common neighbors {0,2} =", sorted(cn02))
    print("CHECK PASSED")


if __name__ == "__main__":
    main()
