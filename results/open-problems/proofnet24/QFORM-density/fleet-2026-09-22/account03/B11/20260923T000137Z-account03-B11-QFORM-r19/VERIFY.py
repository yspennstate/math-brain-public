import sympy as sp

s,d,g,f=sp.symbols('s d g f', nonzero=True, real=True)
M=sp.Matrix([[0,s,0],[s,d,g],[0,g,f]])
assert sp.factor(M.det()) == -s**2*f

Cbank=3*2**(sp.Rational(2,3))*(sp.sqrt(2)*sp.E)**(sp.Rational(2,3))
Csingle=3*2**(sp.Rational(2,3))*(sp.E)**(sp.Rational(2,3))
assert sp.simplify(Cbank-6*sp.E**(sp.Rational(2,3)))==0
assert sp.simplify(Csingle-3*(2*sp.E)**(sp.Rational(2,3)))==0

print('detM =', sp.factor(M.det()))
print('C_single = %.12f' % float(Csingle.evalf()))
print('C_bank = %.12f' % float(Cbank.evalf()))
print('QFORM_B11_NULL_COLOOP_BANK_CLOSURE_CHECK_PASS')
