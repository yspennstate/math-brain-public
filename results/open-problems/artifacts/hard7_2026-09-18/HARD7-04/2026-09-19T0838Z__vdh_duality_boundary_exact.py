#!/usr/bin/env python3
"""Exact symbolic self-check for HARD7-04 rotated target VDH-8.3-DUALITY.

Checks the boundary family used to show why the source nondegeneracy
p_2<1 cannot simply be dropped from the first-order duality statement.
"""
import sympy as sp

a, z = sp.symbols("a z", positive=True)
root = (sp.sqrt(5) - 1) / 2

# Offspring law X_a: P(0)=a, P(1)=1-2a, P(3)=a.
g = a + (1 - 2*a)*z + a*z**3
assert sp.factor(g - z) == a*(z - 1)*(z**2 + z - 1)
assert sp.simplify(g.subs(z, root) - root) == 0

eps = a
dual_nu = sp.simplify(sp.diff(g, z).subs(z, root))
dual_delta = sp.simplify(1 - dual_nu)
ratio = sp.simplify(dual_delta / eps)
target_ratio = (3*sp.sqrt(5) - 5) / 2
assert sp.simplify(ratio - target_ratio) == 0
assert sp.simplify(target_ratio - 1) != 0

# Realize X_a as the size-biased excess law of a degree distribution.
p1 = 4*a/(2+a)
p2 = 2*(1-2*a)/(2+a)
p4 = a/(2+a)
assert sp.simplify(p1+p2+p4-1) == 0
mu = sp.simplify(p1 + 2*p2 + 4*p4)
nu = sp.simplify((2*p2 + 12*p4)/mu)
third = sp.simplify(p1 + 8*p2 + 64*p4)
assert sp.simplify(nu - (1+a)) == 0
assert sp.limit(p2, a, 0, dir="+") == 1
assert sp.limit(third, a, 0, dir="+") == 8

G0 = p1*z + p2*z**2 + p4*z**4
dual_nu_from_degree = sp.simplify(
    (z**2*sp.diff(G0, z, 2))/(z*sp.diff(G0, z))
).subs(z, root)
assert sp.simplify(dual_nu_from_degree - dual_nu) == 0

print("extinction_root =", root)
print("supercritical_epsilon =", eps)
print("dual_nu =", dual_nu)
print("dual_delta_over_epsilon =", ratio)
print("limit_p2 =", sp.limit(p2, a, 0, dir="+"))
print("limit_E_D3 =", sp.limit(third, a, 0, dir="+"))
print("ALL_EXACT_CHECKS_PASS = True")
