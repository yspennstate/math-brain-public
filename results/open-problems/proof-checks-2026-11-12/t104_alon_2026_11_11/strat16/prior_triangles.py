"""PROVED on successful replay: two triangle carriers, with arbitrary isolates."""
import sympy as s

g,h,p,q,k=s.symbols('g h p q k',real=True)
m=9*p*p*(s.Rational(1,2)-p)
n=9*q*q*(s.Rational(1,2)-q)
mass=(4-g-h)/2
hd=s.Rational(4,3)-(g+h)/6
B=g*g*(s.Rational(1,6)-m)+h*h*(s.Rational(1,6)-n)
Y=g-6*g*g*m+h-6*h*h*n
X1=2*(g*(1-g)+h*(1-h))
X2=2*(k+2)/k*B
X3=(mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*hd)
T=s.expand(X1+X2+X3-Y)

def main():
    x,y,z=s.symbols('x y z',nonnegative=True)
    # Coefficients are increasing in m,n; m,n <= 1/6 proves strict concavity.
    for var in [g,h]:
        c=s.factor(T.coeff(var,2))
        if var==h:c=c.subs(q,p)
        c=s.factor(c.subs(p,(2+3*x)/(6*(1+x))).subs(k,4+z))
        num,den=s.fraction(c)
        assert all(v<0 for v in s.Poly(num,x,z).coeffs())
        print('PROVED: strict concavity in',var)
    for gg in [0,1/(3*p)]:
        for hh in [0,1/(3*q)]:
            expr=T.subs({g:gg,h:hh,k:4+z,p:(2+3*x)/(6*(1+x)),q:(2+3*y)/(6*(1+y))},simultaneous=True)
            # Simultaneous substitution of g endpoint leaves its p unchanged.
            expr=expr.subs({p:(2+3*x)/(6*(1+x)),q:(2+3*y)/(6*(1+y))})
            num,den=s.fraction(s.factor(expr))
            poly=s.Poly(num,x,y,z)
            neg=sum(bool(v<0) for v in poly.coeffs())
            print('endpoint',gg,hh,'terms',len(poly.terms()),'negative',neg,'den',s.factor(den))
            assert not neg
            if gg!=0 and hh!=0:
                assert poly.coeff_monomial(x)>0 and poly.coeff_monomial(y)>0
                assert all(poly.coeff_monomial(v)>0 for v in [x**3,y**3,x**3*y**3])
            elif gg!=0:assert poly.coeff_monomial(x**3)>0
            elif hh!=0:assert poly.coeff_monomial(y**3)>0
    print('PROVED: all endpoint polynomials nonnegative, hence T>=0 for N>=6.')

if __name__=='__main__':main()
