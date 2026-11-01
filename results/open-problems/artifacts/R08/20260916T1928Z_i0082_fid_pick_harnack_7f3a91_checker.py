#!/usr/bin/env python3
"""
R08 I0082 exact self-check + independent exact audit of R09 Tang Q4.11 package.
No floating assertions are used.
"""
from fractions import Fraction
import sympy as sp

def r08_exact_identities():
    x,r=sp.symbols('x r', positive=True)
    A = r/x + (1-r)*sp.log(x/(1-x))
    Ap=sp.factor(sp.diff(A,x))
    target=(x-r)/(x**2*(1-x))
    assert sp.simplify(Ap-target)==0
    assert sp.simplify(Ap.subs(x,r))==0
    assert sp.simplify(Ap.subs(x,2*r)-1/(4*r*(1-2*r)))==0
    assert sp.simplify(A.subs(x,sp.Rational(1,2))-2*r)==0
    assert sp.simplify(Ap.subs(x,sp.Rational(1,2))-(4-8*r))==0
    X0,Y0,X2,Y2=sp.symbols('X0 Y0 X2 Y2', real=True, positive=True)
    num=(X2-X0)**2+(Y2-Y0)**2
    den=(X2-X0)**2+(Y2+Y0)**2
    assert sp.expand(den-num)==4*Y0*Y2
    c,z,t=sp.symbols('c z t')
    lhs=c*(c+t*z)/(z-c*t)
    rhs=(c**2+z**2)/(z-c*t)-z
    assert sp.simplify(lhs-rhs)==0
    print("R08_C005_boundary_derivative_identities=PASS")
    print("R08_C005_Harnack_crossratio_identity=PASS")
    print("R08_C005_LK_dilation_identity=PASS")

def r09_independent_audit():
    p,y=sp.symbols('p y')
    x0,x2=sp.symbols('x0 x2')
    E0=sp.expand(x0 - (1-(1-p*y)*(1-p*x2)))
    E1=sp.expand(y - (1-(1-p*x0)*(1-p*y)))
    E2=sp.expand(x2 - (1-(1-p*x0)**2*(1-p*y)*(1-p*x2)**2))
    sol_x0=sp.factor(y*(1-p)/(p*(1-p*y)))
    sol_x2=sp.factor(y*(p**3*y-p**2-p+1)/(p**2*(1-p*y)**2))
    assert sp.simplify(E0.subs({x0:sol_x0,x2:sol_x2}))==0
    assert sp.simplify(E1.subs({x0:sol_x0,x2:sol_x2}))==0
    P=(p**6*y**4 -5*p**5*y**3 -p**4*y**3 +10*p**4*y**2
       +p**3*y**3 +2*p**3*y**2 -9*p**3*y
       -2*p**2*y**3 +p**2*y**2 -3*p**2*y +3*p**2
       +p*y**3 +2*p -y**3 +2*y**2 -y -1)
    expr=sp.factor(E2.subs({x0:sol_x0,x2:sol_x2}))
    ratio=sp.factor(expr/P)
    expected=-y*(p-1)/(p**2*(p*y-1)**5)
    assert sp.simplify(ratio-expected)==0
    p0=sp.Rational(17,50)
    P0=sp.Poly(P.subs(p,p0),y,domain=sp.QQ)
    a=sp.Rational(16112,10**6); b=sp.Rational(16113,10**6)
    assert P0.count_roots(a,b)==1
    assert P0.eval(a)>0 and P0.eval(b)<0
    Py=sp.diff(P,y); Py0=sp.Poly(Py.subs(p,p0),y,domain=sp.QQ)
    assert Py0.count_roots(a,b)==0
    mid=(a+b)/2
    assert Py0.eval(mid)<0
    Pp=sp.diff(P,p); Ppp=sp.diff(Pp,p); Ppy=sp.diff(Pp,y); Pyy=sp.diff(Py,y)
    yp=-Pp/Py
    ypp=sp.factor(-(Ppp+2*Ppy*yp+Pyy*yp**2)/Py)
    diff=sp.factor(ypp-sp.Rational(4929,1000))
    num,den=map(sp.factor,sp.fraction(diff))
    num0=sp.Poly(num.subs(p,p0),y,domain=sp.QQ); den0=sp.Poly(den.subs(p,p0),y,domain=sp.QQ)
    assert num0.count_roots(a,b)==0 and den0.count_roots(a,b)==0
    assert num0.eval(mid)<0 and den0.eval(mid)<0
    for rat_expr,name in [(sol_x0,"x0"),(sol_x2,"x2")]:
        n,d=map(sp.factor,sp.fraction(rat_expr.subs(p,p0)))
        pn=sp.Poly(n,y,domain=sp.QQ); pd=sp.Poly(d,y,domain=sp.QQ)
        assert pd.count_roots(a,b)==0 and pn.count_roots(a,b)==0
        assert pn.eval(mid)*pd.eval(mid)>0
        one_num=sp.factor(d-n); po=sp.Poly(one_num,y,domain=sp.QQ)
        assert po.count_roots(a,b)==0 and po.eval(mid)*pd.eval(mid)>0
    k=sp.symbols('k', integer=True, positive=True)
    theta=p**(k-2)*(2*p-1)
    theta2=sp.factor(sp.diff(theta,p,2))
    claimed=(k-2)*p**(k-4)*(2*(k-1)*p-(k-3))
    assert sp.simplify(theta2-claimed)==0
    assert sp.simplify(k**2-16*(k-4)-(k-8)**2)==0
    print("R09_AUDIT_elimination_identity=PASS")
    print("R09_AUDIT_unique_root_interval=PASS")
    print("R09_AUDIT_physical_coordinates=PASS")
    print("R09_AUDIT_curvature_gt_4929_over_1000=PASS")
    print("R09_AUDIT_stem_unbounded_formula=PASS")
    print("R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02=PASS")

if __name__=="__main__":
    r08_exact_identities()
    r09_independent_audit()
    print("ALL_EXACT_CHECKS_PASS")
