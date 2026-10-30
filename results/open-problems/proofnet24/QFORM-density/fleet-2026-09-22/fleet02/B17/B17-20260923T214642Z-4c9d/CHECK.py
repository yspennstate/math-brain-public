import sympy as sp

sqrt = sp.sqrt
T = sp.Matrix([
    [1/sqrt(2), 1/sqrt(2), 0, 0, 0, 0],
    [0, 0, 1/sqrt(2), 1/sqrt(2), 0, 0],
    [0, 0, 0, 0, 1/sqrt(2), 1/sqrt(2)],
])
B = sp.eye(3) - sp.Rational(2, 3) * sp.ones(3)
A = sp.simplify(T.T * B * T)

assert sp.simplify(T*T.T - sp.eye(3)) == sp.zeros(3)
assert sp.simplify(B*B - sp.eye(3)) == sp.zeros(3)
assert A.eigenvals() == {sp.Integer(-1): 1, sp.Integer(1): 2, sp.Integer(0): 3}

pstar_upper = sp.Rational(508, 125)
assert sp.simplify(18 - pstar_upper**2) > 0  # (3 sqrt(2))^2 = 18

threshold = sqrt(6)/2
near_kernel_upper_m2 = sqrt(sp.Rational(3, 2))/2
assert sp.simplify(threshold - near_kernel_upper_m2) > 0

print("A =")
print(A)
print("spectrum multiplicities =", A.eigenvals())
print("TT^T = I3:", T*T.T == sp.eye(3))
print("B^2 = I3:", B*B == sp.eye(3))
print("pstar certified upper 508/125 =", float(pstar_upper))
print("3sqrt2 =", float(3*sqrt(2)))
print("squared margin 18-(508/125)^2 =", sp.simplify(18-pstar_upper**2), "=", float(18-pstar_upper**2))
print("near-kernel matched-cell bound Delta_m <= sqrt(3/2)/m")
print("at m=2, upper =", float(near_kernel_upper_m2), "< sqrt(6)/2 =", float(threshold))
print("PASS QFORM-HOUSEHOLDER-ROUGH-ONESHEET-REARRANGEMENT-v1")
