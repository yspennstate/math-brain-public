"""Numerical sign search for individually colored Eulerian-cycle coefficients.
No proof or counterexample is asserted from floating-point output.
"""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize


def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_flow_and_smoothing.json').read_text())['Fourier_polynomial']
 n=np.array([list(map(int,key.split(','))) for key in F],dtype=int)
 c=np.array(list(F.values()),dtype=float)
 H=np.array([[(-1)**((i&j).bit_count()) for j in range(4)] for i in range(4)],dtype=float)
 rng=np.random.default_rng(823341)
 out={'status':'numerical colored-cycle sign search only','records':{}}
 for k in [4,6,8,10]:
  select=n[:,1::2].sum(axis=1)==k
  N=n[select];C=c[select]
  def objective(z):
   a=np.exp(z[:4]-z[:4].max());a/=a.sum()
   d=np.exp(z[4:]-z[4:].max());d/=d.sum()
   signs=np.array([-1,1,1,1]);b=signs*d
   r=np.empty(8);r[::2]=H@a;r[1::2]=H@b
   powers=r[:,None]**np.arange(16)[None,:]
   terms=C*np.prod(powers[np.arange(8)[None,:],N],axis=1)
   value=terms.sum();gr=np.zeros(8)
   for j in range(8):
    active=N[:,j]>0;sub=N[active].copy();sub[:,j]-=1
    gr[j]=np.sum(C[active]*N[active,j]*np.prod(powers[np.arange(8)[None,:],sub],axis=1))
   ga=H.T@gr[::2];gd=signs*(H.T@gr[1::2])
   gradient=np.r_[a*(ga-a@ga),d*(gd-d@gd)]
   return value,gradient
  z=rng.normal(size=8);val,grad=objective(z);epsilon=1e-5
  fd=np.array([(objective(z+epsilon*np.eye(8)[i])[0]-objective(z-epsilon*np.eye(8)[i])[0])/(2*epsilon) for i in range(8)])
  records=[]
  for trial in range(100):
   z=rng.normal(size=8)*rng.choice([.2,1,3,6])
   res=minimize(objective,z,jac=True,method='L-BFGS-B',options={'maxiter':400,'ftol':1e-14,'gtol':1e-9})
   a=np.exp(res.x[:4]-res.x[:4].max());a/=a.sum()
   d=np.exp(res.x[4:]-res.x[4:].max());d/=d.sum()
   records.append({'value':float(res.fun),'a':a.tolist(),'b':(-d[0]).tolist() if False else (np.array([-1,1,1,1])*d).tolist(),'success':bool(res.success)})
   if trial%20==0:print(k,trial,'minimum',min(t['value'] for t in records),flush=True)
   if res.fun < -1e-7:break
  out['records'][str(k)]={'flow_terms':int(select.sum()),'gradient_fd_error':float(np.max(abs(fd-grad))),
                        'minimum':min(t['value'] for t in records),'tests':records}
  Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print(json.dumps({k:{j:l for j,l in v.items() if j!='tests'} for k,v in out['records'].items()},indent=2))
if __name__=='__main__':main()
