import sympy as sp

m = sp.symbols('m', integer=True, positive=True)

T0 = sp.Matrix([
    [1, 1, 1],
    [1,-1,-1],
    [-1,1,-1],
    [-1,-1,1],
]) / 2
n = sp.Matrix([1,2,3]) / sp.sqrt(14)
B = sp.eye(3) - 2*n*n.T
C = sp.simplify(T0*B*T0.T)

assert T0.T*T0 == sp.eye(3)
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert sp.factor(B.det()) == -1
assert B.eigenvals() == {-1:1, 1:2}
assert all(x != 0 for x in C)
assert max(abs(x) for x in C) == sp.Rational(3,4)

# comb law: m teeth of length a=1/m separated by d=1/m^3
# centered tooth spacing h=a+d.
a = sp.Rational(1,1)/m
d = sp.Rational(1,1)/m**3
h = a+d
v_direct = sp.simplify((h**2*(m**2-1) + 1/m**2)/12)
v_formula = sp.simplify((1 + 2/m**2 - 1/m**4 - 1/m**6)/12)
assert sp.simplify(v_direct-v_formula) == 0
assert sp.factor(v_formula-sp.Rational(1,12)) == (m-1)*(m+1)*(2*m**2+1)/(12*m**6)

Cstar = (4*sp.pi)**sp.Rational(3,2) + 6**sp.Rational(3,2)
bridge = sp.N((3/sp.pi)*Cstar**sp.Rational(2,3), 18)

print('T0^T T0 = I3')
print('B^2 = I3; spec(B)={1,1,-1}')
print('C=T0 B T0^T =')
print(C)
print('comb variance =', v_formula)
print('variance excess =', sp.factor(v_formula-sp.Rational(1,12)))
print('partner bridge coefficient =', bridge)
print('PASS_QFORM_B17_MICROCOMB_NO_FIXED_CARRIER')
