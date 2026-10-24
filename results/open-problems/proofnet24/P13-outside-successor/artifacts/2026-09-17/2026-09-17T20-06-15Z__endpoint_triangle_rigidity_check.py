#!/usr/bin/env python3
"""
SELF-CHECK for P13-P0082-ENDPOINT-TRIANGLE-RIGIDITY-03.

Exact symbolic identities only. This does not prove the analytic theorem;
it checks the finite algebraic core used in the endpoint triangle rigidity step.
"""
import sympy as sp

a,b,c = sp.symbols("a b c", positive=True)
M = sp.Matrix([
    [a+b, 2*b, 2*a],
    [2*b, b+c, 2*c],
    [2*a, 2*c, c+a],
])
target_det = -3*((a+b+c)*(a*b+b*c+c*a)-9*a*b*c)
assert sp.expand(M.det()-target_det) == 0

u,v = sp.symbols("u v", positive=True)
pair_gap = sp.factor(1/u + 1/v - 4/(u+v))
assert sp.simplify(pair_gap - (u-v)**2/(u*v*(u+v))) == 0

t = sp.symbols("t", positive=True)
Mu = sp.simplify(M.subs({a:t,b:t,c:t}))
b1 = sp.Matrix([1,-1,0])
b2 = sp.Matrix([1,0,-1])
one = sp.Matrix([1,1,1])
assert Mu*b1 == sp.zeros(3,1)
assert Mu*b2 == sp.zeros(3,1)
assert Mu*one == 6*t*one
assert sp.factor(Mu.det()) == 0

# For the uniform triangle, the signless-cycle numerator has eigenvalues 4,1,1.
Qsign = sp.Matrix([[2,1,1],[1,2,1],[1,1,2]])
lam = sp.symbols("lam")
char = sp.factor(Qsign.charpoly(lam).as_expr())
assert char == (lam-4)*(lam-1)**2

print("SELF-CHECK ONLY")
print("det(M) =", sp.factor(M.det()))
print("AM-GM factor =", sp.expand((a+b+c)*(a*b+b*c+c*a)-9*a*b*c))
print("pair reciprocal gap =", pair_gap)
print("uniform M eigenvalues =", Mu.eigenvals())
print("triangle signless eigenvalues =", Qsign.eigenvals())
print("ALL EXACT SYMBOLIC CHECKS PASSED")
