import sympy as sp

z = sp.symbols("z")
p1, p2, p3 = sp.symbols("p1 p2 p3")
T = 1/(2-z)
q1, q2, q3 = 1-p1, 1-p2, 1-p3
a1, a2, a3 = 2*p1-1, 2*p2-1, 2*p3-1

B = sp.expand(((1-a1)+a1*z)*((1-a2)+a2*z)*((1-a3)+a3*z))

P1 = sp.simplify(
    q1 + p1*q2*z + p1*p2*q3*z**2 + p1*p2*p3*z**3*T
)
P2 = sp.simplify(
    q1*q2
    + (p1*q2*q3 + q1*p2*q3)*z
    + (q1*p2*p3 + p1*q2*p3 + p1*p2*q3)*z**2*T
    + p1*p2*p3*z**3*T**2
)

A = sp.simplify((1-a1)*(a2+a3-a2*a3)/2)
D = sp.simplify(a3*(1+a1+a2-3*a1*a2)/4)
C = sp.simplify(a3*(1-a1)*(1-a2)/4)

assert sp.simplify(P1 - T*B - (A*(1-z) + D*z*(1-z))) == 0
assert sp.simplify(P2 - T**2*B - C*(1-z)) == 0
assert sp.simplify(sp.diff(B,z).subs(z,1) - (a1+a2+a3)) == 0

sub = {p1:sp.Rational(4,5), p2:sp.Rational(4,5), p3:sp.Rational(4,5)}
target_B = (
    sp.Rational(8,125)
    + sp.Rational(36,125)*z
    + sp.Rational(54,125)*z**2
    + sp.Rational(27,125)*z**3
)
assert sp.simplify(B.subs(sub) - target_B) == 0
assert sp.simplify(A.subs(sub) - sp.Rational(21,125)) == 0
assert sp.simplify(D.subs(sub) - sp.Rational(21,125)) == 0
assert sp.simplify(C.subs(sub) - sp.Rational(3,125)) == 0
assert sp.simplify((P1-T*B).subs(sub) - sp.Rational(21,125)*(1-z**2)) == 0
assert sp.simplify((P2-T**2*B).subs(sub) - sp.Rational(3,125)*(1-z)) == 0

print("GENERAL_ROW1_IDENTITY=PASS")
print("GENERAL_ROW2_IDENTITY=PASS")
print("IMMIGRATION_MEAN_IDENTITY=PASS")
print("BENCHMARK_B(z)=(8+36*z+54*z^2+27*z^3)/125")
print("BENCHMARK_A=D=21/125")
print("BENCHMARK_C=3/125")
print("BENCHMARK_ROW1_DEFECT=(21/125)*(1-z^2)")
print("BENCHMARK_ROW2_DEFECT=(3/125)*(1-z)")
print("ALL_EXACT_CHECKS_PASS")
