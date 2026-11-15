"""Exact triangle concavity and inherited two-triangle equality at infinity."""
import sympy as s
import prior_triangles as tri
from split34_audit import value


def main():
    k,g,t=s.symbols('k g t');V=s.Matrix([1,2,-3]);R=V.dot(V)
    vv=V*V.T/R;H3=s.eye(3)-s.ones(3)/3;P3=H3-vv;L3=H3-g*vv
    U=s.Matrix([3,1,-1,-3]);H4=s.eye(4)-s.ones(4)/4;P4=U*U.T/U.dot(U);L4=H4-(H4-P4)/10
    L=s.diag(L4,L3);P=s.diag(P4,P3)
    expr=s.Poly(s.expand(value(L,P,k)),g);m=sum(v**3 for v in V)**2/R**3
    mm,mo,ho=s.symbols('mm mo ho')
    abstract=-s.Rational(5,3)-1/(6*k)+1/(3*k*k)+4*(1-1/k)*mm
    q=abstract.subs(mm,m)
    assert s.cancel(expr.coeff_monomial(g*g)-q)==0
    mass=mo+1-g/2;hd=ho+s.Rational(2,3)-g/6
    general=(2*g*(1-g)+2*(k+2)/k*g*g*(s.Rational(1,6)-mm)-g+6*g*g*mm
             +(mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*hd))
    assert s.cancel(s.Poly(s.expand(general),g).coeff_monomial(g*g)-abstract)==0
    # For zero-sum unit v in R^3, ||v^2-1/3-(sum v^3)v||^2=1/6-m.
    # Hence m<=1/6, so the displayed quadratic coefficient is negative.
    bound=-1-s.Rational(5,6)/k+1/(3*k*k)
    assert s.cancel(abstract.subs(mm,s.Rational(1,6))-bound)==0
    z=s.symbols('z',nonnegative=True)
    assert all(c>0 for c in s.Poly(s.expand((6*k*k+5*k-2).subs(k,5+z)),z).coeffs())
    # Inherited finite-k corner polynomials, plus explicit leading-k equality.
    x,y=s.symbols('x y',nonnegative=True)
    ps=(2+3*x)/(6*(1+x));qs=(2+3*y)/(6*(1+y))
    for ge in (0,1/(3*tri.p)):
        for he in (0,1/(3*tri.q)):
            expr=tri.T.subs({tri.g:ge,tri.h:he}).subs({tri.p:ps,tri.q:qs,tri.k:5+z})
            num,den=s.fraction(s.factor(expr));poly=s.Poly(num,x,y,z)
            assert all(c>=0 for c in poly.coeffs())
            lead=s.Poly(num,z).coeff_monomial(z*z);lp=s.Poly(lead,x,y)
            if ge==0 or he==0:assert lp.coeff_monomial(1)>0
            else:
                assert lp.coeff_monomial(x**3)>0 and lp.coeff_monomial(y**3)>0 and lp.coeff_monomial(x**3*y**3)>0
                assert lead.subs({x:0,y:0})==0
    print('PROVED (split34_reduction.py): strict separate triangle-gap concavity, all two-triangle corner signs and equality at infinity.')

if __name__=='__main__':main()
