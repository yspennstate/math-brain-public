from sympy import Matrix, Rational, symbols, integrate, simplify, sqrt, factor

d = symbols("d", positive=True)
x = symbols("x", real=True)

B = Matrix([[6,-2,-3],[-2,3,-6],[-3,-6,-2]])/7
assert B*B == Matrix.eye(3)
assert factor(B.charpoly().as_expr()) == (symbols("lambda")-1)**2*(symbols("lambda")+1)
assert all(B[i,j] != 0 for i in range(3) for j in range(3))

outer = 2*integrate(x**2, (x, Rational(1,2), Rational(1,2)+d/2))
missing = 2*integrate(x**2, (x, Rational(1,2)-d/2, Rational(1,2)))
assert simplify(outer-missing-d**2/2) == 0

var = Rational(1,12)+d**2/2
l1 = 2*d
assert simplify(var-Rational(1,12)-l1**2/8) == 0

peak = simplify(1/(2*sqrt(2)*var))
assert simplify(peak-3*sqrt(2)/(1+6*d**2)) == 0
peak13 = simplify(peak.subs(d,Rational(1,3)))
assert peak13 == 9*sqrt(2)/5
assert float(peak13) < 2.55
assert float(3*sqrt(2)) > 4.24

print("QFORM_B17_VARIANCE_RIGIDITY_CHECK_PASS")
print("boundary_swap_variance =", var)
print("sharp_L1_penalty =", l1**2/8)
print("B_charpoly =", factor(B.charpoly().as_expr()))
print("peak_delta_1_3 =", peak13, float(peak13))
print("universal_obstruction =", 3*sqrt(2), float(3*sqrt(2)))
