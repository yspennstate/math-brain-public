import math,json,time
from pathlib import Path
import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.integrate import quad
from scipy.stats import kstest,ks_2samp

rng=np.random.default_rng(2572026)
results=[]

def mean_time(a,u,R=math.inf):
 a=np.sort(a);total=0.;hazard=0.
 for j in range(1,len(a)+1):
  left=a[j-1];right=a[j] if j<len(a) else math.inf
  if left>=R:break
  length=min(right,R)-left;rate=u*j
  total+=math.exp(-hazard)*(-math.expm1(-rate*length))/rate
  if math.isinf(right) or right>=R:break
  hazard+=rate*(right-left)
 return total

def draw_time(a,u):
 a=np.sort(a);c=np.cumsum(a);j=np.arange(1,len(a)+1)
 candidates=(rng.exponential()/u+c)/j
 right=np.r_[a[1:],np.inf]
 index=np.flatnonzero(candidates<=right)[0]
 return float(candidates[index])

def update_metric(D,w):
 b=np.min(w[:,None]+D,axis=0)
 m=len(w);out=np.zeros((m+1,m+1))
 out[:m,:m]=np.minimum(D,b[:,None]+b[None,:])
 out[-1,:m]=out[:m,-1]=b
 return out

def state_sampler(n,checks=False):
 D=np.zeros((1,1));h=np.zeros(1);T=[];drift=[]
 for m in range(1,n):
  d=D[-1];a=d+h;u=(n-m)/n
  drift.append(mean_time(a,u));t=draw_time(a,u);T.append(t)
  active=np.flatnonzero(a<t+1e-12);win=int(rng.choice(active))
  hp=np.maximum(h,t-d)
  w=hp+rng.exponential(n,m);w[win]=t-d[win]
  D=update_metric(D,w);h=np.r_[hp,0.]
  if checks:
   assert np.max(h[:,None]-h[None,:]-D)<=1e-8
   assert np.max(h-D[-1])<=1e-8
 return np.array(T),np.array(drift)

def graph_run(n,all_checks=False):
 W=np.zeros((n,n));i,j=np.triu_indices(n,1);W[i,j]=rng.exponential(n,len(i));W+=W.T
 dg=shortest_path(W,directed=False);np.fill_diagonal(dg,np.inf)
 order=[0];remaining=list(range(1,n));D=np.zeros((1,1));h=np.zeros(1)
 T=[];innov=[];drift=[]
 for m in range(1,n):
  d=D[-1];cut=W[np.ix_(order,remaining)]
  trial=d[:,None]+cut;row,col=np.unravel_index(np.argmin(trial),trial.shape)
  t=float(trial[row,col]);q=remaining[col]
  # Global NUV must choose the same first unvisited target and time.
  g=dg[order[-1],remaining];assert q==remaining[int(np.argmin(g))]
  assert abs(t-float(np.min(g)))<=1e-8
  a=d+h;u=(n-m)/n
  innov.append(u*np.maximum(t-a,0).sum());T.append(t);drift.append(mean_time(a,u))
  assert np.min(cut-h[:,None])>=-1e-8
  hp=np.maximum(h,t-d);w=W[q,order]
  assert np.min(w-hp)>=-1e-8
  D=update_metric(D,w);order.append(q);remaining.remove(q);h=np.r_[hp,0.]
  if all_checks:
   exact=shortest_path(W[np.ix_(order,order)],directed=False)
   assert np.max(np.abs(D-exact))<=1e-8
   assert np.max(h[:,None]-h[None,:]-D)<=1e-8
 return np.array(T),np.array(innov),np.array(drift)

def run_initial_checks():
    # Integration and inversion checks are independent of a full NUV simulation.
    integration_errors=[]
    for _ in range(100):
     a=np.r_[0.,rng.uniform(0,15,9)];u=rng.uniform(.05,1)
     exact=mean_time(a,u)
     q=quad(lambda t:np.exp(-u*np.maximum(t-a,0).sum()),0,np.inf,points=None,epsabs=1e-7)[0]
     integration_errors.append(abs(exact-q));assert abs(exact-q)<1e-5
    results.append({'check':'piecewise_hazard_integration','cases':100,'max_error':max(integration_errors)})
    
    # Original graph runs: test the exact ordering, metric update, thresholds, and PIT.
    innov=[];pairs=[]
    for _ in range(250):
     ts,e,drift=graph_run(25,True);innov.extend(e.tolist());pairs.extend(zip(e[:-1],e[1:]))
    pairs=np.array(pairs)
    results.append({'check':'presampled_graph_invariants','graphs':250,'steps':6000,'all_passed':True,'innovation_mean':float(np.mean(innov)),'innovation_exp1_KS':list(map(float,kstest(innov,'expon'))),'adjacent_innovation_correlation':float(np.corrcoef(pairs.T)[0,1])})
    
    # A finite exact check: E L_3=15/4 for mean-3 edge weights.
    v=[]
    for _ in range(5000):v.append(state_sampler(3)[0].sum())
    results.append({'check':'n3_exact_mean','target':15/4,'replicates':len(v),'measured':float(np.mean(v)),'standard_error':float(np.std(v,ddof=1)/np.sqrt(len(v)))})
    
    # Distributional comparison; these samples cannot prove transition correctness.
    for n,reps in [(12,150),(40,100),(80,60)]:
     direct=[];deferred=[]
     for _ in range(reps):
      direct.append(graph_run(n)[0].sum()/n)
      deferred.append(state_sampler(n,True)[0].sum()/n)
     results.append({'check':'direct_vs_deferred','n':n,'replicates_each':reps,'direct_mean':float(np.mean(direct)),'deferred_mean':float(np.mean(deferred)),'two_sample_KS':list(map(float,ks_2samp(direct,deferred)))})
    
    Path('deferred_checks.json').write_text(json.dumps(results,indent=2))
    for r in results:print(r)

if __name__ == '__main__':
    run_initial_checks()
