import math,json
from pathlib import Path

def distribution(lam,minimum):
 terms=[1.]
 for e in range(1,160):terms.append(terms[-1]*lam/(minimum+e))
 z=sum(terms);prob=[t/z for t in terms]
 return sum((minimum+e)*p for e,p in enumerate(prob)),prob
def param(mean,minimum):
 lo=0.;hi=mean+10
 for _ in range(100):
  mid=(lo+hi)/2
  if distribution(mid,minimum)[0]<mean:lo=mid
  else:hi=mid
 return (lo+hi)/2

rows=[]
for c in [1.5001,1.51,1.6,1.8,2.,2.662]:
 mu=2*c;lam=param(mu,3);tau=param(mu-2,1)
 _,p=distribution(lam,3);_,q=distribution(tau,1)
 kl=sum(a*math.log(a/b) for a,b in zip(p,q) if a>0 and b>0)
 differences=[abs(p[i]-q[i]) for i in range(3)]
 rows.append({'c':c,'lambda_target':lam,'tau_planted_residual':tau,
 'target_p3_p4_p5':p[:3],'planted_q3_q4_q5':q[:3],
 'KL_target_degrees_to_planted_degrees':kl,'max_degree_3_to_5_difference':max(differences),
 'unconditioned_loop_free_upper_bound':math.exp(-3*p[0]/mu),
 'planted_simplicity_limit':math.exp(-tau/2-tau*tau/4-(mu-2))})
Path('planted_degrees.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
