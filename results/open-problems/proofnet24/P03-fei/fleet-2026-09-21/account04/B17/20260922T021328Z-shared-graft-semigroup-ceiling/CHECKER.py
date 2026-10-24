from __future__ import annotations

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction as F

PREC = 100
NTERMS = 55
getcontext().prec = 110

ALPHA = F(9, 256)
D0 = F(133, 128)
CAP = F(65218513, 10_000_000)  # 6.5218513
THRESH = D0 * CAP
F7_LOWER = Decimal("6.521850949550448184840160538860511501350329679")

# Exact multiplicities of source-bound nine-bit shared-core Walsh numerator
# classes (A_S,Q_S), inherited from the checked shared-graft construction.
PAIRS = [
    ((-18, -2), 72),
    ((2, 2), 72),
    ((0, 0), 46),
    ((-16, 0), 36),
    ((16, 0), 36),
    ((10, -6), 36),
    ((4, 4), 36),
    ((-4, -4), 36),
    ((-2, -2), 36),
    ((44, -4), 18),
    ((-44, 4), 18),
    ((-6, 10), 18),
    ((38, 6), 12),
    ((114, 2), 9),
    ((8, 8), 9),
    ((-8, -8), 9),
    ((4, -12), 6),
    ((-4, 12), 6),
    ((2, 18), 1),
]


def qbounds(q: F):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = Decimal(q.numerator) / Decimal(q.denominator)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = Decimal(q.numerator) / Decimal(q.denominator)
    return lo, hi


def add(a, b):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] + b[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] + b[1]
    return lo, hi


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def scale_exact(a, r: F):
    if r == 0:
        return Decimal(0), Decimal(0)
    if r < 0:
        return neg(scale_exact(a, -r))
    rb = qbounds(r)
    lows, highs = [], []
    for x in a:
        for y in rb:
            with localcontext() as c:
                c.prec = PREC
                c.rounding = ROUND_FLOOR
                lows.append(x * y)
            with localcontext() as c:
                c.prec = PREC
                c.rounding = ROUND_CEILING
                highs.append(x * y)
    return min(lows), max(highs)


def mulpos(a, b):
    assert a[0] >= 0 and b[0] >= 0
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] * b[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] * b[1]
    return lo, hi


def divpos(a, b):
    assert a[0] >= 0 and b[0] > 0
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] / b[1]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] / b[0]
    return lo, hi


def log_unit(m: F):
    assert F(1) <= m <= F(2)
    if m == 1:
        return Decimal(0), Decimal(0)
    z = qbounds((m - 1) / (m + 1))
    z2 = mulpos(z, z)
    power = z
    s = (Decimal(0), Decimal(0))
    for k in range(NTERMS):
        s = add(s, scale_exact(power, F(1, 2 * k + 1)))
        power = mulpos(power, z2)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        one_minus_z2_lo = Decimal(1) - z2[1]
        lo = Decimal(2) * s[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        rem_hi = Decimal(2) * power[1] / (
            Decimal(2 * NTERMS + 1) * one_minus_z2_lo
        )
        hi = Decimal(2) * s[1] + rem_hi
    return lo, hi


LN2 = log_unit(F(2))
INV_LN2 = divpos((Decimal(1), Decimal(1)), LN2)


def log2_ge1(x: F):
    assert x >= 1
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2) ** e:
        e -= 1
    m = x / (F(2) ** e)
    return add((Decimal(e), Decimal(e)), divpos(log_unit(m), LN2))


def phi_interval(p: F):
    # phi(p)=-p log_2 p for 0<=p<=1.
    if p == 0:
        return Decimal(0), Decimal(0)
    assert 0 < p <= 1
    return scale_exact(log2_ge1(1 / p), p)


def slope_phi_interval(p: F):
    # phi'(p)=log_2(1/p)-1/ln 2.
    assert 0 < p < 1
    return sub(log2_ge1(1 / p), INV_LN2)


def g_interval(b: F):
    # g(b)=-phi(b^2)+16(1-b^2).
    if b == 0:
        return Decimal(16), Decimal(16)
    b2 = b * b
    return add(neg(phi_interval(b2)), qbounds(F(16) * (1 - b2)))


def gprime_interval(b: F):
    # g'(b)=2b(log_2 b^2 +1/ln2 -16).
    assert b > 0
    logb2 = neg(log2_ge1(1 / (b * b)))
    inside = add(add(logb2, INV_LN2), (Decimal(-16), Decimal(-16)))
    return scale_exact(inside, 2 * b)


def k_interval(b: F):
    out = (Decimal(0), Decimal(0))
    for (a, q), mult in PAIRS:
        coeff = F(a, 512) + b * F(q, 512)
        p = coeff * coeff
        out = add(out, scale_exact(phi_interval(p), F(mult)))
    return add(out, scale_exact(g_interval(b), ALPHA))


