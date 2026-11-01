"""Exact rational corroboration for the PROB20-13 C_n^2 theorem.

This script is corroborative, not an independent proof.  It checks the exact
primal/dual identities used in the run report for n=5,...,80, and records the
C_8^2 obstruction to the uniform graph metric being dual-optimal.

No floating-point arithmetic is used.
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
    # d_{C_n^2}=ceil(d_{C_n}/2)
    total = 0
    for a in range(n):
        for b in range(n):
            r = cycle_dist(n, a, b)
            total += (r + 1) // 2
    return F(total, n * n)


def theory_F(n):
    return F(4, 3) * mean_cycle_dist(n)


def expected_step_counts(n):
    """Return stationary product expectations E N_1 and E N_2 exactly."""
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
                # The routing mixes B=N_2 between floor(r/3) and ceil(r/3)
                # so that E B=r/3.  Check that both support values yield
                # valid nonnegative compositions r=N_1+2N_2.
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

    # Closed form for cycle mean distance.
    if n % 2 == 0:
        assert bar == F(n, 4)
        closed = F(n, 3)
    else:
        assert bar == F(n * n - 1, 4 * n)
        closed = F(n * n - 1, 3 * n)

    value = theory_F(n)
    assert value == closed

    # Dual certificate: n edges of each type; capacity 1/(4n).
    cap = F(1, 4 * n)
    dual_norm = n * cap * F(4, 3) + n * cap * F(8, 3)
    assert dual_norm == 1
    dual_obj = F(4, 3) * bar
    assert dual_obj == value

    # Primal aggregate type loads.
    t1, t2 = expected_step_counts(n)
    assert t1 == t2 == bar / 3
    per_edge_load = t1 / n
    primal_congestion = per_edge_load / cap
    assert primal_congestion == value

    # Combinatorial part of the target for n>=6: F <= 2D, while the proof
    # separately establishes tau_rel >= 1 from a nonnegative Fourier mode.
    D = ceil((n // 2) / 2)
    if n >= 6:
        assert value <= 2 * D

    return {
        "n": n,
        "mean_cycle_distance": str(bar),
        "F": str(value),
        "D": D,
        "E_N1": str(t1),
        "E_N2": str(t2),
    }


def main():
    rows = [check_n(n) for n in range(5, 81)]

    # Exact C_8^2 diagnostic against the uniform graph metric.
    n = 8
    f8 = theory_F(n)
    uniform_graph_metric_dual = 2 * mean_square_graph_dist(n)
    assert f8 == F(8, 3)
    assert uniform_graph_metric_dual == F(5, 2)
    assert f8 > uniform_graph_metric_dual

    cn01 = common_neighbors_c8(0, 1)
    cn02 = common_neighbors_c8(0, 2)
    assert cn01 == {2, 7}
    assert cn02 == {1}

    print("exact C_n^2 checks passed for n=5,...,80")
    print("sample rows:")
    for row in rows[:4] + rows[-2:]:
        print(row)
    print("C8^2 exact F:", f8)
    print("C8^2 uniform graph-metric dual value:", uniform_graph_metric_dual)
    print("common neighbors of edge {0,1}:", sorted(cn01))
    print("common neighbors of edge {0,2}:", sorted(cn02))
    print("CHECK PASSED")


if __name__ == "__main__":
    main()
