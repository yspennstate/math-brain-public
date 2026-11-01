import math,random,json,pathlib,time
rng=random.Random(301230);start=time.monotonic()
# Exact finite-window likelihood recurrence for the duration-1-or-2 construction.
# Monte Carlo only estimates its moments under an iid normal reference.
def density(features,eps):
 n=len(features);nxt=[0.]*(n+1);nxt[n]=1.
 for j in range(n-1,-1,-1):
  cur=[0.]*(n+1);cur[n]=1.;cur[n-1]=1.+eps[j]*features[n-1]
  for r in range(j,n-1):cur[r]=(.5+eps[j]*features[r])*nxt[r+1]+(.5-eps[j]*features[r+1])*nxt[r+2]
  nxt=cur
 return nxt[0]
patterns={
 'iid_positive_control':lambda j:.24,
 'square_summable_proved_case':lambda j:.125/(j+1),
 'alternating_periodic_positive_control':lambda j:.24*(-1)**j,
 'growing_sign_blocks_unproved':lambda j:.24*(-1)**int(math.log2(j+1))}
results=[]
for n in [16,64,128]:
 features=[[-math.tanh(rng.gauss(0,1)) for _ in range(n)] for _ in range(500)]
 for name,ep in patterns.items():
  e=[ep(j) for j in range(n)];v=[density(f,e) for f in features]
  mean=sum(v)/len(v);second=sum(x*x for x in v)/len(v)
  results.append(dict(pattern=name,N=n,samples=len(v),mean_density=mean,second_moment=second,minimum=min(v),maximum=max(v)))
pathlib.Path('second_likelihood_probe.json').write_text(json.dumps(dict(elapsed_seconds=time.monotonic()-start,results=results),indent=2),encoding='utf8');print(json.dumps(results,indent=2))
