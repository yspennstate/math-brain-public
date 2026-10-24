#!/usr/bin/env python3
"""Exact self-check for P15 I0066 infinite-cascade limit analysis.

This is deliberately a finite algebra check only.  The infinite-dimensional
SMR failure at the endpoint is proved analytically in the accompanying report.
The script verifies the finite weighted-shift identities used by that proof and
an alternating non-small local-gain example which is rescued by diagonal
Lyapunov reweighting.
"""

import sympy as sp

N = 8
r = sp.Integer(2)
c = sp.Integer(1)  # endpoint d=c^2*r=2

lam = [r**n for n in range(N + 1)]
A = sp.diag(*lam)
B = sp.zeros(N + 1)
for n in range(N):
    B[n + 1, n] = c * sp.sqrt(lam[n])

# ||A^(1/2) Bx||^2 = 2 ||Ax||^2 on every nonterminal level at the endpoint.
quad = sp.simplify(B.T * A * B)
target_diag = [2 * lam[n]**2 if n < N else 0 for n in range(N + 1)]
assert quad == sp.diag(*target_diag)

# Stationary second-moment recursion for the finite truncation with forcing in
# level zero: v_0=1/2 and
# v_n = c^2 lambda_{n-1} v_{n-1}/(2 lambda_n).
v = [sp.Rational(1, 2)]
for n in range(1, N + 1):
    v.append(sp.simplify(c**2 * lam[n - 1] * v[n - 1] / (2 * lam[n])))
w = [sp.simplify(lam[n]**2 * v[n]) for n in range(N + 1)]
assert all(x == sp.Rational(1, 2) for x in w)

# A non-small alternating example.  With r=2, take c_even=2 and c_odd=1/4.
# The raw local energy gains d_n=c_n^2*r are 8 and 1/8, so the B norm is not
# perturbatively small.  Weights theta_even=1, theta_odd=1/8 transform every
# local gain to exactly 1<2.  This is a concrete instance of the already-counted
# heterogeneous Lyapunov family, not a new metric family.
d = []
theta = [sp.Integer(1) if n % 2 == 0 else sp.Rational(1, 8)
         for n in range(N + 1)]
for n in range(N):
    c_n = sp.Integer(2) if n % 2 == 0 else sp.Rational(1, 4)
    d_n = sp.simplify(c_n**2 * r)
    d.append(d_n)
    assert sp.simplify(theta[n + 1] * d_n / theta[n]) == 1

for n in range(0, N - 1, 2):
    assert sp.simplify((d[n] / 2) * (d[n + 1] / 2)) == sp.Rational(1, 4)

print("P15 I0066 infinite-cascade exact self-check")
print(f"N={N}, r={r}, endpoint c={c}, d=c^2*r={c**2*r}, q=d/2={c**2*r/2}")
print("B^T A B diagonal =", [quad[i, i] for i in range(N + 1)])
print("2 A^2 on nonterminal levels =", target_diag)
print("stationary v =", v)
print("stationary w_n=lambda_n^2 v_n =", w)
print("alternating d_n =", d)
print("alternating theta_n =", theta)
print("transformed gains theta_{n+1} d_n/theta_n =",
      [sp.simplify(theta[n + 1] * d[n] / theta[n]) for n in range(N)])
print("two-step q products =",
      [sp.simplify((d[n] / 2) * (d[n + 1] / 2))
       for n in range(0, N - 1, 2)])
print("ALL_EXACT_CHECKS_PASSED")
