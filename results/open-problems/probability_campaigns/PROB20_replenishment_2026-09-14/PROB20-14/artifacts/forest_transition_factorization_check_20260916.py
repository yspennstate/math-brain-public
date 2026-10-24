#!/usr/bin/env python3
"""Exact-rational consistency checks for PROB20-14 report 2026-09-16T10:00:30Z.

This is an algebra/indexing certificate only. It does NOT prove the universal
infinite-variance theorem.  The test law is the finite-support critical law
P(xi=0)=1/2, P(xi=1)=1/4, P(xi=3)=1/4.
"""
from fractions import Fraction
from math import sqrt

PI = {0: Fraction(1,2), 1: Fraction(1,4), 3: Fraction(1,4)}
R = Fraction(1,2)  # fractional moment exponent r


def sum_dist(n):
    d = {0: Fraction(1)}
    for _ in range(n):
        nd = {}
        for a, pa in d.items():
            for x, px in PI.items():
                nd[a+x] = nd.get(a+x, Fraction(0)) + pa*px
        d = nd
    return d


_CACHE = {}
def psum(n, s):
    if n not in _CACHE:
        _CACHE[n] = sum_dist(n)
    return _CACHE[n].get(s, Fraction(0))


def forest_total_prob(m, b):
    """P(sum of b iid total progenies = m) by Dwass; m>=b>=1."""
    if m < b or b < 1:
        return Fraction(0)
    return Fraction(b, m) * psum(m, m-b)


def kappa(b, c):
    return Fraction(c, b) * psum(b, c)


def eta(m, b, c):
    den = forest_total_prob(m, b)
    if not den:
        return Fraction(0)
    return psum(b, c) * forest_total_prob(m-b, c) / den


def local_L(m, b, c):
    den = psum(m, m-b)
    if not den:
        return None
    return Fraction(m, m-b) * psum(m-b, m-b-c) / den


def root_R(n, b):
    a = psum(n, n-1)
    return Fraction(n, n-1) * psum(n-1, n-1-b) / a


def level2_R(n, b, c):
    a = psum(n, n-1)
    return Fraction(n, n-1-b) * psum(n-1-b, n-1-b-c) / a


def size_biased_dist():
    return {d: Fraction(d)*p for d,p in PI.items() if d > 0}


def conv(d1, d2):
    out = {}
    for a, pa in d1.items():
        for b, pb in d2.items():
            out[a+b] = out.get(a+b, Fraction(0)) + pa*pb
    return out


def kappa_via_spine(b):
    d = size_biased_dist()
    for _ in range(b-1):
        d = conv(d, PI)
    return d


def check_transition(m, b):
    assert m > b >= 1
    den = forest_total_prob(m,b)
    assert den > 0
    eta_mass = Fraction(0)
    l_mass = Fraction(0)
    for c in range(1, min(3*b, m-b)+1):
        e = eta(m,b,c)
        k = kappa(b,c)
        if e:
            assert k > 0
            L = local_L(m,b,c)
            assert L is not None
            assert e == k*L
            eta_mass += e
        if k:
            L = local_L(m,b,c)
            if L is not None:
                l_mass += k*L
    assert eta_mass == 1, (m,b,eta_mass)
    assert l_mass == 1, (m,b,l_mass)


def check_product(n, b, c):
    # transition from level 1 to level 2: A_1=1, B_1=b, m=n-1
    r1 = root_R(n,b)
    r2 = level2_R(n,b,c)
    L = local_L(n-1,b,c)
    if r1 and r2 and L is not None:
        assert r2 == r1*L, (n,b,c,r1,r2,L)


def check_kappa_spine(b):
    kd = kappa_via_spine(b)
    for c, p in kd.items():
        assert p == kappa(b,c), (b,c,p,kappa(b,c))
    assert sum(kd.values(), Fraction(0)) == 1


def check_normalized_ui_inequality(b, M):
    # Numerical check of report (5.4), r=1/2.
    kd = kappa_via_spine(b)
    lhs = 0.0
    for c, p in kd.items():
        W = (c**0.5)/(1+b**0.5)
        if W > 2*M:
            lhs += float(p)*W
    sb = size_biased_dist()
    tail_x = 0.0
    for x,p in sb.items():
        xr = x**0.5
        if xr > M:
            tail_x += float(p)*xr
    rhs = tail_x + M**(-1.0)  # (1-r)/r=1 for r=1/2
    assert lhs <= rhs + 1e-12, (b,M,lhs,rhs)
    return lhs, rhs


def main():
    # Criticality.
    assert sum(Fraction(x)*p for x,p in PI.items()) == 1

    transition_cases = []
    for m,b in [(8,1),(8,2),(10,2),(12,3),(15,4),(20,5)]:
        if forest_total_prob(m,b):
            check_transition(m,b)
            transition_cases.append((m,b))

    for b in range(1,7):
        check_kappa_spine(b)

    product_cases = 0
    for n in [8,10,12,15,20]:
        for b in range(1, min(5,n-2)):
            if root_R(n,b) == 0:
                continue
            for c in range(1, min(3*b,n-1-b)+1):
                if level2_R(n,b,c):
                    check_product(n,b,c)
                    product_cases += 1

    tail_checks = []
    for b in [1,2,3,5,10]:
        for M in [1.0,2.0,4.0]:
            tail_checks.append((b,M)+check_normalized_ui_inequality(b,M))

    print('ALL_ASSERTIONS_PASSED')
    print('transition_cases=', transition_cases)
    print('product_cases=', product_cases)
    print('kappa_spine_b=1..6 passed')
    print('tail_checks=', tail_checks)


if __name__ == '__main__':
    main()
