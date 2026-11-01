import itertools
import sympy as sp

m = 8
c = sp.Rational(3, 4)
s1 = [1, 1, 1, 1, -1, -1, -1, -1]
s2 = [1, 1, -1, -1, 1, 1, -1, -1]
sqrtm = sp.sqrt(m)
v0 = [1 / sqrtm] * m
v1 = [sp.Integer(s) / sqrtm for s in s1]
v2 = [sp.Integer(s) / sqrtm for s in s2]

rows = [[sp.sqrt(c), 0, 0]]
for i in range(m):
    rows.append([sp.sqrt(1-c) * v0[i], v1[i], v2[i]])
U = sp.Matrix(rows)
Lambda = sp.diag(1, 1, -1)
A = sp.simplify(U * Lambda * U.T)

assert sp.simplify(U.T * U) == sp.eye(3)
assert A.rank() == 3
assert A.eigenvals() == {-1: 1, 1: 2, 0: 6}
assert sp.simplify(A[0, 0]) == sp.Rational(3, 4)
for i in range(1, m+1):
    assert sp.simplify(A[i, i]) == sp.Rational(1, 32)

maxdet = sp.Rational(0)
maxw = sp.Rational(0)
argmax = None
for I in itertools.combinations(range(m+1), 3):
    det = abs(sp.det(A.extract(I, I)))
    if det > maxdet:
        maxdet = det
    for k in I:
        w = sp.Pow(abs(A[k, k] * det), sp.Rational(1, 4))
        if float(w.evalf()) > float(maxw.evalf()):
            maxw = w
            argmax = (I, k, det, A[k, k])

assert sp.simplify(maxdet - sp.Rational(3, 64)) == 0
assert sp.simplify(maxw - sp.sqrt(3)/4) == 0
assert sp.simplify(maxw - sp.sqrt(2*c)/sp.sqrt(m)) == 0

print("U^T U =", U.T * U)
print("rank(A) =", A.rank())
print("eigenvalues =", A.eigenvals())
print("diagonal =", [sp.simplify(A[i, i]) for i in range(m+1)])
print("max_abs_principal_3x3_det =", maxdet)
print("max_pivot_weight =", maxw)
print("argmax =", argmax)
print("theoretical_heavy_bound =", sp.sqrt(2*c)/sp.sqrt(m))
print("QFORM_HEAVY_WALSH_CHECK_PASS")
