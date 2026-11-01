import numpy as np,json
from pathlib import Path
rng=np.random.default_rng(409)
results={}
for d in [2,3]:
 p=d-1;n=d+1
 angles=np.arange(3)*2*np.pi/3 if d==2 else None
 theta=np.column_stack((np.cos(angles),np.sin(angles))) if d==2 else np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/np.sqrt(3)
 us=[];aa=[]
 for i in range(n):
  kept=np.delete(theta,i,axis=0)
  _,_,vh=np.linalg.svd(kept[1:]-kept[0]);u=vh[-1]
  if (kept[0]-theta[i])@u<0:u=-u
  us.append(u);aa.append(kept[0]@u)
 us=np.array(us);aa=np.array(aa)
 ts=np.linspace(.2,.8,n);q=np.tanh(ts)
 phi=rng.normal(size=(250000,d));phi/=np.linalg.norm(phi,axis=1)[:,None]
 caps=((1-aa*q)/(1-(phi@us.T)*q))**p
 A=np.maximum(0,np.max(caps-1,axis=1)).mean()
 pred=(1+A)**(-n)
 # Simulate the common finite PPP exactly on S<R<Rmax. Its restriction contains every blocker before the chosen times.
 M=np.max(((1-aa*q)/(1-q))**p)
 hits=0;trials=12000
 for z in range(trials):
  S=rng.gamma(n);N=rng.poisson(S*(M-1))
  ph=rng.normal(size=(N,d));ph/=np.linalg.norm(ph,axis=1)[:,None]
  R=rng.uniform(S,S*M,size=N)
  threshold=S*((1-aa*q)/(1-(ph@us.T)*q))**p
  hits+=int(not np.any(R[:,None]<threshold))
 results[str(d)]={'theta':theta.tolist(),'u':us.tolist(),'a':aa.tolist(),'times':ts.tolist(),'union_integral_MC':float(A),'predicted':float(pred),'poisson_survival':hits/trials,'trials':trials,'standard_error':float(np.sqrt(pred*(1-pred)/trials))}
 # Independently check local derivative/Jacobian using centered differences.
 S=2.3;eps=1e-6
 def radii(y):
  x=y[:d];s=y[d];return s/(np.sqrt(1+x@x)-theta@x)**p
 y=np.r_[np.zeros(d),S];J=np.column_stack([(radii(y+np.eye(n)[k]*eps)-radii(y-np.eye(n)[k]*eps))/(2*eps) for k in range(n)])
 D=abs(np.linalg.det(np.column_stack((np.ones(n),theta))))
 results[str(d)]['jacobian_relative_error']=float(abs(abs(np.linalg.det(J))-(p*S)**d*D)/((p*S)**d*D))
Path('checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8');print(json.dumps(results,indent=2))
