import json,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();rows=[];rho=F(1)
for r in range(257):
 if r:rho*=F(2*r-1,2*r)
 assert rho*rho<=F(1,r+1)
 assert (2*r+1)*rho>=1
for k in range(4,65,2):
 delta=F(1,1<<k);s=F(1,1<<(k//2));p=delta*delta
 R=k*k*(1<<(2*k+2));M=2*R+1;upper=delta/(2*k)
 W=F(5,2)-2*s+3*delta
 for q in range(3*k+1):
  lowmass=(1-q*upper)*p/2
  assert lowmass>=29*p/64>p/4
  D=3*k*M+1-q
  # Sufficient eligibility inequality with rho dominated by upper.
  gap=F(D,M)*(1-2*q*upper)-k*W-delta
  assert gap>0
  price=3*delta+7*delta/(4*k)
  assert price<=F(55,256)
  ratio=(upper/delta)/(1-q*upper)**2
  assert ratio<=F(128,841)<1
  assert 1/(1-q*upper)<=F(32,29)
  rows.append({'k':k,'q':q,'eligibility_lower_gap':str(gap),'price_upper':str(price),'max_background_over_selector_upper':str(ratio)})
assert len(rows)==3193
result={'helper_version':'A026-prefix-rational-v1','status':'PASS','parameter_cases':len(rows),'central_binomial_cases':257,'elapsed_seconds':time.perf_counter()-start,'all_k_proof':'PROOF.md section 3; finite cases not used to infer universal k','records':rows}
(ROOT/'out'/'symbolic_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
