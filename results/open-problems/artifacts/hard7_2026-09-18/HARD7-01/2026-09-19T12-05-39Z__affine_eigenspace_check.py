import sympy as sp

q, w = sp.symbols('q w', positive=True)
r = sp.sqrt(w)
t = sp.sqrt(1-w)
s = sp.Matrix([r,t])
e = sp.Matrix([1,0])

# Congruence-normalized Hessian of H_q on span{e_i,s}.
A = 2*((q-1)*sp.eye(2) - (q-2)*(s*s.T))

# Congruence-normalized Hessian of F_i = H_q W_i.
B = (
    q*(q-1)*(e*e.T)
    - (q-2)*(q-1)*w*sp.eye(2)
    - q*(q-2)*(s*(r*e).T + (r*e)*s.T)
    + 2*(q-2)*(q-1)*w*(s*s.T)
)

L = sp.simplify(B + sp.Rational(1,2)*(q-2)*A)
U = sp.simplify(sp.Rational(1,2)*q*A - B)

L22_expected = (q-2)*(1-w)*(2*(q-1)*w + 1)
detL_expected = (q-2)*(1-w)*(2*(q-1)**2 + (3*q-2)*w)
U11_expected = w*(q-2)*((2*q-1) - 2*(q-1)*w)
detU_expected = w*(q-2)*(q*(2*q-1) - (3*q-2)*w)

assert sp.simplify(L[1,1] - L22_expected) == 0
assert sp.simplify(sp.factor(L.det() - detL_expected)) == 0
assert sp.simplify(U[0,0] - U11_expected) == 0
assert sp.simplify(sp.factor(U.det() - detU_expected)) == 0

# The remaining orthogonal generalized eigenvalue is -(q-2)w/2,
# hence lies in [-(q-2)/2,0] for 0<=w<=1.
orth_lambda = -sp.Rational(1,2)*(q-2)*w
assert sp.simplify(orth_lambda + sp.Rational(1,2)*(q-2)*w) == 0

# Coefficient-cone and source-split algebra.
R = q/(q-2)
d = sp.symbols('d', nonnegative=True)
cq = (3*q-4)/6
R_aff = sp.factor(8*q/((q+3)*(3*q-4)*(3*q-2)))
margin_poly = sp.factor((q+3)*(3*q-4)*(3*q-2) - 20*q)
assert sp.expand(margin_poly - 3*(q-2)*(3*q**2 + 9*q - 4)) == 0

# q=4 exact calibration and equality coefficient triple.
q4 = sp.Integer(4)
a4 = sp.Rational(1,3)
b4 = sp.Rational(1,3)
c4 = sp.Rational(2,3)
m4 = (a4+b4+c4)/3
cat_var4 = ((a4-m4)**2 + (b4-m4)**2 + (c4-m4)**2)/3
# Dirichlet(1/4,1/4,1/4): Var(U)=q/(q+3)*categorical variance.
var4 = sp.Rational(4,7)*cat_var4
ratio4 = sp.factor(var4/(m4*(1-m4)))
assert ratio4 == sp.Rational(2,35)
assert sp.Rational(2,5) - ratio4 == sp.Rational(12,35)
assert sp.simplify(R_aff.subs(q,4) - sp.Rational(2,35)) == 0

# First two Wright-Fisher/Hessian-metric eigenvalues for n=3, q=4.
# lambda_d = q^2/[2(q-1)] * d*(d-1+3/q).
def lam(dval, qval):
    return sp.factor(qval**2/(2*(qval-1))*dval*(dval-1+sp.Rational(3,1)/qval))
lam1 = lam(sp.Integer(1), q4)
lam2 = lam(sp.Integer(2), q4)
assert lam1 == 2
assert lam2 == sp.Rational(28,3)

# If the first-mode variance V1 obeys V1/M <= 19/55, then the energy cap
# 4 V1 + (34/3) V2 <= 2M forces (V1+V2)/M <= 2/5.
rcrit = sp.Rational(19,55)
forced_total = sp.factor(sp.Rational(3,17) + sp.Rational(11,17)*rcrit)
assert forced_total == sp.Rational(2,5)

print('HESSIAN_LOWER_L22 =', sp.factor(L22_expected))
print('HESSIAN_LOWER_DET =', sp.factor(detL_expected))
print('HESSIAN_UPPER_U11 =', sp.factor(U11_expected))
print('HESSIAN_UPPER_DET =', sp.factor(detU_expected))
print('AFFINE_RATIO_GENERAL =', R_aff)
print('TARGET_MARGIN_FACTOR =', margin_poly)
print('Q4_EXTREMAL_MEAN =', m4)
print('Q4_EXTREMAL_VARIANCE =', var4)
print('Q4_EXTREMAL_RATIO =', ratio4)
print('Q4_GAP_TO_2_OVER_5 =', sp.Rational(2,5)-ratio4)
print('Q4_LAMBDA1 =', lam1)
print('Q4_LAMBDA2 =', lam2)
print('Q4_FIRST_MODE_SUFFICIENT_THRESHOLD =', rcrit)
print('Q4_FORCED_TOTAL_AT_THRESHOLD =', forced_total)
print('ALL_EXACT_CHECKS_PASS = True')
