"""Exact symbolic checks for PROB20-05 checkpoint 2026-09-15T16-01-37Z.

Checks:
- one-sided truncated-triangular Gini/height ratio <= 2/5;
- crossing-interval universal ratio <= 7/10 via exact Bernstein coefficients;
- crossing-interval ratio <= 2/3 when one endpoint-depth <=1/2;
- m=3 displacement statistics;
- exact n=3 three-cycle endpoint value J=13/81.

This is a reproducibility/self-check artifact, not independent verification.
"""

import itertools
import sympy as sp

A, B, r = sp.symbols("A B r", nonnegative=True)
u, v = sp.symbols("u v", real=True)
x, y = sp.symbols("x y", real=True)


def bernstein_coeffs(poly_expr, vars_, degrees):
    x0, y0 = vars_
    n, m = degrees
    poly = sp.Poly(sp.expand(poly_expr), x0, y0)
    out = [[sp.Rational(0) for _ in range(m + 1)] for __ in range(n + 1)]
    for (i, j), aij in poly.terms():
        for k in range(i, n + 1):
            for l in range(j, m + 1):
                out[k][l] += (
                    aij
                    * sp.binomial(k, i) / sp.binomial(n, i)
                    * sp.binomial(l, j) / sp.binomial(m, j)
                )
    return [[sp.factor(c) for c in row] for row in out]


# 1. One-sided truncated triangular law.
# After scaling, density is 2w/(1-r^2), r<=w<=1.
C = 2 / (1 - r**2)
H_one = sp.simplify(C * sp.integrate(u**2, (u, r, 1)))
G_one = sp.simplify(
    2 * C**2 * sp.integrate(
        sp.integrate((u - v) * u * v, (v, r, u)),
        (u, r, 1),
    )
)
ratio_one = sp.factor(G_one / H_one)
assert ratio_one == -2 * (r - 1) * (r**2 + 3*r + 1) / (
    5 * (r + 1) * (r**2 + r + 1)
)
deficit_one = sp.factor(sp.Rational(2, 5) - ratio_one)
assert deficit_one == 4 * r**2 * (r + 2) / (
    5 * (r + 1) * (r**2 + r + 1)
)


# 2. Crossing support [-A,B], triangular density proportional to 1-|u|.
L = sp.simplify(A - A**2 / 2 + B - B**2 / 2)
Hnum = sp.integrate((1 + u)**2, (u, -A, 0)) + sp.integrate((1 - u)**2, (u, 0, B))
H = sp.simplify(Hnum / L)

Gneg = 2 * sp.integrate(
    sp.integrate((u - v) * (1 + u) * (1 + v), (v, -A, u)),
    (u, -A, 0),
)
Gpos = 2 * sp.integrate(
    sp.integrate((u - v) * (1 - u) * (1 - v), (v, 0, u)),
    (u, 0, B),
)
Gcross = 2 * sp.integrate(
    sp.integrate((u - v) * (1 - u) * (1 + v), (v, -A, 0)),
    (u, 0, B),
)
G = sp.factor((Gneg + Gpos + Gcross) / L**2)

# Universal G/H <= 7/10.
F710 = sp.factor(7 * H - 10 * G)
num710, den710 = sp.together(F710).as_numer_denom()
Q710 = sp.expand(num710 / 2)
assert sp.simplify(F710 - 2 * Q710 / den710) == 0
bc710 = bernstein_coeffs(Q710, (A, B), (5, 5))
expected710 = [
    [0, 0, sp.Rational(21,5), sp.Rational(43,10), 3, 3],
    [0, sp.Rational(84,25), sp.Rational(423,50), sp.Rational(202,25), 6, 6],
    [sp.Rational(21,5), sp.Rational(423,50), sp.Rational(651,50), sp.Rational(1147,100), sp.Rational(42,5), sp.Rational(42,5)],
    [sp.Rational(43,10), sp.Rational(202,25), sp.Rational(1147,100), sp.Rational(43,5), sp.Rational(23,5), sp.Rational(23,5)],
    [3, 6, sp.Rational(42,5), sp.Rational(23,5), 0, 0],
    [3, 6, sp.Rational(42,5), sp.Rational(23,5), 0, 0],
]
assert bc710 == expected710
assert all(c >= 0 for row in bc710 for c in row)
assert sp.simplify((G/H).subs({A:1,B:1}) - sp.Rational(7,10)) == 0

# Stronger G/H <= 2/3 when A<=1/2.
F23 = sp.factor(2 * H - 3 * G)
num23, den23 = sp.together(F23).as_numer_denom()
Q23 = sp.expand(num23.subs({A:x/2, B:y}) / 4)
bc23 = bernstein_coeffs(Q23, (x, y), (5, 5))
expected23 = [
    [0, 0, 3, 3, 2, 2],
    [0, sp.Rational(6,5), sp.Rational(9,2), sp.Rational(43,10), 3, 3],
    [sp.Rational(3,4), sp.Rational(27,10), sp.Rational(483,80), sp.Rational(441,80), sp.Rational(31,8), sp.Rational(31,8)],
    [sp.Rational(3,2), sp.Rational(77,20), sp.Rational(563,80), sp.Rational(489,80), sp.Rational(33,8), sp.Rational(33,8)],
    [2, sp.Rational(9,2), sp.Rational(297,40), sp.Rational(243,40), sp.Rational(15,4), sp.Rational(15,4)],
    [sp.Rational(9,4), sp.Rational(19,4), sp.Rational(59,8), sp.Rational(45,8), 3, 3],
]
assert bc23 == expected23
assert all(c >= 0 for row in bc23 for c in row)


# 3. Displacement statistic D(sigma) for m=3.
def D_perm(p):
    m = len(p)
    ds = sorted(sp.Integer(j - p[j]) for j in range(m))
    mus = [sp.Rational(2*l + 1 - m, m) for l in range(m)]
    return sp.simplify(sum(d * mu for d, mu in zip(ds, mus)))

D_table = {p: D_perm(p) for p in itertools.permutations(range(3))}
assert D_table[(0,1,2)] == 0
assert D_table[(0,2,1)] == sp.Rational(4,3)
assert D_table[(1,0,2)] == sp.Rational(4,3)
assert D_table[(1,2,0)] == 2
assert D_table[(2,0,1)] == 2
assert D_table[(2,1,0)] == sp.Rational(8,3)


# 4. Exact endpoint certificate for n=3 three-cycles.
def psi(k):
    k = abs(int(k))
    if k == 0:
        return sp.Rational(2,3)
    if k == 1:
        return sp.Rational(13,12)
    return sp.Integer(k)


def J_shuffle(p):
    n = len(p)
    total = sp.Rational(0)
    for i in range(n):
        for j in range(n):
            d = i-j
            e = p[i]-p[j]
            total += abs(d-e) * psi(d+e)
    return sp.simplify(total / n**4)

for p in [(1,2,0), (2,0,1)]:
    assert J_shuffle(p) == sp.Rational(13,81)
assert sp.Rational(13,81) > sp.Rational(2,15)
assert sp.Rational(1,6) - sp.Rational(13,162) == sp.Rational(7,81)
assert sp.Rational(7,81) < sp.Rational(1,10)

print("ALL EXACT CHECKS PASSED")
print("one-sided ratio =", ratio_one)
print("one-sided 2/5 deficit =", deficit_one)
print("Bernstein 7/10 matrix:")
for row in bc710:
    print(row)
print("Bernstein 2/3 matrix:")
for row in bc23:
    print(row)
print("m=3 D table:", D_table)
print("n=3 three-cycle J =", J_shuffle((1,2,0)))
