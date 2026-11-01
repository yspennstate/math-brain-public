#!/usr/bin/env python3
"""Exact rational certificate for the sharpened P05 renewal endpoint error.

For T_r = sum of r iid Geom(1/2) run lengths and A_r=|T_r-2r|,
eta_r=(2r)^(-1) E max(A_r,B_r) with B_r an independent copy.
The finite sum is exact.  The omitted tail is bounded by the decreasing
negative-binomial pmf ratio, so both endpoints below are rigorous rationals.
"""
from fractions import Fraction


def eta_interval_exact(r: int, K: int):
    assert r >= 2 and K >= r

    # Negative-binomial endpoint law:
    # P(T_r=t)=C(t-1,r-1)2^{-t}, t>=r.
    # Start at P(T_r=r)=2^{-r} and use the exact pmf ratio.
    p = {}
    cur = Fraction(1, 2**r)
    p[r] = cur
    for t in range(r, 2*r + K + 1):
        cur *= Fraction(t, 2*(t-r+1))
        p[t+1] = cur

    center = 2*r
    # F=P(A_r<=0).
    F = p[center]
    partial = Fraction(0)

    # E max(A,B)=sum_{k>=1} P(max(A,B)>=k)
    #              =sum_{k>=1} (1-P(A<=k-1)^2).
    for k in range(1, K+1):
        partial += 1 - F*F
        lo = center-k
        hi = center+k
        if lo >= r:
            F += p[lo]
        F += p[hi]

    # If K>=r, A_r>K can only come from the upper tail T_r>2r+K.
    # For t>=t0 the pmf ratio decreases, hence p_{t0+j}<=p_{t0}q^j.
    # Therefore E[(A_r-K)_+] <= p_{t0} sum_{j>=0}(j+1)q^j
    # = p_{t0}/(1-q)^2, and the max tail is at most twice this.
    t0 = 2*r + K + 1
    p0 = p[t0]
    q = Fraction(t0, 2*(t0-r+1))
    tail = 2*p0/(1-q)**2

    lower = partial/Fraction(2*r)
    upper = (partial+tail)/Fraction(2*r)
    return lower, upper, tail/Fraction(2*r)


checks = [
    (100, 100, Fraction(797011737, 10**10)),
    (1000, 1000, Fraction(252285656, 10**10)),
]

for r, K, advertised_upper in checks:
    lo, hi, tail = eta_interval_exact(r, K)
    assert lo <= hi < advertised_upper
    print("r =", r)
    print("K =", K)
    print("eta_lower_decimal =", format(float(lo), ".15f"))
    print("eta_upper_decimal =", format(float(hi), ".15f"))
    print("tail_budget_decimal =", format(float(tail), ".3e"))
    print("certified_upper_decimal =", format(float(advertised_upper), ".10f"))

print("EXACT_RENEWAL_ENDPOINT_MAX_CERTIFICATE_PASS")
