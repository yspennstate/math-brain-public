"""Independent exact values: inherited rational-frame evaluator vs local chart."""
from fractions import Fraction as F
from corner_algebra import chart
from corner_boxes import SOURCE
import sys
sys.path.insert(0,str(SOURCE))
from rational_rays import frame_data


def value(poly,h):
    out=F(0)
    for mon,c in poly.items():
        term=F(int(c.numerator),int(c.denominator))
        for exponent,v in zip(mon,h):term*=v**exponent
        out+=term
    return out


if __name__=='__main__':
    rr,B,K,gap,den,Qn,weights,num=chart()
    for s,r in [(F(1,10000),F(1)),(F(1,10000),F(9999,10000)),(F(1,100000),F(99999,100000))]:
        U=[-4,1+s,1+s,1-s,1-s];W=[0,1,-1,-1,1]
        data=frame_data(U,W,r);a=data['a'];tu=sum(u*u for u in U)
        h=[20*a/tu-1,a*r-1,F(0),s,F(0),F(0),F(0)]
        assert value(num,h)/value(den,h)==data['T']
        assert value(den,h)>0
        assert all(value(w,h)==old for w,old in zip(weights.values(),data['weights']))
        d=sum(abs(v) for v in h)
        assert 0<d<=F(1,400) and data['T']>=d/12
        if r==1:
            expected=s*(1100-335*s+185*s*s+19*s**3+26*s**4-11*s**5)/(4*(s*s+5)*(s*s-10*s-5)**2)
            assert data['T']==expected
    print('PROVED: three independent exact rational-frame evaluations match chart, weights and lower bound (including r<1).')
