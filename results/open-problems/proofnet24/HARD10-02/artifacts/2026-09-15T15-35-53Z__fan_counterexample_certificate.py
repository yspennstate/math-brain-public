"""
HARD10-02 exact certificate for the fan-family obstruction.

Graph F_m:
  vertices r, x, b, y_1,...,y_m;
  edges r-x, x-b, r-y_i, x-y_i for every i.
Start at x immediately after r->x, so r-x is already reinforced.
Root r is absorbing failure; b is absorbing success.

The report proves:
  h(x)=2/(m+4),
  D_m=(5-m)/((m+4)(m+5)),
where d/dc P_c(success)|_{c=1} = -D_m.
Thus m>=6 gives a positive derivative at c=1 and refutes the proposed
universal finite-graph excursion domination P_c <= P_1.

The full-c transition recursion below supplies an explicit exact
counterexample at m=6, c=4/3.
"""

from fractions import Fraction as Q


def first_order_D(m: int) -> Q:
    return Q(5 - m, (m + 4) * (m + 5))


def srw_escape(m: int) -> Q:
    return Q(2, m + 4)


def fan_escape(m: int, c: Q) -> Q:
    """Exact ORRW target-before-root probability for F_m.

    P_k is the success probability from x when exactly k of the m
    edges x-y_i have already been traversed. At an intermediate y_i,
    the old edge back to x has weight c and the fresh edge to r has
    weight 1, so the walk returns to x with probability c/(c+1).
    """
    P = (c + 1) / ((c + 1) * (c + m + 1) - m)  # k=m
    for k in range(m - 1, -1, -1):
        P = (c + 1 + (m - k) * c * P) / ((c + 1) * (c + m + 1) - k)
    return P


def certificate():
    assert first_order_D(5) == 0
    assert first_order_D(6) == Q(-1, 110)

    m = 6
    c = Q(4, 3)
    p = fan_escape(m, c)
    h = srw_escape(m)
    diff = p - h
    assert h == Q(1, 5)
    assert p == Q(528154735443, 2635499877725)
    assert diff == Q(1054759898, 2635499877725)
    assert diff > 0

    # Correction to the previous parity claim: on a triangle u-v-w-u,
    # the path u->v->w->u->v traverses {u,v} twice in the same
    # direction without a reverse traversal. Edge crossings therefore
    # need not alternate directions on graphs with cycles.

    return {
        "m": m,
        "c": c,
        "srw_escape": h,
        "orrw_escape": p,
        "difference": diff,
        "first_order_D": first_order_D(m),
        "escape_derivative_at_1": -first_order_D(m),
    }


if __name__ == "__main__":
    out = certificate()
    for key, value in out.items():
        print(f"{key}: {value}")
    print("ALL EXACT CHECKS PASSED")
