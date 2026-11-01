"""Exact three-site obstruction to pointwise normalized-resolvent positivity."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from verify_shuffle_obstruction import log_bounds,scale,enclose_decimal

def det3(d,x,y,z):
    return d[0]*d[1]*d[2]-d[0]*z*z-d[1]*y*y-d[2]*x*x+2*x*y*z

def main():
    diagonal=list(map(lambda x:F(x,100),[87,49,51]));x,y,z=F(-7,100),F(-8,100),F(-37,100)
    # Sylvester's criterion certifies both strict inequalities 0<K<I.
    minorK=[diagonal[0],diagonal[0]*diagonal[1]-x*x,det3(diagonal,x,y,z)]
    comp=[1-d for d in diagonal]
    minorI=[comp[0],comp[0]*comp[1]-x*x,det3(comp,-x,-y,-z)]
    assert all(a>0 for a in minorK+minorI)
    rows=[]
    for bits in product([0,1],repeat=3):
        d=[a-(1-b) for a,b in zip(diagonal,bits)];sgn=(-1)**(3-sum(bits))
        p=sgn*det3(d,x,y,z)
        # A=iT, T12=9,T13=-8,T23=0. This is the coefficient of t^2.
        c=sgn*(-64*d[1]-81*d[2]-144*z)
        q=F(1)
        for a,b in zip(diagonal,bits):q*=a if b else 1-a
        assert p>0 and q>0
        rows.append((bits,p,c,q))
    assert sum(p for _,p,_,_ in rows)==1 and sum(c for _,_,c,_ in rows)==0
    s=F(10);integrand=-sum(2*c/(p/q+s) for _,p,c,q in rows)
    assert integrand < -F(1,1200)
    lo=hi=F(0)
    for _,p,c,q in rows:
        l,u=scale(2*c,log_bounds(p));lo+=l;hi+=u
    assert lo>0
    out=dict(status='PASS: integrand shortcut false; actual entropy curvature has correct sign',K_numerator=[[87,-7,-8],[-7,49,-37],[-8,-37,51]],K_denominator=100,T=[[0,9,-8],[-9,0,0],[8,0,0]],leading_minors_K=list(map(str,minorK)),leading_minors_I_minus_K=list(map(str,minorI)),s='10',normalized_resolvent_integrand=str(integrand),integrand_upper_bound='-1/1200',negative_entropy_curvature_interval=enclose_decimal((lo,hi)),atom_data=[dict(bits=''.join(map(str,b)),p=str(p),t_squared_coefficient=str(c),product_reference=str(q)) for b,p,c,q in rows])
    Path('resolvent_obstruction_certificate.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='atom_data'},indent=2))

if __name__=='__main__':main()
