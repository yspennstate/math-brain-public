"""Exact radial identity and sufficient lower bound for its linear term."""
from sympy import symbols,Rational as Q,expand

def replay():
    a,E,L,H=symbols('a E L H')
    T=lambda x:x*L+x*x*H
    assert expand(T(a)-a*(1-a/E)*L-(a/E)**2*T(E))==0
    A,B,C,r=symbols('A B C r')
    # A+C>=1/4 and B+C>=1/4 are among the inherited moment bounds.
    ell=Q(14,9)*(A+r*B+(1+r)*C-(1+r)/5)
    lower=Q(7,90)*(1+r)
    assert expand(ell-lower-Q(14,9)*((A+C-Q(1,4))+r*(B+C-Q(1,4))))==0
    print('PROVED (verify_radial.py): T(a,ar)=a(1-a/E)L+(a/E)^2 T(E,rE), L>=7(1+r)/90>0.',flush=True)

if __name__=='__main__':replay()
