import numpy as np,json,time
from pathlib import Path
EPS=.25
results=[]
def experiment(name,steps,N,finite_mod=None):
 t=time.time();width=finite_mod or (2*N+1);off=0 if finite_mod else N
 # orientations 0:+1, 1:-1; integer coordinate x, product (x,o)(t,s)=(x+o*t,o*s)
 P=np.zeros((2,2,width,width));P[0,0,off,off]=1
 d=len(steps);weights=np.full((d,d),EPS/d**2);weights[np.diag_indices(d)]+=(1-EPS)/d
 checkpoints={2,5,10,20,40,80,120}&set(range(1,N+1))
 for n in range(1,N+1):
  nxt=np.zeros_like(P)
  for oi in range(2):
   for oj in range(2):
    for i,(ti,si) in enumerate(steps):
     for j,(tj,sj) in enumerate(steps):
      shx=(1-2*oi)*ti;shy=(1-2*oj)*tj
      nxt[oi^(si==-1),oj^(sj==-1)]+=weights[i,j]*np.roll(P[oi,oj],(shx,shy),(0,1))
  P=nxt
  if n in checkpoints:
   p=P.sum(axis=(1,3));q=P.sum(axis=(0,2));product=p[:,None,:,None]*q[None,:,None,:]
   tv=.5*np.abs(P-product).sum()
   mask=product>1e-300;chi=((P[mask]-product[mask])**2/product[mask]).sum()
   B=np.zeros_like(P);B[mask]=(P[mask]-product[mask])/np.sqrt(product[mask]);B=B.transpose(0,2,1,3).reshape(2*width,2*width)
   row={'model':name,'n':n,'epsilon':EPS,'tv':float(tv),'chi_squared':float(chi),'mass':float(P.sum()),'symmetry_error':float(np.max(np.abs(B-B.T)))}
   # Numerical PSD audit, not proof; finite endpoint matrix from Section 2.
   row['min_eigenvalue']=float(np.linalg.eigvalsh(B).min())
   results.append(row);print(row,flush=True)
 print(name,'seconds',time.time()-t,flush=True)
experiment('Z SRW',[(1,1),(-1,1)],80)
experiment('D_infinity nonlazy',[(0,-1),(1,-1)],80)
experiment('D_infinity aperiodic SRW',[(0,-1),(1,-1),(1,1),(-1,1)],80)
experiment('C5 SRW',[(1,1),(-1,1)],80,5)
experiment('C6 SRW bipartite',[(1,1),(-1,1)],80,6)
Path('experiments.json').write_text(json.dumps(results,indent=2),encoding='utf8')
# Exact information-counterexample data, no numerical KL cancellation.
import math
Path('information_counterexample.json').write_text(json.dumps([{'k':k,'TV':(1-2.**(-k))/k,'I_lower_bound_nats':math.log(2)-(-1/k*math.log(1/k)-(1-1/k)*math.log(1-1/k)),'I_upper_bound_nats':math.log(2)} for k in [2,10,100,1000]],indent=2))
