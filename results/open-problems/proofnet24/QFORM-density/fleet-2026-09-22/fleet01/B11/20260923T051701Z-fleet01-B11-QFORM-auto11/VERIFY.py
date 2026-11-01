import sympy as sp
import math

a = sp.symbols('a', nonnegative=True, real=True)
sig = sp.sqrt(1-a*a)
H = sp.Matrix([[-a, 0, sig], [0, 1, 0], [sig, 0, a]])
charpoly = sp.factor(H.charpoly().as_expr())
assert sp.simplify(charpoly - (sp.Symbol('lambda')-1)**2*(sp.Symbol('lambda')+1)) == 0
assert sp.simplify(H.det() + 1) == 0

# After W -> Z/sqrt(2), regroup the pair as (X1,Z), leaving X2^2.
B = sp.Matrix([[-a, sig/sp.sqrt(2)], [sig/sp.sqrt(2), a/2]])
assert sp.simplify(B.det() + sp.Rational(1,2)) == 0

# Direct scalar-Schur treatment with W as the scalar pivot (a>0).
c = sp.Matrix([sig, 0])
B0 = sp.diag(-a, 1)
S = sp.simplify(B0 - (c*c.T)/a)
assert sp.simplify(S[0,0] + 1/a) == 0
assert S[0,1] == 0 and S[1,0] == 0 and S[1,1] == 1
assert sp.simplify(S.det() + 1/a) == 0
assert sp.simplify(a*S.det() - H.det()) == 0

# Correction-safe physical-triple dichotomy at tau=1/2.
tau = sp.Rational(1,2)
b2 = (1-tau**2)/2              # some off-diagonal square / s^2
D0 = sp.simplify(b2-tau**2)     # lower bound for |det pair| / s^2
k0 = sp.simplify(sp.sqrt(b2)-tau) # lower bound for sigma_min(pair) / s
assert D0 == sp.Rational(1,8)
assert k0 > 0
C_pair = 8*sp.sqrt(5)*(D0*k0)**(-sp.Rational(1,4))
C_scalar = 16*sp.sqrt(30)*2**sp.Rational(1,4)
assert float(C_pair) < float(C_scalar)

print('charpoly(H_a)=', charpoly)
print('det(H_a)=', sp.simplify(H.det()))
print('det(B_pair_after_Z=sqrt(2)W)=', sp.simplify(B.det()))
print('scalar-Schur S=', S)
print('tau=1/2 pair D0=', D0, 'kappa0=', k0)
print('pair-branch constant=', float(C_pair))
print('scalar-branch/three-coordinate constant=', float(C_scalar))
print('partner-family uniform constant=', float(C_scalar))
print('QFORM_B11_CROSSCOUPLED_SCHUR_CHECK_PASS')
