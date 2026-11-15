from fractions import Fraction as F
from pathlib import Path
import json
checks=0
for rho in [F(1,100),F(1,2),F(1),F(3,2),F(10),F(100)]:
 E=rho+2+rho/(1+rho); L=2*rho+2*rho/(1+rho)
 assert E-L==(2-rho*rho)/(1+rho)
 assert L-3==(rho-1)*(2*rho+3)/(1+rho)
 assert min(F(3),E,L)==min(F(3),L)
 assert [rho+3-E,2*rho+2-E,2*rho+2-L]==[1/(1+rho),rho*rho/(1+rho),2/(1+rho)]
 assert all(z>0 for z in [rho+3-E,2*rho+2-E,2*rho+2-L])
 for q in [F(0),F(1,4),rho/(1+rho),F(1)]:
  assert q*q+rho*(1-q)**2==(1+rho)*(q-rho/(1+rho))**2+rho/(1+rho)
  checks+=1
out={'rational_completed_square_cases':checks,'noise_ratios_checked':6,'phase_boundary':'rho=1, asymptotic preference only','scope':'Exact scalar identities only. Does not certify phase subsequence limits, nonlinear transfer, lower critical noise or novelty.'}
with (Path(__file__).resolve().parent.parent/'logs/noise_phase_algebra_checks.json').open('w',encoding='utf-8',newline='') as f:json.dump(out,f,indent=2)
print(json.dumps(out))
