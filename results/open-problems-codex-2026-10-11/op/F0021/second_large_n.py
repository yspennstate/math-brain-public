from pathlib import Path
import math,time,json,numpy as np
from scipy.special import gammaln,logsumexp
p=Path('~/brain_workers/TRIO_1011/op/F0021');rng=np.random.default_rng(21013);start=time.monotonic()
def lp(t,x):
 if abs(x)>t or (t+x)%2:return -math.inf
 k=(t+x)//2
 return float(gammaln(t+1)-gammaln(k+1)-gammaln(t-k+1)-t*math.log(2))
def cluster(sites):
 v=[];dp=[];cost=[]
 for j,(t,x,w) in enumerate(sites):
  terms=[lp(t,x)];scores=[-x*x/(2*t)]
  for i,(ti,xi,wi) in enumerate(sites[:j]):
   if t>ti:
    lk=lp(t-ti,x-xi)
    if lk!=-math.inf:terms.append(v[i]+lk);scores.append(dp[i]-(x-xi)**2/(2*(t-ti)))
  v.append(w+math.log1p(-math.exp(-w))+float(logsumexp(terms)));dp.append(2*w+max(scores));cost.append(x*x/(2*t))
 le=float(logsumexp(v)) if v else -math.inf
 return float(np.logaddexp(0,le)),le,max([0.]+dp),min(cost,default=math.inf)
records=[]
for n in [2**18,2**22,2**26,2**30]:
 N=n*(n+3)//2;alpha=5.5;kappa=.32;u=n**kappa;A=n**(1/3);vals=[];good=0;failure=0;Ks=[]
 for rep in range(200):
  K=int(rng.binomial(N,u**(-alpha)));ranks=set()
  while len(ranks)<K:ranks.add(int(rng.integers(N)))
  sites=[]
  for rank in sorted(ranks):
   t=(math.isqrt(9+8*rank)-3)//2+1
   previous=(t-1)*(t+2)//2;x=-t+2*(rank-previous)
   assert previous<=rank<t*(t+3)//2 and abs(x)<=t and (x+t)%2==0
   w=u*(1-float(rng.random()))**(-1/alpha);sites.append((t,x,w))
  lz,le,score,mc=cluster(sites);vals.append(lz/A);Ks.append(K)
  if mc>A and score==0 and K*math.log(2)<=A/4:
   good+=1;assert le<=-A/4+1e-5
  if le>-A/4:failure+=1
 records.append({'n':n,'alpha':alpha,'kappa':kappa,'repetitions':200,'mean_large_sites':float(np.mean(Ks)),'fraction_full_sufficient_event':good/200,'fraction_exponential_bound_failure':failure/200,'mean_logZ_over_n_one_third':float(np.mean(vals)),'max_logZ_over_n_one_third':float(max(vals))})
z={'seed':21013,'experiments':records,'elapsed_seconds':time.monotonic()-start,'memory_method':'Store only large sites; no n-size or n^2-size arrays.'}
p.joinpath('SECOND_LARGE_N_CHECKS.json').write_text(json.dumps(z,indent=2),encoding='utf-8');print(json.dumps(z,indent=2))
