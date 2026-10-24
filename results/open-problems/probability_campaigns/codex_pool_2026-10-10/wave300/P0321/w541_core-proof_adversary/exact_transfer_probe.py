"""Exact rational counterexample checks; no numerical evidence substituted for proof."""
from fractions import Fraction as F
from pathlib import Path
import json

rows=[]
for power in range(1,13):
    h=F(1,2**power)
    reference=target=error_square=mean_a0=mean_ar=mean_br=F(0)
    maxabs=F(0)
    for u in [-1,1]:
        for v in [-1,1]:
            p=(1+h*u*v)/4
            br=(v-h*u)/(1+h)
            reference+=p*u*v
            target+=p*u*br
            error_square+=p*(br-v)**2
            mean_a0+=p*u
            mean_ar+=p*v
            mean_br+=p*br
            maxabs=max(maxabs,abs(br))
    assert reference==h and target==0
    assert error_square==2*h*h/(1+h)
    assert mean_a0==mean_ar==mean_br==0 and maxabs<=1
    rows.append({"h":str(h),"reference":str(reference),"target":str(target),"l2_error_squared":str(error_square),"maximum_absolute_target_observable":str(maxabs)})
result={"status":"pass","parameter_cases":len(rows),"probability_atoms_checked":4*len(rows),"arithmetic":"exact fractions","rows":rows,"command":"python -X utf8 ~/brain_workers/w541/exact_transfer_probe.py","proof_scope":"finite observable-transfer counterexample only; independent review pending"}
(Path(__file__).resolve().parent/"exact_transfer_probe.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
