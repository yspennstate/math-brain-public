from fractions import Fraction as Q
from pathlib import Path
import json,time
start=time.perf_counter();R=Path(__file__).resolve().parents[1]
assert Q(22,15)**3<4
assert Q(6,5)**2/8<Q(9,20)**2
assert 704**2<2**19
assert 2+Q(2,3)+Q(9,20)+Q(19,32)==Q(1781,480)<4
assert Q(8,3)+Q(5,96)<Q(11,4)
rows=0;checks=5
for a in range(1,9):
    for b in range(1,9):
        q=Q(1,2**a);r=Q(1,2**b)
        for l in range(1,4):
            eta=Q(1,2**(a+b+l));e=q+r-q*r-eta
            assert eta<=Q(8,25)*e*e;checks+=1
            for j in range(8):
                rho=Q(1,2**j)
                mass=2*eta-eta*eta-rho*eta*e+rho*rho*e*(1-e/2)
                deriv=rho*rho*e*(2-e)/4
                assert 0<=deriv<=mass<=2*eta+rho*rho*e
                assert deriv/(rho*e/2)<=rho
                rows+=1;checks+=2
result={'status':'PASS','formal_parameter_rows':rows,'rational_assertions':checks,'seconds':time.perf_counter()-start,'scope':'independent algebra/constant checks, all-width scope supplied by REVIEW_NOTE.md proof'}
(R/'out/AUDIT_CONSTANTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
