#!/usr/bin/env python3
"""Exact arithmetic certificate for the five-input endpoint witness."""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
import json
import math

getcontext().prec = 100
D = Decimal
LN2 = D(2).ln()
U_INDEX = 22338
V_INDEX = 38505
U = [1 if (U_INDEX >> r) & 1 else -1 for r in range(16)]
V = [1 if (V_INDEX >> r) & 1 else -1 for r in range(16)]


def walsh(values):
    out = [Fraction(x) for x in values]
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2*step):
            for k in range(base, base+step):
                x, y = out[k], out[k+step]
                out[k], out[k+step] = x+y, x-y
        step *= 2
    return [x/len(out) for x in out]


def upper(values):
    out = list(values)
    n = len(out).bit_length()-1
    for bit in range(n):
        for mask in range(1 << n):
            if not ((mask >> bit) & 1):
                out[mask] += out[mask | (1 << bit)]
    return out


def dec(x):
    return D(x.numerator)/D(x.denominator)


def entropy(atoms, caps=None):
    caps = upper(atoms) if caps is None else caps
    ans = D(0)
    for p, c in zip(atoms, caps):
        if p:
            ans += dec(p)*(dec(c)/dec(p)).ln()/LN2
    return ans


uh = walsh(U)
vh = walsh(V)
a = [(x+y)/2 for x, y in zip(uh, vh)]
b = [(y-x)/2 for x, y in zip(uh, vh)]
b2 = [x*x for x in b]
beta = sum(b2, Fraction())
eb = entropy(b2)


def psi(mu):
    q = mu*mu
    return D(0) if not q else dec(q)*(D(1)/dec(q)).ln()/LN2


def theta(mu):
    alpha2 = 1-mu*mu
    c = [x+mu*y for x, y in zip(a, b)]
    c2 = [x*x for x in c]
    mixed = [x+alpha2*y for x, y in zip(c2, b2)]
    return entropy(c2, upper(mixed))+dec(alpha2)*eb-dec(beta)*psi(mu)


def endpoint_ratio_decimal():
    c = uh
    c2 = [x*x for x in c]
    caps = upper(c2)
    cap_primes = upper([2*x*y for x, y in zip(a, b)])
    qprime = D(0)
    for x, y, cap, cp in zip(c, b, caps, cap_primes):
        if x:
            xd, yd, cd, cpd = dec(x), dec(y), dec(cap), dec(cp)
            qprime += 2*xd*yd*(cd/(xd*xd)).ln()/LN2
            qprime += xd*xd*(cpd/cd-2*yd/xd)/LN2
    tprime = qprime+2*eb-2*dec(beta)/LN2
    tm, tp = theta(Fraction(-1)), theta(Fraction(1))
    slope = tprime+(tm-tp)/2
    return slope/(2*dec(beta)), tprime, tm, tp


endpoint_ratio, tprime, tm, tp = endpoint_ratio_decimal()
finite = []
chosen = None
for n in range(2, 17):
    mu = Fraction(-1)+Fraction(2, 1 << n)
    centered = theta(mu)-(dec(1-mu)*tm+dec(1+mu)*tp)/2
    ratio = centered/(dec(beta)*dec(1-mu*mu))
    finite.append({"child_bits": n, "mu": str(mu), "ratio": str(ratio)})
    if chosen is None and ratio > 4:
        chosen = (n, mu, centered, ratio)

out = {
    "status": "EXACT_RATIONAL_WALSH_PLUS_100_DIGIT_LOG_EVALUATION",
    "u_index": U_INDEX,
    "v_index": V_INDEX,
    "u_truth_table": U,
    "v_truth_table": V,
    "a_exact": [str(x) for x in a],
    "b_exact": [str(x) for x in b],
    "beta_exact": str(beta),
    "theta_minus_one": str(tm),
    "theta_plus_one": str(tp),
    "theta_prime_minus_one": str(tprime),
    "endpoint_ratio": str(endpoint_ratio),
    "endpoint_ratio_minus_4": str(endpoint_ratio-4),
    "finite_point_defects": finite,
    "first_finite_ratio_above_4": None if chosen is None else {
        "child_bits": chosen[0], "mu": str(chosen[1]),
        "centered_theta": str(chosen[2]), "ratio": str(chosen[3]),
        "ratio_minus_4": str(chosen[3]-4),
    },
    "decimal_precision": getcontext().prec,
    "random_seed": None,
}
print(json.dumps(out, indent=2, sort_keys=True))
