from fractions import Fraction
import sympy as sp

# Exact finite/algebraic self-check for the balanced-spike exclusion theorem.
# This does NOT independently verify the analytic Gaussian argument; it checks
# the finite identities and rational inequalities used in that proof.

n, m = sp.symbols('n m', integer=True, positive=True)

# Explicit orthogonal Q with balanced spike eigenvector as column 2.
Q = sp.Matrix([
    [1/sp.sqrt(2), 1/sp.sqrt(3),  1/sp.sqrt(6)],
    [-1/sp.sqrt(2), 1/sp.sqrt(3), 1/sp.sqrt(6)],
    [0,               1/sp.sqrt(3), -2/sp.sqrt(6)],
])
assert sp.simplify(Q.T*Q - sp.eye(3)) == sp.zeros(3)

# For L_n = 2 n^2 - 2, the 1D lower bound on E[m_1] simplifies exactly.
s2 = n**2 - 1
Ilow = sp.Rational(2,3) * (
    s2*(1-sp.Rational(1,1)/n**3)/3
    + (sp.Rational(2,3)-1/n+sp.Rational(1,3)/n**3)
    - sp.Rational(2,3)*s2**2/n**3
)
Ilow_target = sp.Rational(2,9)*(n-1)**2
assert sp.simplify(Ilow-Ilow_target) == 0

D = 2*n**2 - 4*n - 1
C_lb = sp.simplify(Ilow_target - sp.Rational(1,3))
A_lb = sp.simplify(2*Ilow_target - sp.Rational(2,3))
assert sp.simplify(C_lb - D/9) == 0
assert sp.simplify(A_lb - 2*D/9) == 0

# Exact upper formula for M = E[m_2^(3/2)] from the pointwise max bound.
s = sp.sqrt(n**2-1)
b = sp.sqrt(sp.Rational(2,3))
U_from_integrals = sp.simplify(b**3 * (
    s**3*sp.Rational(1,4)
    + 3*s**2*sp.pi/sp.Integer(16)
    + 3*s*sp.Rational(1,4)
    + 3*sp.pi/sp.Integer(16)
))
U_target = sp.sqrt(6) * (s*(n**2+2)/18 + sp.pi*n**2/24)
assert sp.simplify(U_from_integrals-U_target) == 0

# Self-contained exact proof of pi > 31/10 from the 30-term Gregory-Leibniz lower partial sum.
# With 30 terms the last term is negative, so the alternating-series theorem gives S_30 < pi/4.
S30 = sum(Fraction(1 if k % 2 == 0 else -1, 2*k+1) for k in range(30))
assert 4*S30 > Fraction(31,10)

# Elementary radical upper bounds used for n=7.
assert Fraction(283,200)**2 > 2
assert Fraction(49,20)**2 > 6

# n=7: U/pi < S7, and the resulting large-lambda threshold is < 23.
S7 = Fraction(34*283*10, 200*31) + Fraction(49*49, 20*24)
H7_upper = (Fraction(16,69)*S7)**2
assert H7_upper < 23

# n>=8: crude uniform upper bound U/pi < V_n reduces the overlap condition to a polynomial.
P = 120*n**2 + 279*n + 240
V = sp.Rational(5,1)*n*P / 13392
poly = sp.expand(D**3*13392**2 - 19200*n**2*P**2)
poly_factor = sp.factor(poly)
expected_factor = 6912*(
    167576*n**6 - 1431456*n**5 + 1803323*n**4 - 787152*n**3
    - 1249774*n**2 - 311364*n - 25947
)
assert sp.expand(poly_factor-expected_factor) == 0
shifted = sp.Poly(sp.expand((expected_factor/6912).subs(n,m+8)), m)
coeffs = shifted.all_coeffs()
assert all(c > 0 for c in coeffs)

print('ALL_EXACT_CHECKS_PASS')
print('Q_ORTHOGONAL=PASS')
print('E_MIN_LOWER_IDENTITY=2(n-1)^2/9')
print('C_LOWER=D/9, A_LOWER=2D/9, D=2n^2-4n-1')
print('U_FORMULA=PASS')
print('PI_LOWER_31_OVER_10_FROM_30_TERM_LEIBNIZ=PASS')
print('N7_H_UPPER=', H7_upper, '≈', float(H7_upper), '< 23')
print('N_GE_8_SHIFTED_POLY_COEFFS=', coeffs)
