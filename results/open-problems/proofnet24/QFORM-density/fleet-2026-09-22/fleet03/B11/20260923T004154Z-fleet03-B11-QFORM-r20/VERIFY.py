import math
import sympy as sp

s,d,g,f = sp.symbols('s d g f', nonzero=True, real=True)
M = sp.Matrix([[0,s,0],[s,d,g],[0,g,f]])
assert sp.expand(M.det() + s**2*f) == 0
assert sp.simplify(M.inv()[2,2] - 1/f) == 0

# Constant arithmetic from the proved thresholds.
c_eta1 = 16 * 2**0.25
c_eta_half = 32 * 2**0.25
c_partner = 6 * math.e**(2/3)

assert abs(c_eta1 - 19.027313840043536) < 1e-12
assert abs(c_eta_half - 38.05462768008707) < 1e-12
assert abs(c_partner - 11.686404246328054) < 1e-12

# Algebraic simplification in Theorem 4.1:
# 4*(sqrt(2)/sqrt(mu))*sqrt((sqrt(2)/sqrt(lambda))*sqrt(2))
# = 8*lambda^(-1/4)*mu^(-1/2).
lam, mu = sp.symbols('lam mu', positive=True)
expr = 4*(sp.sqrt(2)/sp.sqrt(mu))*sp.sqrt((sp.sqrt(2)/sp.sqrt(lam))*sp.sqrt(2))
target = 8*lam**(-sp.Rational(1,4))*mu**(-sp.Rational(1,2))
assert sp.simplify(expr-target) == 0

print('det(M)=', sp.factor(M.det()))
print('(M^-1)_33=', sp.simplify(M.inv()[2,2]))
print('16*2^(1/4)=', repr(c_eta1))
print('32*2^(1/4)=', repr(c_eta_half))
print('6*e^(2/3)=', repr(c_partner))
print('QFORM_B11_TANGENT_RAY_OVERLAP_CHECK_PASS')
