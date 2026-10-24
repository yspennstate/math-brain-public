from sympy import symbols, sqrt, Rational, simplify

# HARD7-01 exact symbolic self-check for Xi generalized-radii geometry.
# This verifies only algebraic identities used in the analytic report.

z1, z2 = symbols("z1 z2", positive=True)
z3 = 1/(z1*z2)

def lam(z):
    return (sqrt(z) + 1/sqrt(z))/2

e1 = z1 + z2 + z3
e2 = 1/z1 + 1/z2 + 1/z3
P_identity = simplify(8*lam(z1)*lam(z2)*lam(z3) - (2 + e1 + e2))
assert P_identity == 0
print("PRODUCT_IDENTITY = PASS")

r1, r2 = symbols("r1 r2", positive=True)
r3 = 1/(r1*r2)
A = r1 + r2 + r3
B = 1/r1 + 1/r2 + 1/r3
q = simplify((2 + A + B)/8)
c1 = lam(r1)
c2 = lam(r2)
c3 = lam(r3)
assert simplify(q - c1*c2*c3) == 0
print("BOX_VOLUME_IDENTITY = PASS")

# Explicit selector for equal-volume aligned boxes:
# t1=1/r1, t2=1/r2, z3=1/(t1*t2)=1/r3.
t1 = 1/r1
t2 = 1/r2
t3 = 1/(t1*t2)
assert simplify((t1+t2+t3) - B) == 0
assert simplify((1/t1+1/t2+1/t3) - A) == 0
assert simplify(lam(t1)-c1) == 0
assert simplify(lam(t2)-c2) == 0
assert simplify(lam(t3)-c3) == 0
print("BOX_SELECTOR_SATURATES_B3 = PASS")

# Exact witness used in prior AF-point obstruction: r=(4,2,1/8).
rv1, rv2, rv3 = Rational(4), Rational(2), Rational(1,8)
tv1, tv2, tv3 = 1/rv1, 1/rv2, 1/rv3
lv1, lv2, lv3 = lam(tv1), lam(tv2), lam(tv3)
Av = rv1 + rv2 + rv3
Bv = 1/rv1 + 1/rv2 + 1/rv3
qv = simplify((2+Av+Bv)/8)
Sv = simplify(lv1+lv2+lv3)
Pv = simplify(lv1*lv2*lv3)
assert qv == Rational(135,64)
assert simplify(Pv-qv) == 0
assert simplify(Sv - (Rational(5,4)+Rational(15,8)*sqrt(2))) == 0
assert simplify(tv1+tv2+tv3-Bv) == 0
assert simplify(1/tv1+1/tv2+1/tv3-Av) == 0
print("PRIOR_WITNESS_ADAPTIVE_SELECTOR = PASS")
print("q =", qv)
print("sum_lambda =", Sv)
print("selector =", tv1, tv2)

# Pairwise Aleksandrov-Fenchel scalar inequalities alone do not force
# existence of a simultaneous-saturation triple.  The rational pair below
# satisfies a^2 >= 3b and b^2 >= 3a but has negative cubic discriminant.
a = Rational(61,20)
b = Rational(31,10)
Delta = simplify(a*a*b*b - 4*a**3 - 4*b**3 - 27 + 18*a*b)
assert simplify(a*a-3*b) == Rational(1,400)
assert simplify(b*b-3*a) == Rational(23,50)
assert Delta == Rational(-2699,40000)
print("AF_ONLY_NOT_ENOUGH_FOR_DOUBLE_SATURATION = PASS")
print("Delta_test =", Delta)
print("ALL_EXACT_CHECKS_PASS = True")
