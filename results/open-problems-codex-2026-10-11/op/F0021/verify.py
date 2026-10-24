import pathlib, itertools, math, json, time
import numpy as np
from scipy.special import gammaln
p=pathlib.Path('.');start=time.monotonic();rng=np.random.default_rng(21)
res={'seed':21,'checks':{},'exact_pareto_single_site_cdf':[]}
# Every binomial point probability through i=1200.
worst=0.
for i in range(1,1201):
 x=np.arange(-i,i+1,2);k=(i+x)//2
 lp=gammaln(i+1)-gammaln(k+1)-gammaln(i-k+1)-i*math.log(2)
 worst=max(worst,float(np.max(lp+x*x/(2*i))))
assert worst<=1e-10
res['checks']['walk_log_probability_plus_cost_max']=worst
# Exact enumeration of all 1024 paths and the cap/tube inequality.
n=10;w=3;beta=.9
paths=np.array(list(itertools.product([-1,1],repeat=n)));pos=np.cumsum(paths,axis=1)
omega=rng.uniform(-1,1,(n,2*n+1));T=1.2
for i in range(n):
 for x in range(-(i+1),i+2,2):
  if abs(x)>w:omega[i,n+x]+=rng.uniform(0,3)
cap=np.minimum(omega,T)
energy=beta*omega[np.arange(n)[None,:],pos+n].sum(axis=1)
ce=beta*cap[np.arange(n)[None,:],pos+n].sum(axis=1)
in_tube=(np.abs(pos)<=w).all(axis=1)
Z=float(np.exp(energy).mean());ZT=float(np.exp(ce).mean());R=float(np.exp(energy[in_tube]).sum()/2**n);Q=R/Z
assert R<=ZT<=Z
assert 0<=math.log(Z/ZT)<=-math.log(Q)+1e-12
res['checks']['partition_bruteforce']={'n':n,'tube_width':w,'Z':Z,'Z_cap':ZT,'R':R,'Q':Q,'log_difference':math.log(Z/ZT),'minus_log_Q':-math.log(Q),'tube_paths':int(in_tube.sum())}
# Single-spike formula versus explicit enumeration.
errors=[]
for i,x in [(1,1),(5,1),(10,10),(10,0)]:
 for bval in [-2.,0.,2.,9.]:
  hit=(pos[:,i-1]==x);direct=float(np.exp(bval*hit).mean());pi=math.comb(i,(i+x)//2)/2**i
  formula=1+pi*math.expm1(bval);errors.append(abs(direct-formula))
  if bval>=0:assert math.log(direct)<=math.log(2)+max(0,bval-x*x/(2*i))+1e-12
res['checks']['single_spike_formula_max_abs_error']=max(errors)
# Numerical integral-sum envelope for q>5.
from scipy.special import gamma
for q in [5.01,5.5,7.]:
 J=math.sqrt(math.pi)*gamma(q-.5)/(2*gamma(q))
 for i in [1,10,1000]:
  for a in [1.,10.,100.]:
   x=np.arange(-100000,100001);val=float(np.sum((a+x*x/(2*i))**(-q)))
   bound=a**(-q)+2*math.sqrt(2*i)*a**(.5-q)*J
   assert val<=bound*(1+1e-12)
res['checks']['integral_envelope_cases_passed']=27
# Exact finite probability under independent uncentered Pareto(alpha), scale 1.
for n in [64,256,1024,4096]:
 sums={alpha:0. for alpha in [4.,5.,6.]};a=n**(1/3)
 for i in range(1,n+1):
  x=np.arange(-i,i+1,2,dtype=float);u=a+x*x/(2*i)
  for alpha in sums:sums[alpha]+=float(np.log1p(-u**(-alpha)).sum())
 for alpha,v in sums.items():res['exact_pareto_single_site_cdf'].append({'n':n,'alpha':alpha,'P_M_gt_n_one_third':-math.expm1(v)})
J5=math.sqrt(math.pi)*gamma(4.5)/(2*gamma(5.));res['pareto_alpha5_predicted_single_site_limit']=1-math.exp(-(2*math.sqrt(2)/3)*J5)
res['elapsed_seconds']=time.monotonic()-start
p.joinpath('CHECKS.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res,indent=2))
