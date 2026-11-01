"""Exact-rational checks for the PROB20-13 wheel theorem.

No floating-point arithmetic is used for the mathematical assertions.

For W_{q+1}=K_1 join C_q, q>=4, the report proves

    F(W_{q+1}) = max_{1<=k<=floor(q/2)}
                  3*k*(4*q-3*k)/(2*q*(k+2)).

This script independently checks:
  * the direct parity-specific dual objective at every breakpoint;
  * its reduction to the closed formula above;
  * the exact discrete-difference identity;
  * q=37 has unique maximizer k=8 and F=744/185 > 4;
  * q=37 is the first wheel parameter q>=4 with F>4;
  * all tested finite wheel values are <6;
  * for q>=6, the elementary spectral lower bound tau_rel>=3/2
    is sufficient because F<6.
"""

from fractions import Fraction as Q
from math import isqrt


def breakpoint_x(k: int) -> Q:
    return Q(4 * k, k + 2)


def breakpoint_y(k: int) -> Q:
    return Q(8, k + 2)


def delta(t: int, k: int) -> Q:
    """Weighted rim distance at the k-th breakpoint."""
    return Q(8 * min(t, k), k + 2)


def direct_objective(q: int, k: int) -> Q:
    """Parity-specific dual objective evaluated exactly at breakpoint k."""
    assert q >= 4
    R = q // 2
    assert 1 <= k <= R

    x = breakpoint_x(k)
    hub = Q(3, 8) * x

    if q % 2:  # q=2R+1
        rim = Q(9, 8 * q) * sum((delta(t, k) for t in range(1, R + 1)), Q(0))
    else:      # q=2R
        subtotal = Q(2) * sum((delta(t, k) for t in range(1, R)), Q(0))
        subtotal += delta(R, k)
        rim = Q(9, 16 * q) * subtotal

    return hub + rim


def closed_value(q: int, k: int) -> Q:
    return Q(3 * k * (4 * q - 3 * k), 2 * q * (k + 2))


def difference_closed(q: int, k: int) -> Q:
    """V_q(k+1)-V_q(k), exact closed form."""
    return Q(3 * (8 * q - 3 * k * k - 15 * k - 6),
             2 * q * (k + 2) * (k + 3))


def exact_optimum(q: int):
    vals = [(closed_value(q, k), k) for k in range(1, q // 2 + 1)]
    best_value = max(v for v, _ in vals)
    best_ks = [k for v, k in vals if v == best_value]
    return best_value, best_ks


def ceil_sqrt_rational_root_index(q: int) -> int:
    """One maximizing index from the report's quadratic threshold.

    k = ceil((sqrt(96q+153)-15)/6), capped by floor(q/2).
    Implemented with integer comparisons, no floating point.
    """
    R = q // 2
    # Find the smallest k with 3 k^2 + 15 k + 6 >= 8q.
    k = 1
    while 3 * k * k + 15 * k + 6 < 8 * q:
        k += 1
    return min(R, k)


def run_checks(max_q: int = 5000):
    # Parity-specific objective equals the closed formula.
    for q in range(4, max_q + 1):
        R = q // 2
        for k in range(1, R + 1):
            assert direct_objective(q, k) == closed_value(q, k), (q, k)

        # Exact discrete difference.
        for k in range(1, R):
            lhs = closed_value(q, k + 1) - closed_value(q, k)
            rhs = difference_closed(q, k)
            assert lhs == rhs, (q, k, lhs, rhs)

        # Quadratic threshold returns an actual maximizer.
        best, best_ks = exact_optimum(q)
        k0 = ceil_sqrt_rational_root_index(q)
        assert k0 in best_ks, (q, k0, best_ks)

        # Strict finite upper bound from the proof.
        assert best < 6, (q, best)

    # Exact counterexample to the auxiliary D=2 => F<=4 claim.
    best37, ks37 = exact_optimum(37)
    assert ks37 == [8], ks37
    assert best37 == Q(744, 185), best37
    assert best37 > 4

    # First wheel parameter crossing 4.
    first = None
    for q in range(4, max_q + 1):
        best, _ = exact_optimum(q)
        if best > 4:
            first = q
            break
    assert first == 37, first

    # q=4,5 exact small values quoted in the report.
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
