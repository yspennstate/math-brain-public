"""NUMERICAL: candidate SOS discovery; success requires exact replay."""
import json,sys
from fractions import Fraction as F
from small_ratio_polynomial import construct
from quartic_sos import certify
rho=F(sys.argv[1])if len(sys.argv)>1 else F(3,25)
rr,polys=construct(rho);data=dict(rho=str(rho),controls=[])
for j,p in enumerate(polys):
    print('OPEN: constructing small-ratio Bernstein control',j,flush=True)
    result=certify(p);data['controls'].append(result)
    with open('small_ratio_candidate.json','w')as out:json.dump(data,out,indent=2)
    if result['failed']:
        print('OPEN: incomplete small-ratio control',j,'unresolved',len(result['failed']),flush=True)
        sys.exit(1)
assert all(not c['failed']for c in data['controls'])
with open('small_ratio_certificate.json','w')as out:json.dump(data,out,indent=2)
print('PROVED: all small-ratio Bernstein controls have exact rational SOS decompositions, rho',rho)
