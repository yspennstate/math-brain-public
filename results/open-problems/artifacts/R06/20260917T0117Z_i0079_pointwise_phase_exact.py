#!/usr/bin/env python3
"""
R06 / I0079 exact-arithmetic certificate for phase dependence of the
pointwise-random tie refinement on T_4 x T_4.

All certification inequalities use fractions.Fraction only.
Floating point is not used in any proof-relevant computation.

For the ideal phase with level intensities lambda_m = a*3^m and an edge
(o,w) in the first tree factor, let E={o and w are assigned to the same
Voronoi nucleus} under independent pointwise Uniform tie-breaking.

The proof in the accompanying run report gives
  P_a(E) = sum_{m in Z} g(a*3^m),
  g(lam) = exp(-lam/2) H(lam) + exp(-3*lam/2) H(3*lam),
  H(x) = exp(-x) sum_{n>=1} x^n/n! * (1-(3/4)^n)/n.

Equivalently,
  g(lam) = exp(-3lam/2) S(lam) + exp(-9lam/2) S(3lam),
where S is the positive series without exp(-x).

We certify disjoint intervals for a=27/100 and a=47/100.
"""

from fractions import Fraction as Q
from decimal import Decimal, getcontext

THREE = Q(3)


def qceil(x: Q) -> int:
    return (x.numerator + x.denominator - 1) // x.denominator


def exp_neg_bounds(x: Q, extra: int = 80):
    """Exact rational L <= exp(-x) <= U for x>=0."""
    assert x >= 0
    N = max(20, qceil(x) + extra)
    term = Q(1)
    partial = Q(1)
    for k in range(1, N + 1):
        term = term * x / k
        partial += term
    next_term = term * x / (N + 1)
    ratio = x / (N + 2)
    assert ratio < 1
    # Positive Taylor tail: next_term * (1 + ratio + ratio^2 + ...).
    e_upper = partial + next_term / (1 - ratio)
    e_lower = partial
    # Reciprocals reverse inequalities.
    return Q(1) / e_upper, Q(1) / e_lower


def S_bounds(x: Q, extra: int = 80):
    """
    Exact rational bounds for
      S(x)=sum_{n>=1} x^n/n! * (1-(3/4)^n)/n.
    """
    assert x >= 0
    N = max(30, qceil(x) + extra)
    poisson_term = Q(1)  # x^0/0!
    qpow = Q(1)
    partial = Q(0)
    for n in range(1, N + 1):
        poisson_term = poisson_term * x / n
        qpow *= Q(3, 4)
        partial += poisson_term * (1 - qpow) / n
    # Since 0 <= (1-(3/4)^n)/n <= 1, bound the remaining
    # S-tail by the ordinary exp(x) tail.
    next_term = poisson_term * x / (N + 1)
    ratio = x / (N + 2)
    assert ratio < 1
    tail_upper = next_term / (1 - ratio)
    return partial, partial + tail_upper


def g_bounds(lam: Q):
    s1_l, s1_u = S_bounds(lam)
    e1_l, e1_u = exp_neg_bounds(Q(3, 2) * lam)
    x3 = 3 * lam
    s3_l, s3_u = S_bounds(x3)
    e3_l, e3_u = exp_neg_bounds(Q(9, 2) * lam)
    lower = e1_l * s1_l + e3_l * s3_l
    upper = e1_u * s1_u + e3_u * s3_u
    return lower, upper


def geom_exp_tail_upper(c: Q):
    """
    For c>0:
      sum_{j>=0} exp(-c*3^j)
        <= exp(-c) / (1-exp(-2c)),
    since 3^j >= 1+2j.
    Return a rigorous rational upper bound.
    """
    assert c > 0
    _, e_c_u = exp_neg_bounds(c)
    _, e_2c_u = exp_neg_bounds(2 * c)
    assert e_2c_u < 1
    return e_c_u / (1 - e_2c_u)


def phase_probability_bounds(a: Q, mlo: int = -12, mhi: int = 4):
    lower = Q(0)
    upper = Q(0)
    for m in range(mlo, mhi + 1):
        lam = a * (THREE ** m)
        gl, gu = g_bounds(lam)
        lower += gl
        upper += gu

    # Negative tail m < mlo:
    # H(x) <= x/4 (Bernoulli inequality), hence g(lam)<=lam.
    # sum_{m=-infty}^{mlo-1} a 3^m = a 3^mlo / 2.
    upper += a * (THREE ** mlo) / 2

    # Positive tail m > mhi:
    # H <= 1, so g(lam) <= exp(-lam/2)+exp(-3lam/2).
    lam0 = a * (THREE ** (mhi + 1))
    upper += geom_exp_tail_upper(lam0 / 2)
    upper += geom_exp_tail_upper(3 * lam0 / 2)
    return lower, upper


def dec(q: Q, places=18):
    getcontext().prec = places + 10
    x = Decimal(q.numerator) / Decimal(q.denominator)
    return f"{x:.{places}f}"


def main():
    a1 = Q(27, 100)
    a2 = Q(47, 100)

    # These are admissible phase prefactors:
    # a=(2/3)*3^xi, so 3^xi=3a/2.
    assert 3 * a1 / 2 == Q(81, 200)
    assert 3 * a2 / 2 == Q(141, 200)

    l1, u1 = phase_probability_bounds(a1)
    l2, u2 = phase_probability_bounds(a2)

    assert l1 <= u1 and l2 <= u2
    assert l1 > u2, "phase intervals failed to separate"

    gap = l1 - u2
    print("R06-I0079-POINTWISE-PHASE-01")
    print("all proof-relevant arithmetic: fractions.Fraction")
    print("a1=27/100, corresponding 3^xi1=81/200")
    print("a2=47/100, corresponding 3^xi2=141/200")
    print("P_a1(E) in [", dec(l1), ",", dec(u1), "]")
    print("P_a2(E) in [", dec(l2), ",", dec(u2), "]")
    print("certified separation lower(P_a1)-upper(P_a2) >=", dec(gap))
    print("EXACT_RATIONAL_INTERVALS_DISJOINT")
    print("PASS")


if __name__ == "__main__":
    main()
