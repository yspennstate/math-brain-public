#!/usr/bin/env python3
"""Exact symbolic self-check for NM13-07 / E0095 C20 short-girth theorem.

The mathematical proof uses the average quotient of the adjacency matrix for
(V(C_g), N(C_g)\V(C_g), rest) around a shortest cycle g<=5 in a cubic graph
on 20 vertices.  This script checks the symbolic factorization and the finite
integer feasibility relaxation exactly; it does not replace the interlacing
argument written in the run report.
"""
import math
import sympy as sp

lam, g, m, x = sp.symbols('lam g m x')

n2 = 20 - g - m
e12 = 3*m - g - 2*x
e22 = 30 - g - 3*m + x

Q = sp.Matrix([
    [2,   1,                         0],
    [g/m, 2*x/m,                     e12/m],
    [0,   e12/n2,                    2*e22/n2],
])

# Cubic degree counting makes every quotient row sum to 3.
for i in range(3):
    assert sp.factor(sum(Q.row(i)) - 3) == 0

cp = sp.factor(Q.charpoly(lam).as_expr())
assert sp.rem(sp.Poly(cp, lam), sp.Poly(lam-3, lam)) == 0
quad = sp.factor(sp.cancel(cp/(lam-3)))
assert sp.Poly(quad, lam).degree() == 2
assert sp.Poly(quad, lam).LC() == 1

# If r>=s are the two non-Perron quotient roots, quad=(lam-r)(lam-s).
# The decisive exact sign at lam=2 is:
expected_at_2 = sp.factor(2*g*(10 - 2*m + x)/(m*(g + m - 20)))
assert sp.factor(quad.subs(lam, 2) - expected_at_2) == 0

feasible = []
strict = []
equality = []
for gg in (3,4,5):
    # Every outside-neighbor vertex can receive at most 3 of the g cycle exits.
    for mm in range(math.ceil(gg/3), gg+1):
        nn2 = 20 - gg - mm
        for xx in range(mm*(mm-1)//2 + 1):
            ee12 = 3*mm - gg - 2*xx
            ee22 = 30 - gg - 3*mm + xx
            if ee12 < 0 or ee22 < 0:
                continue
            # Harmless simple-graph feasibility relaxations.  We prove the sign
            # on this superset, so no realizable shortest-cycle configuration is lost.
            if ee12 > mm*nn2 or ee22 > nn2*(nn2-1)//2:
                continue
            val = sp.Rational(2*gg*(10 - 2*mm + xx), mm*(gg + mm - 20))
            assert val <= 0
            feasible.append((gg,mm,xx,ee12,ee22,val))
            if val < 0:
                strict.append((gg,mm,xx))
            else:
                equality.append((gg,mm,xx))

assert len(feasible) == 31
assert len(strict) == 30
assert equality == [(5,5,0)]

# Previous girth>=6 theorem uses alpha, unique root of p in this rational interval.
z = sp.symbols('z')
p = z**3 + 2*z**2 - 4*z - 7
lo = sp.Rational(9677,5000)
hi = sp.Rational(3871,2000)
assert sp.count_roots(p, lo, hi) == 1
assert hi < 2

print('E0095 C20 SHORT-GIRTH QUOTIENT EXACT SELF-CHECK')
print('charpoly_factor:', cp)
print('nonperron_quadratic:', quad)
print('quadratic_at_2:', expected_at_2)
print('feasible_relaxed_triples:', len(feasible))
print('strict_q2_negative:', len(strict))
print('q2_zero_triples:', equality)
print('alpha_interval_upper_lt_2:', hi, '< 2')
print('CONCLUSION: for every cubic 20-vertex graph with girth <=5, the shortest-cycle quotient has second eigenvalue >=2; hence adjacency lambda2 >=2 > alpha. Combined with the prior exact girth>=6 theorem, the fixed C20 matching optimum is exactly alpha.')
print('ALL_EXACT_CHECKS_PASS')
