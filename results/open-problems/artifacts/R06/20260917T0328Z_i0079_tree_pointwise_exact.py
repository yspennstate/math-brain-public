#!/usr/bin/env python3
"""
R06 / I0079 exact-arithmetic certificate for the T4 pointwise-independent
tie refinement one-edge limit.

It checks the shell identities used in the finite-p proof and rigorously
separates the two limiting one-edge cylinder probabilities. All
proof-relevant arithmetic uses fractions.Fraction.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext

THREE = Q(3)

def qceil(x: Q) -> int:
    return (x.numerator + x.denominator - 1) // x.denominator

def exp_neg_bounds(x: Q, extra: int = 80):
    assert x >= 0
    N = max(20, qceil(x) + extra)
    term = Q(1)
    partial = Q(1)
    for k in range(1, N + 1):
        term = term * x / k
        partial += term
    nxt = term * x / (N + 1)
    ratio = x / (N + 2)
    assert ratio < 1
    eup = partial + nxt / (1 - ratio)
    elo = partial
    return Q(1) / eup, Q(1) / elo

def S_bounds(x: Q, extra: int = 80):
    # S(x)=sum_{n>=1} x^n/n! * (1-(3/4)^n)/n
    assert x >= 0
    N = max(30, qceil(x) + extra)
    poisson_term = Q(1)
    qpow = Q(1)
    partial = Q(0)
    for n in range(1, N + 1):
        poisson_term = poisson_term * x / n
        qpow *= Q(3, 4)
        partial += poisson_term * (1 - qpow) / n
    nxt = poisson_term * x / (N + 1)
    ratio = x / (N + 2)
    assert ratio < 1
    return partial, partial + nxt / (1 - ratio)

def g_bounds(lam: Q):
    # g(lam)=exp(-lam/2)H(lam)+exp(-3lam/2)H(3lam)
    # with H(x)=exp(-x)S(x), hence:
    # g=exp(-3lam/2)S(lam)+exp(-9lam/2)S(3lam)
    s1l, s1u = S_bounds(lam)
    e1l, e1u = exp_neg_bounds(Q(3, 2) * lam)
    s3l, s3u = S_bounds(3 * lam)
    e3l, e3u = exp_neg_bounds(Q(9, 2) * lam)
    return e1l*s1l + e3l*s3l, e1u*s1u + e3u*s3u

def geom_exp_tail_upper(c: Q):
    _, ecu = exp_neg_bounds(c)
    _, e2cu = exp_neg_bounds(2*c)
    assert e2cu < 1
    return ecu / (1 - e2cu)

def phase_bounds(a: Q, mlo=-12, mhi=4):
    lo = Q(0); hi = Q(0)
    for m in range(mlo, mhi + 1):
        lam = a * (THREE ** m)
        gl, gu = g_bounds(lam)
        lo += gl; hi += gu
    # m<mlo: H(x)<=x/4 and total g<=lambda.
    hi += a * (THREE ** mlo) / 2
    # m>mhi: H<=1.
    lam0 = a * (THREE ** (mhi + 1))
    hi += geom_exp_tail_upper(lam0 / 2)
    hi += geom_exp_tail_upper(3 * lam0 / 2)
    return lo, hi

def dec(q: Q, places=18):
    getcontext().prec = places + 12
    x = Decimal(q.numerator) / Decimal(q.denominator)
    return f"{x:.{places}f}"

def main():
    # Exact T4 shell identities used in the finite-p decomposition.
    for r in range(1, 13):
        s = 4 * 3**(r-1)
        ball_prev = 2 * 3**(r-1) - 1
        A_r = 3**(r-1)
        B_r = 3**r
        A_r1 = 3**r
        A_r2 = 3**(r+1)
        assert ball_prev == s//2 - 1
        assert A_r == s//4
        assert B_r == 3*s//4
        assert A_r + A_r1 == s
        assert B_r + A_r2 == 3*s

    a1 = Q(27, 100)
    a2 = Q(47, 100)
    l1, u1 = phase_bounds(a1)
    l2, u2 = phase_bounds(a2)
    assert l1 > u2
    gap = l1 - u2

    print("R06-I0079-T4-POINTWISE-TREE-EXACT-01")
    print("shell identities r=1..12: PASS")
    print("all proof-relevant arithmetic: fractions.Fraction")
    print("a1=27/100")
    print("a2=47/100")
    print("L(a1) in [", dec(l1), ",", dec(u1), "]")
    print("L(a2) in [", dec(l2), ",", dec(u2), "]")
    print("certified separation lower(L(a1))-upper(L(a2)) >=", dec(gap))
    print("EXACT_RATIONAL_INTERVALS_DISJOINT")
    print("PASS")

if __name__ == "__main__":
    main()
