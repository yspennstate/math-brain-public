import pathlib,random,math,json,time
from fractions import Fraction
root=pathlib.Path(__file__).resolve().parent
rng=random.Random(3912026)
lam=0.8;rho=Fraction(4,5);scale=5
def weights(n,kind):
 if kind=='PS':return [1/n]*n
 if kind=='middle':return [float(i==n//2) for i in range(n)]
 if kind=='alternating':return [float(i==(0 if n%2 else n-1)) for i in range(n)]
 if n==1:return [1.0]
 return [0.5 if i in (0,n-1) else 0.0 for i in range(n)]
def choose(ws):
 u=rng.random();s=0.0
 for i,w in enumerate(ws):
  s+=w
  if u<s:return i
 return len(ws)-1
def cycle(kind):
 t=rng.expovariate(lam);res=[1.0];nextarr=t+rng.expovariate(lam)
 arrivals=1;reward=0
 while res:
  ws=weights(len(res),kind)
  dep=min(x/w for x,w in zip(res,ws) if w>0)
  dt=min(nextarr-t,dep);res=[max(0.0,x-w*dt) for x,w in zip(res,ws)];t+=dt
  if abs(t-nextarr)<1e-9:
   if len(res)<=6 and sum(res)>=2:reward+=1
   idx=choose(weights(len(res)+1,kind));res.insert(idx,1.0)
   arrivals+=1;nextarr=t+rng.expovariate(lam)
  else:res=[x for x in res if x>1e-9]
 return t,arrivals,reward
def uniform_tail(n,x=2):
 if n==0 or x>=n:return Fraction(0)
 cdf=sum(((-1)**k)*math.comb(n,k)*Fraction(x-k)**n for k in range(min(n,x)+1))/math.factorial(n)
 return 1-cdf
pi_f=sum((1-rho)*rho**n*uniform_tail(n) for n in range(7))
expected_reward=scale*pi_f
reps=8000;results=[];t0=time.monotonic()
for kind in ['PS','middle','alternating','ends']:
 runs=[cycle(kind) for _ in range(reps)]
 vals=[x[2] for x in runs];mean=sum(vals)/reps
 variance=sum((x-mean)**2 for x in vals)/(reps-1)
 results.append(dict(gamma=kind,cycles=reps,mean_length=sum(x[0] for x in runs)/reps,
  mean_arrivals=sum(x[1] for x in runs)/reps,mean_reward=mean,
  reward_standard_error=math.sqrt(variance/reps),
  reward_z=(mean-float(expected_reward))/math.sqrt(variance/reps)))
record=dict(seed=3912026,model='M/D/1; service=1; lambda=0.8; complete empty-to-empty cycles',
 predicate='prearrival Q<=6 and workload>=2; all arrivals are marked',
 stationary_predicate_exact=str(pi_f),expected_cycle_reward_exact=str(expected_reward),
 expected_cycle_reward=float(expected_reward),expected_cycle_length=6.25,expected_cycle_arrivals=5,
 elapsed_seconds=time.monotonic()-t0,results=results,
 caveat='Monte Carlo tests the regenerative counting identity for four gamma; it does not establish the theorem.')
(root/'regeneration_checks.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
