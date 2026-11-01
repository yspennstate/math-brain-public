import check as h
from fractions import Fraction as F
from pathlib import Path
import time,json
out=[];counter=None
for mask in range(16):
 g=tuple(1 if mask&(1<<s) else -1 for s in range(4));t=h.carrier(g);R=[F(x,11) for x in (1,2,3,5)]
 for eps in (F(1,4),F(1,2),F(3,4)):
  Q=[]
  for s in range(16):
   su=s&1;old=(s>>2)^(3 if su else 0)
   Q.append(R[old]*F(1,4)*(1+eps if not su else 1-eps))
  _,_,reach,O,_,_,ref=h.transport(t,1,Q)
  U=[Q[h.insert(s,1,0)]+Q[h.insert(s,1,1)] for s in range(8)]
  eta=sum((abs(U[s]-U[(s^1)^6]) for s in range(8)),F())/2
  h.ck(eta==eps,'actual erased-reference TV measured')
  h.ck(abs(reach[0]-reach[1])<=eta,'kernel pair imbalance bound')
  bound=h.plus((-F(1,2),h.log(1-eta*eta)))
  gap=h.plus((1,bound),(-1,O));h.ck(not gap or h.interval(gap)[0]>=0,'full logarithmic outcome bound')
  if eta<=F(1,2):h.ck(h.interval(O)[1]<=eta*eta,'quadratic bound at stated cutoff')
  if mask==7:
   h.eq(O,bound,'bent full-support sharp logarithmic envelope')
   if eta==F(3,4):
    h.ck(h.interval(O)[0]>eta*eta,'cutoff omission actual counterexample')
    counter={'mask':mask,'eta':str(eta),'O':h.enc(O),'O_interval':h.enciv(O),'eta_squared':str(eta*eta)}
  out.append({'mask':mask,'eta':str(eta),'predicted_reach':[str(x) for x in reach],'O':h.enc(O),'reference_only_mass':str(ref)})
h.ck(counter is not None);h.ck(time.perf_counter()-h.START<20)
r={'status':'PASS','fixtures':len(out),'exact_assertions':h.COUNT,'seconds':time.perf_counter()-h.START,'cutoff_counterexample':counter,'records':out}
(h.ROOT/'out/IMBALANCE.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in r.items() if k!='records'}))
