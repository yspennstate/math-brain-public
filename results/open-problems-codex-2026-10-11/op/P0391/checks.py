import random,math,json,pathlib,time
root=pathlib.Path(__file__).resolve().parent
rng=random.Random(3911011)
def gamma(n,kind):
 if kind=='PS':return [1/n]*n
 if kind=='middle':return [float(i==n//2) for i in range(n)]
 if kind=='alternating':return [float(i==(0 if n%2 else n-1)) for i in range(n)]
 if n==1:return [1.0]
 return [0.5 if i in (0,n-1) else 0.0 for i in range(n)]
def choose(weights):
 u=rng.random();s=0.0
 for i,w in enumerate(weights):
  s+=w
  if u<s:return i
 return len(weights)-1
def run(r,kind,law):
 # Both laws have mean 1. Pareto(alpha=3) has finite second and infinite fourth moment.
 h=0.5 if law=='constant' else 2/3
 lam=1-1/r;end=0.25*r*r
 residual=[];t=0.0;arr=rng.expovariate(lam);maxpos=maxneg=0.0;worst_bridge=0.0;events=0
 while t<end:
  n=len(residual);weights=gamma(n,kind) if n else []
  dep=min((x/w for x,w in zip(residual,weights) if w>0),default=math.inf)
  dt=min(arr-t,dep,end-t)
  d0=sum(residual)-h*n
  residual=[max(0.0,x-w*dt) for x,w in zip(residual,weights)]
  t+=dt;isarrival=abs(t-arr)<1e-8;reached=end-t<1e-8
  if not reached:
   if isarrival:
    b=1.0 if law=='constant' else (2/3)*(1-rng.random())**(-1/3)
    idx=choose(gamma(len(residual)+1,kind));residual.insert(idx,b)
    arr=t+rng.expovariate(lam)
   else:residual=[x for x in residual if x>1e-9]
  d1=sum(residual)-h*len(residual)
  worst_bridge=min(worst_bridge,d1-d0+dt+h*int(isarrival))
  maxpos=max(maxpos,d1/r);maxneg=max(maxneg,-d1/r);events+=1
 return dict(positive=maxpos,negative=maxneg,bridge_slack_min=worst_bridge,events=events)
t0=time.monotonic();output=[]
for law in ['constant','pareto3']:
 for kind in ['PS','middle','alternating','ends']:
  for r in [16,32,64]:
   runs=[run(r,kind,law) for _ in range(12)]
   output.append(dict(law=law,gamma=kind,r=r,reps=12,
    mean_positive=sum(x['positive'] for x in runs)/12,
    mean_negative=sum(x['negative'] for x in runs)/12,
    minimum_bridge_slack=min(x['bridge_slack_min'] for x in runs),
    events=sum(x['events'] for x in runs)))
record=dict(seed=3911011,elapsed_seconds=time.monotonic()-t0,results=output,
 caveat='Finite simulations check implementation and the deterministic inequality; they do not prove convergence or search all gamma.')
(root/'numerical_checks.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
