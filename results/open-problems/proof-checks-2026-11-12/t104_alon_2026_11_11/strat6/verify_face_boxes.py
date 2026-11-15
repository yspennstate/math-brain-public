"""PROVED: rational interval replay of every saved zero-face box."""
import json
from fractions import Fraction as F
from face_intervals import source_chart,evaluate
from directional_bounds import vector_from_record,lower_value
from rational_rays import cell_bound
from zero_face import construct
from moment_bounds import value

sources=json.load(open('residual_rays.json'))['residual']
records=json.load(open('zero_face_boxes.json'))
assert len(records)==len(sources)>0
base=json.load(open('strong_moment_cells.json'))+json.load(open('enhanced_moment_cells.json'))
directional=[(c,vector_from_record(c))for c in json.load(open('directional_moment_cells.json'))]
polynomial=construct()[-1]
stronger_missed=0
for number,rec in enumerate(records):
    source=sources[rec['source']]
    coords,perm,data=source_chart(source)
    assert perm==rec['permutation']
    box=[tuple(map(F,v))for v in rec['box']]
    assert all(lo<hi and lo<=v.lo<=v.hi<=hi for(lo,hi),v in zip(box,coords))
    t,delta,D,num=evaluate(box)
    assert min(t.lo,delta.lo,D.lo,num.lo)>0
    assert delta.lo==F(rec['lower_delta'])and D.lo==F(rec['lower_D'])and num.lo==F(rec['lower_numerator'])
    # The enclosed exact endpoint is outside all general moment certificates.
    r,a=F(source['r']),data['a']
    assert data['lam']>a and min(data['weights'])==0 and data['T']>0
    values=[cell_bound(c,data['moments'],a,r)for c in base if F(c['rlo'])<=r<=F(c['rhi'])]
    values += [lower_value(data['moments'],a,r,v)for c,v in directional if F(c['rlo'])<=r<=F(c['rhi'])]
    assert max(values)==F(source['bound'])<0
    # Count which centers also miss the strengthened nonlinear sufficient test.
    if r<F(3,5):
        stronger_missed+=1
    else:
        A,B,C=data['moments']
        K=A+B+2*C
        fm=A+r*B+(1+r)*C
        la=data['lam']
        S=a*(1+r-fm)-2*la/5
        zn=a*fm*fm/(1+r)-la*(2-K)/5+S*S/2
        zj=a*fm*fm/(1+r)-la*(4-K)/5+S*S/2
        nonlinear=value(data['moments'],a,r,0,0,0,0,0)
        nonlinear+=(5*r/3-1)*max(F(0),zn)+(1+r)*max(F(0),zj)
        if nonlinear<0:
            stronger_missed+=1
    if r==1:
        assert a>F(69,125)  # Also beyond the isolated cubic-root endpoint.
    if number<3:
        # Independent 1,254-coefficient evaluation at the rational box center.
        point=[(lo+hi)/2 for lo,hi in box]
        val=sum(F(int(c.numerator),int(c.denominator))*__import__('functools').reduce(
                    lambda x,y:x*y,(x**m for x,m in zip(point,mon)),F(1))
                for mon,c in polynomial.terms())
        exact=evaluate([(x,x)for x in point])[-1]
        assert exact.lo==exact.hi==val
print('PROVED:',len(records),'rational boxes have positive zero-face numerator throughout.')
print('PROVED: each box encloses an exact connected endpoint missed by all general moment cells.')
print('PROVED: three center evaluations independently matched the 1,254-coefficient polynomial.')
assert stronger_missed==46
print('PROVED: 46 enclosed endpoints also fail the strengthened nonlinear sufficient test (where applicable).')
