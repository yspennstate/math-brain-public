#!/usr/bin/env python3
"""Exact Walsh enumeration plus rational log enclosures for degree <= 2 Boolean functions."""
from fractions import Fraction as F
from functools import lru_cache


class LogExpr:
    # constant + sum_p coeff[p] log_2(p), with p odd prime
    def __init__(self, constant=F(0), coeff=None):
        self.constant = F(constant)
        self.coeff = dict(coeff or {})
        self.coeff = {p: c for p, c in self.coeff.items() if c}

    def __add__(self, other):
        if not isinstance(other, LogExpr):
            other = LogExpr(other)
        d = dict(self.coeff)
        for p, c in other.coeff.items():
            d[p] = d.get(p, F(0)) + c
            if not d[p]:
                del d[p]
        return LogExpr(self.constant + other.constant, d)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return LogExpr(-self.constant, {p: -c for p, c in self.coeff.items()})

    def __mul__(self, q):
        q = F(q)
        return LogExpr(self.constant*q, {p: c*q for p, c in self.coeff.items()})

    __rmul__ = __mul__


def factors(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def log2_fraction(q):
    q = F(q)
    c = F(0)
    d = {}
    for p, e in factors(q.numerator).items():
        if p == 2:
            c += e
        else:
            d[p] = d.get(p, F(0)) + e
    for p, e in factors(q.denominator).items():
        if p == 2:
            c -= e
        else:
            d[p] = d.get(p, F(0)) - e
    return LogExpr(c, d)


@lru_cache(None)
def ln_bounds_int(m, terms=220):
    # ln(m)=2*sum_{k>=0} z^(2k+1)/(2k+1), z=(m-1)/(m+1).
    z = F(m-1, m+1)
    s = F(0)
    zpow = z
    for k in range(terms):
        s += zpow / (2*k+1)
        zpow *= z*z
    lo = 2*s
    # tail <= 2*z^(2N+1)/((2N+1)*(1-z^2))
    tail = 2*zpow / ((2*terms+1)*(1-z*z))
    return lo, lo + tail


LN2_LO, LN2_HI = ln_bounds_int(2)


def bounds(expr):
    num_lo = num_hi = F(0)
    for p, c in expr.coeff.items():
        lo, hi = ln_bounds_int(p)
        if c >= 0:
            num_lo += c*lo; num_hi += c*hi
        else:
            num_lo += c*hi; num_hi += c*lo
    if num_lo >= 0:
        qlo, qhi = num_lo/LN2_HI, num_hi/LN2_LO
    elif num_hi <= 0:
        qlo, qhi = num_lo/LN2_LO, num_hi/LN2_HI
    else:
        qlo, qhi = num_lo/LN2_LO, num_hi/LN2_LO
    return expr.constant + qlo, expr.constant + qhi


def fwht(vals):
    a = [F(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/F(len(a)) for x in a]


def spectral(vals):
    n = (len(vals)).bit_length()-1
    h = fwht(vals)
    p = [x*x for x in h]
    pi = p[:]
    for bit in range(n):
        for s in range(1<<n):
            if not (s>>bit)&1:
                pi[s] += pi[s | (1<<bit)]
    U = LogExpr()
    I = F(0)
    for s, mass in enumerate(p):
        I += s.bit_count()*mass
        if mass:
            U += mass*log2_fraction(pi[s]/mass)
    return h, p, pi, U, I


def restrict(vals, bit, value):
    out = []
    for x in range(len(vals)):
        if ((x>>bit)&1) == value:
            out.append(vals[x])
    return out


def metrics(vals):
    n = len(vals).bit_length()-1
    _, p, _, U, I = spectral(vals)
    H = LogExpr()
    for mass in p:
        if mass:
            H += mass*log2_fraction(1/mass)
    G = n*U
    for i in range(n):
        for value in (0, 1):
            G -= F(1,2)*spectral(restrict(vals, i, value))[3]
    return U, I, G, H


def main():
    n = 4
    size = 1<<n
    cases = equality = positive = 0
    min_pos = None
    min_h_pos = None
    h_equality = 0
    worst_residual_hi = None
    worst_mask = None
    for mask in range(1<<(size-1)):
        vals = [1] + [1 if (mask>>(x-1))&1 else -1 for x in range(1,size)]
        hat, _, _, _, _ = spectral(vals)
        if any(hat[s] and s.bit_count()>2 for s in range(size)):
            continue
        cases += 1
        U, I, G, H = metrics(vals)
        slack = LogExpr(2*I) - G
        lo, hi = bounds(slack)
        assert lo >= 0, (mask, float(lo), float(hi))
        if lo == 0 and hi == 0:
            equality += 1
        elif lo > 0:
            positive += 1
            if min_pos is None or lo < min_pos:
                min_pos = lo
        hslack = LogExpr(2*I) - H
        hlo, hhi = bounds(hslack)
        assert hlo >= 0, ('H', mask, float(hlo), float(hhi))
        if hlo == 0 and hhi == 0:
            h_equality += 1
        elif hlo > 0 and (min_h_pos is None or hlo < min_h_pos):
            min_h_pos = hlo
        # frozen residual R=G-4I-3U/4
        R = G - LogExpr(4*I) - F(3,4)*U
        rlo, rhi = bounds(R)
        assert rhi <= 0
        if worst_residual_hi is None or rhi > worst_residual_hi:
            worst_residual_hi = rhi; worst_mask = mask
    assert cases == 111
    print('claim=B11-A052-DEGREE-TWO-EXTREMAL-v1')
    print('verdict=PASS_EXACT_INTERVAL_CERTIFICATE')
    print('n4_signs_mod_output_degree_le_2', cases)
    print('exact_equality_cases_G_eq_2I', equality)
    print('strict_cases_G_lt_2I', positive)
    print('minimum_positive_slack_lower', float(min_pos))
    print('exact_equality_cases_H_eq_2I', h_equality)
    print('minimum_positive_H_slack_lower', float(min_h_pos))
    print('maximum_frozen_residual_upper', float(worst_residual_hi))
    print('maximum_frozen_residual_mask', worst_mask)
    print('all_dimensional_extension=Nisan-Szegedy_degree_2_junta_at_most_4')
    print('conclusion=degree_le_2_implies_G_le_2I')
    print('direct_FEI_conclusion=degree_le_2_implies_H_le_2I')
    print('minimal_positive_residual_counterexample_has_degree_at_least_3')
    print('universal_GU=OPEN')


if __name__ == '__main__':
    main()
