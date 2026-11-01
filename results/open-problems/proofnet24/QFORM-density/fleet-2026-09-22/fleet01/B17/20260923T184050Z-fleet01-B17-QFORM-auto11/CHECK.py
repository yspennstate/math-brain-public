import sympy as sp

x, y, z, t = sp.symbols("x y z t", positive=True)

B = sp.Matrix([
    [sp.Rational(1,3), sp.Rational(-2,3), sp.Rational(-2,3)],
    [sp.Rational(-2,3), sp.Rational(1,3), sp.Rational(-2,3)],
    [sp.Rational(-2,3), sp.Rational(-2,3), sp.Rational(1,3)],
])
assert B*B == sp.eye(3)
assert B.det() == -1
assert B.trace() == 1

w = sp.symbols("w")
ls = sp.series(sp.log(sp.sin(w)/w), w, 0, 8).removeO()
assert sp.expand(ls - (-w**2/sp.Integer(6)-w**4/sp.Integer(180)-w**6/sp.Integer(2835))) == 0

eps = sp.symbols("eps")
corr = -t**4*eps/sp.Integer(20) - t**6*eps**2/sp.Integer(105)
ser = sp.series(sp.exp(corr), eps, 0, 3).removeO()
assert sp.expand(ser - (1-t**4*eps/sp.Integer(20)+eps**2*(-t**6/sp.Integer(105)+t**8/sp.Integer(800)))) == 0

e2, e3 = sp.symbols("e2 e3", nonnegative=True)
c1 = -sp.Rational(3,640)*(59-13*(1-2*e2))
c2 = (449085*e2**2-125514*e2-337380*e3-17411)/sp.Integer(2867200)
axis2 = -sp.Rational(17411,2867200)

assert sp.simplify(c1.subs(e2,0)+sp.Rational(69,320)) == 0
assert sp.simplify(c2.subs({e2:0,e3:0})-axis2) == 0
assert sp.simplify(c1.subs(e2,sp.Rational(1,3))+sp.Rational(41,160)) == 0
assert sp.simplify(c2.subs({e2:sp.Rational(1,3),e3:sp.Rational(1,27)})+sp.Rational(3511,460800)) == 0

t0 = sp.Rational(41838,149695)
G = (1347255*t**2-826382*t+112460)/9
assert t0 > sp.Rational(1,4)
assert G.subs(t,t0) == -sp.Rational(397141244,269451)
assert G.subs(t,sp.Rational(1,3)) == -sp.Rational(39917,27)

partner = sp.simplify(2/(sp.Integer(2)-sp.sqrt(3)/2))
assert partner == (16+4*sp.sqrt(3))/13
assert sp.N(partner,20) < 2
assert sp.N(partner,20) < sp.N(3*sp.sqrt(2),20)

print("QFORM_B17_SECOND_ORDER_CHECK_PASS")
print("balanced c1 =", -sp.Rational(41,160))
print("balanced c2 =", -sp.Rational(3511,460800))
print("axis c1 =", -sp.Rational(69,320))
print("axis c2 =", axis2)
print("partner R=2 bound =", sp.N(partner,20))
print("3sqrt2 =", sp.N(3*sp.sqrt(2),20))
