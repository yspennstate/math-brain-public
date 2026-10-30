#!/usr/bin/env python3
"""Rigorous continuum certificate for the rare-p half-tax tail.

The directly evaluated margin has a p log(1/p) singularity at p=0.
We first prove that its coefficient A(p,q) is nonnegative and then replace
log(1/p) by log(64) on 0<p<=1/64.  The remaining normalized lower bound is
continuous at p=0.  This program encloses that lower bound on the complete
closed rectangle [0,1/64] x [0,1] using directed Decimal arithmetic.
"""

from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from hashlib import sha256

PREC = 80
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
Z, O, TWO, FOUR, EIGHT = D(0), D(1), D(2), D(4), D(8)
HALF = O / TWO


def dn(f):
    with localcontext(DOWN):
        return +f()


def up(f):
    with localcontext(UP):
        return +f()


def add(x, y):
    return dn(lambda: x[0] + y[0]), up(lambda: x[1] + y[1])


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    lo = [dn(lambda a=a, b=b: a*b) for a in x for b in y]
    hi = [up(lambda a=a, b=b: a*b) for a in x for b in y]
    return min(lo), max(hi)


def div(x, y):
    assert y[0] > 0
    lo = [dn(lambda a=a, b=b: a/b) for a in x for b in y]
    hi = [up(lambda a=a, b=b: a/b) for a in x for b in y]
    return min(lo), max(hi)


def log_point(x):
    assert x > 0
    return dn(lambda: x.ln()), up(lambda: x.ln())


def log_iv(x):
    return log_point(x[0])[0], log_point(x[1])[1]


def square_iv(x):
    a, b = x
    if a <= 0 <= b:
        return Z, max(up(lambda: a*a), up(lambda: b*b))
    vals_lo = [dn(lambda t=t: t*t) for t in (a, b)]
    vals_hi = [up(lambda t=t: t*t) for t in (a, b)]
    return min(vals_lo), max(vals_hi)


def s_iv(q):
    a, b = q
    va = (dn(lambda: FOUR*a*(O-a)), up(lambda: FOUR*a*(O-a)))
    vb = (dn(lambda: FOUR*b*(O-b)), up(lambda: FOUR*b*(O-b)))
    return min(va[0], vb[0]), O if a <= HALF <= b else max(va[1], vb[1])


def c_iv(q):
    a, b = q
    return dn(lambda: FOUR*a*a), up(lambda: FOUR*b*b)


def ell_point(x):
    # ell(x)=-(1-x)log(1-x), continuously extended at 1.
    if x == O:
        return Z, Z
    y = O-x
    l = log_point(y)
    return dn(lambda: -y*l[1]), up(lambda: -y*l[0])


ELL_CRIT_X_LO = dn(lambda: O - (-O).exp())
ELL_CRIT_X_HI = up(lambda: O - (-O).exp())
ELL_CRIT_V_LO = dn(lambda: (-O).exp())
ELL_CRIT_V_HI = up(lambda: (-O).exp())


def ell_iv(x):
    a, b = x
    ea, eb = ell_point(a), ell_point(b)
    lo = min(ea[0], eb[0])
    if a <= ELL_CRIT_X_HI and b >= ELL_CRIT_X_LO:
        hi = ELL_CRIT_V_HI
    else:
        hi = max(ea[1], eb[1])
    return lo, hi


def psi_point(x):
    # psi(x)=ell(x)/x, with psi(0)=1.  It is decreasing on [0,1].
    if x == Z:
        return O, O
    e = ell_point(x)
    return dn(lambda: e[0]/x), up(lambda: e[1]/x)


def psi_iv(x):
    # Monotonicity follows from psi'(x)=(log(1-x)+x)/x^2 <= 0.
    return psi_point(x[1])[0], psi_point(x[0])[1]


INV_E_LO = dn(lambda: (-O).exp())
INV_E_HI = up(lambda: (-O).exp())
PHI_MAX_LO, PHI_MAX_HI = INV_E_LO, INV_E_HI


