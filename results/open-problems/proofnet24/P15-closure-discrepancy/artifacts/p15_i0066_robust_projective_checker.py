from fractions import Fraction as F
import sympy as sp

x, y = sp.symbols("x y", real=True)
z = sp.Matrix([x, y])
r2 = x*x + y*y


def Q(M, Cs):
    drift = 4*r2*(z.dot(M*z))
    noise = 0
    for C in Cs:
        Cz = C*z
        noise += 4*(z.dot(Cz))**2 + 2*r2*(Cz.dot(Cz))
    return sp.expand(drift-noise)


M0 = sp.diag(2, 3)
J = sp.Matrix([[0, -1], [1, 0]])
D = sp.diag(1, -1)
C10 = J
C20 = sp.Rational(1, 2)*D

q0 = sp.expand(Q(M0, [C10, C20]))
base_margin = sp.Rational(9, 2)
rem0 = sp.factor(q0-base_margin*r2**2)
assert rem0 == 4*y**2*(2*x**2+y**2)

delta = F(1, 8)
loss = 4*delta + (12*F(1, 1)*delta + 6*delta*delta) + (12*F(1, 2)*delta + 6*delta*delta)
robust_margin = F(9, 2)-loss
assert loss == F(47, 16)
assert robust_margin == F(25, 16)

M1 = sp.diag(sp.Rational(17, 8), sp.Rational(23, 8))
C11 = sp.Rational(7, 8)*J
C21 = sp.Rational(5, 8)*D
q1 = sp.expand(Q(M1, [C11, C21]))
rem1 = sp.expand(q1-sp.Rational(25, 16)*r2**2)
expected1 = (49*x**4 + 246*x**2*y**2 + 97*y**4)/16
assert sp.expand(rem1-expected1) == 0

comm = C11*C21-C21*C11
assert comm != sp.zeros(2)

t = sp.symbols("t", real=True)
h0 = sp.expand((q0-base_margin*r2**2).subs({x: 1, y: t}))
h1 = sp.expand(rem1.subs({x: 1, y: t}))
assert h0 == 8*t**2 + 4*t**4
assert h1 == sp.Rational(49, 16)+sp.Rational(246, 16)*t**2+sp.Rational(97, 16)*t**4
assert sp.LC(sp.Poly(h1, t)) == sp.Rational(97, 16)

print("P15 I0066 robust/projective exact checker")
print("baseline_Q =", q0)
print("baseline_remainder_at_9/2 =", rem0)
print("operator_norm_ball_radius =", delta)
print("worst_case_loss_bound =", loss)
print("certified_uniform_margin =", robust_margin)
print("endpoint_Q =", q1)
print("endpoint_remainder_at_25/16 =", sp.factor(rem1))
print("endpoint_commutator =", comm.tolist())
print("projective_baseline =", h0)
print("projective_endpoint =", h1)
print("ALL_EXACT_CHECKS_PASSED")
