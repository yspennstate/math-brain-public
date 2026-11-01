import sympy as sp

# Three colors 0,1,2 and deterministic offspring count 2.
# Automaton rule on unordered child-color pairs:
# 01 -> 1, 02 -> 2, every other pair -> 0.
x, y, z, t = sp.symbols('x y z t', real=True)

F0 = x**2 + y**2 + z**2 + 2*y*z
F1 = 2*x*y
F2 = 2*x*z

assert sp.expand(F0 + F1 + F2 - (x+y+z)**2) == 0

# Restrict to the probability simplex x+y+z=1.
F0s = sp.expand(F0.subs(z, 1-x-y))
F1s = sp.expand(F1.subs(z, 1-x-y))
F2s = sp.expand(F2.subs(z, 1-x-y))

r0 = sp.factor(F0s - x)
r1 = sp.factor(F1s - y)
r2 = sp.factor(F2s - (1-x-y))

assert sp.expand(r0 - (x-1)*(2*x-1)) == 0
assert sp.expand(r1 - y*(2*x-1)) == 0
assert sp.expand(r2 - (1-x-y)*(2*x-1)) == 0

# The whole segment p_t=(1/2,t,1/2-t), 0<=t<=1/2, is fixed.
pt = {x: sp.Rational(1,2), y: t, z: sp.Rational(1,2)-t}
assert sp.simplify(F0.subs(pt) - sp.Rational(1,2)) == 0
assert sp.simplify(F1.subs(pt) - t) == 0
assert sp.simplify(F2.subs(pt) - (sp.Rational(1,2)-t)) == 0

# The tangent vector is nonzero, certifying a genuine one-dimensional family.
param_vec = sp.Matrix([sp.Rational(1,2), t, sp.Rational(1,2)-t])
tangent = param_vec.diff(t)
assert tangent == sp.Matrix([0,1,-1])

# Exact classification of the fixed locus in the simplex:
# if x != 1/2, r1=r2=0 forces y=z=0, hence x=1; otherwise x=1/2
# and y+z=1/2 is free. The symbolic factors above certify these cases.
print('AUTOMATON: 01->1, 02->2, all other two-child multisets ->0')
print('CHILD_LAW: delta_2')
print('MAP: F0=', sp.factor(F0s), 'F1=', sp.factor(F1s), 'F2=', sp.factor(F2s))
print('FIXED_RESIDUAL_FACTORS:', r0, ';', r1, ';', r2)
print('FIXED_SEGMENT: (1/2, t, 1/2-t), 0<=t<=1/2')
print('TANGENT:', list(tangent))
print('D_fix_lower_bound: 1')
print('ALL_EXACT_CHECKS_PASS')
