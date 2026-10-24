#!/usr/bin/env python3
"""Exact finite sanity checks for B15 self-XOR dual-slice inequalities.

Analytic theorems are in REPORT.md. This checker exhausts all Boolean functions
through n=4 and verifies the rational parts for every nonzero frequency shift d
and every physical translation x with d·x=1. It also checks the scalar
Hellinger contribution inequalities numerically at high precision.
"""
from fractions import Fraction
import json, math


def fwht_int(vals):
    a = list(map(int, vals))
    h = 1
    N = len(a)
    while h < N:
        for i in range(0, N, 2*h):
            for j in range(i, i+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return a


def parity(z):
    return z.bit_count() & 1


def check_one(n, bits):
    N = 1 << n
    vals = [1 if ((bits >> y) & 1) else -1 for y in range(N)]
    W = fwht_int(vals)
    W2 = [w*w for w in W]
    pair_checks = 0
    singleton_checks = 0
    b_zero_single = 0.0
    qs = []

    for i in range(n):
        disc = sum(vals[y] != vals[y ^ (1 << i)] for y in range(N))
        q = Fraction(min(disc, N-disc), N)
        qs.append(q)

    c0 = Fraction(sum(w2*w2 for w2 in W2), N**4)
    if c0 > 0:
        b_zero_single += float(c0) * math.log2(1.0/float(c0))

    for d in range(1, N):
        signed = sum(W[s] * W[s ^ d] for s in range(N))
        assert signed == 0, ("boolean self-convolution", n, bits, d, signed)

        cnum = sum(W2[s] * W2[s ^ d] for s in range(N))
        anum = sum(abs(W[s] * W[s ^ d]) for s in range(N))
        c = Fraction(cnum, N**4)
        A = Fraction(anum, N**2)
        assert A >= c

        for x in range(1, N):
            if parity(d & x) == 0:
                continue
            disc = sum(vals[y] != vals[y ^ x] for y in range(N))
            qnum = min(disc, N-disc)
            q = Fraction(qnum, N)
            assert cnum <= 2*qnum*qnum*(N-qnum)*N, (
                "collision", n, bits, d, x, c, q)
            assert anum*anum <= 4*qnum*(N-qnum)*N*N, (
                "hellinger", n, bits, d, x, A, q)
            pair_checks += 1

        if d & (d-1) == 0:
            i = d.bit_length()-1
            q = qs[i]
            if c > 0:
                b = float(c) * math.log2(float(A/c))
                assert b <= 2.0*float(q) + 2e-14, (
                    "singleton-B", n, bits, i, b, float(q))
                b_zero_single += b
            singleton_checks += 1

    J = sum(qs, Fraction(0,1))
    if J > 0:
        bound = (2.0 + 2.0/math.log(2.0))*float(J)
        assert b_zero_single <= bound + 5e-13, (
            "zero+singleton", n, bits, b_zero_single, bound)
    else:
        assert abs(b_zero_single) < 1e-14
    return pair_checks, singleton_checks, b_zero_single, float(J)


def main():
    total_functions = 0
    pair_checks = 0
    singleton_checks = 0
    worst_low_ratio = 0.0
    worst_where = None
    per_n = []
    for n in range(1,5):
        N = 1 << n
        fn = 0
        pc = 0
        sc = 0
        for bits in range(1 << N):
            a,b,low,J = check_one(n,bits)
            fn += 1; pc += a; sc += b
            if J > 0 and low/J > worst_low_ratio:
                worst_low_ratio = low/J
                worst_where = [n,bits]
        total_functions += fn; pair_checks += pc; singleton_checks += sc
        per_n.append({"n":n,"functions":fn,"dual_pair_checks":pc,"singleton_checks":sc})
    out = {
        "status":"PASS",
        "scope":"all Boolean truth tables n<=4; every d!=0 and every x with d.x=1",
        "functions":total_functions,
        "dual_pair_checks":pair_checks,
        "singleton_checks":singleton_checks,
        "worst_observed_zero_plus_singleton_B_over_J":worst_low_ratio,
        "worst_where_n_bits":worst_where,
        "analytic_bound_zero_plus_singleton_B_over_J":2.0+2.0/math.log(2.0),
        "per_n":per_n,
        "note":"Finite checks validate implementation only; universal inequalities are proved analytically in REPORT.md."
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
