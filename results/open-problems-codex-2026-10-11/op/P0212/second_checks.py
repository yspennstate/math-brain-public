import itertools,json,pathlib,time,math
from fractions import Fraction as F
import numpy as np

root=pathlib.Path(__file__).resolve().parent
out={'model':'free stationary Poisson walk cloud on a finite 3D torus; independent tags; NOT CBRW','seed':21210112}

# Exact finite Markov-chain check of the conditional contact-volume inequality.
def volume(path):
 mass=[F(1) for _ in range(4)];mass[path[0]]=0
 for x in path[1:]:
  mass=[mass[y]*F(1,2)+(mass[(y-1)%4]+mass[(y+1)%4])*F(1,4) for y in range(4)]
  mass[x]=0
 return 4-sum(mass)
checks=0
for tail in itertools.product(range(4),repeat=4):
 path=(0,)+tail;full=volume(path)
 for split in range(1,4):
  assert full<=volume(path[:split+1])+volume(path[split:]);checks+=1
out['exact_C4_subadditivity']={'paths':256,'split_checks':checks,'passed':True,'arbitrary_tag_paths':True}
out['categorical_checks']={'note':'Enumerate exact categorical sums against directly expanded convolution; no floating-point claim of proof.'}
for p in [F(1,10),F(1,3)]:
 # 3 independent categorical marks, types 0/1/none, probabilities p/4,p/2,1-3p/4.
 dist={(0,0):F(1)}
 for _ in range(3):
  new={}
  for (a,b),w in dist.items():
   for da,db,v in [(0,0,1-3*p/4),(1,0,p/4),(0,1,p/2)]:
    key=(a+da,b+db);new[key]=new.get(key,F(0))+w*v
  dist=new
 assert sum(dist.values())==1
 assert sum(a*w for (a,b),w in dist.items())==3*p/4
 assert sum(b*w for (a,b),w in dist.items())==3*p/2
out['categorical_checks']['passed']=True
(root/'second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')

rng=np.random.default_rng(out['seed'])
def trial(p,H):
 T=H/p;R=math.ceil(5*math.sqrt(T)+8);side=2*R+1
 n=int(rng.poisson(p*side**3));flat=rng.integers(side**3,size=n)
 pos=np.column_stack(np.unravel_index(flat,(side,side,side))).astype(np.int32)
 tags=np.array([[R,R,R],[R+1,R,R]],dtype=np.int32)
 bins=np.full((n,2),-1,dtype=np.int8)
 def detect(binidx):
  for i in range(2):
   hit=(bins[:,i]<0)&np.all(pos==tags[i],axis=1);bins[hit,i]=binidx
 detect(0)
 nextjump=rng.exponential(size=2);now=0.;binidx=0;boundaries=[T/2,T]
 while now<T:
  jumpindex=int(np.argmin(nextjump));stop=min(float(nextjump[jumpindex]),boundaries[binidx]);dt=stop-now
  numbers=rng.poisson(dt,size=n)
  for k in range(int(numbers.max()) if n else 0):
   ids=np.flatnonzero(numbers>k)
   axis=rng.integers(3,size=len(ids));direction=2*rng.integers(2,size=len(ids))-1
   pos[ids,axis]=(pos[ids,axis]+direction)%side
   detect(binidx)
  now=stop
  if now==boundaries[binidx]:
   binidx+=1
   if binidx==2:break
  else:
   axis=int(rng.integers(3));direction=2*int(rng.integers(2))-1
   tags[jumpindex,axis]=(tags[jumpindex,axis]+direction)%side
   nextjump[jumpindex]+=rng.exponential();detect(binidx)
 counts=np.array([[(bins[:,i]==j).sum() for j in range(2)] for i in range(2)])
 shared=int(np.all(bins>=0,axis=1).sum())
 return counts,shared,side,n

start=time.monotonic();H=1.;samples=60
for p in [.08,.04,.02,.01]:
 cs=[];shared=[];sizes=[]
 for _ in range(samples):
  c,b,side,n=trial(p,H);cs.append(c);shared.append(b);sizes.append(n)
  if time.monotonic()-start>210:break
 c=np.array(cs);tot=c.sum(axis=2)
 result={'p':p,'H':H,'T':H/p,'side':side,'samples':len(cs),'mean_particles':float(np.mean(sizes)),
  'mean_count_by_tag_and_bin':c.mean(axis=0).tolist(),'total_means':tot.mean(axis=0).tolist(),
  'total_mean_standard_errors':(tot.std(axis=0,ddof=1)/math.sqrt(len(cs))).tolist() if len(cs)>1 else None,
  'total_variances':tot.var(axis=0,ddof=1).tolist() if len(cs)>1 else None,
  'empirical_tag_covariance':float(np.cov(tot.T,ddof=1)[0,1]) if len(cs)>1 else None,
  'mean_shared_particles':float(np.mean(shared)),'prob_any_shared_particle':float(np.mean(np.array(shared)>0)),
  'asymptotic_mean_per_tag':2*0.6594626704592524*H,
  'finite_torus_and_finite_sample':True}
 # Independent relative-walk range check for finite-time mean, same torus.
 ranges=[]
 for _ in range(1200):
  x=[0,0,0];seen={tuple(x)}
  for __ in range(int(rng.poisson(2*H/p))):
   axis=int(rng.integers(3));x[axis]=(x[axis]+2*int(rng.integers(2))-1)%side;seen.add(tuple(x))
  ranges.append(len(seen))
 result['finite_time_range_predicted_mean']=p*float(np.mean(ranges))
 result['range_prediction_standard_error']=p*float(np.std(ranges,ddof=1))/math.sqrt(len(ranges))
 out[f'p={p}']=result
 (root/'second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
 print(json.dumps(result),flush=True)
 if time.monotonic()-start>210:break
out['elapsed_seconds']=time.monotonic()-start
(root/'second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('Elapsed:',out['elapsed_seconds'],flush=True)
