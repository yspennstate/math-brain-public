#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

# Exact sanity checks for P26 T08 distance-{2,3} spherical transfer.
d = 6
q = d - 1
J = (2, 3)
x = sp.symbols("x", real=True)

# Normalized nonbacktracking endpoint polynomials p_j(P).
p = {0: sp.Integer(1), 1: x}
for j in range(1, 3):
    p[j+1] = sp.expand(sp.Rational(d, q) * x * p[j] - sp.Rational(1, q) * p[j-1])

assert sp.expand(p[2] - (6*x**2 - 1)/5) == 0
assert sp.expand(p[3] - (36*x**3 - 11*x)/25) == 0

shell_deg = {j: d * q**(j-1) for j in J}
D = sum(shell_deg.values())
weights = {j: sp.Rational(shell_deg[j], D) for j in J}
F = sp.expand(sum(weights[j] * p[j] for j in J))
assert D == 180
assert F == (36*x**3 + 6*x**2 - 11*x - 1)/30

# Exact spectral optimization on the Ramanujan interval |lambda| <= 2 sqrt(q)/d.
rho = sp.sqrt(5) / 3
crit = sp.solve(sp.diff(F, x), x)
candidates = [rho, -rho] + crit
values = [sp.simplify(F.subs(x, c)) for c in candidates]
M = sp.simplify(F.subs(x, rho))
assert M == sp.Rational(7, 90) + sp.sqrt(5)/10
assert M.is_positive
for v in values:
    delta = sp.simplify(M**2 - v**2)
    assert delta.is_nonnegative, (v, delta)
gap_lb = sp.simplify(1 - M)
assert gap_lb == sp.Rational(83, 90) - sp.sqrt(5)/10
assert gap_lb.is_positive

# Exact radial increment counts on T_6 for a uniform X_{2,3} neighbor.
def counts_for_length(j):
    c = {j: q**j, -j: 1}
    for a in range(1, j):
        c[j - 2*a] = (q - 1) * q**(j-a-1)
    assert sum(c.values()) == d * q**(j-1)
    return c

combined = {}
for j in J:
    for inc, n in counts_for_length(j).items():
        combined[inc] = combined.get(inc, 0) + n

assert combined == {2:25, 0:4, -2:1, 3:125, 1:20, -1:4, -3:1}
assert sum(combined.values()) == D

v = sum(Fraction(inc*n, D) for inc, n in combined.items())
m2 = sum(Fraction(inc*inc*n, D) for inc, n in combined.items())
assert v == Fraction(109, 45)
assert m2 == Fraction(631, 90)
tau2 = m2 / (v**3)
assert tau2 == Fraction(1277775, 2590058)

# Output long-range branching mismatch: one output step changes base distance by at most 3.
assert q**3 == 125
assert D - 1 == 179
assert q**3 < D - 1

print("d =", d, "q =", q, "J =", J)
print("shell_degrees =", shell_deg, "D =", D, "weights =", weights)
print("p2 =", p[2])
print("p3 =", p[3])
print("F =", F)
print("critical_points =", crit)
print("candidate_values =", values)
print("ramanujan_abs_spectral_radius_bound =", M)
print("spectral_gap_lower_bound =", gap_lb)
print("radial_counts =", dict(sorted(combined.items())))
print("radial_speed =", v)
print("compound_poisson_second_moment_rate =", m2)
print("profile_tau_squared =", tau2)
print("branching_mismatch =", q**3, "<", D-1)
print("P26_T08_DISTANCE23_SPHERICAL_EXACT_PASS")
