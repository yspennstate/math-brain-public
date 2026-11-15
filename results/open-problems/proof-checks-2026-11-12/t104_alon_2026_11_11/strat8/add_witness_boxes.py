"""PROVED exports: add exact boxes for rational witnesses missed after rounding."""
import json
from fractions import Fraction as F
from rational_rays import frame_data
from exact_witnesses import candidates,contains
from zero_face import construct
from centered_bounds import integer_polynomial,translate,bound_translated

poly=integer_polynomial(construct()[-1],80)
data=json.load(open('face_boxes.json'));records=data['boxes'];scale=2**18
sources=json.load(open('exact_witnesses.json'))['witnesses']
for i,row in enumerate(sources):
    d=frame_data(row['U'],row['W'],F(row['r']))
    charts=list(candidates(row['U'],row['W'],F(row['r']),d))
    if any(contains(box['box'],coords)for box in records for perm,sign,coords in charts):continue
    # Select a definite chart, with vertex 4 the larger-diagonal endpoint.
    charts.sort(key=lambda x: (-x[2][0].lo,x[0],x[1]))
    perm,sign,coords=charts[0]
    c=[round((x.lo+x.hi)*scale/2)for x in coords]
    tr,degree=translate(poly,c,scale)
    low=0;high=scale
    while high-low>1:
        mid=(low+high)//2
        if bound_translated(tr,[mid]*6)[0]>0:low=mid
        else:high=mid
    h=max(1,low*9//10);lb=bound_translated(tr,[h]*6)[0];assert lb>0
    box=[[str(F(ci-h,scale)),str(F(ci+h,scale))]for ci in c]
    assert contains(box,coords)
    records.append(dict(exact_seed=i,box=box,lower_Cface=str(F(80*lb,scale**degree)),
                        method='centered_integer_polynomial',half_width=str(F(h,scale))))
    print('PROVED: added exact witness box',len(records)-1,'witness',i,'halfwidth',float(F(h,scale)))
with open('face_boxes.json','w')as f:json.dump(data,f,indent=2)