def tangent_upper(center: F, x: F):
    """
    Rigorous upper interval for the tangent majorant Q_center(x).

    phi is concave in p, hence
       phi(p(x)) <= phi(p0)+phi'(p0)(p(x)-p0).
    At all chosen centers every nonzero-class p0<1/4, so phi'(p0)>0.
    Since p(x) is a square of an affine function, the sum of these
    tangent terms is a convex quadratic in x.  The g-tangent is linear.
    Thus the total Q_center is convex and its maximum on a certified
    interval is attained at an endpoint.

    Also g''(b)=2 log_2(b^2)+6/ln2-32<0 on (0,1], so the g tangent is
    a global upper bound.
    """
    out = (Decimal(0), Decimal(0))
    for (a, q), mult in PAIRS:
        if a == 0 and q == 0:
            continue
        p0 = (F(a, 512) + center * F(q, 512)) ** 2
        px = (F(a, 512) + x * F(q, 512)) ** 2
        assert p0 > 0
        assert p0 < F(1, 4)
        slope = slope_phi_interval(p0)
        assert slope[0] > 0
        term = add(phi_interval(p0), scale_exact(slope, px - p0))
        out = add(out, scale_exact(term, F(mult)))

    gt = add(
        g_interval(center),
        scale_exact(gprime_interval(center), x - center),
    )
    return add(out, scale_exact(gt, ALPHA))


# Rational interval cover of [0,1].  For each row the tangent majorant
# at `center` lies strictly below D0*CAP at both endpoints; convexity
# then certifies the whole row interval.
CERTS = [
    (F(1, 1000), F(0), F(17, 10000)),
    (F(3, 2000), F(17, 10000), F(41, 20000)),
    (F(1, 500), F(41, 20000), F(47, 20000)),
    (F(23, 10000), F(47, 20000), F(129, 50000)),
    (F(1, 400), F(129, 50000), F(139, 50000)),
    (F(27, 10000), F(139, 50000), F(63, 20000)),
    (F(29, 10000), F(63, 20000), F(77, 20000)),
    (F(31, 10000), F(77, 20000), F(3, 625)),
    (F(17, 5000), F(3, 625), F(31, 5000)),
    (F(1, 250), F(31, 5000), F(23, 2500)),
    (F(1, 200), F(23, 2500), F(7, 500)),
    (F(7, 1000), F(7, 500), F(23, 1000)),
    (F(1, 100), F(23, 1000), F(37, 1000)),
    (F(1, 50), F(37, 1000), F(2, 25)),
    (F(1, 20), F(2, 25), F(19, 100)),
    (F(1, 10), F(19, 100), F(9, 25)),
    (F(1, 5), F(9, 25), F(13, 20)),
    (F(2, 5), F(13, 20), F(1)),
]


def main():
    assert sum(mult for _, mult in PAIRS) == 512

    # Global concavity check for g: max_{0<b<=1} g''(b)
    # <= 6/ln2-32 <0.
    g2_upper = scale_exact(INV_LN2, F(6))[1] - Decimal(32)
    assert g2_upper < 0

    threshold_lo = qbounds(THRESH)[0]
    previous = F(0)
    worst_upper = Decimal("-Infinity")
    worst_gap = None
    worst_row = None

    for row, (center, left, right) in enumerate(CERTS):
        assert left == previous
        for endpoint in (left, right):
            upper = tangent_upper(center, endpoint)[1]
            gap = threshold_lo - upper
            assert gap > 0
            if upper > worst_upper:
                worst_upper = upper
                worst_gap = gap
                worst_row = (row, center, endpoint)
        previous = right
    assert previous == 1

    # A near-maximizer probe, not needed for the upper theorem, showing
    # the scalar K/D0 ceiling is tightly localized.
    probe = F(2713295, 10**9)
    probe_ratio = divpos(k_interval(probe), qbounds(D0))

    cap_dec = qbounds(CAP)[0]
    remaining_to_cap = cap_dec - F7_LOWER
    assert remaining_to_cap > 0

    print("PASS")
    print("shared_graft_ratio_cap_lt=6.5218513")
    print("threshold_D0_times_cap=" + str(threshold_lo))
    print("certificate_intervals=" + str(len(CERTS)))
    print("worst_tangent_upper=" + str(worst_upper))
    print("worst_tangent_gap=" + str(worst_gap))
    print(
        "worst_row="
        + str(worst_row[0])
        + ",center="
        + str(worst_row[1])
        + ",endpoint="
        + str(worst_row[2])
    )
    print("probe_K_over_D0_lower=" + str(probe_ratio[0]))
    print("probe_K_over_D0_upper=" + str(probe_ratio[1]))
    print("F7_lower_consumed=" + str(F7_LOWER))
    print("F7_to_shared_graft_cap_gap_lt=" + str(remaining_to_cap))
    print("full_FEI_status=OPEN")
    print("brain_status=WITHOUT_VERIFIED_BRAIN")


if __name__ == "__main__":
    main()
