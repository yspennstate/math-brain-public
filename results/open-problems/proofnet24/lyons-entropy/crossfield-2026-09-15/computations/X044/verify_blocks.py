"""Symbolic count-to-block normalization and the strict negative-B witness."""
import json
from pathlib import Path
import sympy as S


def verify_blocks():
    r,s,a,b,e,f,L,W,tau=S.symbols('r s a b e f L W tau',real=True)
    R=1-r*s; ta=a+b; tb=e+f; mu=s*a+r*b; nu=s*e+r*f
    count=(ta+tb-mu-nu)**2/(2*(1-r)*(1-s))
    count+=(ta-tb+mu-nu)**2/(2*(1+r)*(1+s))
    count+=((ta+nu)**2+(tb+mu)**2)/R
    full=count-L*(a*b+e*f)-W*ta*tb+tau*(s*a*e+r*b*f)/2
    pred=0
    for eps in (1,-1):
        x=(a+eps*e)/S.sqrt(2); y=(b+eps*f)/S.sqrt(2)
        B=(2+eps*(r+s))/R-eps*W/2-L/2
        u=(r-s)**2/((1-eps*r)*R)+L/2+eps*s*tau/4
        v=(r-s)**2/((1-eps*s)*R)+L/2+eps*r*tau/4
        pred+=B*(x+y)**2+u*x*x+v*y*y
    assert S.factor(full-pred)==0
    c,d=S.Rational(499,1000),S.Rational(1,5)
    r,s=4*c*c,4*d*d
    rational=(2+r+s)/(1-r*s); arg=(1+r*s)/((1-r)*(1-s))
    assert rational<4 and arg>81
    assert c*d*(c*c-d*d)>0
    return {'status':'PASS','symbolic_quadratic_identity':True,
            'witness_rational_term':str(rational),'witness_log_argument':str(arg),
            'strict_negative_B_plus':True,'nonreal_cycle_product':True}

if __name__=='__main__':
    out=verify_blocks()
    Path(__file__).with_name('blocks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
