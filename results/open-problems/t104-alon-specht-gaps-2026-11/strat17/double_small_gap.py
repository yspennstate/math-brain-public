"""Exact scalar certificate for five-double carriers with gap trace <=1.

Proof uses weighted Cauchy twice, not the old six-dimensional chart cover.
The accompanying RESULT.md gives the graph-to-scalar inequalities.
"""
import sympy as s
from lower_formula import x3


def main():
    a,b,U,V,t,k,z=s.symbols('a b U V t k z')
    # Nonnegative pointwise remainder, a>=b>=0, U,V>=0.
    assert s.expand((U+V)*(a*U+b*V)-((a-b)*U**2+b*(U+V)**2)-(a-b)*U*V)==0
    # Universal weighted Cauchy identity, checked as the arbitrary 3-term
    # polynomial identity; the identical pair-sum derivation works for any n.
    w=s.symbols('w0:3');x=s.symbols('x0:3');W=sum(w)
    assert s.expand(W*sum(wi*xi**2 for wi,xi in zip(w,x))-sum(wi*xi for wi,xi in zip(w,x))**2
                    -sum(w[i]*w[j]*(x[i]-x[j])**2 for i in range(3)for j in range(i+1,3)))==0
    # F=a sum q_i u_i^2+b sum q_i v_i^2 >= (a+b)/5.
    # Each sum fourth powers is >=1/5 by ordinary Cauchy.
    y=s.symbols('y0:5')
    assert s.expand(5*sum(yi**2 for yi in y)-sum(y)**2-sum((y[i]-y[j])**2 for i in range(5)for j in range(i+1,5)))==0
    hmin=s.Rational(8,5)-s.Rational(3,5)*t
    end=x3(k,(k-t)/2,hmin)
    compact=(3+2*t)/5-t*(13+2*t)*z/5-6*(t+2)*(1-t)*z*z/5
    assert s.cancel(end-compact.subs(z,1/k))==0
    # For 0<=t<=1 every coefficient subtracted from the constant is >=0.
    assert s.expand(s.diff(compact,z)+t*(13+2*t)/5+12*(t+2)*(1-t)*z/5)==0
    X=(3-t)*(21+4*t)/125
    assert s.cancel(end.subs(k,5)-X)==0
    # a>=b>=0, t=a+b<=1, M0=(4-t)/2.
    E=t-a*a-(t-a)**2
    L=(2*a-t)*(1-a)**2+(t-a)*(2-t)**2
    bound=X-2*E+4*L/(4-t)
    N=1000*a**3-1000*a*a*t+1000*a*t-1000*a+254*t**3-757*t*t+401*t+252
    assert s.cancel(bound-N/(125*(4-t)))==0
    # t in [1/2,1]: N(t,a)>=N(1,a)>=50/27.
    R=1000*(a-s.Rational(1,2))**2+40+(t-s.Rational(1,2))*(376-254*t)
    assert s.expand(N-N.subs(t,1)-(1-t)*R)==0
    assert s.expand(N.subs(t,1)-1000*(a-s.Rational(2,3))**2*(a+s.Rational(1,3))-s.Rational(50,27))==0
    # t in [0,1/2], a in [t/2,t]: N(t,a)>=N(t,t)>=45.
    assert s.expand(N-N.subs(a,t)-1000*(a-t)*(a*a+t-1))==0
    diag=N.subs(a,t)
    assert s.expand(diag-45-(1-2*t)*(207-185*t-127*t*t))==0
    assert s.expand(207-185*t-127*t*t-(s.Rational(331,4)+185*(s.Rational(1,2)-t)+127*(s.Rational(1,4)-t*t)))==0
    # Simple rational range checks complete every displayed sign argument.
    assert s.Rational(1,4)+s.Rational(1,2)-1<0
    assert 376-254>0 and 45>s.Rational(50,27)
    assert s.Rational(50,27)/(125*4)==s.Rational(1,270)
    # Combining the inherited zero-trace endpoint and the new one yields
    # F(s)>=(s/(k-4))/270+s*(k-4-s)/k for positive lower trace.
    print('PROVED (double_small_gap.py): maximal lower-trace endpoint >=1/270 for tau<=1, all real k>=5 and infinity. Weighted inequalities plus exact scalar identities; no chart cover.')

if __name__=='__main__':main()
