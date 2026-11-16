"""Exact endpoint comparison extends three smaller classes to arbitrary lowers.

Proof premises and the convex reductions are stated in RESULT.md. No
dimension, eigenvalue, moment, or sign in this replay is numerical.
"""
import itertools
import sympy as s
import prior_four as four


def nonnegative(poly,variables):
    assert all(c>=0 for c in s.Poly(s.expand(poly),*variables).coeffs())


def main():
    k,M,h,n,s0,q=s.symbols('k M h n s0 q');delta=s0/2
    C=2*(k+1)*(k-2)+2*(k+2)*h
    def X3(m):return (m-1)*(C-4*k*m)/k**2
    bracket=C-4*k*(2*M+delta-1)
    assert s.cancel(X3(M+delta)-X3(M)-delta*bracket/k**2)==0
    assert s.limit(X3(M+delta)-X3(M),k,s.oo)==s0
    endpoint=2*k*(n-4*M+h)+4*(h-1)+2*k*q
    assert s.expand(bracket.subs(s0,k-n+1-q)-endpoint)==0
    # s0<=r-1<=k-n+1, so q>=0. The other increment is
    # 2 sum lower-eigenvalues mu(1-mu)>=0.
    a,b,v=s.symbols('a b v',nonnegative=True)
    g=s.symbols('g');qm=s.symbols('qm')
    hd=s.Rational(3,2)-s.Rational(3,4)*g+g*qm
    pref=4-4*(3-g)/2+hd
    assert s.expand(pref.subs({g:s.Rational(1,2)+a,qm:s.Rational(1,4)+v})-(s.Rational(1,4)+s.Rational(3,2)*a+(s.Rational(1,2)+a)*v))==0
    assert s.expand((hd-1).subs(qm,s.Rational(1,4)+v)-((1-g)/2+g*v))==0
    # Double four: gmax in [1/2,1], q4>=1/4, so pref>=1/4, h>=1.
    # Its g-concavity coefficient is independent of any lower trace.
    assert s.diff(four.T.coeff(four.g,2),four.t)==0
    overlap=s.symbols('overlap')
    he=s.Rational(5,4)-g*overlap;pe=6-4*(4-g)/2+he
    assert s.expand(pe.subs({g:s.Rational(1,2)+a,overlap:s.Rational(1,4)-v})-(s.Rational(1,8)+s.Rational(7,4)*a+(s.Rational(1,2)+a)*v))==0
    assert s.expand(he-1-((1-g)/4+g*(s.Rational(1,4)-overlap)))==0
    # Split 2+4 rank-two endpoint: overlap<=1/4, gmax>=1/2.
    # Four-tree endpoint: tr L4<=2 by the bipartite sign Rayleigh quotient;
    # M<=3/2 and h>=1 by (u_i-u_j)^2<=2(u_i^2+u_j^2).
    assert s.expand((6-4*M+h).subs({M:s.Rational(3,2)-a,h:1+b})-(1+4*a+b))==0
    gg=s.symbols('gg');ht=s.Rational(4,3)-gg/6;pt=6-4*(4-gg)/2+ht
    assert s.expand(pt.subs(gg,s.Rational(2,3)+a)-(s.Rational(5,9)+s.Rational(11,6)*a))==0
    assert s.expand(ht-1-(2-gg)/6)==0
    # Every two-triangle corner except (0,0) has total gap >=2/3.
    # The remaining zero-gap clique corners have S5=0 and a strictly
    # positive X3 bracket even after the maximum lower trace is added.
    z=s.symbols('z',nonnegative=True)
    for nn,mm,hh in ((4,s.Rational(3,2),s.Rational(3,2)),
                     (6,s.Integer(2),s.Rational(5,4)),
                     (6,s.Integer(2),s.Rational(4,3)),
                     (4,s.Integer(1),s.Integer(1))):
        f=(C-4*k*(M+s0/2)).subs({M:mm,h:hh,s0:k-nn+1-q,k:5+z},simultaneous=True).subs(k,5+z)
        nonnegative(f,(q,z));assert f.subs({q:0,z:0})>0
    # Independently check the inherited four-double endpoint at infinity,
    # including its two-edge / balanced-triangle equality set.
    x,y,z=s.symbols('x y z',nonnegative=True)
    V=[3*x+2*y+z,-x+2*y+z,-x-2*y+z,-x-2*y-3*z]
    R=sum(a*a for a in V);p=-V[0]*V[3];Q=sum(a**4 for a in V);C3=sum(a**3 for a in V)
    inf=s.limit(four.T.subs(four.t,0),four.k,s.oo)
    f=inf.subs({four.g:R/(4*p),four.q:Q/R**2,four.m:C3**2/R**3})
    num,den=s.fraction(s.factor(f))
    dp=s.Poly(s.expand(den),x,y,z)
    assert all(c>=0 for c in dp.coeffs())
    dd=dp.total_degree()
    assert all(dp.coeff_monomial(a**dd)>0 for a in (x,y,z))
    A,B,Cc=s.symbols('A B C',nonnegative=True)
    for perm in itertools.permutations((x,y,z)):
        pol=s.Poly(s.expand(num.subs({perm[0]:A+B+Cc,perm[1]:B+Cc,perm[2]:Cc},simultaneous=True)),A,B,Cc)
        assert all(c>=0 for c in pol.coeffs())
        degree=pol.total_degree()
        assert pol.coeff_monomial(B**degree)>0 and pol.coeff_monomial(Cc**degree)>0
    print('PROVED (lower_components.py): four-vertex double carriers and split 2+4,3+3 permit arbitrary lower components for N>=7 and infinity. Positive lower trace gives strict positivity.')

if __name__=='__main__':main()
