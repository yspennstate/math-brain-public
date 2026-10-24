#!/usr/bin/env python3
"""Standard-library checks for B16 arbitrary-residual OR-lift theorem."""
from itertools import combinations
from math import log2, log
import random


def ell(t):
    return 0.0 if t == 0.0 else -t * log2(t)


def ah_formula(r, s):
    q = 2.0 ** (-r)
    M = 2 ** r - 1
    p = q + (1.0-q)*s
    return (ell((1-p)**2) + ell(p*p)
            - (1-q)*(ell((1-s)**2)+ell(s*s))
            + 2*s*(1-s)*(ell((1-q)**2)+M*ell(q*q))
            + 2*M*ell(q*q*(1-s)**2))


def d_formula(r, s):
    q = 2.0 ** (-r)
    return q*(1.0+r*(1.0-s))


def fwht(vals):
    a = [float(v) for v in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    z = float(len(a))
    return [x/z for x in a]


def entropy(vals):
    out = 0.0
    for a in fwht(vals):
        p = a*a
        if p:
            out -= p*log2(p)
    return out


def influences(vals, n):
    N = 1 << n
    out = []
    for k in range(n):
        b = 1 << k
        hit = 0
        for x in range(N):
            if not (x & b) and vals[x] != vals[x | b]:
                hit += 2
        out.append(hit/N)
    return out


def folded_J(vals, n):
    return sum(min(t, 1-t) for t in influences(vals, n))


def gate_parent(r, m, R):
    n = 1+r+m
    vals = []
    for z in range(1 << n):
        x = 1 if (z & 1) else -1
        qhit = all((z >> (1+k)) & 1 for k in range(r))
        w = z >> (1+r)
        vals.append(x if (qhit or w in R) else 1)
    return vals


def gate_child(m, R):
    vals = []
    for z in range(1 << (1+m)):
        x = 1 if (z & 1) else -1
        w = z >> 1
        vals.append(x if w in R else 1)
    return vals


rng = random.Random(160922)
cases = 0
max_err = 0.0
max_ratio = 0.0
for r in range(2, 5):
    q = 2.0**(-r)
    for m in range(1, 5):
        N = 1 << m
        tests = [set()]
        for _ in range(24):
            k = rng.randrange(0, N//3 + 1)
            tests.append(set(rng.sample(range(N), k)))
        for R in tests:
            s = len(R)/N
            p = q+(1-q)*s
            if p > 0.5:
                continue
            P = gate_parent(r, m, R)
            C = gate_child(m, R)
            dH = entropy(P) - (1-q)*entropy(C)
            dJ = folded_J(P, 1+r+m) - (1-q)*folded_J(C, 1+m)
            max_err = max(max_err, abs(dH-ah_formula(r,s)), abs(dJ-d_formula(r,s)))
            if dJ > 0:
                max_ratio = max(max_ratio, dH/dJ)
            cases += 1

assert max_err < 1e-11, max_err

# Direct scalar scan in the theorem's fixed-relative regime.
scan = 0
for r in range(2, 80):
    q = 2.0**(-r)
    smax = q/(16*(1-q))
    for j in range(101):
        s = smax*j/100
        A = ah_formula(r,s)
        D = d_formula(r,s)
        assert A <= 5*D + 1e-13
        scan += 1

# Check the analytic coefficient comparison used in the proof.
Acoef = 2369/512
Bcoef = (17/8 + 1/16 + 4/47)/log(2)
assert Acoef < 5*47/48
assert Bcoef < 5

print("PASS")
print("truth_table_cases", cases)
print("scalar_scan_cases", scan)
print("max_direct_formula_error", max_err)
print("max_unrestricted_small_truth_table_DeltaH_over_D", max_ratio)
print("analytic_qr_coefficient", Acoef)
print("analytic_q_coefficient", Bcoef)
