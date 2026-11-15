"""PROVED: exact interval boxes on zero faces missed by the moment tests."""
import json
from fractions import Fraction as F
from face_intervals import source_chart,evaluate

sources=json.load(open('residual_rays.json'))['residual']
records=[]
for number,source in enumerate(sources):
    coordinates,perm,data=source_chart(source)
    centers=[(v.lo+v.hi)/2 for v in coordinates]
    accepted=None
    low,high=0,50001
    while low+1<high:
        mid=(low+high)//2
        radius=F(mid,10**6)
        box=[(x-radius,x+radius)for x in centers]
        assert all(lo<=actual.lo<=actual.hi<=hi for(lo,hi),actual in zip(box,coordinates))
        t,delta,D,numerator=evaluate(box)
        if min(t.lo,delta.lo,D.lo,numerator.lo)>0:
            accepted=dict(source=number,permutation=perm,
                 box=[[str(lo),str(hi)]for lo,hi in box],radius=str(radius),
                 lower_delta=str(delta.lo),lower_D=str(D.lo),lower_numerator=str(numerator.lo))
            low=mid
        else:
            high=mid
    assert accepted is not None
    records.append(accepted)
    print('PROVED: zero-face box',number,'radius',accepted['radius'],
          'positive numerator lower bound',accepted['lower_numerator'],flush=True)
    with open('zero_face_boxes.json','w')as out:
        json.dump(records,out,indent=2)
