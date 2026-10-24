"""Exact symbolic checker for the R7-06 I0114 / omega*_9 reduction.

This script uses SymPy rational arithmetic only.  It verifies the five low-A2-degree
orbit-polynomial evaluations/derivatives at the two omega*_9 interpolation nodes
and at the top-left corner, and eliminates the first three interpolation constraints.
It does NOT prove the global minorant inequality F-g >= 0.
"""

import sympy as s

x, y = s.symbols("t1 t2")
F_p, F_q, F_r, F1_p, F2_p, F1_q, F22_q = s.symbols(
    "F_p F_q F_r F1_p F2_p F1_q F22_q", real=True
)
A, B, C, D, c0 = s.symbols("A B C D c0", real=True)
Delta = s.symbols("Delta", real=True)

T2 = lambda z: 2*z**2 - 1
T3 = lambda z: 4*z**3 - 3*z
T4 = lambda z: 8*z**4 - 8*z**2 + 1
T5 = lambda z: 16*z**5 - 20*z**3 + 5*z

# A2 orbit polynomials for degrees 0,2,3,4,5.
alpha = s.expand((-1 + 2*y*(x+y))/3)  # P_[1,1/sqrt(3)]
beta = s.expand((-1 + 2*x*(x-3*y+4*y**3))/3)  # P_[2,0]
gamma = s.expand((2*T2(x)*T2(y) + T4(y))/3)  # P_[2,2/sqrt(3)]
delta = s.expand((T3(x)*y + x*T5(y) + T2(x)*T4(y))/3)  # P_[3,1/sqrt(3)]
basis = s.Matrix([1, alpha, beta, gamma, delta])

p = {x: s.Rational(-1,2), y: s.Integer(1)}
q = {x: s.Integer(-1), y: s.Rational(1,2)}
r = {x: s.Integer(-1), y: s.Integer(1)}


def vec(exprs, pt):
    return s.Matrix([s.factor(e.subs(pt)) for e in exprs])


V_p = vec(basis, p)
V_q = vec(basis, q)
V_r = vec(basis, r)
X_p = vec([s.diff(e,x) for e in basis], p)
Y_p = vec([s.diff(e,y) for e in basis], p)
X_q = vec([s.diff(e,x) for e in basis], q)
YY_q = vec([s.diff(e,y,2) for e in basis], q)

assert list(V_p) == [1, 0, s.Rational(-1,2), 0, 0]
assert list(V_q) == [1, s.Rational(-1,2), 1, s.Rational(-1,2), s.Rational(-1,2)]
assert list(V_r) == [1, s.Rational(-1,3), s.Rational(-1,3), 1, s.Rational(-1,3)]
assert list(X_p) == [0, s.Rational(2,3), 0, s.Rational(-4,3), s.Rational(-1,3)]
assert list(Y_p) == [0, 1, -3, 4, s.Rational(-13,2)]
assert list(X_q) == [0, s.Rational(1,3), -2, s.Rational(4,3), s.Rational(7,3)]
assert list(YY_q) == [0, s.Rational(4,3), -8, s.Rational(16,3), s.Rational(28,3)]

# Equality at p and q, plus tangency in t1 at p.  Here Delta=F(p)-F(q).
eqs = [
    s.Eq(c0 + A*V_p[1] + B*V_p[2] + C*V_p[3] + D*V_p[4], F_p),
    s.Eq(c0 + A*V_q[1] + B*V_q[2] + C*V_q[3] + D*V_q[4], F_q),
    s.Eq(A*X_p[1] + B*X_p[2] + C*X_p[3] + D*X_p[4], F1_p),
]
sol = s.solve(eqs, [c0,A,B], dict=True)[0]
sol = {k: s.factor(v.subs(F_q, F_p-Delta)) for k,v in sol.items()}

assert s.factor(sol[A] - (s.Rational(3,2)*F1_p + 2*C + s.Rational(1,2)*D)) == 0
assert s.factor(sol[B] - (s.Rational(1,2)*F1_p + C + s.Rational(1,2)*D - s.Rational(2,3)*Delta)) == 0
assert s.factor(sol[c0] - (F_p + sol[B]/2)) == 0

# Inward derivative condition at p: because the domain lies below t2=1,
# h=F-g >=0 and h(p)=0 imply g_y(p) >= F_y(p).
gy = s.factor((A*Y_p[1] + B*Y_p[2] + C*Y_p[3] + D*Y_p[4]).subs(sol))
assert s.factor(gy - (3*C - s.Rational(15,2)*D + 2*Delta)) == 0

# At q the curved boundary is t1=4*t2^3-3*t2.  It has t1'=0 and t1''=6,
# so h restricted to that boundary has second derivative
# h_yy + 6 h_x >= 0.  The expression below is g_yy+6g_x.
qcombo = s.factor(
    (A*(YY_q[1]+6*X_q[1]) + B*(YY_q[2]+6*X_q[2])
     + C*(YY_q[3]+6*X_q[3]) + D*(YY_q[4]+6*X_q[4])).subs(sol)
)
assert s.factor(qcombo - (-5*F1_p + s.Rational(40,3)*Delta + 15*D)) == 0

# Top-left-corner value constraint g(r)<=F(r).
gr = s.factor((c0 + A*V_r[1] + B*V_r[2] + C*V_r[3] + D*V_r[4]).subs(sol))
assert s.factor(gr - (F_p - s.Rational(5,12)*F1_p + s.Rational(1,2)*C
                      - s.Rational(5,12)*D - Delta/s.Integer(9))) == 0

print("EXACT CHECK PASS")
print("A =", sol[A])
print("B =", sol[B])
print("c0 =", sol[c0])
print("g_y(p) =", gy)
print("g_yy(q)+6g_x(q) =", qcombo)
print("g(r) =", gr)
