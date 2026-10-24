import time,json,math
from pathlib import Path
import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.integrate import quad
import deferred_checks as base

rng=np.random.default_rng(2572718);start=time.monotonic();out=[]
def save(row):
 out.append(row);Path('deferred_followup.json').write_text(json.dumps(out,indent=2));print(row,flush=True)

# Resolve the initial generic infinite-interval quadrature warnings by putting
# breakpoints only in the independent numerical integral, not changing the
# algebraic piecewise formula under test.
errs=[]
for _ in range(100):
 a=np.r_[0.,rng.uniform(0,15,9)];u=rng.uniform(.05,1);b=float(a.max())
 f=lambda t:math.exp(-u*np.maximum(t-a,0).sum())
 q=quad(f,0,b,points=np.sort(a)[1:-1],epsabs=1e-10)[0]+quad(f,b,np.inf,epsabs=1e-10)[0]
 err=abs(q-base.mean_time(a,u));errs.append(err);assert err<1e-8
save({'check':'quadrature_with_breakpoints','cases':100,'max_error':max(errs),'passed':True})

# Coupled reconstruction, cone field, and covering-count checks from fully
# presampled graphs. No distributional agreement is used as a proof.
states=0;covers=0
for trial in range(60):
 n=20;W=np.zeros((n,n));i,j=np.triu_indices(n,1);W[i,j]=rng.exponential(n,len(i));W+=W.T
 full=shortest_path(W,directed=False)
 order=[0];rem=list(range(1,n));D=np.zeros((1,1));h=np.zeros(1);steps=[]
 for m in range(1,n):
  d=D[-1];cut=W[np.ix_(order,rem)];row,col=np.unravel_index(np.argmin(d[:,None]+cut),cut.shape)
  t=float(d[row]+cut[row,col]);q=rem[col];steps.append(t)
  hp=np.maximum(h,t-d);D=base.update_metric(D,W[q,order]);h=np.r_[hp,0.];order.append(q);rem.remove(q)
  expected=np.maximum(0.,np.max(np.array(steps)[:,None]-D[:-1,:],axis=0))
  assert np.max(np.abs(h-expected))<1e-8
  for old in range(m):
   assert np.argmin(D[old,old+1:])==0
   assert abs(D[old,old+1]-steps[old])<1e-8
  states+=1
 for r in [.5,1.,2.,3.,4.]:
  s=min(n,math.ceil(n*math.exp(-r/4)))
  uncovered=int(np.count_nonzero(np.min(full[:s],axis=0)>r))
  assert np.count_nonzero(np.array(steps)>2*r)<=s+uncovered
  covers+=1
save({'check':'cone_history_recovery_and_cover_counts','states':states,'cover_cases':covers,'passed':True})

# Probe the remaining random drift, rather than merely another lower bound.
# Stop between replicates after three minutes and preserve every completed row.
for n,reps in [(40,40),(100,20),(200,10)]:
 vals=[];profiles=[]
 for _ in range(reps):
  if time.monotonic()-start>180:break
  t,m=base.state_sampler(n)
  vals.append([t.sum()/n,m.sum()/n,(t.sum()-m.sum())/n])
  profiles.append([float(np.mean(m[int(.1*(n-1)):int(.3*(n-1))])),float(np.mean(m[int(.4*(n-1)):int(.6*(n-1))])),float(np.mean(m[int(.7*(n-1)):int(.9*(n-1))]))])
 if not vals:break
 a=np.array(vals)
 save({'check':'predictable_drift_samples','n':n,'replicates':len(vals),'mean_length_drift_difference':a.mean(axis=0).tolist(),'std_length_drift_difference':a.std(axis=0,ddof=1).tolist(),'mean_drift_at_discovery_fraction_10to30_40to60_70to90':np.mean(profiles,axis=0).tolist(),'interpretation':'Numerical only; does not prove drift concentration or determine a limit constant.'})
save({'elapsed_seconds':time.monotonic()-start})
