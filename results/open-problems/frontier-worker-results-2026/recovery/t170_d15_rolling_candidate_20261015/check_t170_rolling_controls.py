from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import json
H=Path(__file__).resolve().parent;u=28
# Independent hand-enumerated four-state accepted-event process, in order
# (1,1),(1,2),(2,1),(2,2). Each entry is(child,rate,advance reward).
edges=[[(2,u,0),(1,u,0),(0,1,1)],[(3,u,0),(2,2,1)],[(3,u+1,0),(0,1,1)],[(2,2,1)]]
def solve(A,b):
 z=[[F(v) for v in row]+[F(rhs)] for row,rhs in zip(A,b)];n=len(b)
 for i in range(n):
  pivot=next(k for k in range(i,n) if z[k][i]);z[i],z[pivot]=z[pivot],z[i]
  q=z[i][i];z[i]=[v/q for v in z[i]]
  for k in range(n):
   if k!=i:
    q=z[k][i];z[k]=[a-q*b for a,b in zip(z[k],z[i])]
 return [row[-1] for row in z]
Q=[[F(0) for _ in range(4)] for _ in range(4)]
for s,transitions in enumerate(edges):
 for child,rate,reward in transitions:Q[s][child]+=rate;Q[s][s]-=rate
A=[[Q[s][j] for s in range(4)] for j in range(3)]+[[F(1)]*4]
pi=solve(A,[0,0,0,1]);assert all(x>0 for x in pi)
mean=sum(pi[s]*sum(rate*reward for _,rate,reward in transitions) for s,transitions in enumerate(edges))
ratio=1/mean
# Independent closed first-step regeneration equations are derived in the
# accompanying route notes: return to(1,1), including a self front advance.
ET=F(2*u*u+7*u+2,2*(2*u+1));EA=F(2*u*u+5*u+1,2*u+1)
assert ratio==ET/EA==F(883,1709)
wrong_mean=sum(pi[s]*sum(rate*reward for child,rate,reward in transitions if child!=s) for s,transitions in enumerate(edges))
assert 1/wrong_mean!=ratio,'Missing self-advance reward must be detectable'
one=json.loads((H/'T170_ROLLING_d15_C1_RECEIPT.json').read_bytes());two=json.loads((H/'T170_ROLLING_d15_C2_RECEIPT.json').read_bytes())
assert F(one['conditional_axis_certificate'])==1
assert abs(two['stationary_axis_estimate']-float(ratio))<1e-10
assert F(two['conditional_axis_certificate'])>=ratio
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS finite model controls; physical comparison still unaudited','cap1_axis_exact':'1','cap2_axis_exact':str(ratio),'regeneration_ET':str(ET),'regeneration_EA':str(EA),'stationary_probabilities':list(map(str,pi)),'omitted_self_reward_ratio':str(1/wrong_mean),'omitted_self_reward_rejected':True,'scope':'Independent four-state generator versus closed regeneration first-step equations; validates reward orientation, not adaptive spatial realization.'}
(H/'T170_ROLLING_CONTROL_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
