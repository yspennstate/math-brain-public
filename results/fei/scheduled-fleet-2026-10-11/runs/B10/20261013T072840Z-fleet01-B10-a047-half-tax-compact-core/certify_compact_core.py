#!/usr/bin/env python3
"""Outward-Decimal interval certificate for the two-bit half-tax margin.

Certified rectangle:
    p in [1/64, 49/100], q in [1/100, 99/100].
Every elementary operation and logarithm is evaluated with directed rounding.
Concavity gives an exact range enclosure for binary entropy on an interval.
"""

from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from hashlib import sha256

PREC = 70
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
ZERO, ONE, TWO, FOUR = D(0), D(1), D(2), D(4)
HALF = D(1) / D(2)


def dn(f):
    with localcontext(DOWN):
        return +f()


def up(f):
    with localcontext(UP):
        return +f()


LN2_LO = dn(lambda: TWO.ln())
LN2_HI = up(lambda: TWO.ln())


def add(x, y):
    return dn(lambda: x[0] + y[0]), up(lambda: x[1] + y[1])


def sub(x, y):
    return dn(lambda: x[0] - y[1]), up(lambda: x[1] - y[0])


def mul(x, y):
    lo = [dn(lambda a=a, b=b: a * b) for a in x for b in y]
    hi = [up(lambda a=a, b=b: a * b) for a in x for b in y]
    return min(lo), max(hi)


def div(x, y):
    assert y[0] > 0
    lo = [dn(lambda a=a, b=b: a / b) for a in x for b in y]
    hi = [up(lambda a=a, b=b: a / b) for a in x for b in y]
    return min(lo), max(hi)


def log2_point(x):
    assert x > 0
    llo = dn(lambda: x.ln())
    lhi = up(lambda: x.ln())
    # ln(x) is negative for the only entropy calls, while ratio calls are
    # handled through their positive argument and this generic division.
    vals_lo = [dn(lambda a=a, b=b: a / b) for a in (llo, lhi) for b in (LN2_LO, LN2_HI)]
    vals_hi = [up(lambda a=a, b=b: a / b) for a in (llo, lhi) for b in (LN2_LO, LN2_HI)]
    return min(vals_lo), max(vals_hi)


def h_point(x):
    if x == 0 or x == 1:
        return ZERO, ZERO
    lx = log2_point(x)
    l1 = log2_point(ONE - x)
    a = mul((x, x), lx)
    b = mul((ONE - x, ONE - x), l1)
    z = add(a, b)
    return -z[1], -z[0]


def h_iv(x):
    a, b = x
    ha, hb = h_point(a), h_point(b)
    lo = min(ha[0], hb[0])
    if a <= HALF <= b:
        hi = ONE
    else:
        hi = max(ha[1], hb[1])
    return lo, hi


def s_iv(q):
    a, b = q
    sa = (dn(lambda: FOUR * a * (ONE - a)), up(lambda: FOUR * a * (ONE - a)))
    sb = (dn(lambda: FOUR * b * (ONE - b)), up(lambda: FOUR * b * (ONE - b)))
    lo = min(sa[0], sb[0])
    hi = ONE if a <= HALF <= b else max(sa[1], sb[1])
    return lo, hi


def c_iv(q):
    a, b = q
    return dn(lambda: FOUR * a * a), up(lambda: FOUR * b * b)


def p_one_minus_p(p):
    # p <= 0.49 throughout the certified rectangle, so this is increasing.
    a, b = p
    return dn(lambda: a * (ONE - a)), up(lambda: b * (ONE - b))


def ratio_log_iv(p):
    # log_2((1-p)/p) is decreasing and positive on the rectangle.
    a, b = p
    rb_lo = dn(lambda: (ONE - b) / b)
    ra_hi = up(lambda: (ONE - a) / a)
    return log2_point(rb_lo)[0], log2_point(ra_hi)[1]


def margin_lower(pa, pb, qa, qb):
    p, q = (pa, pb), (qa, qb)
    s, c = s_iv(q), c_iv(q)
    sp = mul(s, p)
    one_minus_sp = (dn(lambda: ONE - sp[1]), up(lambda: ONE - sp[0]))
    z = div(mul(c, p_one_minus_p(p)), one_minus_sp)
    # The exact expression is a conditional Bernoulli probability, hence is
    # in [0,1]. Intersecting a wider dependency enclosure with that known
    # range is a valid interval contraction.
    z = (max(ZERO, z[0]), min(ONE, z[1]))
    assert ZERO <= z[0] <= z[1] <= ONE

    # M=(1-sp)h(z)+sp h(p), J=h(sp)-p h(s).
    M = add(mul(one_minus_sp, h_iv(z)), mul(sp, h_iv(p)))
    J = sub(h_iv(sp), mul(p, h_iv(s)))
    Delta = mul(p, ratio_log_iv(p))
    D_iv = sub(add(M, mul((HALF, HALF), Delta)), J)
    return D_iv[0]


def main():
    p0, p1 = D(1) / D(64), D(49) / D(100)
    q0, q1 = D(1) / D(100), D(99) / D(100)
    stack = [(p0, p1, q0, q1, 0)]
    leaves = 0
    visited = 0
    max_depth = 0
    min_certified = None
    digest = sha256()

    while stack:
        pa, pb, qa, qb, depth = stack.pop()
        visited += 1
        lower = margin_lower(pa, pb, qa, qb)
        if lower > 0:
            leaves += 1
            max_depth = max(max_depth, depth)
            min_certified = lower if min_certified is None else min(min_certified, lower)
            digest.update(f"{pa}|{pb}|{qa}|{qb}|{lower}\n".encode())
            continue
        if depth >= 52:
            raise AssertionError(f"unresolved box at depth {depth}: {(pa,pb,qa,qb,lower)}")

        # Split the larger normalized side. Midpoints are exact Decimals.
        pwidth = dn(lambda: (pb - pa) / (p1 - p0))
        qwidth = dn(lambda: (qb - qa) / (q1 - q0))
        if pwidth >= qwidth:
            mid = (pa + pb) / TWO
            stack.append((pa, mid, qa, qb, depth + 1))
            stack.append((mid, pb, qa, qb, depth + 1))
        else:
            mid = (qa + qb) / TWO
            stack.append((pa, pb, qa, mid, depth + 1))
            stack.append((pa, pb, mid, qb, depth + 1))

    print("B10/A047 outward interval certificate: PASS")
    print("rectangle: p in [1/64,49/100], q in [1/100,99/100]")
    print(f"precision: {PREC} decimal digits with ROUND_FLOOR/ROUND_CEILING")
    print(f"visited boxes: {visited}")
    print(f"accepted leaves: {leaves}")
    print(f"maximum depth: {max_depth}")
    print(f"smallest positive interval lower endpoint: {min_certified}")
    print(f"leaf-certificate sha256: {digest.hexdigest()}")
    print("scope: compact core only; boundary collars and higher arity remain open")


if __name__ == "__main__":
    main()
