"""PROVED: replay all rational face boxes and their exact witnesses."""
import json
from fractions import Fraction as F
from functools import reduce
from face_intervals import source_chart,evaluate
from cells import vector_from_record,lower_value
from zero_face import construct

def main():
    sources=json.load(open('source_rays.json'))['residual'];recs=json.load(open('face_boxes.json'))
    cells=json.load(open('moment_cells.json'));poly=construct()[-1]
    misses=0;alln=0
    for number,rec in enumerate(recs):
        coords,perm,data=source_chart(sources[rec['source']])
        box=[tuple(map(F,p))for p in rec['box']]
        assert perm==rec['permutation'] and all(lo<hi and lo<=v.lo<=v.hi<=hi for(lo,hi),v in zip(box,coords))
        t,de,D,ps=evaluate(box)
        assert min(t.lo,de.lo,D.lo,ps[0].lo)>0
        assert [str(v.lo)for v in ps]==rec['lower_coefficients']
        assert str(de.lo)==rec['lower_delta'] and str(D.lo)==rec['lower_D']
        assert rec['all_N']==(min(p.lo for p in ps)>0)
        alln+=rec['all_N']
        rr=F(sources[rec['source']]['r']);aa=data['a']
        assert aa>F(11,25) and data['lam']>aa and min(data['weights'])==0 and data['T']>0
        values=[lower_value(data['moments'],aa,rr,vector_from_record(c))for c in cells if F(c['rlo'])<=rr<=F(c['rhi'])]
        assert rec['missed_by_cells']==(max(values)<0)
        misses+=rec['missed_by_cells']
        if number<3:
            point=[(lo+hi)/2 for lo,hi in box]
            expected=[]
            for i in range(3):
                expected.append(sum(F(int(c.numerator),int(c.denominator))*reduce(lambda x,y:x*y,(x**m for x,m in zip(point,mon[:6])),F(1))for mon,c in poly.terms()if mon[-1]==i))
            actual=evaluate([(x,x)for x in point])[-1]
            assert all(v.lo==v.hi==p for v,p in zip(actual,expected))
    assert len(recs)==47 and alln==47
    print('PROVED:',len(recs),'rational face boxes, all for every N>=6;',misses,'exact endpoints missed by current N=6 moment cells.')
if __name__=='__main__':main()
