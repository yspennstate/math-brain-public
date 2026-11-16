"""NUMERICAL seeds, PROVED exports: exact rational face boxes."""
import json,time
from fractions import Fraction as F
from zero_face import construct
from centered_bounds import integer_polynomial,translate,bound_translated


def main():
    poly=integer_polynomial(construct()[-1],80)
    rows=json.load(open('frame_evaluations.json'))['rows']
    scale=2**18
    records=[]
    start=time.time()
    for i,row in enumerate(rows):
        c=[round(x*scale)for x in row['coordinates']]
        tr,degree=translate(poly,c,scale)
        def check(h): return bound_translated(tr,[h]*6)[0]
        low=0; high=scale
        while high-low>1:
            mid=(low+high)//2
            if check(mid)>0: low=mid
            else: high=mid
        h=max(1,low*9//10)
        lb=check(h)
        assert lb>0
        box=[[str(F(ci-h,scale)),str(F(ci+h,scale))]for ci in c]
        rec=dict(seed=i,r_numerical=row['r'],box=box,
                 lower_Cface=str(F(80*lb,scale**degree)),
                 method='centered_integer_polynomial',half_width=str(F(h,scale)))
        records.append(rec)
        print('PROVED: box',i,'r seed',row['r'],'halfwidth',float(F(h,scale)),flush=True)
        with open('face_boxes.json','w') as f:json.dump(dict(status='PROVED',divisor=80,boxes=records),f,indent=2)
    print('PROVED:',len(records),'rational boxes exported; elapsed',time.time()-start)

if __name__=='__main__': main()
