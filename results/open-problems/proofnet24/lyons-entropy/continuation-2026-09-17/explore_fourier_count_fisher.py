"""Unproved final Fourier route: count Fisher payment in negative imbalance."""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution
from explore_fourier_adverse import counts,channel
C,bits=channel();W=np.array([[1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,1,0,-1]])

def matrix(logits):
 lam=1/(1+np.exp(-np.array(logits)));ip=np.prod(np.where(bits,lam,1-lam),axis=1);p=C@ip
 ell=np.log(p[5]/p[3]);variance=float(sum(lam*(1-lam)));f=counts(lam)
 g=np.array([counts(np.delete(lam,i)) for i in range(4)]).T@W
 df=np.vstack([np.zeros(4),g])-np.vstack([g,np.zeros(4)])
 FI=df.T@(df/f[:,None]);M=.4*FI;M[0,1]+=2*ell;M[1,0]+=2*ell
 return lam,ell,variance,M

def objective(z,detail=False):
 lam,ell,variance,M=matrix(z)
 if ell>=0 or -ell*variance<=1.6:return 2
 diag=np.diag(M)
 if min(diag)<=1e-15:return 2
 scale=np.sqrt(diag);B=M/scale[:,None]/scale[None,:];ww,V=np.linalg.eigh(B)
 if not detail:return ww[0]
 direction=V[:,0]/scale;direction/=np.linalg.norm(direction)
 return dict(lambda_values=lam.tolist(),ell=float(ell),variance=variance,unproved_domain_value=float(-ell*variance),scaled_minimum_eigenvalue=float(ww[0]),direction=direction.tolist(),unscaled_directional_bound=float(direction@M@direction))

def main():
 start=time.time();records=[]
 for seed in [901,902,903]:
  res=differential_evolution(objective,[(-14,14)]*4,seed=seed,popsize=10,maxiter=120,tol=1e-9,polish=False,workers=1,updating='immediate')
  detail=objective(res.x,True)
  rec=detail if isinstance(detail,dict) else dict(no_feasible_candidate=True,objective=float(detail))
  rec.update(seed=seed,function_evaluations=res.nfev,optimizer_success=bool(res.success));records.append(rec);print(json.dumps(rec),flush=True)
  Path(__file__).with_name('fourier_count_fisher_exploration.json').write_text(json.dumps(dict(status='unproved candidate inequality; numerical exploration only',elapsed=time.time()-start,results=records),indent=2)+'\n')
if __name__=='__main__':main()
