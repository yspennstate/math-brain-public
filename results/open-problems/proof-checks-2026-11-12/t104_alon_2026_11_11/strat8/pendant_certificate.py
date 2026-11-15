"""PROVED: exact certificate for the pendant subface with neighbor y=0.

Default: verify pendant_certificate.json and the polynomial identities.
--export: regenerate the certificate (still checks every coefficient exactly).
"""
import json,sys
import sympy as s
from fractions import Fraction as F
from math import comb
from zero_face import construct


def expressions():
    t,v,h=s.symbols('t v h')
    A=-21*t**6+231*t**5-1115*t**4+3715*t**3-8490*t**2+10884*t-5544
    B=-(6*t**4-78*t**3+355*t**2-847*t+414)/2
    E=-7*(3*t**2-9*t+23)/4
    H=12*(t*t-3*t+6)
    P=s.Poly(s.expand(A*(1+v)**2*(3+v*v)+B*(t+1)*h*(1+v)*(3+v*v)**2
        +E*(t+1)**2*h*h*(3+v*v)**3+s.Rational(9,2)*H*(t+1)**2*h*h*(1-v*v)**2),h)
    return t,v,h,A,B,E,H,P


def bernstein(expr,t,v):
    x=s.symbols('x')
    po=s.Poly(s.expand(expr.subs(t,(3+5*x)/2)),x,v)
    n,m=po.degree_list()
    coeff=[]
    for i in range(n+1):
        row=[]
        for j in range(m+1):
            val=sum(F(int(c.p),int(c.q))*F(comb(i,a),comb(n,a))*F(comb(j,b),comb(m,b))
                    for(a,b),c in po.terms()if a<=i and b<=j)
            assert val>=0
            row.append(str(val))
        coeff.append(row)
    return dict(degrees=[n,m],coefficients=coeff)


def replay():
    t,v,h,A,B,E,H,P=expressions()
    rr,*other=construct();C=other[-1]
    y1,y2=s.symbols('y1 y2')
    sub=dict(zip(rr.symbols,(t,-1,y1,-1,y2,-y1-y2)))
    K=2*(y1*y1+y1*y2+y2*y2);J=-3*y1*y2*(y1+y2)
    assert s.expand(C.as_expr().subs(sub)/80-K*(A+B*K+E*K*K)-H*J*J)==0
    # The exact parameterization by two nonnegative roots a>=b>=0.
    root=s.symbols('root',positive=True)
    aa=root*(1+v)/2;bb=root*(1-v)/2
    kp=s.factor(K.subs({y1:aa,y2:bb}))
    jp=s.factor(J.subs({y1:aa,y2:bb}))
    check=s.expand((kp*(A+B*kp+E*kp*kp)+H*jp*jp)*(1+v)**2*(3+v*v)/kp)
    check=s.cancel(check.subs(root**2,2*(t+1)*h/(1+v)))
    assert s.cancel(check-P.as_expr())==0
    q2=P.coeff_monomial(h**2)
    assert s.expand(P.as_expr()-((1-h)*P.eval(0)+h*P.eval(1)-q2*h*(1-h)))==0
    # M00=2(t^2-3t+6); PSD of 5t I-M yields this t interval.
    assert s.expand(5*t-2*(t*t-3*t+6)-(4-t)*(2*t-3))==0
    data=dict(status='PROVED',domain={'t':['3/2','4'],'v':['0','1'],'h':['0','1']},
              A=bernstein(A,t,v),minus_quadratic=bernstein(-q2,t,v),endpoint_h1=bernstein(P.eval(1),t,v))
    assert min(F(x)for row in data['A']['coefficients']for x in row)>0
    assert min(F(x)for row in data['minus_quadratic']['coefficients']for x in row)>0
    if '--export'in sys.argv:
        with open('pendant_certificate.json','w')as f:json.dump(data,f,indent=2)
    else:
        assert json.load(open('pendant_certificate.json'))==data
    count=sum(len(row)for key in('A','minus_quadratic','endpoint_h1')for row in data[key]['coefficients'])
    print('PROVED: pendant subface identities and',count,'nonnegative rational Bernstein coefficients verified.')

if __name__=='__main__':replay()
