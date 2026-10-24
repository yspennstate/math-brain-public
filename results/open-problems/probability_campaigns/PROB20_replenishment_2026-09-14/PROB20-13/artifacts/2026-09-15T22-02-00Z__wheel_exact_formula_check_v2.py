"""Efficient exact-rational checker for the PROB20-13 wheel theorem.

This supersedes the earlier same-run checker only as an execution convenience:
all files remain append-only.  No floating-point arithmetic is used.
"""

from fractions import Fraction as Q


def sum_min(n: int, k: int) -> int:
    """sum_{t=1}^n min(t,k), for positive integers."""
    if k >= n:
        return n * (n + 1) // 2
    return k * (k + 1) // 2 + (n - k) * k


def direct_objective(q: int, k: int) -> Q:
    """Parity-specific dual objective at x=4k/(k+2), y=8/(k+2)."""
    assert q >= 4
    R = q // 2
    assert 1 <= k <= R
    x = Q(4 * k, k + 2)
    hub = Q(3, 8) * x
    scale = Q(8, k + 2)
    if q % 2:
        # (9/(8q)) * sum_{t=1}^R delta_t
        rim = Q(9, 8 * q) * scale * sum_min(R, k)
    else:
        # (9/(16q)) * [2 sum_{t=1}^{R-1} delta_t + delta_R]
        bracket_counts = 2 * sum_min(R - 1, k) + min(R, k)
        rim = Q(9, 16 * q) * scale * bracket_counts
    return hub + rim


def closed_value(q: int, k: int) -> Q:
    return Q(3 * k * (4 * q - 3 * k), 2 * q * (k + 2))


def difference_closed(q: int, k: int) -> Q:
    return Q(3 * (8 * q - 3 * k * k - 15 * k - 6),
             2 * q * (k + 2) * (k + 3))


def predicted_index(q: int) -> int:
    """Smallest k with V(k+1)-V(k)<=0, capped by floor(q/2)."""
    R = q // 2
    k = 1
    while k < R and 3 * k * k + 15 * k + 6 < 8 * q:
        k += 1
    return k


def exact_optimum(q: int):
    R = q // 2
    vals = [(closed_value(q, k), k) for k in range(1, R + 1)]
    best = max(v for v, _ in vals)
    return best, [k for v, k in vals if v == best]


def run_checks(max_q: int = 1000):
    for q in range(4, max_q + 1):
        R = q // 2
        for k in range(1, R + 1):
            assert direct_objective(q, k) == closed_value(q, k), (q, k)
        for k in range(1, R):
            assert closed_value(q, k + 1) - closed_value(q, k) == difference_closed(q, k)
        best, best_ks = exact_optimum(q)
        assert predicted_index(q) in best_ks, (q, predicted_index(q), best_ks)
        assert best < 6

    best37, ks37 = exact_optimum(37)
    assert ks37 == [8]
    assert best37 == Q(744, 185)
    assert best37 > 4

    first = next(q for q in range(4, max_q + 1) if exact_optimum(q)[0] > 4)
    assert first == 37
    assert exact_optimum(4)[0] == Q(15, 8)
    assert exact_optimum(5)[0] == Q(21, 10)

    return {
        "checked_q_through": max_q,
        "first_q_with_F_gt_4": first,
        "F_W38": str(best37),
        "maximizer_q37": ks37,
    }


if __name__ == "__main__":
    print(run_checks())
