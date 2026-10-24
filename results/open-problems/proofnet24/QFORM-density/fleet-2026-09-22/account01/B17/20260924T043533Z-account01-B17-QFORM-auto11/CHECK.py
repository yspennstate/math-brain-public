import sympy as sp
import mpmath as mp

B = sp.eye(3) - sp.Rational(2,3)*sp.ones(3,3)
lam = sp.Symbol('lambda')
assert sp.factor(B.charpoly(lam).as_expr()) == (lam - 1)**2*(lam + 1)

z1 = 4 + 3*sp.sqrt(3) - 3*sp.sqrt(2) - 2*sp.sqrt(6)
z2 = (sp.sqrt(6) - sp.sqrt(3))/3
C = (44*sp.sqrt(3)*sp.atanh(z1)
     - 2*sp.sqrt(3)*sp.atanh(z2)
     - sp.Rational(165,4) + 12*sp.sqrt(3) + 15*sp.sqrt(2))

# Antiderivatives after z = tan(x/2)/(1+sqrt(2)).
z = sp.symbols('z', real=True)
J1 = 2*sp.sqrt(6)*sp.atanh(z)
J2 = 12*(sp.sqrt(2)*z/(1-z**2) - sp.atanh(z))
J3 = (24*sp.sqrt(6)*(z/(1-z**2)**2 + sp.atanh(z))
      - 12*sp.sqrt(6)*(1+2*sp.sqrt(2))*z/(1-z**2))
A = 1 + sp.sqrt(2)
a0 = 1/sp.sqrt(6)
for k,J in [(1,J1),(2,J2),(3,J3)]:
    rhs = 2*A**(1-k)*a0**(-k)*(1+A**2*z**2)**(k-1)/(1-z**2)**k
    assert sp.simplify(sp.diff(J,z)-rhs) == 0

# Actual target-valid matrix used for the completed account02/B17 theorem.
Ap = sp.Matrix([[1,1,-1],[1,0,1],[-1,1,0]])
assert sp.factor(Ap.charpoly(lam).as_expr()) == (lam-1)*(lam**2-3)
assert Ap.det() == -3

# Rigorous interval evaluation of the exact six-variable witness constant.
mp.iv.dps = 50
iv = mp.iv
s2, s3, s6 = iv.sqrt(2), iv.sqrt(3), iv.sqrt(6)
zz1 = 4 + 3*s3 - 3*s2 - 2*s6
zz2 = (s6-s3)/3
atanh_iv = lambda u: iv.log((1+u)/(1-u))/2
CI = 44*s3*atanh_iv(zz1) - 2*s3*atanh_iv(zz2) - 165/4 + 12*s3 + 15*s2
lo, hi = float(CI.a), float(CI.b)
assert lo > 4.063
assert hi < 3*(2**0.5)

print('QFORM_B17_EXACT_SIX_HOUSEHOLDER_CHECK_PASS')
print('C_exact_interval =', CI)
print('partner_charpoly =', sp.factor(Ap.charpoly(lam).as_expr()))
print('partner_bound = 2 + log(5/3) =', sp.N(2+sp.log(sp.Rational(5,3)), 30))
