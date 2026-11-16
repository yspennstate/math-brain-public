"""Numerical probes near the zero denominator and zero second gap boundaries."""
import json
import numpy as np
from scipy.linalg import expm
from stratum import *
rng=np.random.default_rng(613119)
records=[];best=(1.,None)
for family in ['triangle','two_edges','small_gap']:
 for eps in ([.1,.03,.01,.003,.001,.0001,.00001,.000001] if family!='small_gap' else [1e-2,1e-3,1e-4,1e-5,1e-6,1e-8,1e-10]):
  vals=[];dens=[]
  for k in range(1000):
   if family=='small_gap':
    U=frame(rng.uniform(-np.pi,np.pi,5));r=eps
    a=tmax(r,U)*rng.uniform(.2,1)
   else:
    L=np.zeros((5,5))
    edges=[(0,1,1/3),(0,2,1/3),(1,2,1/3)] if family=='triangle' else [(0,1,.5),(2,3,.5)]
    for i,j,z in edges:L[i,i]+=z;L[j,j]+=z;L[i,j]-=z;L[j,i]-=z
    ev,V=np.linalg.eigh(BASIS.T@L@BASIS)
    A=rng.normal(size=(4,4));A=(A-A.T)*eps
    U=BASIS@expm(A)@V[:,:2]
    r=1-eps*rng.uniform(0,1)
    a=tmax(r,U)*(1-eps*rng.uniform(0,.2))
   terms=closed(a,r*a,U);den=sum(terms[:3]);val=ratio(terms)
   assert min(matrices(a,r*a,U)[-1])>=-2e-15
   if den>1e-10:
    vals.append(val);dens.append(den)
    if val<best[0]:best=(val,{'family':family,'eps':eps,'a':a,'b':r*a,'U':U.tolist(),'den':den})
  rec={'family':family,'epsilon':eps,'samples':len(vals),'min_ratio':float(min(vals)),'min_denominator':float(min(dens))}
  records.append(rec);print(json.dumps(rec),flush=True)
print('BEST',json.dumps(best),flush=True)
with open('boundary_checks.json','w') as f:json.dump(records,f,indent=2)
