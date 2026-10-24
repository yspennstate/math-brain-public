#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

# P26 / T08 exact checker for the parity-smoothed Green transfer application.
# This certifies the finite/algebraic core for the pure distance-three graph
# built from a bipartite degree-six Ramanujan base.

d = 6
q = 5
m = 3
D = d * q**(m-1)

# Exact radial multiplicities on T_d for one distance-m step.
counts = {}
for a in range(m+1):
    delta = m - 2*a
    if a == 0:
        c = q**m
    elif a == m:
        c = 1
    else:
        c = (q-1)*q**(m-a-1)
    counts[delta] = c
assert sum(counts.values()) == D

v = sum(Fraction(delta*c, D) for delta, c in counts.items())
M2 = sum(Fraction(delta*delta*c, D) for delta, c in counts.items())
tau2 = M2 / (v**3)

# NBRW endpoint polynomials for normalized adjacency.
x = sp.symbols('x', real=True)
p0 = sp.Integer(1)
p1 = x
p2 = sp.simplify((d*x*p1 - p0)/q)
p3 = sp.simplify((d*x*p2 - p1)/q)
p4 = sp.simplify((d*x*p3 - p2)/q)

assert sp.factor(p2) == (6*x**2-1)/5
assert sp.factor(p3) == x*(36*x**2-11)/25
assert sp.simplify(p3.subs(x,-1)) == -1
assert sp.simplify(p4.subs(x,-1)) == 1
assert sp.simplify(p3.subs(x,-1)+p4.subs(x,-1)) == 0

# Exact maximum of |p3| on the degree-six Ramanujan interval.
rho = sp.sqrt(q)*2/d
crit = [c for c in sp.solve(sp.diff(p3, x), x) if c.is_real]
candidates = [-rho, rho] + crit
vals = []
for c in candidates:
    if float(abs(c)) <= float(rho) + 1e-14:
        vals.append((c, sp.simplify(p3.subs(x,c))))
max_abs = max(vals, key=lambda cv: float(abs(cv[1])))
assert sp.simplify(abs(max_abs[1]) - 3*sp.sqrt(5)/25) == 0

# General exact drift identity for several distances (the report proves it algebraically).
def radial_counts(mm):
    Dm = d*q**(mm-1)
    out = {}
    for a in range(mm+1):
        delta = mm-2*a
        if a == 0:
            c = q**mm
        elif a == mm:
            c = 1
        else:
            c = (q-1)*q**(mm-a-1)
        out[delta] = c
    assert sum(out.values()) == Dm
    return Dm, out

for mm in range(1,16):
    Dm, cs = radial_counts(mm)
    vv = sum(Fraction(delta*c,Dm) for delta,c in cs.items())
    formula = Fraction(mm,1) - Fraction(2*q*(q**mm-1),(q*q-1)*q**mm)
    assert vv == formula

# The Ramanujan bulk estimate (m+1) q^{-m/2}<1 for every odd m>=3.
for mm in range(3,40,2):
    assert (mm+1)/(q**(mm/2)) < 1.0

# The output tree benchmark is strictly larger than inherited base-volume growth.
assert q**m < D-1

print('P26_T08_TAUBERIAN_PARITY_GREEN_EXACT_PASS')
print('degree_D =', D)
print('radial_counts =', dict(sorted(counts.items())))
print('v =', v)
print('M2 =', M2)
print('tau2 =', tau2, '=', float(tau2))
print('p2(x) =', sp.factor(p2))
print('p3(x) =', sp.factor(p3))
print('Ramanujan_rho =', rho)
print('bulk_candidates =', vals)
print('bulk_max_abs =', max_abs[1], 'at', max_abs[0], '=', float(abs(max_abs[1])))
print('one_sided_gap_lower =', sp.simplify(1-abs(max_abs[1])), '=', float(1-abs(float(max_abs[1]))))
print('parity_mode_p3(-1) =', sp.simplify(p3.subs(x,-1)))
print('two_shell_parity_sum =', sp.simplify(p3.subs(x,-1)+p4.subs(x,-1)))
print('branching =', q**m, '<', D-1)
print('center_coefficient_1/v =', Fraction(1,1)/v)
