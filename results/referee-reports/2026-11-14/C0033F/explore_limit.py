import json,time,random,resource
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
import mpmath as mp
from general_collar import block,limit
from mp_core import strings
mp.mp.dps=100
start=time.monotonic();rng=random.Random(33601);best=None;n=0

def decode(y):
 L0,L1,ang,va,phase=map(lambda z:mp.mpf(str(z)),y)
 C=block(mp.exp(-L0),mp.exp(-L1),mp.pi/(2*(1+mp.exp(-ang))))
 v=mp.matrix([mp.cos(va),mp.sin(va)*mp.exp(mp.j*phase)])
 return C,v

def objective(y):
 global best,n
 n+=1
 try:
  C,v=decode(y);d=limit(C,v,True);Lam=-mp.log(min(d['pi'])/2);val=Lam*d['m0']
  if not best or val<mp.mpf(best['value']):
   best=strings(dict(value=val,params=list(y),m0=d['m0'],Lambda=Lam,K=d['K'],ratio=d['w']/d['K']),65)
  if n%100==0:Path('data/limit_search_checkpoint.json').write_text(json.dumps(dict(n=n,best=best,seconds=time.monotonic()-start),indent=2)+'\n')
  return float(val)
 except (ArithmeticError,ValueError,ZeroDivisionError):return 1e9

if __name__=='__main__':
 runs=[]
 for L in (10,40,100):
  mp.mp.dps=120+int(4*L/2.3)
  bounds=[(.7,L),(.7,L),(-L,L),(0,float(mp.pi/2)),(0,float(mp.pi))]
  rr=differential_evolution(objective,bounds,seed=33600+L,popsize=8,maxiter=55,tol=1e-9,polish=False,workers=1)
  runs.append(dict(L=L,value=rr.fun,params=list(rr.x),nfev=rr.nfev,success=rr.success))
  print(L,n,best,flush=True)
 Path('data/limit_search.json').write_text(json.dumps(dict(runs=runs,n=n,best=best,seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20),indent=2)+'\n')
