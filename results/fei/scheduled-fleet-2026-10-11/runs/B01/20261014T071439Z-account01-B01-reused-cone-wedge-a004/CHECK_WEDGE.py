#!/usr/bin/env python3
"""Exact parameter-wedge calculation for the mask-10049 cone witness.

Entropy expressions are represented as rational prime exponents.  The code
reconstructs the witness directly from its truth table; it does not import
the B19 checker.
"""
from fractions import Fraction
from math import gcd, log2


def fwht(v):
    a = [Fraction(x) for x in v]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                x, y = a[k], a[k+h]
                a[k], a[k+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


def caps(p):
    a = list(p)
    n = len(a).bit_length()-1
    for i in range(n):
        bit = 1 << i
        for s in range(len(a)):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def factor(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def add_log(expr, weight, ratio):
    for p, e in factor(ratio.numerator).items():
        expr[p] = expr.get(p, Fraction()) + weight*e
    for p, e in factor(ratio.denominator).items():
        expr[p] = expr.get(p, Fraction()) - weight*e


def add(a, b, scale=Fraction(1)):
    out = dict(a)
    for p, e in b.items():
        out[p] = out.get(p, Fraction()) + scale*e
    return {p: e for p, e in out.items() if e}


def scale(a, c):
    return {p: c*e for p, e in a.items() if c*e}


def val(a):
    return sum(float(e)*log2(p) for p, e in a.items())


def uexpr(v):
    p = [x*x for x in fwht(v)]
    c = caps(p)
    out = {}
    for x, y in zip(p, c):
        if x:
            add_log(out, x, y/x)
    return out


def bexpr(v):
    p = [x*x for x in fwht(v)]
    n = len(v).bit_length()-1
    out = {}
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if s & bit:
                continue
            t = p[s] + p[s | bit]
            if p[s]:
                add_log(out, p[s], t/p[s])
            if p[s | bit]:
                add_log(out, p[s | bit], t/p[s | bit])
    return out


def restrict(v, i, bit):
    n = len(v).bit_length()-1
    out = []
    for z in range(1 << (n-1)):
        lo = z & ((1 << i)-1)
        hi = z >> i
        out.append(v[lo | (bit << i) | (hi << (i+1))])
    return tuple(out)


def gexpr(v):
    n = len(v).bit_length()-1
    out = scale(uexpr(v), Fraction(n))
    for i in range(n):
        out = add(out, uexpr(restrict(v, i, 0)), Fraction(-1, 2))
        out = add(out, uexpr(restrict(v, i, 1)), Fraction(-1, 2))
    return out


def iexact(v):
    p = [x*x for x in fwht(v)]
    return sum(Fraction(s.bit_count())*p[s] for s in range(len(p)))


def mult(v, x):
    return tuple(a*(1 if s & (1 << x) else -1) for s, a in enumerate(v))


def activate(v):
    return tuple(v) + tuple(1 for _ in v)


def mexpr(v):
    return add(gexpr(v), bexpr(v), Fraction(-1))


def threshold_parts(v):
    # c_v(eta)=alpha+beta*eta, where L_{c,eta}(v)<=0 iff c>=c_v.
    i = iexact(v)
    u = uexpr(v)
    alpha = scale(add(mexpr(v), u), 1/i)
    beta = scale(u, 1/i)
    return i, u, mexpr(v), alpha, beta


def lcm(a, b):
    return a//gcd(a, b)*b


def exact_sign(expr):
    den = 1
    for e in expr.values():
        den = lcm(den, e.denominator)
    z = {p: int(e*den) for p, e in expr.items()}
    pos = neg = 1
    for p, e in z.items():
        if e > 0:
            pos *= p**e
        elif e < 0:
            neg *= p**(-e)
    return (1 if pos > neg else -1 if pos < neg else 0), den, z, pos.bit_length(), neg.bit_length()


def fmt_expr(e):
    return "{" + ", ".join(f"{p}:{x}" for p, x in sorted(e.items())) + "}"


def main():
    mask = 10049
    q = tuple(1 if mask & (1 << i) else -1 for i in range(16))
    f = activate(mult(q, 3))
    iq, uq, mq, aq, bq = threshold_parts(q)
    iF, uF, mF, aF, bF = threshold_parts(f)

    d0 = add(aF, aq, -1)
    d1 = add(bF, bq, -1)
    # D(eta)=c_F(eta)-c_q(eta)=d0+d1 eta.  Both coefficients
    # are positive, so the failure interval exists for every eta>=0.
    signs = {name: exact_sign(expr) for name, expr in
             (("D0", d0), ("D_slope", d1), ("D_at_eta1", add(d0, d1)))}
    assert signs["D0"][0] > 0 and signs["D_slope"][0] > 0
    assert signs["D_at_eta1"][0] > 0

    eta = Fraction(1, 4)
    cq = add(aq, bq, eta)
    cF = add(aF, bF, eta)
    assert val(cq) < Fraction(7, 4) < val(cF)

    print("status=PASS")
    print("mask=10049")
    print("coordinate=3")
    print(f"I_q={iq}")
    print(f"I_F={iF}")
    print(f"U_q={val(uq):.15f}")
    print(f"M_q={val(mq):.15f}")
    print(f"U_F={val(uF):.15f}")
    print(f"M_F={val(mF):.15f}")
    print(f"U_F_prime_expression={fmt_expr(uF)}")
    print(f"M_F_prime_expression={fmt_expr(mF)}")
    print(f"alpha_F_prime_expression={fmt_expr(aF)}")
    print(f"beta_F_prime_expression={fmt_expr(bF)}")
    print(f"c_q(eta)={val(aq):.15f}+{val(bq):.15f}*eta")
    print(f"c_F(eta)={val(aF):.15f}+{val(bF):.15f}*eta")
    print(f"D(eta)={val(d0):.15f}{val(d1):+.15f}*eta")
    print("wedge_eta_range=eta>=0")
    print(f"c_q(1/4)={val(cq):.15f}")
    print(f"c_F(1/4)={val(cF):.15f}")
    for name, (sgn, den, z, pb, nb) in signs.items():
        print(f"{name}_sign={sgn}")
        print(f"{name}_integer_scale={den}")
        print(f"{name}_prime_exponents={fmt_expr(z)}")
        print(f"{name}_product_bits={pb},{nb}")


if __name__ == "__main__":
    main()
