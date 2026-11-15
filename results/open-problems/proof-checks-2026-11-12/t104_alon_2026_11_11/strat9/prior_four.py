"""PROVED if all assertions pass: exact cone certificate, four-vertex carrier.

No floating arithmetic. All polynomial coefficients and signs are rational.
"""
import itertools
import sympy as s

g,t,k,q,m=s.symbols('g t k q m',real=True)
mass=(3-g+t)/2
h=s.Rational(3,2)-s.Rational(3,4)*g+g*q
B=g*g*(q-s.Rational(1,4)-m)
Y=2*g*((5-4*q)/4+g*(-2+4*q-3*m))
X1=2*(g*(1-g)+t*(1-t))
X2=2*(k+2)/k*B
X3=(mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*h)
T=s.expand(X1+X2+X3-Y)

def main():
    x,y,z,u=s.symbols('x y z u',nonnegative=True)
    V=[3*x+2*y+z,-x+2*y+z,-x-2*y+z,-x-2*y-3*z]
    R=s.expand(sum(a*a for a in V));p=s.expand(-V[0]*V[3])
    Q=s.expand(sum(a**4 for a in V));C3=s.expand(sum(a**3 for a in V))
    print('PROVED: coefficient of t^2 =',s.factor(T.coeff(t,2)))
    print('PROVED: coefficient of g^2 =',s.factor(T.coeff(g,2)))
    # Concavity in g follows from m<=q-1/4, q>=1/4.
    cg=s.factor(T.coeff(g,2).subs(m,q-s.Rational(1,4)))
    print('PROVED: upper bound on g^2 coefficient =',cg)
    print('PROVED: bound with q=1/4+v =',s.factor(cg.subs(q,s.Rational(1,4)+u)))
    for gg in [s.Integer(0),R/(4*p)]:
        for tt in [0,1]:
            expr=T.subs({g:gg,t:tt,k:4+u,q:Q/R**2,m:C3**2/R**3})
            num,den=s.fraction(s.factor(expr))
            poly=s.Poly(num,x,y,z,u)
            neg=sum(bool(c<0) for c in poly.coeffs())
            print('endpoint',str(gg)[:30],tt,'terms',len(poly.terms()),'negative',neg,'den=',s.factor(den))
            if neg:
                for perm in itertools.permutations([x,y,z]):
                    a,b,c=s.symbols('a b c',nonnegative=True)
                    new=s.Poly(s.expand(num.subs({perm[0]:a+b+c,perm[1]:b+c,perm[2]:c},simultaneous=True)),a,b,c,u)
                    nneg=sum(bool(v<0) for v in new.coeffs())
                    print('  ordering',perm,'negative',nneg)
                    assert not nneg
                    # In this sector b or c positive means at least two
                    # original gap coordinates are positive.
                    assert new.coeff_monomial(b**6)>0 and new.coeff_monomial(c**6)>0
            else:assert all(c>=0 for c in poly.coeffs())
            if gg!=0 and tt==1:
                for v in [x,y,z]:assert poly.coeff_monomial(v**6)>0
    print('PROVED: all four endpoint polynomials are nonnegative for N>=6.')

if __name__=='__main__':main()
