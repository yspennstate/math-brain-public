"""Target the proposed stronger local remainder, not the actual conjecture.

The candidate is a rigorous lower bound on full curvature. Its global sign is
unproved. Retains exact nonpositive-h terms and quantitative positive-h terms.
"""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution
from explore_fourier_adverse import evaluate,counts

def candidate(z,detail=False):
 lam=1/(1+np.exp(-np.array(z[:4])));vel=np.array(z[4:]);norm=np.linalg.norm(vel)
 if norm<1e-12:return 1e10
 vel/=norm;lo,full,term,parts=evaluate(lam,vel)
 c,d,u,v=vel;slopes=np.array([c+u,d+v,c-u,d-v]);f=counts(lam)
 g=sum((slopes[i]*counts(np.delete(lam,i)) for i in range(4)),np.zeros(4))
 h=np.array(parts['h']);rho=np.sqrt(f[:-2]*f[2:])/f[1:-1]
 Q=np.array([g[j]**2/f[j]-2*g[j]*g[j+1]/f[j+1]+g[j+1]**2/f[j+2] for j in range(3)])
 L=-2*np.log(rho);coefficient=1-rho*L/(1-rho*rho)
 sq=(g[:-1]/np.sqrt(f[:-2])-g[1:]/np.sqrt(f[2:]))**2
 remainder=np.where(h<=0,Q,coefficient*Q+rho*L/(1-rho)*sq)
 bound=lo+sum(remainder)
 if detail:return dict(candidate_bound=float(bound),actual_curvature=full,adverse_term=term,lambda_values=lam.tolist(),velocity=vel.tolist(),h=h.tolist(),local_Q=Q.tolist(),local_remainder=remainder.tolist())
 return bound

def main():
 start=time.time();results=[]
 for seed in [811,812,813]:
  res=differential_evolution(candidate,[(-11,11)]*4+[(-1,1)]*4,seed=seed,popsize=10,maxiter=100,tol=1e-8,polish=False,workers=1,updating='immediate')
  r=candidate(res.x,True);r.update(seed=seed,function_evaluations=res.nfev,optimizer_success=bool(res.success));results.append(r);print(json.dumps(r),flush=True)
  Path(__file__).with_name('fourier_local_remainder_exploration.json').write_text(json.dumps(dict(status='numerical exploration; global candidate sign unproved',elapsed=time.time()-start,results=results),indent=2)+'\n')
if __name__=='__main__':main()
