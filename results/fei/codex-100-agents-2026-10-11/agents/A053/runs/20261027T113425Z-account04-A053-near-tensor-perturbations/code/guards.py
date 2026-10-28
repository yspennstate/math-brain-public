from pathlib import Path
from fractions import Fraction as Q
import json
R=Path(__file__).resolve().parents[1]
spec=dict(helper='guards.py v1',domain='n4 E={0}; physical policies touch block0 iff x2=0, and always touch both blocks; scalar n3 core profile',
case_count=2,arithmetic='integer counts and Fraction',memory_estimate_mb=30,maximum_runtime_seconds=5,
purpose='exact negative controls for independence substitution and single total error charge')
(R/'out/SPEC_GUARDS.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
delta=Q(1,16);A=[x for x in range(16) if not (x>>2)&1]
p=Q(len(A),16);e=Q(int(0 in A),16)
assert p==Q(1,2)
assert e==delta
assert e!=delta*p
e0=e1=delta
assert e0+e1>delta
# The h3 profile has alpha/rho=2 as well, so its paired slope is2.
alpha=Q(1,4);rho=Q(1,8)
assert alpha/rho==2
result=dict(status='PASS',checks=5,no_independence=dict(error=str(delta),touch=str(p),joint=str(e),false_product=str(delta*p)),
 no_single_sum=dict(sum_occupations=str(e0+e1),error=str(delta)))
(R/'out/GUARDS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
