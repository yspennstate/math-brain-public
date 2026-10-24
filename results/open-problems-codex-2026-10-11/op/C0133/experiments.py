from fractions import Fraction as F
from pathlib import Path
import json,itertools,random,time
start=time.monotonic();out={}
# Exact rational Gaussian elimination for absorption profile.
def ruin(L):
 A=[[F(0) for _ in range(L)] for _ in range(L-1)]
 for i in range(1,L):
  A[i-1][i-1]=F(2)
  if i>1:A[i-1][i-2]=F(-1)
  if i<L-1:A[i-1][i]=F(-1)
  else:A[i-1][-1]=F(1)
 for j in range(L-1):
  scale=A[j][j];A[j]=[x/scale for x in A[j]]
  for i in range(L-1):
   if i!=j:
    scale=A[i][j];A[i]=[x-scale*y for x,y in zip(A[i],A[j])]
 return [F(0)]+[r[-1] for r in A]+[F(1)]
checks={}
for L in [2,3,5,10,20,40]:
 u=ruin(L);assert all(u[i]==F(i,L) for i in range(L+1));checks[str(L)]={'from_one':str(u[1]),'excursion_tail':str(u[1]/2)}
out['exact_ruin']=checks
# Every 12-step nearest-neighbor path: sum drift before grouping = sum after grouping.
B=F(3,2);count=0
for arrows in itertools.product([-1,1],repeat=12):
 x=0;counts={};drift=F(0)
 for e in arrows:
  i=counts.get(x,0)+1;counts[x]=i
  b=F(((x+i)%3)-1,2) if i<=3 else F(0)
  drift+=b;x+=e
 grouped=sum((sum((F(((site+i)%3)-1,2) for i in range(1,min(3,n)+1)),F(0)) for site,n in counts.items()),F(0))
 assert drift==grouped and abs(drift)<=B*len(counts);count+=1
out['exact_grouping']={'paths':count,'steps':12,'passed':True}
# Small counterexample probes within IID+UEL: identical stacks = degenerate IID.
# Finite horizons do not classify the non-transient event.
def prob(model,i):
 if model=='periodic':return .8 if i%2 else .2
 if model=='growing_blocks':
  width=1;positive=True
  while i>width:i-=width;width*=4;positive=not positive
  return .8 if positive else .2
 return .5
probes={}
for model in ['fair','periodic','growing_blocks']:
 rows=[]
 for seed in range(12):
  rng=random.Random(133000+seed);x=0;vis={};returns=0;last=0;peak=0
  for t in range(1,100001):
   i=vis.get(x,0)+1;vis[x]=i;x+=1 if rng.random()<prob(model,i) else -1
   if x==0:returns+=1;last=t
   if t>=10000:peak=max(peak,abs(x)/t)
  rows.append({'seed':133000+seed,'X_n_over_n':x/100000,'returns':returns,'last_return':last,'peak_abs_speed_after_10000':peak,'range':len(vis),'max_departures_at_site':max(vis.values())})
 probes[model]=rows
out['iid_elliptic_probes']={'n':100000,'models':probes,'limitation':'Finite-time diagnostics only. No recurrence/transience or limiting-speed verdict follows; no claimed counterexample.'}
out['elapsed_seconds']=time.monotonic()-start
Path('experiment_results.json').write_text(json.dumps(out,indent=2))
for model,rows in probes.items():print(model,'speed range',min(r['X_n_over_n'] for r in rows),max(r['X_n_over_n'] for r in rows),'return counts',min(r['returns'] for r in rows),max(r['returns'] for r in rows))
print('exact checks passed',count,'elapsed',out['elapsed_seconds'])
