"""Numerical nonnegativity test of C4's host-a coefficient quartics.
No SOS or polynomial positivity is inferred from these experiments.
"""
from pathlib import Path
import json
from collections import defaultdict
import numpy as np
from scipy.optimize import minimize


def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_colored_partial_walsh.json').read_text())['records']['4']['polynomial']
 Q=defaultdict(dict)
 for raw,c in F.items():
  n=tuple(map(int,raw.split(',')));Q[n[::2]][n[1::2]]=c
 reps={a:p for a,p in Q.items() if tuple(sorted(a,reverse=True))==a}
 print('representatives',len(reps),flush=True)
 rng=np.random.default_rng(840044)
 records=[]
 for a,p in reps.items():
  N=np.array(list(p));C=np.array(list(p.values()),dtype=float);C/=max(abs(C))
  def objective(b):
   r2=b@b
   if r2<1e-20:return 1e20,np.zeros(4)
   powers=b[:,None]**np.arange(5)[None,:]
   value=np.sum(C*np.prod(powers[np.arange(4)[None,:],N],axis=1))
   grad=np.zeros(4)
   for j in range(4):
    active=N[:,j]>0;sub=N[active].copy();sub[:,j]-=1
    grad[j]=np.sum(C[active]*N[active,j]*np.prod(powers[np.arange(4)[None,:],sub],axis=1))
   return value/r2**2,grad/r2**2-4*value*b/r2**3
  best=None
  for trial in range(30):
   z=rng.normal(size=4);res=minimize(objective,z,jac=True,method='BFGS',options={'maxiter':200,'gtol':1e-10})
   if best is None or res.fun<best['value']:best={'value':float(res.fun),'b':(res.x/np.linalg.norm(res.x)).tolist()}
  records.append({'host_a_exponents':a,'best':best})
  print(a,best['value'],flush=True)
  if best['value'] < -1e-7:break
 Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'numerical coefficient quartic search, no positivity theorem','records':records},indent=2))
if __name__=='__main__':main()
