import sympy as sp

a,b,c,x,y,ell,Delta=sp.symbols("a b c x y ell Delta", nonzero=True, real=True)
q=a*x**2+2*b*x*y+c*y**2
qx=sp.diff(q,x)
J=sp.factor(sp.det(sp.Matrix([
    [sp.diff(q,x), sp.diff(q,y)],
    [sp.diff(qx,x), sp.diff(qx,y)]
])))
assert J == -4*y*(a*c-b**2)

# Optimize 2/T + 2*S + T/S.
T=2**sp.Rational(1,3)
S=2**(-sp.Rational(1,3))
Csb=sp.simplify(2/T+2*S+T/S)
assert Csb == 3*2**sp.Rational(2,3)

# A centered radius-r interval has length 2r.
Kball=sp.simplify(Csb*2**sp.Rational(2,3))
assert Kball == 3*2**sp.Rational(4,3)

# If F(r)<=K r^(2/3), the half-Riesz near/far bound is
# 4 K H^(1/6)+H^(-1/2). Put z=H^(1/6).
K,z=sp.symbols("K z", positive=True)
zopt=(sp.Rational(3,4)/K)**sp.Rational(1,4)
pot=sp.simplify((4*K*z+z**-3).subs(z,zopt))
final=sp.simplify(pot.subs(K,Kball))
assert final == 16*sp.sqrt(2)

print("JACOBIAN =", J)
print("SMALL_BALL_CONSTANT =", Csb)
print("BALL_CONSTANT =", Kball)
print("HALF_RIESZ_CONSTANT =", final)
print("HALF_RIESZ_CONSTANT_NUM =", sp.N(final, 15))
print("STATUS=PASS")
