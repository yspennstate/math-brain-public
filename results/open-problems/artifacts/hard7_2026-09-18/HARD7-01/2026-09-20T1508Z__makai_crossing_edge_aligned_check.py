from sympy import symbols, Rational, integrate, simplify, factor, expand, Poly

a,b,x,y,X,Y = symbols("a b x y X Y", positive=True)
x0 = -(1-b)/(a-b)

u1=(a*x+1)/b
u2=x+1
u3=1

area = simplify(2*(integrate(u1,(x,-1/a,x0))+
                   integrate(u2,(x,x0,0))+
                   integrate(u3,(x,0,1/a))))
AREA = (4*a-a*b-2*b-1)/(a*(a-b))
assert simplify(area-AREA)==0

IBneg = integrate(integrate(y-x,(y,0,u1)),(x,-1/a,x0)) + integrate(integrate(y-x,(y,0,u2)),(x,x0,0))
IBpos = integrate(integrate(x,(y,0,x)) + integrate(y,(y,x,1)),(x,0,1/a))
IB = simplify(2*(IBneg+IBpos))
IBF = (6*a**3-2*a**3*b-3*a**2*b-b)/(3*a**3*(a-b))
assert simplify(IB-IBF)==0

IEneg = integrate(integrate(b*y-a*x,(y,0,u1)),(x,-1/a,x0)) + integrate(integrate(b*y-a*x,(y,0,u2)),(x,x0,0))
IEpos = integrate(integrate(a*x,(y,0,a*x/b)) + integrate(b*y,(y,a*x/b,1)),(x,0,b/a)) + integrate(integrate(a*x,(y,0,1)),(x,b/a,1/a))
IE = simplify(2*(IEneg+IEpos))
IEF = (6*a-b**3-3*b-2)/(3*a*(a-b))
assert simplify(IE-IEF)==0

J = factor(2*area-IB-IE)
JF = (12*a**3-4*a**3*b+a**2*b**3-6*a**2*b-4*a**2+b)/(3*a**3*(a-b))
assert simplify(J-JF)==0

Kvol=(1+a+a*b)/6
defect=factor(Kvol*J-Rational(2,3))
D=expand(defect*18*a**3*(a-b))
DF=(-4*a**4*b**2 + 8*a**4*b + a**3*b**4 + a**3*b**3 - 6*a**3*b**2
    -2*a**3*b + 8*a**3 + a**2*b**3 - 6*a**2*b - 4*a**2
    +a*b**2+a*b+b)
assert simplify(D-DF)==0

P=Poly(expand(D.subs({a:1+X,b:1-Y})),X)
coeffs=P.all_coeffs()
expected=[
    4*(1-Y**2),
    Y**4-5*Y**3-13*Y**2+7*Y+18,
    3*Y**4-16*Y**3-12*Y**2+24*Y+21,
    3*Y**4-17*Y**3+24*Y+6,
    Y*(Y**3-6*Y**2+3*Y+6)
]
assert all(simplify(c-e)==0 for c,e in zip(coeffs,expected))

samples=[(Rational(2),Rational(1,2)),(Rational(2),Rational(4,5)),(Rational(5),Rational(1,10)),(Rational(1),Rational(1,2)),(Rational(3,2),Rational(1))]
for A,B in samples:
    if A==B:
        continue
    p=simplify(((1+a+a*b)/6*JF).subs({a:A,b:B}))
    assert p > Rational(2,3)

print("AREA =", factor(AREA))
print("INT_hB =", factor(IBF))
print("INT_hE =", factor(IEF))
print("DUAL_J =", factor(JF))
print("DEFECT_DENOM = 18*a^3*(a-b)")
print("DEFECT_NUM =", factor(DF))
print("DEFECT_NUM_AFTER_a=1+X_b=1-Y =", expand(P.as_expr()))
print("COEFFICIENTS_IN_X =", coeffs)
print("SAMPLE_PRODUCTS =")
for A,B in samples:
    if A==B:
        continue
    p=simplify(((1+a+a*b)/6*JF).subs({a:A,b:B}))
    print("  a=",A,"b=",B,"product=",p,"gap=",simplify(p-Rational(2,3)))
print("SYMBOLIC_IDENTITIES_PASS = True")
print("ALL_EXACT_CHECKS_PASS = True")
