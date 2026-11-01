from pathlib import Path
import json,itertools,math,time
from fractions import Fraction
import numpy as np
from scipy.special import gammaln,logsumexp
p=Path('~/brain_workers/TRIO_1011/op/F0021');start=time.monotonic();rng=np.random.default_rng(21012)
z={'seed':21012,'checks':{},'sparse_pareto_experiments':[]}
def ent(c):
 last=(0,0);v=Fraction(0)
 for t,x in c:
  v+=Fraction((x-last[1])**2,2*(t-last[0]));last=(t,x)
 return v
n=5;chains=[];coarsenings=0
for opts in itertools.product(*[[None]+list(range(-t,t+1,2)) for t in range(1,n+1)]):
 c=[(t,x) for t,x in enumerate(opts,1) if x is not None]
 if not c:continue
 E=ent(c);chains.append((len(c),E))
 for mask in range(1<<len(c)):
  sub=[v for j,v in enumerate(c) if mask>>j&1]
  assert ent(sub)<=E;coarsenings+=1
z['checks']['exact_entropy_coarsenings']=coarsenings;z['checks']['cone_chains_enumerated']=len(chains)
for B in [Fraction(1,1000),Fraction(1,8),Fraction(1,2),Fraction(1),Fraction(3),Fraction(10)]:
 for k in range(1,n+1):
  count=sum(1 for a,b in chains if a==k and b<=B)
  bound=(math.e**2*n/k*(1+math.sqrt(2*math.pi*float(B)*n)/k))**k
  assert count<=bound
z['checks']['finite_chain_count_comparisons']=30
z['checks']['zero_entropy_chains_by_length']={str(k):sum(1 for a,b in chains if a==k and b==0) for k in range(1,n+1)}
def lp(t,x):
 if t==0:return 0. if x==0 else -math.inf
 if abs(x)>t or (t+x)%2:return -math.inf
 k=(t+x)//2
 return float(gammaln(t+1)-gammaln(k+1)-gammaln(t-k+1)-t*math.log(2))
def logexpm1(v):return v+math.log1p(-math.exp(-v)) if v>40 else math.log(math.expm1(v))
def cluster(sites,beta):
 sites=sorted(sites);vs=[];dp=[];costs=[]
 for j,(t,x,w) in enumerate(sites):
  s=[lp(t,x)];score=[-x*x/(2*t)]
  for i,(ti,xi,wi) in enumerate(sites[:j]):
   if t>ti:
    lk=lp(t-ti,x-xi)
    if lk!=-math.inf:s.append(vs[i]+lk);score.append(dp[i]-(x-xi)**2/(2*(t-ti)))
  vs.append(logexpm1(beta*w)+float(logsumexp(s)))
  dp.append(2*beta*w+max(score));costs.append(x*x/(2*t))
 le=float(logsumexp(vs)) if vs else -math.inf
 return float(np.logaddexp(0,le)),le,max([0.]+dp),min(costs,default=math.inf)
# Cluster expansion against direct enumeration in finite inhomogeneous environments.
errors=[]
for rep in range(50):
 n=8;allpts=[(t,x) for t in range(1,n+1) for x in range(-t,t+1,2)]
 idx=rng.choice(len(allpts),8,replace=False);sites=[(*allpts[int(i)],float(rng.uniform(.1,3))) for i in idx];beta=.8
 d={(t,x):w for t,x,w in sites}
 energies=[]
 for steps in itertools.product([-1,1],repeat=n):
  x=0;H=0
  for t,dx in enumerate(steps,1):x+=dx;H+=beta*d.get((t,x),0)
  energies.append(H)
 direct=float(logsumexp(energies)-n*math.log(2));cl,_,_,_=cluster(sites,beta)
 errors.append(abs(cl-direct));assert abs(cl-direct)<1e-10
z['checks']['cluster_expansion_vs_256_paths_max_log_error']=max(errors)
# Positive backgrounds disprove the multiplicative partition shortcut already at n=1.
a=2.;b=3.;Zab=(1+math.exp(a+b))/2;product=((1+math.exp(a))/2)*((1+math.exp(b))/2)
assert Zab>product
z['checks']['subadditivity_obstruction']={'Z_a_plus_b':Zab,'Z_a_times_Z_b':product,'difference_identity_error':abs((Zab-product)-(math.expm1(a)*math.expm1(b)/4))}
# Exact sparse iid Pareto law via binomial count, uniform sites, and conditional Pareto values.
alpha=5.5;kappa=.32;beta=1.;reps=500
assert 5/(3*alpha)<kappa<1/3
for n in [256,1024,4096,16384,65536]:
 N=n*(n+3)//2;u=n**kappa;prob=u**(-alpha);cum=np.arange(1,n+1,dtype=np.int64);cum=cum*(cum+3)//2
 valid=0;failure=0;logs=[];maxscores=[];Ns=[];excess_logs=[]
 for rep in range(reps):
  K=int(rng.binomial(N,prob));ranks=set()
  while len(ranks)<K:ranks.add(int(rng.integers(N)))
  sites=[]
  for r in sorted(ranks):
   t=int(np.searchsorted(cum,r,side='right'))+1;previous=(t-1)*(t+2)//2;x=-t+2*(r-previous)
   w=u*(1-float(rng.random()))**(-1/alpha);sites.append((t,x,w))
  lz,le,maxscore,mincost=cluster(sites,beta);A=n**(1/3)
  good=(mincost>A and maxscore==0 and K*math.log(2)<=A/4)
  if good:
   valid+=1;assert le<=-A/4+1e-8
  if le>-A/4:failure+=1
  logs.append(lz/A);maxscores.append(maxscore);Ns.append(K);excess_logs.append(le)
 z['sparse_pareto_experiments'].append({'n':n,'alpha':alpha,'kappa':kappa,'repetitions':reps,'mean_large_sites':float(np.mean(Ns)),'fraction_full_sufficient_event':valid/reps,'fraction_exponential_bound_failure':failure/reps,'mean_logZ_over_n_one_third':float(np.mean(logs)),'max_logZ_over_n_one_third':float(max(logs))})
z['elapsed_seconds']=time.monotonic()-start
p.joinpath('SECOND_CHECKS.json').write_text(json.dumps(z,indent=2,allow_nan=False),encoding='utf-8');print(json.dumps(z,indent=2))
