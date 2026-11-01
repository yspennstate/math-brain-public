#!/usr/bin/env python3
"""Exact-rational certificate for the bank-limited replacement-potential barrier."""
from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 60

A = F(258204856, 10**9)
delta0 = F(176114, 10**7)
coef = F(57, 256)
a = F(3, 8)
b = F(967, 2048)


def s(t):
    return (1 - 2*t)**2


def M(p, q):
    return p*q*(1-p)*(1-q)


def lvec(p, q, d):
    sp, sq, spq = s(p), s(q), s(p*q)
    return [q*sp**j + p*sq**j - spq**j for j in range(1, d+1)]


def solve(A0, b0):
    n = len(b0)
    X = [row[:] + [b0[i]] for i, row in enumerate(A0)]
    for c in range(n):
        piv = next(r for r in range(c, n) if X[r][c])
        X[c], X[piv] = X[piv], X[c]
        z = X[c][c]
        X[c] = [v/z for v in X[c]]
        for r in range(n):
            if r == c:
                continue
            z = X[r][c]
            if z:
                X[r] = [X[r][k] - z*X[c][k] for k in range(n+1)]
    return [X[i][-1] for i in range(n)]


pairs = [
    (F(1,64), F(1,64)),
    (F(3,64), F(17,32)),
    (F(5,32), F(35,64)),
    (F(7,16), F(27,32)),
    (F(29,64), F(15,32)),
    (F(29,64), F(3,4)),
    (F(15,32), F(15,32)),
    (F(15,32), F(47,64)),
    (F(61,64), F(61,64)),
    (F(63,64), F(63,64)),
]

d = 10
L = [lvec(p, q, d) for p, q in pairs]
r = [coef*s(a)**j - s(b)**j for j in range(1, d+1)]

# Solve sum_i lambda_i L_i,j = -r_j.  Positivity of all lambda_i makes
# the resulting upper bound a finite Farkas/LP-dual certificate.
mat = [[L[i][j] for i in range(d)] for j in range(d)]
lam = solve(mat, [-x for x in r])
assert all(x > 0 for x in lam)
for j in range(d):
    assert sum(lam[i]*L[i][j] for i in range(d)) == -r[j]

bound = A * sum(lam[i]*M(*pairs[i]) for i in range(d))
assert bound < F(3142, 10**6)
assert delta0 > bound

# General shape forcing for any correction satisfying the same uniform bank.
# The consumed peer proves kappa<0.069645 and decomposes
# kappa=(57/256)(5/64)+B, where B is the output-side tent-cycle coefficient.
kappa_bar = F(69645, 10**6)
Bbar = kappa_bar - coef*F(5,64)
ua = F(5,64)*A
la = (delta0 - Bbar*A)/coef
ub = coef*ua - delta0
lb = -Bbar*A
m = -ub

dist_b = F(57,2048)
dist_ab = F(199,2048)
slope_up = m/dist_b
slope_down = (la-ub)/dist_ab
curv_pos = 2*la/(F(1,8)**2)
curv_neg = 2*m/(dist_b**2)

assert la > 0
assert ub < 0
assert lb < ub

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("PASS")
print("degree_s_max =", d)
print("finite_AND_pairs =", len(pairs))
print("dual_all_positive =", all(x > 0 for x in lam))
print("polynomial_response_upper =", dec(bound))
print("polynomial_response_upper_lt = 0.003142")
print("required_response_gt = 0.0176114")
print("required_over_poly_upper_gt =", dec(delta0/bound))
print("psi_3_8_lower_gt =", dec(la))
print("psi_3_8_upper_le =", dec(ua))
print("psi_967_2048_lower_gt =", dec(lb))
print("psi_967_2048_upper_lt =", dec(ub))
print("forced_rebound_slope_gt =", dec(slope_up))
print("forced_drop_slope_mag_gt =", dec(slope_down))
print("C2_positive_curvature_somewhere_gt =", dec(curv_pos))
print("C2_negative_curvature_mag_somewhere_gt =", dec(curv_neg))
