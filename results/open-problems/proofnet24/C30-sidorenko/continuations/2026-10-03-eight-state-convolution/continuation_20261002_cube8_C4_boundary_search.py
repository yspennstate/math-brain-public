"""Numerical C4 sign attack near a sparse quotient boundary; no claim."""
from pathlib import Path
import json
from collections import defaultdict
import numpy as np
from scipy.optimize import minimize


def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_C4_host_sos.json').read_text())['host_polynomial']
 terms=[(tuple(map(int,n.split(',')))[::2],tuple(map(int,n.split(',')))[1::2],c) for n,c in F.items()]
 rng=np.random.default_rng(434323);out=[]
 for eps in [.5,.2,.1,.05,.02,.01,.005,.002,.001,.0001]:
  a=np.array([1,eps,eps,0])
  q=defaultdict(float)
  for A,B,c in terms:q[B]+=c*np.prod(a**np.array(A))
  N=np.array(list(q));C=np.array(list(q.values()));C/=max(abs(C))
  def objective(b):
   norm=b@b;powers=b[:,None]**np.arange(5)[None,:]
   value=np.sum(C*np.prod(powers[np.arange(4)[None,:],N],axis=1));g=np.zeros(4)
   for j in range(4):
    active=N[:,j]>0;sub=N[active].copy();sub[:,j]-=1
    g[j]=np.sum(C[active]*N[active,j]*np.prod(powers[np.arange(4)[None,:],sub],axis=1))
   return value/norm**2,g/norm**2-4*value*b/norm**3
  best=None
  for i in range(100):
   b=rng.normal(size=4)*10**rng.uniform(-4,4,size=4)
   res=minimize(objective,b,jac=True,method='BFGS',options={'maxiter':500,'gtol':1e-14})
   if best is None or res.fun<best['value']:best={'value':float(res.fun),'b':(res.x/np.linalg.norm(res.x)).tolist()}
  out.append({'eps':eps,'best':best});print(eps,best,flush=True)
 Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'boundary numerical search only','records':out},indent=2))
if __name__=='__main__':main()
