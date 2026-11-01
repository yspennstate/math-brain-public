import sympy as sp
from math import log, sqrt

# Strict target family A_delta.
d = sp.symbols('d', positive=True)
A = sp.Matrix([
    [d, 1+d, d],
    [1+d, 0, 0],
    [d, 0, 1+d],
])
M = sp.expand(A*A - sp.eye(3))

assert sp.factor(M[0,0]) == d*(3*d+2)
assert sp.factor(M[:2,:2].det()) == d**2*(2*d**2+6*d+3)
assert sp.factor(M.det()) == d**3*(d+2)*(d**2+4*d+2)
assert sp.factor(A.det()) == -(d+1)**3

# General spectral principal-minor identities.
r,a,c,b = sp.symbols('r a c b', real=True)
G = sp.Matrix([[r,a,c],[a,0,0],[c,0,b]])
N = sp.expand(G*G-sp.eye(3))
assert sp.factor(N[1,1]) == a**2-1
assert sp.factor(N.extract([1,2],[1,2]).det()) == (a**2-1)*(b**2-1)-c**2
assert sp.factor(N.extract([0,1],[0,1]).det()) == (a**2-1)*(a**2+c**2-1)-r**2

# Exact centered-cube primitive used in the zero-density calculation.
z,beta = sp.symbols('z beta', positive=True)
primitive = z*(2-sp.log(2*beta*z**2))
assert sp.simplify(sp.diff(primitive,z) + sp.log(2*beta*z**2)) == 0

C0 = 2 + log(4)
frontier = 3*sqrt(2)
centered = 2 + log(2)
assert C0 < frontier
assert centered < C0
assert (C0/(1+0.1)) < frontier

print('PASS QFORM_B17_NULL_LEAF_TARGET_RIGIDITY')
print(f'C0={C0:.15f}')
print(f'3sqrt2={frontier:.15f}')
print(f'gap={frontier-C0:.15f}')
print(f'centered_exact={centered:.15f}')
print(f'delta_0p1_partner_bound={C0/1.1:.15f}')
