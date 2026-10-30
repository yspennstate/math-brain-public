from math import comb
import math
import sympy as sp

# Exact 3x3 zero-diagonal determinant.
a,b,c = sp.symbols('a b c', nonzero=True)
H = sp.Matrix([[0,a,b],[a,0,c],[b,c,0]])
assert sp.factor(H.det()) == 2*a*b*c

# Exact saddle-plus-square coordinate identity.
x1,x2,x3 = sp.symbols('x1 x2 x3')
U = a*x2 + b*x3
V = a*x2 - b*x3
lhs = 2*a*x1*x2 + 2*b*x1*x3 + 2*c*x2*x3
rhs = 2*x1*U + c/(2*a*b)*(U**2 - V**2)
assert sp.simplify(lhs-rhs) == 0

# Optimization in the one-sided saddle-plus-square estimate.
L,M,beta,r = sp.symbols('L M beta r', positive=True)
rstar = 2**(sp.Rational(1,3))*L**(sp.Rational(1,3))*beta**(sp.Rational(1,3))/(4*M**(sp.Rational(2,3)))
F = L/(2*r) + 4*sp.sqrt(2)*M*sp.sqrt(L)*beta**(-sp.Rational(1,2))*sp.sqrt(r)
opt = sp.simplify(F.subs(r,rstar))
target = 3*2**(sp.Rational(2,3))*L**(sp.Rational(2,3))*M**(sp.Rational(2,3))*beta**(-sp.Rational(1,3))
assert sp.simplify(opt-target) == 0

# Constants used in the report.
lemma_constant = 3*2**(2/3)
normalized_three_scalar = 6*2**(2/3)
k5_constant = normalized_three_scalar * comb(5,3)**(1/3)
partner_constant = normalized_three_scalar * 2**(-1/3)
assert abs(lemma_constant - 4.762203155904599) < 1e-12
assert abs(normalized_three_scalar - 9.524406311809198) < 1e-12
assert abs(k5_constant - 20.51971136013366) < 1e-10
assert abs(partner_constant - 7.559526299369239) < 1e-12

# Deterministic Cauchy-Binet sanity check: an explicit 5x3 matrix with orthonormal columns.
B = sp.Matrix([
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,1,0],
    [0,1,1],
])
G = B.T*B
# Whiten numerically and verify sum of squared 3x3 minors = det(U^T U)=1.
import numpy as np
Bn = np.array(B.tolist(), dtype=float)
Gn = Bn.T @ Bn
vals, vecs = np.linalg.eigh(Gn)
Gmhalf = vecs @ np.diag(vals**-0.5) @ vecs.T
Un = Bn @ Gmhalf
assert np.max(np.abs(Un.T @ Un - np.eye(3))) < 1e-12
from itertools import combinations
minor_sum = 0.0
for J in combinations(range(5),3):
    minor_sum += np.linalg.det(Un[list(J),:])**2
assert abs(minor_sum-1.0) < 1e-12
assert max(np.linalg.det(Un[list(J),:])**2 for J in combinations(range(5),3)) >= 1/comb(5,3)-1e-12

print('detH =', detH := sp.factor(H.det()))
print('lemma_constant =', lemma_constant)
print('normalized_three_scalar =', normalized_three_scalar)
print('k5_constant =', k5_constant)
print('partner_constant =', partner_constant)
print('cauchy_binet_minor_sum =', minor_sum)
print('QFORM_B11_FIVE_NULL_RAY_CHECK_PASS')
