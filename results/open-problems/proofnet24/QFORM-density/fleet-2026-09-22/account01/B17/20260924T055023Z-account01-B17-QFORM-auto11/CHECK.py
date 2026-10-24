from fractions import Fraction
import sympy as sp

# Core Householder block.
B = sp.eye(3) - sp.Rational(2,3)*sp.ones(3)
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert B.eigenvals() == {-1: 1, 1: 2}

# Symbolic scalar identities used in the principal-submatrix estimate.
m = sp.symbols('m', integer=True, positive=True)
eps = sp.Rational(1,2)/m**2
principal_bound = sp.expand((1+1/m)*(m-1)/m + eps)
assert sp.simplify(principal_bound - (1-sp.Rational(1,2)/m**2)) == 0
same = (m+1)/(3*m**2)
cross = -2*(m+1)/(3*m**2)
assert same != 0 and cross != 0

# Exact finite matrices for sample m; checks spectrum and entrywise density for both tail signs.
def build(mv, sigma):
    R = sp.zeros(3*mv,3)
    for j in range(3):
        for r in range(mv):
            R[j*mv+r,j] = 1/sp.sqrt(mv)
    P = sp.simplify(R*R.T)
    e = sp.Rational(1,2*mv*mv)
    A = sp.simplify((1+sp.Rational(1,mv))*R*B*R.T + sigma*e*(sp.eye(3*mv)-P))
    return R,P,A,e

for mv in (2,3,4,7):
    for sigma in (-1,1):
        R,P,A,e = build(mv,sigma)
        assert sp.simplify(R.T*R-sp.eye(3)) == sp.zeros(3)
        expected = {
            -(1+sp.Rational(1,mv)): 1,
            +(1+sp.Rational(1,mv)): 2,
            sigma*e: 3*mv-3,
        }
        assert A.eigenvals() == expected
        assert all(A[i,j] != 0 for i in range(3*mv) for j in range(3*mv))
        A2 = sp.simplify(A*A)
        rhs = sp.simplify((1+sp.Rational(1,mv))**2*P + e**2*(sp.eye(3*mv)-P))
        assert sp.simplify(A2-rhs) == sp.zeros(3*mv)

# Partner account02/B17 concrete target matrix: beta=1/2,a=kappa=1.
Ap = sp.Matrix([[1,1,-1],[1,sp.Rational(1,2),1],[-1,1,1]])
assert sp.factor(Ap.charpoly().as_expr()) == (sp.Symbol('lambda')-2)*(2*sp.Symbol('lambda')**2-sp.Symbol('lambda')-4)/2
expected_partner = {2:1, sp.Rational(1,4)-sp.sqrt(33)/4:1, sp.Rational(1,4)+sp.sqrt(33)/4:1}
assert Ap.eigenvals() == expected_partner
assert (sp.sqrt(33)-1)/4 > 1

print('QFORM_B17_STRICT_THRESHOLD_PRINCIPAL_DELOCALIZATION_CHECK_PASS')
