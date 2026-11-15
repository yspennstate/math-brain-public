"""Full connected-domain high precision optimization in a Schur chart."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource,math,argparse
from pathlib import Path
import mpmath as mp
from scipy.optimize import differential_evolution,minimize
from general_collar import block,kernel,limit
from mp_core import evaluate,strict,strings

def sigmoid(z):return 1/(1+mp.exp(-z))

def make(y):
 y=[mp.mpf(str(z)) for z in y];s0,s1,ang,beta,phi,aa,kk=y
 l0,l1=sorted([sigmoid(s0),sigmoid(s1)])
 if l0==l1:raise ArithmeticError('equal block eigenvalues')
 angle=mp.atan(mp.exp(ang));C=block(l0,1-l1,angle)
 U=mp.matrix([[mp.cos(angle),-mp.sin(angle)],[mp.sin(angle),mp.cos(angle)]])
 beta=mp.atan(mp.exp(beta));v=U*mp.matrix([mp.cos(beta),mp.sin(beta)*mp.exp(mp.j*phi)])
 a=sigmoid(aa);kappa=sigmoid(kk)
 bound0=mp.re((v.H*(C**-1)*v)[0])/a;bound1=mp.re((v.H*((mp.eye(2)-C)**-1)*v)[0])/(1-a)
 x=kappa/max(bound0,bound1)
 return kernel(a,C,v,x),dict(a=a,C=C,v=v,x=x,kappa=kappa)

def main():
 start=time.monotonic();out=dict(seed=33604,runs=[],evaluations=0,rejections=0,negative=[],best=None)
 path=Path('data/global_optimization.json');groupbest=None
 def save():
  out.update(seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20,priority=os.getpriority(os.PRIO_PROCESS,0))
  tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(path)
 def objective(y):
  nonlocal groupbest
  out['evaluations']+=1
  try:
   q,params=make(y);ev=evaluate(q);val=ev['logscale']*ev['margin']
   row=dict(params=list(map(float,y)),precision=mp.mp.dps,**strings(dict(product=val,margin=ev['margin'],Lambda=ev['logscale']),75))
   if groupbest is None or val<mp.mpf(groupbest['product']):groupbest=row
   if out['best'] is None or val<mp.mpf(out['best']['product']):out['best']=row
   if ev['margin']<0:out['negative'].append(row);save();raise RuntimeError('negative margin: independent audit needed')
   result=float(val)
  except (ValueError,ArithmeticError,ZeroDivisionError):out['rejections']+=1;result=1e6
  if out['evaluations']%100==0:save()
  return result
 for L in (20,80,200):
  mp.mp.dps=120+math.ceil(12*L/math.log(10));groupbest=None
  bounds=[(-L,L)]*4+[(-math.pi,math.pi),(-L,L),(-6*L,5)]
  result=differential_evolution(objective,bounds,seed=33604+L,popsize=7,maxiter=65,polish=False,workers=1,tol=1e-10)
  # Bounded local refinement; phase and mode alignment remain free.
  local=minimize(objective,result.x,method='Nelder-Mead',bounds=bounds,options=dict(maxfev=1200,xatol=1e-9,fatol=1e-12))
  out['runs'].append(dict(L=L,dps=mp.mp.dps,best=groupbest,DE=dict(nfev=result.nfev,success=bool(result.success),message=str(result.message)),local=dict(nfev=local.nfev,success=bool(local.success),message=str(local.message))))
  print('L',L,'evaluations',out['evaluations'],'best',groupbest,flush=True);save()
 save()
if __name__=='__main__':main()
