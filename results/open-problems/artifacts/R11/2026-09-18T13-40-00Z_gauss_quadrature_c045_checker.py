#!/usr/bin/env python3
"""
Exact self-check for R11 / I0054 U024 and C045.

This does not prove the general Gaussian-quadrature theorem; the run report gives
that proof. It checks the finite algebraic core with SymPy exact rationals and
quadratic radicals, including the N=9 frozen-equivalence witness.
"""
import math
import sympy as sp

x = sp.symbols("x")
ASSERTIONS = 0

def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not bool(cond):
        raise AssertionError(msg)

# U024 integer complexity formulas:
# M_min(k)=ceil((k-1)/2), r_min(k)=ceil((k-1)/4).
for k in range(2, 501):
    d = k - 2
    M = k // 2
    r = (k + 2) // 4
    check(M == math.ceil((k - 1) / 2), f"M formula k={k}")
    check(r == math.ceil((k - 1) / 4), f"r formula k={k}")
    check(2 * M - 1 >= d, f"Gauss exactness threshold k={k}")
    check(M > d / 2, f"positive-support lower bound k={k}")
    check(2 * r >= M, f"raw-phase orbit capacity k={k}")
    check(2 * (r - 1) < M, f"raw-phase minimality k={k}")

# Exact shifted Gauss-Legendre rules for m=1,2,3.
rules = {
    1: (
        [sp.Rational(1, 2)],
        [sp.Rational(1, 1)],
    ),
    2: (
        [
            (1 - sp.sqrt(sp.Rational(1, 3))) / 2,
            (1 + sp.sqrt(sp.Rational(1, 3))) / 2,
        ],
        [sp.Rational(1, 2), sp.Rational(1, 2)],
    ),
    3: (
        [
            (1 - sp.sqrt(sp.Rational(3, 5))) / 2,
            sp.Rational(1, 2),
            (1 + sp.sqrt(sp.Rational(3, 5))) / 2,
        ],
        [sp.Rational(5, 18), sp.Rational(4, 9), sp.Rational(5, 18)],
    ),
}

for m, (nodes, weights) in rules.items():
    check(sp.simplify(sum(weights) - 1) == 0, f"weight sum m={m}")
    for d in range(0, 2 * m):
        Q = sp.simplify(sum(w * z**d for z, w in zip(nodes, weights)))
        check(Q == sp.Rational(1, d + 1), f"moment exact m={m},d={d}")
    Q2m = sp.simplify(sum(w * z ** (2 * m) for z, w in zip(nodes, weights)))
    check(
        sp.simplify(sp.Rational(1, 2 * m + 1) - Q2m) > 0,
        f"first Gauss miss m={m}",
    )

# C045 at N=9: m=floor(sqrt(9))=3 transformed Gauss nodes,
# compressed by reflection into two raw Bernoulli paintbox phases.
z = (1 - sp.sqrt(sp.Rational(3, 5))) / 2
check(sp.simplify(z * (1 - z) - sp.Rational(1, 10)) == 0, "z(1-z)")
check(
    sp.simplify(sp.Rational(25, 9) * z * (1 - z) - sp.Rational(5, 18))
    == 0,
    "paired raw-phase transformed mass",
)
check(
    sp.simplify(
        2 * sp.Rational(8, 9) * sp.Rational(1, 4) - sp.Rational(4, 9)
    )
    == 0,
    "midpoint raw-phase transformed mass",
)

nodes, weights = rules[3]

def Qpoly(expr):
    return sp.simplify(sum(w * expr.subs(x, z0) for z0, w in zip(nodes, weights)))

def beta_rate(i, j):
    return sp.factorial(i - 1) * sp.factorial(j - 1) / sp.factorial(i + j - 1)

def q(i, j):
    return Qpoly(x ** (i - 1) * (1 - x) ** (j - 1))

# Exact CTCS generator agreement for every specified split on blocks b<=7.
for b in range(2, 8):
    for i in range(1, b):
        j = b - i
        check(sp.simplify(q(i, j) - beta_rate(i, j)) == 0, f"beta b={b},i={i}")

# First deliberate mismatch: degree 6 / block size 8.
q71 = sp.simplify(q(7, 1))
check(q71 == sp.Rational(57, 400), "q(7,1)")
check(sp.Rational(1, 7) - q71 == sp.Rational(1, 2800), "q(7,1) gap")
check(q(1, 1) == 1, "q(1,1)")
check(q(2, 2) == sp.Rational(1, 6), "q(2,2)")

# Exact finite-law separation from the closest earlier quadrature models at N=9.
N = 9
c044_q22 = sp.Rational(2 * N * N + 1, 12 * N * N)
c001_q22 = sp.Rational(N * N - 1, 6 * N * N)
check(c044_q22 == sp.Rational(163, 972), "C044 q22 N=9")
check(sp.Rational(1, 6) - c044_q22 == -sp.Rational(1, 972), "C044 gap")
check(c001_q22 == sp.Rational(40, 243), "C001 q22 N=9")
check(sp.Rational(1, 6) - c001_q22 == sp.Rational(1, 486), "C001 gap")

print(f"ASSERTIONS={ASSERTIONS}")
print("N9_RAW_PHASES=2")
print("N9_EXACT_CTCS_BLOCK_CUTOFF=7")
print(f"N9_Q71={q71}")
print("N9_CTCS_Q71=1/7")
print("N9_Q71_GAP=1/2800")
print("N9_Q22=1/6")
print("C044_N9_Q22=163/972")
print("C001_N9_Q22=40/243")
print("ALL_EXACT_CHECKS_PASS")
