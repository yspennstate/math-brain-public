"""
PROB20-05 exact symbolic checker for the adjacent-swap local-surgery theorem.

Checks:
1. exact factorization of the cost deficit when the affected rank interval lies in [0,1/2];
2. exact crossing polynomial when the interval straddles 1/2;
3. exact tensor Bernstein degree-(5,5) coefficient matrix, all coefficients nonnegative.

This is a reproducibility/self-check artifact, not independent or formal verification.
"""

import sympy as sp

# ------------------------------------------------------------------
# 1. Left-half interval [a,b] subset [0,1/2]
# ------------------------------------------------------------------
p, a, b = sp.symbols('p a b', positive=True)
h = (b-a)/2
m = (a+b)/2
q_left = -1 + sp.sqrt(2*p)

Delta_left = sp.integrate((p-m)*q_left, (p,a,b)) - h**2 \
    + h/2 * sp.integrate(-q_left, (p,a,b))

# Substitute a=r^2 b.
r, B = sp.symbols('r B', nonnegative=True)
left_sub = sp.simplify(Delta_left.subs({a:r**2*B, b:B}))
left_target = -sp.sqrt(2)*B**sp.Rational(5,2)*(r-1)**2 \
    *(7*r**3 + 14*r**2 + 6*r + 3)/30
assert sp.simplify(left_sub-left_target) == 0

# ------------------------------------------------------------------
# 2. Crossing interval a<1/2<b.
#    Parameterize a=r^2/2 and b=1-s^2/2.
# ------------------------------------------------------------------
s = sp.symbols('s', nonnegative=True)
a_cross = r**2/2
b_cross = 1-s**2/2
h_cross = (b_cross-a_cross)/2
m_cross = (a_cross+b_cross)/2
q_right = 1-sp.sqrt(2*(1-p))

# Integral (p-m)q split at 1/2.
I1 = sp.integrate((p-m_cross)*q_left, (p,a_cross,sp.Rational(1,2)))
I2 = sp.integrate((p-m_cross)*q_right, (p,sp.Rational(1,2),b_cross))

# |q| is -q on left and +q on right.
A1 = sp.integrate(-q_left, (p,a_cross,sp.Rational(1,2)))
A2 = sp.integrate(q_right, (p,sp.Rational(1,2),b_cross))

Delta_cross = sp.factor(sp.simplify(I1+I2-h_cross**2+h_cross*(A1+A2)/2))

P = (
    7*r**5 + 15*r**3*s**2 - 30*r**3
    + 15*r**2*s**3 - 30*r**2*s**2 + 20*r**2
    + 7*s**5 - 30*s**3 + 20*s**2 + 6
)
assert sp.simplify(Delta_cross + P/120) == 0

# ------------------------------------------------------------------
# 3. Tensor Bernstein coefficient matrix of P on [0,1]^2.
#    Convert power coefficients to degree-5 Bernstein coefficients.
#    In 1D, x^k = sum_{i=k}^5 C(i,k)/C(5,k) B_i^5(x).
# ------------------------------------------------------------------
poly = sp.Poly(P, r, s)
beta = [[sp.Rational(0) for _ in range(6)] for _ in range(6)]

for (kr, ks), coeff in poly.terms():
    for i in range(kr, 6):
        cr = sp.Rational(sp.binomial(i,kr), sp.binomial(5,kr))
        for j in range(ks, 6):
            cs = sp.Rational(sp.binomial(j,ks), sp.binomial(5,ks))
            beta[i][j] += coeff*cr*cs

expected = [
    [6, 6, 8, 9, 6, 3],
    [6, 6, 8, 9, 6, 3],
    [8, 8, sp.Rational(97,10), sp.Rational(41,4), sp.Rational(34,5), sp.Rational(7,2)],
    [9, 9, sp.Rational(41,4), sp.Rational(51,5), sp.Rational(63,10), 3],
    [6, 6, sp.Rational(34,5), sp.Rational(63,10), sp.Rational(12,5), 0],
    [3, 3, sp.Rational(7,2), 3, 0, 0],
]
expected = [[sp.Rational(x) for x in row] for row in expected]
assert beta == expected
assert all(x >= 0 for row in beta for x in row)

print('EXACT CHECKS PASSED')
print('left-band factor =', sp.factor(left_sub))
print('cross-center Delta = -P/120 with P =', sp.expand(P))
print('Bernstein coefficient matrix:')
for row in beta:
    print(row)
