from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
spec={'version':'A040-vanishing-KL-corollary-v1','family':'same actual Boolean G_r, same-alpha1/r^2 before/after rare j query','domain':[3,4,8,16,32,64],'case_count':6,'symmetry':'grouped exact mass classes; no search or dimension escalation','arithmetic':'Fraction plus existing36-term proved log intervals/outward2^-120','memory_estimate_mb':30,'maximum_runtime_seconds':55,'helper_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'code/corollary.py',R/'code/arithmetic.py',R/'code/model.py')}}
(R/'out/COROLLARY_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
from model import *
import arithmetic as ar
results=[];constant=(F(9,200)/L2[1],F(9,200)/L2[0])
for r in spec['domain']:
 d=F(1,2**r);m=d*d;a=F(1,r*r);b=1-a;q=a+b*m
 rev=scale(Fmix(m,a),F(1,2));fw=scale(add(scale(log(q/m),q),scale(log(b),b*(1-m))),F(1,2))
 kap=scale(log(1/(1-F(9,100)*a*a)),F(1,2))
 sig=add(kap,scale(sub(add(Fmix(4*m,a),Fmix(16*m,a)),scale(Fmix(10*m,a),2)),F(1,4)))
 ck(rev[0]>0 and fw[0]>0 and kap[0]>0);ck(fw[1]<2 and rev[1]<1);ck(sig[1]>=kap[0])
 scaled=scale(sig,r**4)
 if r>=16:ck(scaled[0]>=constant[0] and scaled[1]<=constant[1]*F(102,100))
 results.append({'r':r,'alpha':str(a),'reverse':fmt(rev),'forward':fmt(fw),'sigma':fmt(sig),'r4_sigma':fmt(scaled),'sigma_over_Inf_lower':str(sig[0]/(d/2))})
out={'status':'PASS','checks':ar.checks,'runtime_seconds':time.perf_counter()-start,'cases':results,'analytic_bridge':'Exact all-alpha identities and controlled expansions in PROOF.md, not finite extrapolation.'}
(R/'out/COROLLARY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:out[k] for k in ('status','checks','runtime_seconds')}))
