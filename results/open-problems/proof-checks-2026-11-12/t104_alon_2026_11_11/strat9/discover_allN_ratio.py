"""NUMERICAL: all-N strip discovery followed by exact Gram acceptance."""
import json,sys
from fractions import Fraction as F
from allN_ratio_polynomial import construct
from quartic_sos import certify
rho=F(sys.argv[1])if len(sys.argv)>1 else F(3,20)
data=dict(rho=str(rho),padding=[])
for index in range(3):
    rr,polys=construct(rho,index);group=[]
    for j,p in enumerate(polys):
        print('OPEN: all-N small-ratio padding coefficient',index,'control',j,flush=True)
        result=certify(p);group.append(result)
        if result['failed']:
            print('OPEN: incomplete all-N small-ratio attempt, failures',len(result['failed']),flush=True)
            with open('allN_ratio_candidate.json','w')as out:json.dump(dict(rho=str(rho),padding=data['padding'],failed_group=group),out,indent=2)
            sys.exit(1)
    data['padding'].append(group)
with open('allN_ratio_certificate.json','w')as out:json.dump(data,out,indent=2)
print('PROVED: complete rational all-N small-ratio SOS certificate, rho',rho)
