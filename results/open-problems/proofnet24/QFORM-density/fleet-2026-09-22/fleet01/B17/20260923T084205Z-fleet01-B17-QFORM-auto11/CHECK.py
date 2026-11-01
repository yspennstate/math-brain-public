from sympy import Matrix, Rational, diag, sqrt, symbols, factor, simplify
from mpmath import mp

mp.dps = 50

O = Matrix([
    [1, 1, 1, 1],
    [1,-1, 1,-1],
    [1, 1,-1,-1],
    [1,-1,-1, 1],
]) / 2
J0 = diag(1,1,-1,0)
A = O*J0*O.T
lam = symbols("lam")

assert O.T*O == Matrix.eye(4)
assert factor(A.charpoly(lam).as_expr()) == lam*(lam-1)**2*(lam+1)
assert 4*A == Matrix([
    [1,-1,3,1],
    [-1,1,1,3],
    [3,1,1,-1],
    [1,3,-1,1],
])

C = 8*(sqrt(2)-1)
assert simplify(3*sqrt(2)-C) == 8-5*sqrt(2)
assert 8-5*sqrt(2) > 0
assert simplify(2-Rational(39,28)**2) == Rational(47,784)
assert C > Rational(22,7)

# Deterministic angular check of the exact cone formula.
def invD(theta):
    c = abs(mp.cos(theta))
    s = abs(mp.sin(theta))
    D = 2*(1+max(c,s))
    return 1/D

breaks = [k*mp.pi/4 for k in range(9)]
I = 2*sum(mp.quad(invD,[breaks[k],breaks[k+1]]) for k in range(8))
C_mp = 8*(mp.sqrt(2)-1)
assert abs(I-C_mp) < mp.mpf("1e-40")

print("QFORM_HADAMARD4_CHECK_PASS")
print("charpoly =", factor(A.charpoly(lam).as_expr()))
print("8(sqrt(2)-1) =", mp.nstr(C_mp,30))
print("3sqrt(2) - C =", mp.nstr(3*mp.sqrt(2)-C_mp,30))
print("C - 22/7 =", mp.nstr(C_mp-mp.mpf(22)/7,30))
print("cone quadrature error =", mp.nstr(I-C_mp,10))
