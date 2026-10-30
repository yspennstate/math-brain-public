import sympy as sp
import math

h = sp.Rational(3,4)
alpha = sp.sqrt(1-h)
C = sp.Matrix([
    [sp.sqrt(h), 0, 0],
    [alpha/2, sp.Rational(1,2), sp.Rational(1,2)],
    [alpha/2, sp.Rational(1,2),-sp.Rational(1,2)],
    [alpha/2,-sp.Rational(1,2), sp.Rational(1,2)],
    [alpha/2,-sp.Rational(1,2),-sp.Rational(1,2)],
])
M = sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
B = sp.simplify(C*M*C.T)
P = sp.simplify(C*C.T)

assert sp.simplify(C.T*C) == sp.eye(3)
assert B.eigenvals() == {-1: 1, 1: 2, 0: 2}
assert [sp.simplify(P[i,i]) for i in range(1,5)] == [sp.Rational(9,16)]*4
assert [sp.simplify(B[0,i]) for i in range(1,5)] == [sp.sqrt(3)/4,sp.sqrt(3)/4,-sp.sqrt(3)/4,-sp.sqrt(3)/4]
assert [sp.simplify(B[i,i]) for i in range(1,5)] == [sp.Rational(1,2),sp.Rational(1,2),0,0]

K = math.sqrt(math.e)
a0coef = 1/(2*math.sqrt(2*math.e))
pivot_constant = 128*math.sqrt(2)*math.e*(2*math.e)**(1/8)
pair_constant = 3*400**(1/3)*(2*math.e/a0coef**5)**(1/6)

print("C^T C =")
print(C.T*C)
print("B =")
print(B)
print("spectrum =", B.eigenvals())
print("bank leverages =", [P[i,i] for i in range(1,5)])
print("heavy-bank coefficients =", [B[0,i] for i in range(1,5)])
print("bank diagonals =", [B[i,i] for i in range(1,5)])
print("K =", K)
print("a0/s =", a0coef)
print("pivot universal constant =", pivot_constant)
print("pair universal constant =", pair_constant)
assert pivot_constant < 608.045
assert pair_constant < 105.749
print("QFORM_FOUR_BANK_WALSH_OVERLAP_CHECK_PASS")
