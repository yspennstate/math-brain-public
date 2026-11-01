#!/usr/bin/env python3
"""Checks for B16 signed noise-square payment / L1 obstruction.

This is support code only; the all-n statements are proved in REPORT.md.
Uses only the Python standard library.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp
import random

def popcount(x):
    return x.bit_count()

def walsh_int(f):
    N = len(f)
    out = []
    for s in range(N):
        tot = 0
        for x, fx in enumerate(f):
            parity = popcount(s & x) & 1
            tot += fx * (-1 if parity else 1)
        out.append(tot)
    return out

def influence_from_k(k):
    N = len(k)
    return sum(Fraction(popcount(s) * k[s] * k[s], N*N) for s in range(N))

def hardy_bank_exact(f):
    """Exact rational form of int_0^1 sum_{U!=0} C_U(rho)^2/(1-rho^2) drho."""
    N = len(f)
    n = N.bit_length() - 1
    k = walsh_int(f)
    a = [Fraction(v, N) for v in k]
    bank = Fraction(0, 1)
    for U in range(1, N):
        K = n - popcount(U)
        q = [Fraction(0, 1) for _ in range(K + 1)]
        for S in range(N):
            j = popcount(S & (~U & (N-1)))
            q[j] += a[S] * a[S ^ U]
        assert sum(q, Fraction(0, 1)) == 0  # Boolean convolution cancellation
        B = []
        run = Fraction(0, 1)
        for j in range(K):  # B_K=0 is omitted
            run += q[j]
            B.append(run)
        for j, bj in enumerate(B):
            for ell, be in enumerate(B):
                m = popcount(U) + j + ell
                bank += Fraction(2, (2*m+1)*(2*m+3)) * bj * be
    return bank, influence_from_k(k)

def pointwise_bank(f, rho):
    N = len(f)
    k = walsh_int(f)
    a = [v/N for v in k]
    C = []
    for U in range(N):
        c = 0.0
        for S in range(N):
            c += a[S]*a[S ^ U]*(rho ** (popcount(S)+popcount(S ^ U)))
        C.append(c)
    Z = C[0]
    I = float(influence_from_k(k))
    lhs = sum(c*c for c in C[1:])
    return lhs, Z*(1-Z), (1-rho*rho)*I

def onepoint_l1_l2(n, rho):
    N = 1 << n
    aa = (1 + rho*rho)/2
    l1 = (4/N)*((1+rho)**n - 1 - (aa+rho)**n + aa**n)
    s = ((1+rho*rho)**n - 1
         - 2*((aa+rho*rho)**n - aa**n)
         + ((aa*aa+rho*rho)**n - aa**(2*n)))
    l2sq = (16/(N*N))*s
    I = 2*n/N
    rhs = (1-rho*rho)*I
    return l1, l2sq, rhs

def main():
    # Exact all-function Hardy-bank checks through n=3.
    exact_cases = 0
    max_exact_ratio = Fraction(0, 1)
    for n in range(1, 4):
        N = 1 << n
        for mask in range(1 << N):
            f = [1 if ((mask >> x) & 1) else -1 for x in range(N)]
            bank, I = hardy_bank_exact(f)
            assert bank <= I
            if I:
                max_exact_ratio = max(max_exact_ratio, bank/I)
            exact_cases += 1

    # Independent pointwise checks, exhaustive n<=3 and deterministic random n=4..6.
    pointwise_cases = 0
    max_pointwise_ratio = 0.0
    rhos = (0.1, 0.25, 0.5, 0.75, 0.9, 0.97)
    rng = random.Random(160021)
    families = []
    for n in range(1, 4):
        N = 1 << n
        families.append((n, [[1 if ((mask >> x) & 1) else -1 for x in range(N)]
                              for mask in range(1 << N)]))
    for n in range(4, 7):
        N = 1 << n
        families.append((n, [[rng.choice((-1,1)) for _ in range(N)] for _ in range(80)]))
    for n, funcs in families:
        for f in funcs:
            for rho in rhos:
                lhs, mid, rhs = pointwise_bank(f, rho)
                assert lhs <= mid + 1e-10
                assert mid <= rhs + 1e-10
                if rhs > 1e-14:
                    max_pointwise_ratio = max(max_pointwise_ratio, lhs/rhs)
                pointwise_cases += 1

    # One-point-defect exact closed form at the natural rho_n=1-1/n scale.
    rows = []
    d = exp(-0.5)-exp(-1.0)
    for n in (8, 12, 16, 20, 30, 40):
        rho = 1 - 1/n
        l1, l2sq, rhs = onepoint_l1_l2(n, rho)
        rows.append({
            "n": n,
            "rho": rho,
            "L1": l1,
            "L2sq": l2sq,
            "rhs": rhs,
            "L1_over_rhs": l1/rhs,
            "L2sq_over_rhs": l2sq/rhs,
        })
    assert abs(rows[-1]["L1"] - 4*d) < 0.01
    assert abs(rows[-1]["L2sq_over_rhs"] - 4*d*d) < 0.02

    print("PASS")
    print("exact_hardy_cases", exact_cases)
    print("max_exact_hardy_ratio", float(max_exact_ratio))
    print("pointwise_cases", pointwise_cases)
    print("max_pointwise_ratio", max_pointwise_ratio)
    print("onepoint_limit_L1", 4*d)
    print("onepoint_limit_L2_ratio", 4*d*d)
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
