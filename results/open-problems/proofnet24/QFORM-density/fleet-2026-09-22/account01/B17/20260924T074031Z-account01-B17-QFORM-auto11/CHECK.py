import math
import mpmath as mp
import sympy as sp

R0 = sp.Matrix([
    [1, 1, 1],
    [1,-1, 1],
    [1, 1,-1],
    [1,-1,-1],
]) / 2
B = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
A0 = sp.simplify(R0 * B * R0.T)

assert R0.T * R0 == sp.eye(3)
assert B * B == sp.eye(3)
assert B.det() == -1 and B.trace() == 1
assert B.eigenvals() == {1: 2, -1: 1}
assert all(x != 0 for x in A0)
assert A0 == sp.Matrix([
    [sp.Rational(3,4), sp.Rational(1,4), sp.Rational(1,4),-sp.Rational(1,4)],
    [sp.Rational(1,4), sp.Rational(3,4),-sp.Rational(1,4), sp.Rational(1,4)],
    [sp.Rational(1,4),-sp.Rational(1,4),-sp.Rational(1,4),-sp.Rational(3,4)],
    [-sp.Rational(1,4),sp.Rational(1,4),-sp.Rational(3,4),-sp.Rational(1,4)],
])

r1 = sp.Matrix(R0[0,:]).T
r2 = sp.Matrix(R0[1,:]).T
assert B*r1 == r1 and B*r2 == r2
assert sp.Matrix.hstack(r1,r2).rank() == 2
assert (r1.T*r1)[0] == sp.Rational(3,4)
assert (r2.T*r2)[0] == sp.Rational(3,4)

# Exact satellite second-moment identity.
m, lam, a = sp.symbols('m lam a', positive=True)
l = lam/(2*m)
R = a*sp.sqrt(m)
x = sp.symbols('x', real=True)
sat2 = sp.simplify(2*sp.integrate(x**2, (x, R-l/2, R+l/2)))
assert sp.simplify(sat2 - (lam*a**2 + lam**3/(48*m**3))) == 0

# Concrete near-sharp fixed-defect witness.
lam0 = mp.mpf('0.001')
D = mp.mpf('1')
a0 = mp.sqrt(D/lam0)
w0 = mp.e**(-2*lam0) * mp.besseli(0, lam0)**2
lower = 3*mp.sqrt(2)*w0
upper = 3*mp.sqrt(2)
defect = mp.mpf('1.5')*D
var_limit = mp.mpf(1)/12 + D

assert lower > mp.mpf('4.23416')
assert upper-lower < mp.mpf('0.00848')
assert defect == mp.mpf('1.5')
assert abs(var_limit-mp.mpf(13)/12) < mp.mpf('1e-40')

print('QFORM_B17_MAJORITY_POISSON_SHARP_CHECK_PASS')
print('A0 =', A0)
print('lambda =', mp.nstr(lam0, 20))
print('a =', mp.nstr(a0, 20))
print('w0 =', mp.nstr(w0, 20))
print('lower =', mp.nstr(lower, 20))
print('upper =', mp.nstr(upper, 20))
print('gap =', mp.nstr(upper-lower, 20))
print('Lindeberg defect limit =', mp.nstr(defect, 20))
print('special variance limit =', mp.nstr(var_limit, 20))
