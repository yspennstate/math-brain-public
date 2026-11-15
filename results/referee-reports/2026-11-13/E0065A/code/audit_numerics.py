"""Independent scalar checks of optimizer output and random differential checks."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import json,math,resource
from pathlib import Path
import numpy as np
from search import Model
rng=np.random.default_rng(651115)
summary={'seed':651115,'nice':os.getpriority(os.PRIO_PROCESS,0),'two_point_summary':[]}
runs=json.loads(Path('data/search_results.json').read_text())['runs']
for m in [3,4]:
 for kind in ['cycle','fixed']:
  for gap in [.02,.002,.0002]:
   records=[r for r in runs if r['m']==m and r['kind']==kind and r['requested_gap']==gap]
   valid=[]
   for rec in records:
    def V(x):
     return [math.fsum((1 if i==j else 2)*float(rec['P'][r][k])*float(x[i])*float(x[j]) for r,(i,j) in enumerate(rec['pairs'])) for k in range(m)]
    vx,vy=V(rec['x']),V(rec['y'])
    u,v=(rec['y'],rec['x']) if kind=='cycle' else (rec['x'],rec['y'])
    err=max([abs(i-j) for i,j in zip(vx,u)]+[abs(i-j) for i,j in zip(vy,v)]+[abs(math.fsum(row)-1) for row in rec['P']]+[abs(math.fsum(rec['x'])-1),abs(math.fsum(rec['y'])-1)])
    floor=min(min(row) for row in rec['P'])
    if err<2e-8 and floor>=rec['lambda']-2e-8 and rec['x'][0]-rec['y'][0]>=gap-2e-8:
     valid.append((rec,err))
   best,err=max(valid,key=lambda r:r[0]['lambda'])
   summary['two_point_summary'].append({'m':m,'kind':kind,'gap':gap,'starts':len(records),'feasible_scalar':len(valid),'best_lambda':best['lambda'],'best_equality_residual_scalar':err,'best_actual_gap':best['x'][0]-best['y'][0]})
# Finite-difference audit of the analytic optimization Jacobian, on random points.
jerr=0.
for m in [3,4]:
 for kind in ['cycle','fixed']:
  M=Model(m,.02,kind);w=M.seed(rng,3);J=M.jac(w);eps=1e-6
  for k in range(M.n):
   e=np.zeros(M.n);e[k]=eps
   num=(M.fun(w+e)-M.fun(w-e))/(2*eps)
   jerr=max(jerr,float(max(abs(num-J[:,k]))))
summary['analytic_jacobian_max_central_difference_error']=jerr
# Audit equation (13) without relying on the optimizer and in dimensions >4 too.
max_quadratic=0.;max_mixture=0.;max_full=0.;samples=0
for m in [3,4,10]:
 for trial in range(600):
  x=rng.dirichlet(np.full(m,.7));h=rng.normal(size=m);h-=h.mean()
  mu=rng.uniform(.001,.95/m);t=1-m*mu
  pairs=[(i,j) for i in range(m) for j in range(i,m)]
  Q=rng.dirichlet(np.full(m,.3),len(pairs))
  w=np.zeros(m);dw=np.zeros(m)
  for row,(i,j) in zip(Q,pairs):
   coeff=1 if i==j else 2
   w+=coeff*x[i]*x[j]*row
   dw+=coeff*(h[i]*x[j]+x[i]*h[j])*row
  base=math.fsum(float(h[i])**2/float(x[i]) for i in range(m))
  qnorm=math.fsum(float(dw[i])**2/float(w[i]) for i in range(m))
  out=math.fsum(float(t*dw[i])**2/float(mu+t*w[i]) for i in range(m))
  max_quadratic=max(max_quadratic,qnorm/(2*base))
  max_mixture=max(max_mixture,out/(t*t*qnorm/(t+2*mu)))
  max_full=max(max_full,out/(2*t*t*base/(t+2*mu)));samples+=1
summary['fisher_random_checks']={'samples':samples,'quadratic_ratio_max_le_1':max_quadratic,'mixture_ratio_max_le_1':max_mixture,'composite_ratio_max_le_1':max_full}
assert jerr<1e-7
assert max_quadratic<=1+1e-10 and max_mixture<=1+1e-10 and max_full<=1+1e-10
summary['family_fixed_point_stability']=[]
for m in [3,4]:
 crit=(1-1/math.sqrt(m+1))/(2*m)
 for mu in [crit-1e-4,crit,crit+1e-4]:
  t=1-m*mu;beta=(m-2)*mu
  z=(1+t-math.sqrt((1+t)**2-6*t*beta-3*t*t))/(3*t)
  eigs=[-t*(1+z),t*(3*z-1)]+[0]*(m-3)
  summary['family_fixed_point_stability'].append({'m':m,'lambda':mu,'z':z,'eigenvalues':eigs,'rho':max(abs(v) for v in eigs)})
summary['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
Path('data/numerical_audit.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