def phi_point(x):
    # phi(x)=x log(1/x), with phi(0)=0; domain here is [0,4].
    if x == Z:
        return Z, Z
    l = log_point(x)
    return dn(lambda: -x*l[1]), up(lambda: -x*l[0])


def phi_iv(x):
    a, b = x
    fa, fb = phi_point(a), phi_point(b)
    lo = min(fa[0], fb[0])
    if a <= INV_E_HI and b >= INV_E_LO:
        hi = PHI_MAX_HI
    else:
        hi = max(fa[1], fb[1])
    return lo, hi


LN64 = log_point(D(64))


def lower_bound(pa, pb, qa, qb):
    p, q = (pa, pb), (qa, qb)
    om_p = (dn(lambda: O-pb), up(lambda: O-pa))
    s, c = s_iv(q), c_iv(q)
    sp = mul(s, p)
    b = (dn(lambda: O-sp[1]), up(lambda: O-sp[0]))
    a = div(mul(mul(c, p), om_p), b)
    a = (max(Z, a[0]), min(O, a[1]))

    # A=8(q-1/4)^2+p(s-c) is the coefficient of log(1/p).
    qm = (dn(lambda: qa-D(1)/D(4)), up(lambda: qb-D(1)/D(4)))
    A = add(mul((EIGHT, EIGHT), square_iv(qm)), mul(p, sub(s, c)))
    # The separate analytic lemma proves A>=0 on this entire domain.
    A = (max(Z, A[0]), A[1])

    # Stable continuous remainder F.  The identities ell(x)=x psi(x) and
    # b*a/p=c(1-p) remove every 0/0 occurrence at p=0.
    ratio = div(b, om_p)
    F = mul(mul(c, om_p), log_iv(ratio))
    F = add(F, mul(om_p, phi_iv(c)))
    F = add(F, mul(mul(c, om_p), psi_iv(a)))
    F = add(F, mul(mul(s, p), psi_iv(p)))
    F = sub(F, mul(s, psi_iv(sp)))
    F = add(F, ell_iv(s))
    F = add(F, mul((HALF, HALF), log_iv(om_p)))
    return add(mul(A, LN64), F)[0]


def certify():
    p0, p1, q0, q1 = Z, O/D(64), Z, O
    stack = [(p0, p1, q0, q1, 0)]
    visited = leaves = max_depth = 0
    minimum = None
    digest = sha256()
    while stack:
        pa, pb, qa, qb, depth = stack.pop()
        visited += 1
        lo = lower_bound(pa, pb, qa, qb)
        if lo > 0:
            leaves += 1
            max_depth = max(max_depth, depth)
            minimum = lo if minimum is None else min(minimum, lo)
            digest.update(f"{pa}|{pb}|{qa}|{qb}|{lo}\n".encode())
            continue
        if depth >= 60:
            raise AssertionError(f"unresolved box: {pa,pb,qa,qb,depth,lo}")
        # Bisect the larger normalized side.
        pw = dn(lambda: (pb-pa)/(p1-p0))
        qw = dn(lambda: (qb-qa)/(q1-q0))
        if pw >= qw:
            m = (pa+pb)/TWO
            stack.extend([(pa,m,qa,qb,depth+1),(m,pb,qa,qb,depth+1)])
        else:
            m = (qa+qb)/TWO
            stack.extend([(pa,pb,qa,m,depth+1),(pa,pb,m,qb,depth+1)])

    print("B17/A084 normalized rare-tail certificate: PASS")
    print("domain: p in [0,1/64], q in [0,1]")
    print("meaning: E_64=A*ln(64)+F>0, hence D(p,q)>0 for 0<p<=1/64")
    print(f"precision: {PREC} decimal digits, directed ROUND_FLOOR/ROUND_CEILING")
    print(f"visited_boxes={visited}")
    print(f"accepted_leaves={leaves}")
    print(f"maximum_depth={max_depth}")
    print(f"minimum_certified_lower_endpoint={minimum}")
    print(f"leaf_certificate_sha256={digest.hexdigest()}")
    print("uncertified_boxes=0")
    print("floating_point_used_for_sign_decisions=no")


if __name__ == "__main__":
    certify()
