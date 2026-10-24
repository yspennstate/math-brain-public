import numpy as np,json,time
from pathlib import Path
from numba import njit
from scipy.ndimage import label
@njit(cache=False)
def evolve(eta,lam,T,seed):
 np.random.seed(seed)
 side=eta.shape[0];count=np.random.poisson(side*side*(1+4*lam)*T)
 for step in range(count):
  x=np.random.randint(side);y=np.random.randint(side)
  if np.random.random()<1/(1+4*lam):eta[x,y]=0
  else:
   dr=np.random.randint(4);xx=x;yy=y
   if dr==0:xx+=1
   elif dr==1:xx-=1
   elif dr==2:yy+=1
   else:yy-=1
   if xx<0 or yy<0 or xx>=side or yy>=side or eta[xx,yy]:eta[x,y]=1
 return eta
def crosses(eta,L):
 # D coordinates [-2L,3L-1]; M occupies indices [L,4L-1].
 a=eta[L:4*L,L:4*L];labs,_=label(a)
 inner=labs[L:2*L,L:2*L]
 shell=np.concatenate((labs[0,:],labs[-1,:],labs[:,0],labs[:,-1]))
 return bool(set(np.unique(inner))&set(np.unique(shell))-{0})
results=[]
seed=610111
for lam in [.35,.4,.43]:
 for L in [1,2,4,8]:
  t=time.time();hits=0;density=[];reps=40;T=100.
  for j in range(reps):
   seed+=1;eta=np.ones((5*L,5*L),dtype=np.uint8)
   eta=evolve(eta,lam,T,seed)
   hits+=crosses(eta,L);density.append(float(eta[2*L:3*L,2*L:3*L].mean()))
  rec={'lambda':lam,'L':L,'D_side':5*L,'time_from_full':T,'independent_replicas':reps,'crossing_hits':hits,'crossing_fraction':hits/reps,'mean_inner_density':float(np.mean(density)),'seconds':time.time()-t,'warning':'finite-time numerical evidence, no stationary error bound or percolation conclusion'}
  results.append(rec);Path('wired_mc_results.json').write_text(json.dumps(results,indent=2),encoding='utf8');print(json.dumps(rec),flush=True)
